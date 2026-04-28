# Quy Trình Gửi & Chuyển Đổi Dữ Liệu KCB lên HAPI FHIR

> **Căn cứ:** QĐ 130/QĐ-BYT (hợp nhất QĐ 4750/QĐ-BYT) · Chuẩn HL7 FHIR R4B (4.3.0)  
> **Base URL:** `https://fhir.{domain}`  
> **Xác thực:** JWT Bearer Token

---

## Quy trình A — Gửi dữ liệu XML lên hệ thống

Quy trình này mô tả toàn bộ các bước từ khi chọn tệp XML cho đến khi dữ liệu được tiếp nhận thành công vào hệ thống.

---

### Bước 1 — Chọn & xác định tệp XML cần gửi

Hệ thống nhận 2 luồng gửi riêng biệt:

| Luồng | Loại tệp | Mô tả |
|---|---|---|
| **Luồng A** | `XML0` | Trạng thái KCB — check-in khi bệnh nhân đến khám |
| **Luồng B** | `XML1–XML11` | Hồ sơ KCB đầy đủ — đóng gói trong wrapper GIAMDINHHS |

**Danh sách tệp XML con (Luồng B):**

| Mã | Nội dung |
|---|---|
| XML1 | Tổng hợp KCB (Bảng 1) |
| XML2 | Chi tiết thuốc (Bảng 2) |
| XML3 | Chi tiết DVKT & VTYT (Bảng 3) |
| XML4 | Chi tiết cận lâm sàng (Bảng 4) |
| XML5 | Diễn biến lâm sàng (Bảng 5) |
| XML6 | Hồ sơ HIV/AIDS (Bảng 6) |
| XML7 | Giấy ra viện (Bảng 7) |
| XML8 | Tóm tắt hồ sơ bệnh án (Bảng 8) |
| XML9 | Giấy chứng sinh (Bảng 9) |
| XML10 | Giấy nghỉ dưỡng thai (Bảng 10) |
| XML11 | Giấy nghỉ hưởng BHXH (Bảng 11) |

> **Lưu ý:** Encoding bắt buộc là **UTF-8**. Ký số đơn vị (SHA256) là bắt buộc trước khi mã hóa Base64.

---

### Bước 2 — Xác thực & lấy JWT token

Mọi request đều yêu cầu header `Authorization: Bearer {access_token}`.

**Endpoint:** `POST https://fhir.{domain}/api/auth/login`

**Headers:** `Content-Type: application/json`

**Request Body:**
```json
{
  "username": "your_username",
  "password": "MD5_UPPERCASE(your_password)"
}
```

> ⚠️ Mật khẩu phải được mã hóa **MD5 Uppercase** trước khi gửi.

**Response thành công (HTTP 200):**
```json
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": "2024-07-01T00:00:00Z",
  "username": "string"
}
```

**Khi token hết hạn — làm mới token:**
```
POST /api/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token&refresh_token={refresh_token}
```

---

### Bước 3 — Chuẩn bị tệp XML0 (check-in trạng thái KCB)

**Cấu trúc XML0:**
```xml
<CHI_TIEU_TRANG_THAI_KCB>
  <DSACH_TRANG_THAI_KCB>
    <TRANG_THAI_KCB>
      <MA_LK>...</MA_LK>
      <MA_CSKCB>...</MA_CSKCB>
      <MA_BN>...</MA_BN>
      <NGAY_VAO>yyyyMMddHHmm</NGAY_VAO>
      <!-- ... các trường khác ... -->
    </TRANG_THAI_KCB>
  </DSACH_TRANG_THAI_KCB>
</CHI_TIEU_TRANG_THAI_KCB>
<CHUKYDONVI>[Chữ ký SHA256]</CHUKYDONVI>
```

**Quy trình chuẩn bị XML0:**

1. Tạo nội dung XML0 theo cấu trúc `CHI_TIEU_TRANG_THAI_KCB`
2. Ký số SHA256 vùng từ `<CHI_TIEU_TRANG_THAI_KCB>` đến `</DSACH_TRANG_THAI_KCB>`, điền vào thẻ `<CHUKYDONVI>`
3. Mã hóa toàn bộ nội dung XML thành chuỗi **Base64**

---

### Bước 4 — Gửi XML0 lên endpoint check-in

**Endpoint:** `POST https://fhir.{domain}/api/qd130/checkInKcbQd4750`

```
Authorization: Bearer {access_token}
Content-Type: application/x-www-form-urlencoded

fileHSBase64={chuỗi_base64_của_XML0}
```

**Response thành công (HTTP 200):**
```json
{
  "logId": "abc-123",
  "metadata": {
    "status": "success",
    "message": "Check-in thành công",
    "code": "200"
  }
}
```

| HTTP Status | Nguyên nhân | Xử lý |
|---|---|---|
| 200 | Thành công | Lưu `logId` để tra cứu |
| 401 | Token hết hạn | Làm mới token (bước 2) |
| 403 | Không có quyền | Liên hệ admin |
| 422 | XML không hợp lệ | Kiểm tra cấu trúc XML0 |

> ✅ Lưu **logId** để tra cứu trạng thái sau qua `GET /api/logs`.

---

### Bước 5 — Chuẩn bị XML wrapper GIAMDINHHS

Đóng gói tất cả XML con (XML1–XML11) vào wrapper `GIAMDINHHS`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<GIAMDINHHS>
  <THONGTINDONVI>
    <MACSKCB>{Mã CSKCB}</MACSKCB>
  </THONGTINDONVI>
  <THONGTINHOSO>
    <NGAYLAP>{yyyyMMdd}</NGAYLAP>
    <SOLUONGHOSO>{Số lượng hồ sơ}</SOLUONGHOSO>
    <DANHSACHHOSO>
      <HOSO>
        <FILEHOSO>
          <LOAIHOSO>XML1</LOAIHOSO>
          <NOIDUNGFILE>{Base64 của XML1}</NOIDUNGFILE>
        </FILEHOSO>
        <!-- Thêm FILEHOSO cho XML2, XML3... -->
      </HOSO>
    </DANHSACHHOSO>
  </THONGTINHOSO>
  <CHUKYDONVI/> <!-- SHA256 từ THONGTINDONVI đến /THONGTINHOSO -->
</GIAMDINHHS>
```

**Quy trình đóng gói:**

1. Với mỗi XML con (XML1–XML11): mã hóa **Base64** → điền vào `<NOIDUNGFILE>`
2. Điền `NGAYLAP` (định dạng **yyyyMMdd**) và `SOLUONGHOSO`
3. Ký số **SHA256** vùng từ `<THONGTINDONVI>` đến `</THONGTINHOSO>`, điền vào `<CHUKYDONVI/>`
4. Mã hóa toàn bộ tệp GIAMDINHHS thành chuỗi **Base64**

---

### Bước 6 — Gửi hồ sơ KCB lên hệ thống

**Endpoint:** `POST https://fhir.{domain}/api/qd130/guiHoSoXmlQD4750`

```
Authorization: Bearer {access_token}
Content-Type: application/x-www-form-urlencoded

fileHSBase64={chuỗi_base64_của_GIAMDINHHS}
```

**Response thành công (HTTP 200):**
```json
{
  "logId": "xyz-456",
  "metadata": {
    "status": "success | pending | error",
    "message": "Hồ sơ đã được tiếp nhận",
    "code": "200"
  }
}
```

> ⚠️ `metadata.status = "pending"` có nghĩa hệ thống đã tiếp nhận nhưng đang xử lý. Cần kiểm tra lại bằng `logId`.

---

### Bước 7 — Kiểm tra kết quả

**Endpoint:** `GET https://fhir.{domain}/api/logs?fromDate=yyyyMMdd&toDate=yyyyMMdd&id={logId}`

| `metadata.status` | Ý nghĩa | Hành động |
|---|---|---|
| `success` | Dữ liệu đã vào HAPI FHIR | Hoàn tất |
| `pending` | Đang xử lý | Kiểm tra lại sau vài phút |
| `error` | Xử lý thất bại | Xem thông điệp lỗi, sửa và gửi lại |

---

## Quy trình B — Chuyển đổi dữ liệu XML → FHIR JSON Bundle → HAPI FHIR

Quy trình này mô tả luồng xử lý nội bộ từ khi hệ thống nhận payload Base64, giải mã, phân tích XML, chuyển đổi sang FHIR resources, đóng gói Bundle và nạp vào HAPI FHIR.

---

### Giai đoạn 1 — Tiếp nhận & giải mã

**1.1 Nhận payload Base64 từ request**

Hệ thống nhận trường `fileHSBase64` qua `application/x-www-form-urlencoded`. Đây là chuỗi Base64 của toàn bộ tệp XML wrapper GIAMDINHHS (hoặc XML0 với check-in).

**1.2 Giải mã Base64 → XML bytes**

```
fileHSBase64 (string)
  → Base64 decode
  → raw XML bytes (UTF-8)
```

**1.3 Parse XML → DOM tree**

Hệ thống phân tích cú pháp XML, xây dựng cây DOM. Nếu XML không hợp lệ → trả về `HTTP 422 Unprocessable Entity`.

**1.4 Xác thực chữ ký số**

Kiểm tra SHA256 trong thẻ `<CHUKYDONVI>` khớp với nội dung đã ký.

---

### Giai đoạn 2 — Trích xuất & tách XML con

**2.1 Đọc thông tin đơn vị**

Trích xuất `MACSKCB`, `NGAYLAP`, `SOLUONGHOSO` từ header wrapper.

**2.2 Duyệt danh sách `FILEHOSO`**

Với mỗi `<FILEHOSO>`:
- Đọc `<LOAIHOSO>` → xác định loại (XML1, XML2, ...)
- Đọc `<NOIDUNGFILE>` → giải mã **Base64** → XML con tương ứng

**2.3 Parse từng XML con**

Mỗi XML con được parse thành cấu trúc dữ liệu riêng theo schema của bảng tương ứng (Bảng 1–11).

---

### Giai đoạn 3 — Ánh xạ XML → FHIR Resources

Mỗi bảng XML được ánh xạ sang một hoặc nhiều FHIR resource type:

| XML con | FHIR Resource(s) chính |
|---|---|
| XML1 — Tổng hợp KCB | `Patient`, `Encounter`, `Claim`, `ClaimResponse`, `Coverage` |
| XML2 — Chi tiết thuốc | `Medication`, `MedicationRequest`, `MedicationDispense` |
| XML3 — DVKT & VTYT | `ServiceRequest`, `Procedure`, `ChargeItem`, `Device` |
| XML4 — Cận lâm sàng | `ServiceRequest`, `DiagnosticReport`, `Observation` |
| XML5 — Diễn biến LS | `ClinicalImpression`, `Observation` |
| XML6 — HIV/AIDS | `Condition`, `EpisodeOfCare`, `MedicationStatement` |
| XML7 — Giấy ra viện | `Encounter` (discharge), `Composition` |
| XML8 — Tóm tắt HSBA | `Composition`, `DocumentReference` |
| XML9 — Chứng sinh | `Patient` (newborn), `Observation` |
| XML10 — Nghỉ dưỡng thai | `Condition`, `DocumentReference` |
| XML11 — Nghỉ hưởng BHXH | `Condition`, `DocumentReference`, `Claim` |

**Quy tắc ánh xạ trường:**

- Mã định danh (`MA_LK`, `MA_BN`, `MA_CSKCB`) → `Resource.identifier[]`
- Mã danh mục (`MA_BENH`, `MA_DVKT`) → `CodeableConcept.coding[]` với CodeSystem tương ứng
- Ngày giờ (`NGAY_VAO`, `NGAY_RA`) → FHIR `dateTime` (ISO 8601)
- Tiền tệ (`T_BHTT`, `T_BNTT`) → `Money` với `currency: "VND"`
- Reference nội bộ → `resource:MA_LK` làm khóa liên kết tạm thời trong Bundle

---

### Giai đoạn 4 — Làm giàu dữ liệu (Data Enrichment)

Dữ liệu XML chỉ chứa mã số, cần bổ sung thông tin ngữ nghĩa từ các nguồn phụ:

**4.1 Tra cứu CodeSystem**

Giải mã các mã danh mục (ICD-10, DVKT, thuốc, tỉnh) từ `CodeSystem` đã nạp trước:
- `icd-10-vn` — mã bệnh ICD-10 tiếng Việt
- `dvkt-vn` — danh mục dịch vụ kỹ thuật (~30.000 dịch vụ)
- `thuoc-vn` — danh mục thuốc / ATC WHO

**4.2 Resolve Organization reference**

Ánh xạ `MA_CSKCB`, `MA_KHOA` → `Organization/{id}` đã tồn tại trong HAPI FHIR.

**4.3 Resolve Practitioner reference**

Ánh xạ `MA_BAC_SI`, `NGUOI_THUC_HIEN` → `Practitioner/{id}` đã tồn tại.

---

### Giai đoạn 5 — Đóng gói FHIR Bundle

**5.1 Tạo Bundle transaction**

Tất cả FHIR resources từ một hồ sơ KCB (`MA_LK`) được đóng gói vào một `Bundle` kiểu `transaction`:

```json
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "fullUrl": "urn:uuid:{uuid-patient}",
      "resource": { "resourceType": "Patient", ... },
      "request": { "method": "PUT", "url": "Patient?identifier=MA_BN" }
    },
    {
      "fullUrl": "urn:uuid:{uuid-encounter}",
      "resource": { "resourceType": "Encounter", ... },
      "request": { "method": "PUT", "url": "Encounter?identifier=MA_LK" }
    }
    // ... các resource khác
  ]
}
```

**5.2 Thiết lập internal references**

Các reference nội bộ trong Bundle sử dụng `urn:uuid:` để liên kết tạm thời, HAPI FHIR sẽ giải quyết sau khi commit.

**5.3 Xác thực Bundle**

Kiểm tra tính toàn vẹn: required fields, reference hợp lệ, kiểu dữ liệu, cardinality theo FHIR R4B profile.

---

### Giai đoạn 6 — Nạp Bundle vào HAPI FHIR

**6.1 POST Bundle lên HAPI FHIR**

```
POST https://fhir.{domain}/fhir
Content-Type: application/fhir+json
Authorization: Bearer {access_token}

{Bundle JSON}
```

HAPI FHIR xử lý transaction theo cơ chế **all-or-nothing**: nếu bất kỳ resource nào thất bại, toàn bộ transaction bị rollback.

**6.2 Nhận phản hồi từ HAPI FHIR**

HAPI FHIR trả về `Bundle` kết quả (type = `transaction-response`) với `OperationOutcome` cho từng entry.

**6.3 Ghi log kết quả**

Hệ thống ghi log với `logId` và trả về response cuối cho client:

```json
{
  "logId": "xyz-456",
  "metadata": {
    "resourceType": "OperationOutcome",
    "issue": [
      {
        "severity": "information",
        "code": "informational",
        "diagnostics": "Bundle transaction completed: N created, M updated"
      }
    ]
  }
}
```

---

### Giai đoạn 7 — Bổ sung dữ liệu sau import (FHIR PATCH)

Sau khi import XML thành công, một số resource cần bổ sung thông tin từ nguồn ngoài:

| Resource | Endpoint PATCH | Dữ liệu bổ sung |
|---|---|---|
| `Coverage` | `PATCH /api/fhir/Coverage/{id}` | `subscriber`, `subscriberId`, `beneficiary`, `payor` |
| `Medication` | `PATCH /api/fhir/Medication/{id}` | Mã ATC (WHO), tên INN (Cục Quản lý Dược) |
| `ClaimResponse` | `PATCH /api/fhir/ClaimResponse/{id}` | `status`, `outcome`, `processNote` (kết quả BHXH) |

Các PATCH này dùng định dạng **JSON Patch** (`Content-Type: application/json-patch+json`).

---

## Tóm tắt luồng tổng thể

```
[Client]
  │
  ├─ Luồng A ─────────────────────────────────────────────────────────┐
  │  XML0 → Ký SHA256 → Base64 → POST checkInKcbQd4750               │
  │                                                                    ▼
  └─ Luồng B ─────────────────────────────────────────────────────────┤
     XML1..11 → Base64 từng file → Wrapper GIAMDINHHS → Ký SHA256    │
     → Base64 wrapper → POST guiHoSoXmlQD4750                        │
                                                                      │
[Server — Quy trình B]                                               │
  │                                                                    │
  ├─ 1. Nhận payload ◄──────────────────────────────────────────────┘
  ├─ 2. Decode Base64 → XML bytes
  ├─ 3. Parse XML → DOM → Xác thực chữ ký
  ├─ 4. Tách XML con → Giải mã Base64 từng NOIDUNGFILE
  ├─ 5. Ánh xạ XML → FHIR Resources (Patient, Encounter, Claim...)
  ├─ 6. Làm giàu dữ liệu (CodeSystem, Organization, Practitioner)
  ├─ 7. Đóng gói → FHIR Bundle (transaction)
  ├─ 8. Validate Bundle → POST vào HAPI FHIR
  ├─ 9. Ghi log → Trả logId về client
  └─ 10. (Không đồng bộ) PATCH Coverage / Medication / ClaimResponse
```

---

*Tài liệu tham chiếu: QĐ 130/QĐ-BYT ngày 18/01/2023, QĐ 4750/QĐ-BYT ngày 29/12/2023, HL7 FHIR R4B (4.3.0)*
