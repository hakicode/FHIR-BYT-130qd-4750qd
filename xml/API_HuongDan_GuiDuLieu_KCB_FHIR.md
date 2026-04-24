# Hướng Dẫn Gửi Dữ Liệu Khám Bệnh, Chữa Bệnh Qua Cổng Dữ Liệu Báo Cáo

> Chuẩn kết nối: **RESTful API — JSON**  
> Chuẩn dữ liệu XML: **QĐ 130/QĐ-BYT** (hợp nhất **QĐ 4750/QĐ-BYT**)  
> Xác thực: **JWT Bearer Token**  
> Base URL: `https://fhir.{domain}`

---

## Mục lục

- [I. Xác thực (JWT)](#i-xác-thực-jwt)
  - [1. Đăng nhập — Lấy token](#1-đăng-nhập--lấy-token)
  - [2. Làm mới token](#2-làm-mới-token)
  - [3. Thu hồi token — Đăng xuất](#3-thu-hồi-token--đăng-xuất)
- [II. Gửi dữ liệu XML (QĐ 130/QĐ-BYT)](#ii-gửi-dữ-liệu-xml-qđ-130qđ-byt)
  - [1. Gửi dữ liệu trạng thái KCB (Check-in)](#1-gửi-dữ-liệu-trạng-thái-kcb-check-in)
  - [2. Gửi dữ liệu khám bệnh, chữa bệnh](#2-gửi-dữ-liệu-khám-bệnh-chữa-bệnh)
- [III. Gửi dữ liệu JSON (FHIR)](#iii-gửi-dữ-liệu-json-fhir)
  - [1. Nạp / cập nhật Cơ sở KCB và Khoa (Organization)](#1-nạp--cập-nhật-cơ-sở-kcb-và-khoa-organization)
  - [2. Nạp bộ mã danh mục (CodeSystem)](#2-nạp-bộ-mã-danh-mục-codesystem)
  - [3. Nạp bác sĩ và vai trò (Practitioner)](#3-nạp-bác-sĩ-và-vai-trò-practitioner)
  - [4. Bổ sung thông tin BHYT (Coverage)](#4-bổ-sung-thông-tin-bhyt-coverage)
  - [5. Bổ sung thông tin thuốc (Medication)](#5-bổ-sung-thông-tin-thuốc-medication)
  - [6. Nạp kế hoạch giường (Location)](#6-nạp-kế-hoạch-giường-location)
  - [7. Cập nhật kết quả quyết toán BHXH (ClaimResponse)](#7-cập-nhật-kết-quả-quyết-toán-bhxh-claimresponse)
- [IV. Kiểm soát hồ sơ trên Cổng](#iv-kiểm-soát-hồ-sơ-trên-cổng)
  - [1. Lấy danh sách log dữ liệu đã gửi (phân trang)](#1-lấy-danh-sách-log-dữ-liệu-đã-gửi-phân-trang)
- [V. Ánh xạ tệp XML](#v-ánh-xạ-tệp-xml)

---

## I. Xác thực (JWT)

Tất cả các request đến API (trừ mục I.1) đều yêu cầu header:

```
Authorization: Bearer {access_token}
```

---

### 1. Đăng nhập — Lấy token

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/auth/login` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/json` |

#### Request Body

```json
{
  "username": "string",
  "password": "string"
}
```

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `username` | String | ✓ | Tên tài khoản được cấp |
| `password` | String | ✓ | Mật khẩu truy cập được cấp (mã hóa **MD5 uppercase**) |

#### Response

**HTTP 200 OK**

```json
{
  "access_token": "string",
  "refresh_token": "string",
  "token_type": "Bearer",
  "expires_in": "2024-07-01T00:00:00Z",
  "username": "string"
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `access_token` | String | JWT token dùng để xác thực các request |
| `refresh_token` | String | Token dùng để làm mới `access_token` khi hết hạn |
| `token_type` | String | Kiểu token — luôn là `Bearer` |
| `expires_in` | datetime | Thời gian hết hạn của `access_token` (UTC, ISO 8601) |
| `username` | String | Tên tài khoản đăng nhập |

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Tên tài khoản hoặc mật khẩu không đúng"
}
```

---

### 2. Làm mới token

Dùng khi `access_token` đã hết hạn. Không yêu cầu đăng nhập lại.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/oauth/token` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/x-www-form-urlencoded` |

#### Request Body

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `grant_type` | String | ✓ | Luôn là `refresh_token` |
| `refresh_token` | String | ✓ | Refresh token lấy được tại mục I.1 |

#### Response

**HTTP 200 OK**

```json
{
  "access_token": "string",
  "refresh_token": "string",
  "token_type": "Bearer",
  "expires_in": "2024-07-01T00:00:00Z"
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `access_token` | String | JWT token mới |
| `refresh_token` | String | Refresh token mới (rotation) |
| `token_type` | String | Kiểu token — luôn là `Bearer` |
| `expires_in` | datetime | Thời gian hết hạn của `access_token` mới (UTC, ISO 8601) |

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Refresh token không hợp lệ hoặc đã hết hạn"
}
```

---

### 3. Thu hồi token — Đăng xuất

Vô hiệu hóa `access_token` và `refresh_token` hiện tại. Sau khi gọi thành công, token không thể dùng lại.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/oauth/revoke` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/x-www-form-urlencoded` |
| `Authorization` | String | ✓ | `Bearer {access_token}` |

#### Request Body

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `token` | String | ✓ | `access_token` hoặc `refresh_token` cần thu hồi |

#### Response

**HTTP 200 OK**

```json
{
  "status": 200,
  "message": "Token đã được thu hồi thành công"
}
```

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Token không hợp lệ hoặc đã hết hạn"
}
```

---

## II. Gửi dữ liệu XML (QĐ 130/QĐ-BYT)

> Tất cả các request trong mục này yêu cầu header `Authorization: Bearer {access_token}`.

---

### 1. Gửi dữ liệu trạng thái KCB (Check-in)

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/qd130/checkInKcbQd4750` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/x-www-form-urlencoded` |
| `Authorization` | String | ✓ | `Bearer {access_token}` |

#### Body

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `fileHSBase64` | String | ✓ | File xml theo cấu trúc XML0 (mô tả tại mục II.1 — Cấu trúc file XML) được mã hóa thành chuỗi base64 |

#### Response

**HTTP 200 OK**

```json
{
  "logId": "string",
  "metadata": {
    "status": "success",
    "message": "string",
    "code": "200"
  }
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `logId` | String | Định danh bản ghi log, dùng để tra cứu tại `GET /api/logs` |
| `metadata.status` | String | Trạng thái xử lý: `success` \| `error` \| `pending` |
| `metadata.message` | String | Thông điệp kết quả hoặc mô tả lỗi nếu có |
| `metadata.code` | String | Mã kết quả xử lý |

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Token không hợp lệ hoặc đã hết hạn"
}
```

**HTTP 403 Forbidden**

```json
{
  "status": 403,
  "error": "Forbidden",
  "message": "Tài khoản không có quyền thực hiện thao tác này"
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

#### Cấu trúc file XML (XML0)

Tham chiếu tệp: [`XML0_TrangThai_KCB.xml`](./XML0_TrangThai_KCB.xml)

> **Lưu ý ký số:**
> - Thẻ `<CHUKYDONVI>` chứa nội dung ký là từ thẻ mở `<CHI_TIEU_TRANG_THAI_KCB>` tới hết thẻ đóng `</DSACH_TRANG_THAI_KCB>`.
> - Giải thuật ký: **SHA256**.

---

### 2. Gửi dữ liệu khám bệnh, chữa bệnh

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/qd130/guiHoSoXmlQD4750` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/x-www-form-urlencoded` |
| `Authorization` | String | ✓ | `Bearer {access_token}` |

#### Body

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `fileHSBase64` | String | ✓ | File xml theo cấu trúc quy định tại QĐ 4750/QĐ-BYT (mô tả tại mục II.2 — Cấu trúc file XML wrapper) được mã hóa thành chuỗi base64 |

#### Response

**HTTP 200 OK**

```json
{
  "logId": "string",
  "metadata": {
    "status": "success",
    "message": "string",
    "code": "200"
  }
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `logId` | String | Định danh bản ghi log, dùng để tra cứu tại `GET /api/logs` |
| `metadata.status` | String | Trạng thái xử lý: `success` \| `error` \| `pending` |
| `metadata.message` | String | Thông điệp kết quả hoặc mô tả lỗi nếu có |
| `metadata.code` | String | Mã kết quả xử lý |

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Token không hợp lệ hoặc đã hết hạn"
}
```

**HTTP 403 Forbidden**

```json
{
  "status": 403,
  "error": "Forbidden",
  "message": "Tài khoản không có quyền thực hiện thao tác này"
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

#### Cấu trúc file XML wrapper (GIAMDINHHS)

File XML gốc gửi lên có cấu trúc bao ngoài (`GIAMDINHHS`) chứa danh sách các hồ sơ con. Mỗi hồ sơ con (`FILEHOSO`) bao gồm mã loại (`LOAIHOSO`) và nội dung file XML tương ứng đã được mã hóa Base64 (`NOIDUNGFILE`).

```xml
<?xml version="1.0" encoding="utf-8"?>
<GIAMDINHHS xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <THONGTINDONVI>
    <MACSKCB>{Mã CSKCB}</MACSKCB>
  </THONGTINDONVI>
  <THONGTINHOSO>
    <NGAYLAP>{Ngày lập, định dạng yyyyMMdd}</NGAYLAP>
    <SOLUONGHOSO>{Số lượng hồ sơ}</SOLUONGHOSO>
    <DANHSACHHOSO>
      <HOSO>
        <FILEHOSO>
          <LOAIHOSO>XML1</LOAIHOSO>
          <NOIDUNGFILE>{Nội dung XML1 mã hóa Base64}</NOIDUNGFILE>
        </FILEHOSO>
        <!-- Các FILEHOSO khác: XML2 ... XML15 -->
      </HOSO>
    </DANHSACHHOSO>
  </THONGTINHOSO>
  <CHUKYDONVI/>
</GIAMDINHHS>
```

> **Lưu ý ký số:**
> - Thẻ `<CHUKYDONVI>` chứa nội dung ký số là từ thẻ mở `<THONGTINDONVI>` tới hết thẻ đóng `</THONGTINHOSO>`.
> - Giải thuật ký: **SHA256**.

#### Mô tả các file XML con

Mỗi giá trị `NOIDUNGFILE` là nội dung của tệp XML tương ứng được mã hóa Base64. Bảng ánh xạ đầy đủ xem tại [mục V](#v-ánh-xạ-tệp-xml).

| `LOAIHOSO` | Tệp XML | Mô tả |
|---|---|---|
| `XML1` | [`XML1_TongHop_KCB.xml`](./XML1_TongHop_KCB.xml) | Bảng 1 — Chỉ tiêu tổng hợp khám bệnh, chữa bệnh |
| `XML2` | [`XML2_ChiTiet_Thuoc.xml`](./XML2_ChiTiet_Thuoc.xml) | Bảng 2 — Chỉ tiêu chi tiết thuốc |
| `XML3` | [`XML3_ChiTiet_DVKT_VTYT.xml`](./XML3_ChiTiet_DVKT_VTYT.xml) | Bảng 3 — Chỉ tiêu chi tiết dịch vụ kỹ thuật và vật tư y tế |
| `XML4` | [`XML4_ChiTiet_CanLamSang.xml`](./XML4_ChiTiet_CanLamSang.xml) | Bảng 4 — Chỉ tiêu chi tiết dịch vụ cận lâm sàng |
| `XML5` | [`XML5_ChiTiet_DienBienLamSang.xml`](./XML5_ChiTiet_DienBienLamSang.xml) | Bảng 5 — Chỉ tiêu chi tiết diễn biến lâm sàng |
| `XML6` | [`XML6_HoSo_HIV_AIDS.xml`](./XML6_HoSo_HIV_AIDS.xml) | Bảng 6 — Chỉ tiêu hồ sơ bệnh án chăm sóc và điều trị HIV/AIDS |
| `XML7` | [`XML7_GiayRaVien.xml`](./XML7_GiayRaVien.xml) | Bảng 7 — Chỉ tiêu dữ liệu giấy ra viện |
| `XML8` | [`XML8_TomTat_HoSoBenhAn.xml`](./XML8_TomTat_HoSoBenhAn.xml) | Bảng 8 — Chỉ tiêu dữ liệu tóm tắt hồ sơ bệnh án |
| `XML9` | [`XML9_GiayChungSinh.xml`](./XML9_GiayChungSinh.xml) | Bảng 9 — Chỉ tiêu dữ liệu giấy chứng sinh |
| `XML10` | [`XML10_GiayNghiDuongThai.xml`](./XML10_GiayNghiDuongThai.xml) | Bảng 10 — Chỉ tiêu dữ liệu giấy chứng nhận nghỉ dưỡng thai |
| `XML11` | [`XML11_GiayNghiHuongBHXH.xml`](./XML11_GiayNghiHuongBHXH.xml) | Bảng 11 — Chỉ tiêu dữ liệu giấy chứng nhận nghỉ hưởng BHXH |
| `XML12` | [`XML12_GiamDinhYKhoa.xml`](./XML12_GiamDinhYKhoa.xml) | Bảng 12 — Chỉ tiêu dữ liệu giám định y khoa |

---

## III. Gửi dữ liệu JSON (FHIR)

> Chuẩn: **HL7 FHIR R4B (4.3.0)**  
> Tất cả các request trong mục này yêu cầu header `Authorization: Bearer {access_token}` và `Content-Type: application/fhir+json`.

**Quy tắc response thống nhất toàn hệ thống:**

- **`2xx` — Thành công:** luôn trả về `{ logId, metadata }` — trong đó `metadata` với XML là `{ status, message, code }`, với FHIR là `OperationOutcome`.
- **`4xx` — Lỗi:** luôn trả về `{ status, error, message }` theo HTTP error chuẩn. Không có `logId` vì request thất bại trước khi được ghi log.

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "string"
      }
    ]
  }
}
```

---

### 1. Nạp / cập nhật Cơ sở KCB và Khoa (Organization)

> **Lý do bổ sung:** Sau khi import toàn bộ XML QĐ 130+4750, mọi reference đến cơ sở KCB và khoa lâm sàng chỉ có mã số (`MA_CSKCB`, `MA_KHOA`) — không có tên, không có địa chỉ, không có phân cấp tuyến. Đây là điều kiện tiên quyết để hệ thống hiển thị nhãn có nghĩa: toàn bộ báo cáo thống kê theo cơ sở và theo khoa đều phụ thuộc vào resource này. Dữ liệu lấy từ DMDC QĐ 5937/QĐ-BYT (Phụ lục 4 — danh mục BV, Phụ lục 5 — danh mục khoa).

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/Organization` |
| **Phương thức** | `POST` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Content-Type` | String | ✓ | `application/fhir+json` |
| `Authorization` | String | ✓ | `Bearer {access_token}` |

#### Request Body

Hỗ trợ đơn lẻ hoặc bulk transaction (`Bundle`):

```json
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "resource": {
        "resourceType": "Organization",
        "identifier": [{ "value": "01234" }],
        "name": "Bệnh viện Đa khoa tỉnh X",
        "type": [{ "coding": [{ "code": "prov" }] }],
        "address": [{ "state": "01" }],
        "partOf": { "reference": "Organization/so-yt-tinh-x" }
      },
      "request": { "method": "POST", "url": "Organization" }
    }
  ]
}
```

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `identifier[0].value` | String | ✓ | Mã CSKCB (`MA_CSKCB`) hoặc mã khoa (`MA_KHOA`) |
| `name` | String | ✓ | Tên đầy đủ cơ sở KCB hoặc tên khoa |
| `type[0].coding[0].code` | String | ✓ | Hạng/loại: `prov` (BV), `dept` (khoa), `govt` (Sở YT) |
| `address[0].state` | String |  | Mã tỉnh trực thuộc |
| `partOf.reference` | String |  | Phân cấp: khoa → BV → Sở YT → Bộ YT |
| `active` | Boolean |  | Trạng thái hoạt động (mặc định `true`) |

#### Response

**HTTP 200 OK** — Bundle transaction thành công

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Organization transaction completed: 1 created, 0 updated"
      }
    ]
  }
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

---

### 2. Nạp bộ mã danh mục (CodeSystem)

> **Lý do bổ sung:** QĐ 130+4750 chỉ truyền mã số (ICD-10, mã DVKT, mã thuốc, mã BV, mã khoa) — không truyền kèm tên hiển thị. Không có CodeSystem thì mọi mã trong hệ thống đều là chuỗi ký tự không có nghĩa với người dùng, ảnh hưởng toàn bộ báo cáo. Cần nạp trước khi vận hành: ICD-10 tiếng Việt (~14.000 mã, QĐ 4469/QĐ-BYT), ICD-9-CM phẫu thuật/thủ thuật (QĐ 4440/QĐ-BYT), danh mục DVKT (~30.000 dịch vụ, QĐ 7603/QĐ-BYT), danh mục BV/Khoa (QĐ 5937/QĐ-BYT). Dùng `PUT` (idempotent) vì các bộ mã này được Bộ Y tế cập nhật định kỳ.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/CodeSystem/{id}` |
| **Phương thức** | `PUT` |

**Các giá trị `{id}` được hỗ trợ:**

| `{id}` | Mô tả | Nguồn |
|---|---|---|
| `icd-10-vn` | ICD-10 tiếng Việt (~14.000 mã bệnh) | QĐ 4469/QĐ-BYT |
| `icd-9-cm-vn` | ICD-9-CM phẫu thuật/thủ thuật | QĐ 4440/QĐ-BYT |
| `dvkt-vn` | Danh mục DVKT (~30.000 dịch vụ) | QĐ 7603/QĐ-BYT Phụ lục 1 |
| `thuoc-vn` | Danh mục thuốc / hoạt chất / ATC | Cục Quản lý Dược + WHO ATC |
| `vtyt-vn` | Danh mục vật tư y tế | QĐ 5086/QĐ-BYT |
| `yhct-vn` | Danh mục bệnh Y học cổ truyền | QĐ 26/2022/QĐ-BYT |

#### Request Body

```json
{
  "resourceType": "CodeSystem",
  "id": "icd-10-vn",
  "url": "https://fhir.{domain}/CodeSystem/icd-10-vn",
  "version": "2020",
  "name": "ICD10VN",
  "title": "ICD-10 Tiếng Việt",
  "status": "active",
  "content": "complete",
  "concept": [
    {
      "code": "I21.0",
      "display": "Nhồi máu cơ tim cấp thành trước"
    }
  ]
}
```

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `id` | String | ✓ | Định danh CodeSystem (xem bảng trên) |
| `version` | String | ✓ | Phiên bản ban hành (ví dụ: `2020`, `2023`) |
| `status` | String | ✓ | `active` \| `retired` |
| `content` | String | ✓ | `complete` (toàn bộ) \| `fragment` (một phần) |
| `concept[]` | Array | ✓ | Danh sách mã — mỗi phần tử gồm `code` và `display` |

#### Response

**HTTP 200 OK** — cập nhật thành công  
**HTTP 201 Created** — tạo mới thành công

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "CodeSystem/icd-10-vn upserted: 14000 concepts loaded"
      }
    ]
  }
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

---

### 3. Nạp bác sĩ và vai trò (Practitioner)

> **Lý do bổ sung:** QĐ 130+4750 chỉ truyền mã số BHXH của bác sĩ (`MA_BAC_SI`, `NGUOI_THUC_HIEN`, `MA_BS_DOC_KQ`) — không có tên, chuyên khoa, hay chức danh. Báo cáo phân tích workload, chất lượng điều trị theo bác sĩ hoàn toàn không thể thực hiện nếu chỉ hiển thị mã số. `PractitionerRole` đi kèm để gán bác sĩ vào khoa và chức danh, là cơ sở để liên kết `Encounter.participant`, `MedicationRequest.requester`, `DiagnosticReport.resultsInterpreter`. Dữ liệu lấy từ HIS module nhân sự hoặc Cục Quản lý KCB (Bộ YT).

| Thuộc tính | Giá trị |
|---|---|
| **URL — Bác sĩ** | `https://fhir.{domain}/api/fhir/Practitioner` |
| **URL — Vai trò** | `https://fhir.{domain}/api/fhir/PractitionerRole` |
| **Phương thức** | `POST` |

#### Request Body — Practitioner

```json
{
  "resourceType": "Practitioner",
  "identifier": [
    { "system": "https://bhxh.gov.vn/ma-bac-si", "value": "012345" }
  ],
  "name": [
    {
      "text": "Nguyễn Văn A",
      "family": "Nguyễn",
      "given": ["Văn", "A"]
    }
  ],
  "qualification": [
    {
      "code": {
        "coding": [{ "code": "MD", "display": "Bác sĩ" }]
      }
    }
  ]
}
```

#### Request Body — PractitionerRole

```json
{
  "resourceType": "PractitionerRole",
  "practitioner": { "reference": "Practitioner/012345" },
  "organization": { "reference": "Organization/MA_KHOA" },
  "code": [
    { "coding": [{ "code": "doctor", "display": "Bác sĩ điều trị" }] }
  ],
  "specialty": [
    { "coding": [{ "code": "394579002", "display": "Tim mạch" }] }
  ]
}
```

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `identifier[0].value` | String | ✓ | Mã BHXH của bác sĩ (`MA_BAC_SI`) |
| `name[0].text` | String | ✓ | Họ tên đầy đủ |
| `name[0].family` | String |  | Họ |
| `name[0].given[]` | Array |  | Tên + đệm |
| `qualification[0].code` | CodeableConcept |  | Bằng cấp / chức danh |
| `PractitionerRole.organization` | Reference |  | Khoa trực thuộc (`MA_KHOA`) |
| `PractitionerRole.specialty` | Array |  | Chuyên khoa |

#### Response

**HTTP 201 Created**

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Practitioner/012345 created successfully"
      }
    ]
  }
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

---

### 4. Bổ sung thông tin BHYT (Coverage)

> **Lý do bổ sung:** Coverage được tạo tự động khi import XML B1, nhưng thiếu 4 trường quan trọng: `subscriber` (người tham gia BHYT — khác bệnh nhân trong trường hợp phụ thuộc), `subscriberId` (mã BHXH người đóng), `beneficiary` (liên kết tường minh đến Patient), và `payor` (cơ quan BHXH tỉnh/huyện chi trả). Thiếu các trường này thì không phân biệt được bệnh nhân là người tham gia chính hay người phụ thuộc, không trace được dòng tiền BHYT, không liên kết cross-check với hệ thống BHXH. Dữ liệu bổ sung từ cổng BHXH qua API tra cứu thẻ BHYT.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/Coverage/{id}` |
| **Phương thức** | `PATCH` |

**`{id}`** là `Coverage.id` tương ứng với `MA_THE_BHYT` đã được tạo khi import XML B1.

#### Request Body (JSON Patch)

```json
[
  {
    "op": "add",
    "path": "/subscriber",
    "value": { "reference": "Patient/MA_BN_nguoi_dong" }
  },
  {
    "op": "add",
    "path": "/subscriberId",
    "value": "MA_BHXH_nguoi_dong"
  },
  {
    "op": "add",
    "path": "/beneficiary",
    "value": { "reference": "Patient/MA_BN" }
  },
  {
    "op": "add",
    "path": "/payor/0",
    "value": { "reference": "Organization/bhxh-tinh-01" }
  }
]
```

| Trường bổ sung | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `subscriber` | Reference → Patient | Người tham gia BHYT (người đóng) |
| `subscriberId` | String | Mã số BHXH của người đóng |
| `beneficiary` | Reference → Patient | Người được hưởng BHYT (`MA_BN`) |
| `payor[0]` | Reference → Organization | Cơ quan BHXH tỉnh/huyện chi trả (suy luận từ 2 ký tự đầu `MA_THE_BHYT`) |

#### Response

**HTTP 200 OK**

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Coverage/{id} patched successfully"
      }
    ]
  }
}
```

**HTTP 404 Not Found**

```json
{
  "status": 404,
  "error": "Not Found",
  "message": "Resource không tồn tại"
}
```

---

### 5. Bổ sung thông tin thuốc (Medication)

> **Lý do bổ sung:** `Medication` được tạo tự động khi import XML B2, nhưng chỉ có tên thương mại, số đăng ký và dạng bào chế — thiếu tên INN (International Nonproprietary Name) và mã ATC (Anatomical Therapeutic Chemical). Không có tên INN và ATC code thì không thể phân tích sử dụng thuốc theo nhóm dược lý, không so sánh được chi phí thuốc theo hoạt chất, không hỗ trợ cảnh báo tương tác thuốc. Dữ liệu bổ sung từ Cục Quản lý Dược và bộ mã ATC của WHO.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/Medication/{id}` |
| **Phương thức** | `PATCH` |

**`{id}`** là `Medication.id` tương ứng với `MA_THUOC` đã được tạo khi import XML B2.

#### Request Body (JSON Patch)

```json
[
  {
    "op": "add",
    "path": "/code/coding/-",
    "value": {
      "system": "http://www.whocc.no/atc",
      "code": "C09AA05",
      "display": "Ramipril"
    }
  },
  {
    "op": "add",
    "path": "/code/coding/-",
    "value": {
      "system": "https://duocvn.gov.vn/inn",
      "code": "ramipril",
      "display": "Ramipril (INN)"
    }
  }
]
```

| Trường bổ sung | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `code.coding[]` (ATC) | Coding | Mã ATC WHO: `system = http://www.whocc.no/atc` |
| `code.coding[]` (INN) | Coding | Tên INN: `system = https://duocvn.gov.vn/inn` |

#### Response

**HTTP 200 OK**

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Medication/{id} patched successfully"
      }
    ]
  }
}
```

**HTTP 404 Not Found**

```json
{
  "status": 404,
  "error": "Not Found",
  "message": "Resource không tồn tại"
}
```

---

### 6. Nạp kế hoạch giường (Location)

> **Lý do bổ sung:** QĐ 130+4750 chỉ biết các giường **đã có bệnh nhân sử dụng** trong kỳ báo cáo (qua `MA_GIUONG` B3) — không biết tổng số giường được phân bổ kế hoạch cho từng khoa. Thiếu tổng số giường kế hoạch thì tỷ lệ sử dụng giường (= bệnh nhân đang nằm / tổng giường) không tính được do mẫu số bằng 0. Đây là chỉ số cốt lõi trong quản lý bệnh viện. Ngoài ra, QĐ 130+4750 không có phân cấp vị trí vật lý (giường → phòng → khoa) nên cần bổ sung để phân tích drill-down. Dữ liệu lấy từ HIS module quản lý giường.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/Location` |
| **Phương thức** | `POST` |

#### Request Body

Hỗ trợ bulk transaction (`Bundle`) để nạp toàn bộ cây giường → phòng → khoa:

```json
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "resource": {
        "resourceType": "Location",
        "identifier": [{ "value": "H001" }],
        "name": "Giường 001 — Phòng A — Khoa Nội Tim mạch",
        "physicalType": {
          "coding": [{ "code": "bd", "display": "Bed" }]
        },
        "status": "active",
        "managingOrganization": { "reference": "Organization/MA_KHOA" },
        "partOf": { "reference": "Location/phong-A" }
      },
      "request": { "method": "POST", "url": "Location" }
    }
  ]
}
```

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `identifier[0].value` | String | ✓ | Mã giường (`MA_GIUONG`), mã phòng, hoặc mã khoa |
| `name` | String | ✓ | Tên hiển thị vị trí |
| `physicalType.coding[0].code` | String | ✓ | `bd` (giường) \| `ro` (phòng) \| `wa` (khoa) \| `lvl` (tầng) |
| `status` | String | ✓ | `active` \| `suspended` \| `inactive` |
| `managingOrganization` | Reference | ✓ | Khoa quản lý → `Organization/{MA_KHOA}` |
| `partOf` | Reference |  | Phân cấp: giường → phòng → khoa |

#### Response

**HTTP 200 OK** — Bundle transaction thành công

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Location transaction completed: N created, M updated"
      }
    ]
  }
}
```

**HTTP 422 Unprocessable Entity**

```json
{
  "status": 422,
  "error": "Unprocessable Entity",
  "message": "Mô tả lỗi dữ liệu chi tiết"
}
```

---

### 7. Cập nhật kết quả quyết toán BHXH (ClaimResponse)

> **Lý do bổ sung:** `ClaimResponse` được tạo sơ bộ khi import XML B1 (có số tiền BHYT thanh toán `T_BHTT`, `T_BNTT`), nhưng trạng thái quyết toán cuối cùng chỉ có sau khi cơ quan BHXH phê duyệt — thường sau 30–90 ngày. Thiếu kết quả phê duyệt thì không phân biệt được hồ sơ đã được BHXH chấp nhận thanh toán hay bị từ chối/xuất toán, không theo dõi được tỷ lệ và lý do từ chối theo cơ sở KCB, không phục vụ được đối chiếu công nợ BHYT. Dữ liệu cập nhật từ cổng BHXH sau khi có kết quả giám định chính thức.

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/fhir/ClaimResponse/{id}` |
| **Phương thức** | `PATCH` |

**`{id}`** là `ClaimResponse.id` tương ứng với `MA_LK` đã được tạo khi import XML B1.

#### Request Body (JSON Patch)

```json
[
  {
    "op": "replace",
    "path": "/status",
    "value": "active"
  },
  {
    "op": "replace",
    "path": "/outcome",
    "value": "complete"
  },
  {
    "op": "add",
    "path": "/processNote/-",
    "value": {
      "type": "display",
      "text": "Đã phê duyệt thanh toán ngày 15/08/2024"
    }
  },
  {
    "op": "add",
    "path": "/processNote/-",
    "value": {
      "type": "display",
      "text": "Xuất toán: Thuốc ngoài danh mục — 150.000 VNĐ"
    }
  }
]
```

| Trường cập nhật | Giá trị hợp lệ | Mô tả |
|---|---|---|
| `status` | `active` \| `cancelled` \| `entered-in-error` | Trạng thái hồ sơ sau quyết toán |
| `outcome` | `complete` \| `partial` \| `error` | Kết quả giám định: chấp nhận toàn bộ / một phần / từ chối |
| `processNote[].text` | String | Ghi chú kết quả phê duyệt hoặc lý do xuất toán |

#### Response

**HTTP 200 OK**

```json
{
  "logId": "string",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "ClaimResponse/{id} patched successfully"
      }
    ]
  }
}
```

**HTTP 404 Not Found**

```json
{
  "status": 404,
  "error": "Not Found",
  "message": "Resource không tồn tại"
}
```

---


## IV. Kiểm soát hồ sơ trên Cổng

Cổng tiếp nhận dữ liệu báo cáo: `https://fhir.{domain}`

### 1. Lấy danh sách log dữ liệu đã gửi (phân trang)

| Thuộc tính | Giá trị |
|---|---|
| **URL** | `https://fhir.{domain}/api/logs` |
| **Phương thức** | `GET` |

#### Headers

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `Authorization` | String | ✓ | `Bearer {access_token}` |

#### Query Parameters

| Tên tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|:---:|---|
| `fromDate` | String | ✓ | Từ ngày, định dạng `yyyyMMdd` |
| `toDate` | String | ✓ | Đến ngày, định dạng `yyyyMMdd` (tối đa 60 ngày kể từ `fromDate`) |
| `id` | String |  | Tra cứu theo `logId` cụ thể |
| `resourceType` | String |  | Loại tài nguyên: `xml` \| `json` |
| `page` | Number |  | Số trang, bắt đầu từ `1` (mặc định `1`) |
| `pageSize` | Number |  | Số bản ghi mỗi trang (mặc định `20`, tối đa `100`) |

**Ví dụ request:**

```
GET /api/logs?fromDate=20240601&toDate=20240630&resourceType=xml&page=1&pageSize=20
GET /api/logs?id=abc123
```

#### Response

**HTTP 200 OK**

```json
{
  "page": 1,
  "pageSize": 20,
  "totalRecords": 100,
  "totalPages": 5,
  "data": [
    {
      "id": "string",
      "action": "string",
      "resourceType": "xml",
      "resourceData": "string",
      "timestamp": "2024-06-01T08:00:00Z",
      "metadata": "{\"status\":\"success\",\"message\":\"string\",\"code\":\"200\"}"
    }
  ]
}
```

**Thông tin phân trang:**

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `page` | Number | Trang hiện tại |
| `pageSize` | Number | Số bản ghi mỗi trang |
| `totalRecords` | Number | Tổng số bản ghi thỏa điều kiện |
| `totalPages` | Number | Tổng số trang |
| `data` | Array | Danh sách bản ghi log |

**Thông tin mỗi bản ghi log (`data[]`):**

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `id` | String | Định danh duy nhất của bản ghi log (`logId`) |
| `action` | String | Hành động thực hiện: `checkIn` \| `submitXml` \| `submitFhir` |
| `resourceType` | String | Loại tài nguyên: `xml` \| `json` |
| `resourceData` | String | Nội dung dữ liệu đã gửi (chuỗi raw) |
| `timestamp` | datetime | Thời điểm ghi log (UTC, ISO 8601) |
| `metadata` | String | JSON string kết quả xử lý. Với XML: `{"status":"...","message":"...","code":"..."}`. Với FHIR: `OperationOutcome` dạng chuỗi |

**HTTP 400 Bad Request**

```json
{
  "status": 400,
  "error": "Bad Request",
  "message": "fromDate và toDate không được vượt quá 60 ngày"
}
```

**HTTP 401 Unauthorized**

```json
{
  "status": 401,
  "error": "Unauthorized",
  "message": "Token không hợp lệ hoặc đã hết hạn"
}
```

**HTTP 403 Forbidden**

```json
{
  "status": 403,
  "error": "Forbidden",
  "message": "Tài khoản không có quyền truy cập dữ liệu của cơ sở này"
}
```

---

## V. Ánh xạ tệp XML

Bảng tổng hợp toàn bộ tệp XML theo chuẩn QĐ 130/QĐ-BYT (hợp nhất QĐ 4750/QĐ-BYT):

| Mã loại | Tệp XML | Bảng QĐ | Mô tả | Dịch vụ sử dụng |
|---|---|:---:|---|---|
| `XML0` | [`XML0_TrangThai_KCB.xml`](./XML0_TrangThai_KCB.xml) | Check-in | Dữ liệu trạng thái KCB | `checkInKcbQd4750` |
| `XML1` | [`XML1_TongHop_KCB.xml`](./XML1_TongHop_KCB.xml) | Bảng 1 | Chỉ tiêu tổng hợp khám bệnh, chữa bệnh | `guiHoSoXmlQD4750` |
| `XML2` | [`XML2_ChiTiet_Thuoc.xml`](./XML2_ChiTiet_Thuoc.xml) | Bảng 2 | Chỉ tiêu chi tiết thuốc | `guiHoSoXmlQD4750` |
| `XML3` | [`XML3_ChiTiet_DVKT_VTYT.xml`](./XML3_ChiTiet_DVKT_VTYT.xml) | Bảng 3 | Chỉ tiêu chi tiết dịch vụ kỹ thuật và vật tư y tế | `guiHoSoXmlQD4750` |
| `XML4` | [`XML4_ChiTiet_CanLamSang.xml`](./XML4_ChiTiet_CanLamSang.xml) | Bảng 4 | Chỉ tiêu chi tiết dịch vụ cận lâm sàng | `guiHoSoXmlQD4750` |
| `XML5` | [`XML5_ChiTiet_DienBienLamSang.xml`](./XML5_ChiTiet_DienBienLamSang.xml) | Bảng 5 | Chỉ tiêu chi tiết diễn biến lâm sàng | `guiHoSoXmlQD4750` |
| `XML6` | [`XML6_HoSo_HIV_AIDS.xml`](./XML6_HoSo_HIV_AIDS.xml) | Bảng 6 | Chỉ tiêu hồ sơ bệnh án chăm sóc và điều trị HIV/AIDS | `guiHoSoXmlQD4750` |
| `XML7` | [`XML7_GiayRaVien.xml`](./XML7_GiayRaVien.xml) | Bảng 7 | Chỉ tiêu dữ liệu giấy ra viện | `guiHoSoXmlQD4750` |
| `XML8` | [`XML8_TomTat_HoSoBenhAn.xml`](./XML8_TomTat_HoSoBenhAn.xml) | Bảng 8 | Chỉ tiêu dữ liệu tóm tắt hồ sơ bệnh án | `guiHoSoXmlQD4750` |
| `XML9` | [`XML9_GiayChungSinh.xml`](./XML9_GiayChungSinh.xml) | Bảng 9 | Chỉ tiêu dữ liệu giấy chứng sinh | `guiHoSoXmlQD4750` |
| `XML10` | [`XML10_GiayNghiDuongThai.xml`](./XML10_GiayNghiDuongThai.xml) | Bảng 10 | Chỉ tiêu dữ liệu giấy chứng nhận nghỉ dưỡng thai | `guiHoSoXmlQD4750` |
| `XML11` | [`XML11_GiayNghiHuongBHXH.xml`](./XML11_GiayNghiHuongBHXH.xml) | Bảng 11 | Chỉ tiêu dữ liệu giấy chứng nhận nghỉ hưởng BHXH | `guiHoSoXmlQD4750` |
| `XML12` | [`XML12_GiamDinhYKhoa.xml`](./XML12_GiamDinhYKhoa.xml) | Bảng 12 | Chỉ tiêu dữ liệu giám định y khoa | `guiHoSoXmlQD4750` |

---

*Tài liệu tham chiếu: Quyết định số 130/QĐ-BYT ngày 18/01/2023 và Quyết định số 4750/QĐ-BYT ngày 29/12/2023 của Bộ trưởng Bộ Y tế.*
