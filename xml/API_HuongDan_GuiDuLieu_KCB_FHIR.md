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
  "status": "success",
  "message": "string"
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `logId` | String | Định danh bản ghi log, dùng để tra cứu tại `GET /api/logs` |
| `status` | String | Trạng thái xử lý: `success` \| `error` \| `pending` |
| `message` | String | Thông điệp kết quả hoặc mô tả lỗi nếu có |

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
  "logId": "string",
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
  "status": "success",
  "message": "string"
}
```

| Tên trường | Kiểu dữ liệu | Mô tả |
|---|---|---|
| `logId` | String | Định danh bản ghi log, dùng để tra cứu tại `GET /api/logs` |
| `status` | String | Trạng thái xử lý: `success` \| `error` \| `pending` |
| `message` | String | Thông điệp kết quả hoặc mô tả lỗi nếu có |

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
  "logId": "string",
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

> 🚧 **Tài liệu đang được bổ sung.** Nội dung chi tiết cho các endpoint FHIR sẽ được cập nhật trong phiên bản tiếp theo.

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
      "metadata": "{\"status\":\"success\",\"message\":\"string\"}"
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
| `metadata` | String | JSON string chứa kết quả xử lý: `{"status":"success\|error\|pending","message":"..."}` |

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
