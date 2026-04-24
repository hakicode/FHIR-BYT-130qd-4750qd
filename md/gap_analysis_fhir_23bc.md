# Báo Cáo Phân Tích: Dữ Liệu FHIR Còn Thiếu Để Thực Hiện Đủ 23 Báo Cáo

> **Phạm vi phân tích:** So sánh dữ liệu có thể extract từ QĐ 130/QĐ-BYT + QĐ 4750/QĐ-BYT  
> với yêu cầu dữ liệu đầy đủ của 23 Báo cáo Power BI Y tế theo chuẩn HL7 FHIR R4B (4.3.0)  
> **Ngày lập:** 2024  
> **Kết luận nhanh:** 21/23 báo cáo chạy được ở mức cơ bản từ QĐ 130+4750.  
> 2 báo cáo cần nguồn dữ liệu ngoài hoàn toàn (BC03, BC04).  
> 10 báo cáo cần bổ sung dữ liệu ngoài để đạt chất lượng đầy đủ.

---

## Phần I — Phân Loại Trạng Thái 23 Báo Cáo

| # | Báo cáo | Trạng thái | Nguồn thiếu chính |
|:---:|---|:---:|---|
| 01 | Danh mục Bệnh viện | ⚠️ Thiếu một phần | Tên BV, địa chỉ BV — từ DMDC |
| 02 | Danh mục Khoa | ⚠️ Thiếu một phần | Tên khoa — từ DMDC |
| 03 | Danh mục Bệnh ICD | ❌ Không có | CodeSystem ICD-10 tiếng Việt |
| 04 | Danh mục Nhà thuốc | ❌ Không có | Dữ liệu nhà thuốc từ Cục QLD |
| 05 | Số Giường | ⚠️ Thiếu một phần | Tổng giường kế hoạch từ HIS |
| 06 | Tổng Số Ngày Điều Trị | ✅ Đủ | — |
| 07 | Thống Kê Chi Phí | ✅ Đủ | — |
| 08 | Lượt BN Vào Ra | ✅ Đủ | — |
| 09 | BN theo Loại Hình KCB | ✅ Đủ | — |
| 10 | Ca Cấp Cứu Tử Vong | ⚠️ Thiếu một phần | Dấu hiệu sinh tồn chuẩn hóa |
| 11 | Số Hồ Sơ KCB | ✅ Đủ | — |
| 12 | Thống Kê Tai Nạn | ⚠️ Thiếu một phần | bodySite, severity, onsetDateTime |
| 13 | Thống Kê theo Tuổi | ✅ Đủ | — |
| 14 | Thống Kê theo Khoa | ⚠️ Thiếu một phần | Tên khoa từ DMDC |
| 15 | Lượt Sử Dụng DVKT | ⚠️ Thiếu một phần | ServiceRequest.category (suy luận) |
| 16 | Ca Mắc theo ICD | ⚠️ Thiếu một phần | Tên bệnh ICD tiếng Việt |
| 17 | Số Đơn Thuốc | ✅ Đủ | — |
| 18 | Top 20 Bệnh ICD | ⚠️ Thiếu một phần | Tên bệnh ICD tiếng Việt |
| 19 | Điều Trị Nội Trú | ✅ Đủ | — |
| 20 | Ngày ĐT theo Ngày | ✅ Đủ | — |
| 21 | Chi Phí theo Ngày | ✅ Đủ | — |
| 22 | Nội Trú theo Ngày | ✅ Đủ | — |
| 23 | Hồ Sơ KCB theo Ngày Ra | ✅ Đủ | — |

---

## Phần II — Chi Tiết Gap Theo Từng Báo Cáo

---

### Báo Cáo 01 — Danh Mục Bệnh Viện ⚠️

**Resource FHIR:** `Organization` (type=`prov`)  
**Endpoint nạp dữ liệu:** `POST /Organization`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `Organization.identifier[0].value` | B1(58), Checkin(18) | `MA_CSKCB` — Chuỗi(5) |

#### Trường còn thiếu — cần bổ sung từ nguồn ngoài

| Trường FHIR | Kiểu | Bắt buộc | Mô tả còn thiếu | Nguồn bổ sung |
|---|---|:---:|---|---|
| `Organization.name` | string | ✅ | **Tên đầy đủ bệnh viện** | Bộ mã DMDC QĐ 5937/QĐ-BYT (Phụ lục 4) |
| `Organization.alias[]` | string[] | ⚪ | Tên viết tắt | DMDC QĐ 5937 |
| `Organization.type[0].coding.code` | code | ✅ | Hạng BV (I/II/III/IV) | DMDC QĐ 5937 |
| `Organization.address[0].text` | string | ⚪ | Địa chỉ BV | DMDC QĐ 5937 |
| `Organization.address[0].state` | string | ⚪ | Tỉnh/thành | DMDC QĐ 5937 |
| `Organization.telecom[0].value` | string | ⚪ | SĐT, email, website | DMDC QĐ 5937 |
| `Organization.partOf` | Reference | ⚪ | Sở Y tế chủ quản | DMDC QĐ 5937 + Phân cấp |
| `Organization.active` | boolean | ✅ | Trạng thái hoạt động | Mặc định `true` |

#### Cách nạp dữ liệu

```
Bước 1: Lấy danh sách MA_CSKCB unique từ Bảng 1 / Checkin
Bước 2: JOIN với bảng DMDC QĐ 5937/QĐ-BYT (Phụ lục 4) để lấy tên, địa chỉ, hạng BV
Bước 3: POST từng Organization lên FHIR server

Endpoint: POST /Organization
Content-Type: application/fhir+json

{
  "resourceType": "Organization",
  "id": "org-{MA_CSKCB}",
  "identifier": [{ "system": "https://moh.gov.vn/cskcb", "value": "{MA_CSKCB}" }],
  "active": true,
  "type": [{ "coding": [{ "code": "prov" }] }],
  "name": "{TEN_CSKCB}",      ← từ DMDC
  "address": [{ "text": "{DIA_CHI_BV}" }]  ← từ DMDC
}
```

---

### Báo Cáo 02 — Danh Mục Khoa ⚠️

**Resource FHIR:** `Organization` (type=`dept`) + `Location`  
**Endpoint nạp dữ liệu:** `POST /Organization`, `POST /Location`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `Organization.identifier[0].value` | B1(57), B2(31), B3(31) | `MA_KHOA` — Chuỗi(50) |
| `Organization.partOf` | B1(58) | `MA_CSKCB` — suy luận |
| `Location.name` | B3(32) | `MA_GIUONG` — mã giường |
| `Location.managingOrganization` | B3(31) | `MA_KHOA` |

#### Trường còn thiếu

| Trường FHIR | Kiểu | Bắt buộc | Mô tả | Nguồn bổ sung |
|---|---|:---:|---|---|
| `Organization.name` | string | ✅ | **Tên đầy đủ khoa** | DMDC QĐ 5937 (Phụ lục 5) |
| `Organization.type[0].coding.code` | code | ✅ | `dept` — cố định | Giá trị cố định |
| `Location.physicalType.code` | code | ✅ | `bd` (bed) / `ro` (room) | Suy luận từ tiền tố MA_GIUONG |
| `Location.partOf` | Reference | ⚪ | Phòng chứa giường | Không có trong QĐ 130+4750 |
| `Location.status` | code | ✅ | `active` | Mặc định `active` |

#### Cách nạp dữ liệu

```
Bước 1: Tạo Organization(dept) từ MA_KHOA unique + JOIN DMDC Phụ lục 5
Bước 2: Tạo Location(bed) từ MA_GIUONG unique trong Bảng 3
Bước 3: Liên kết Location.managingOrganization → Organization(khoa)

Phân tích MA_GIUONG → physicalType:
  H??? = Giường kế hoạch    → physicalType = bd
  T??? = Giường kê thêm     → physicalType = bd
  C??? = Giường tự chọn     → physicalType = bd
  K??? = Giường khác        → physicalType = bd

POST /Organization  (cho mỗi khoa)
POST /Location      (cho mỗi giường, mỗi phòng)
```

---

### Báo Cáo 03 — Danh Mục Bệnh ICD ❌

**Resource FHIR:** `CodeSystem` + `ValueSet`  
**Endpoint nạp dữ liệu:** `PUT /CodeSystem/icd-10-vn`, `PUT /ValueSet/icd-10-active`

#### Trạng thái

QĐ 130 + 4750 **không định nghĩa** CodeSystem ICD-10. Chỉ sử dụng mã (tham chiếu) trong các trường `MA_BENH_CHINH`, `MA_BENH_KT`, `MA_BENH_YHCT`. Cần import hoàn toàn từ nguồn ngoài.

#### Toàn bộ trường cần bổ sung từ nguồn ngoài

| Trường FHIR | Kiểu | Mô tả | Nguồn |
|---|---|---|---|
| `CodeSystem.url` | uri | `http://hl7.org/fhir/sid/icd-10` | Cố định theo FHIR |
| `CodeSystem.version` | string | Phiên bản ICD-10 VN | QĐ 4469/QĐ-BYT (28/10/2020) |
| `CodeSystem.name` | string | `ICD-10-VN` | — |
| `CodeSystem.status` | code | `active` | — |
| `CodeSystem.content` | code | `complete` | — |
| `CodeSystem.concept[N].code` | code | Mã ICD-10 (vd: `I21.0`) | **QĐ 4469/QĐ-BYT** |
| `CodeSystem.concept[N].display` | string | **Tên bệnh tiếng Việt** (vd: "Nhồi máu cơ tim cấp thành trước") | **QĐ 4469/QĐ-BYT** |
| `CodeSystem.concept[N].definition` | string | Mô tả định nghĩa | QĐ 4469/QĐ-BYT |
| `ValueSet.compose.include.system` | uri | Hệ thống mã ICD | Kế thừa CodeSystem |
| Mã YHCT | code | Theo danh mục BYT YHCT | QĐ 26/2022/QĐ-BYT |

#### Cách nạp dữ liệu

```
Bước 1: Tải file bảng mã ICD-10 từ QĐ 4469/QĐ-BYT (định dạng CSV/Excel)
Bước 2: Chuyển đổi sang FHIR CodeSystem JSON
Bước 3: Upload lên FHIR Terminology Server

PUT /CodeSystem/icd-10-vn
PUT /ValueSet/icd-10-active
POST /CodeSystem/$validate-code   ← kiểm tra sau khi nạp

Lưu ý quan trọng:
  - CodeSystem ICD-10 có ~14.000 mã — upload hàng loạt (batch)
  - Dùng Transaction Bundle: POST /  với resourceType = Bundle, type = transaction
  - Cập nhật khi BYT ban hành phiên bản mới
```

---

### Báo Cáo 04 — Danh Mục Nhà Thuốc ❌

**Resource FHIR:** `Organization` (type=`pharm`) + `Location`  
**Endpoint nạp dữ liệu:** `POST /Organization`

#### Trạng thái

QĐ 130 + 4750 **không có** bảng danh mục nhà thuốc. Trường `MA_CSKCB_THUOC` trong Bảng 2 chỉ là mã CSKCB đặc biệt (vận chuyển máu, thuốc chuyển thiên tai), không phải danh mục nhà thuốc đầy đủ.

#### Toàn bộ trường cần bổ sung

| Trường FHIR | Kiểu | Mô tả | Nguồn |
|---|---|---|---|
| `Organization.identifier[0].value` | string | **Số giấy phép kinh doanh dược** | Cục Quản lý Dược — BYT |
| `Organization.name` | string | **Tên nhà thuốc/khoa dược** | Cục QLD / HIS module kho dược |
| `Organization.type[0].coding.code` | code | `pharm` | Cố định |
| `Organization.address` | Address | Địa chỉ nhà thuốc | Cục QLD / HIS |
| `Organization.telecom` | ContactPoint | SĐT, email | HIS |
| `Organization.partOf` | Reference | BV/khoa dược chủ quản | HIS |
| `Location.hoursOfOperation` | BackboneElement | Giờ mở cửa | HIS |

#### Cách nạp dữ liệu

```
Nguồn dữ liệu: 
  - Cục Quản lý Dược (https://dav.gov.vn) — danh sách cơ sở bán lẻ thuốc
  - Module kho dược trong HIS bệnh viện

POST /Organization   (cho từng nhà thuốc/khoa dược)
```

---

### Báo Cáo 05 — Số Giường ⚠️

**Resource FHIR:** `Location` (physicalType=`bd`)  
**Endpoint nạp dữ liệu:** `POST /Location`, `PUT /Location/{id}`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Ghi chú |
|---|---|---|
| `Location.name` | `MA_GIUONG` — B3(32) | Chỉ biết giường đã từng sử dụng |
| `Location.managingOrganization` | `MA_KHOA` — B3(31) | |
| `operationalStatus = O` | Suy luận từ Encounter.status=`in-progress` | Giường đang dùng |

#### Trường còn thiếu — vấn đề cốt lõi

| Trường FHIR | Kiểu | Bắt buộc | Mô tả | Nguồn bổ sung |
|---|---|:---:|---|---|
| **Tổng số giường kế hoạch** | — | ✅ | **QĐ 130+4750 chỉ biết giường đã dùng, không biết tổng số giường được phân bổ** | **Kế hoạch giường BV — HIS** |
| `Location.status` | code | ✅ | `active` / `inactive` / `suspended` | HIS module giường bệnh |
| `Location.operationalStatus` | Coding | ⚪ | `O`(Occupied)/`U`(Unoccupied)/`K`(Contaminated) | Cập nhật realtime từ HIS |
| `Location.partOf` | Reference | ⚪ | Phòng chứa giường | HIS |

#### Giải pháp & Cách nạp

```
Vấn đề: MA_GIUONG H001 trong Bảng 3 chỉ xuất hiện khi có BN dùng giường đó.
         → Không thể biết tổng giường BV chỉ từ QĐ 130+4750.

Giải pháp:
  1. Nạp trước (seed): Danh sách toàn bộ giường từ HIS → POST /Location
  2. Cập nhật trạng thái: Dựa vào Encounter.location để cập nhật operationalStatus
  3. PUT /Location/{id} khi Encounter.status đổi sang in-progress / finished

Dữ liệu seed cần thiết từ HIS:
  - Tổng giường kế hoạch (H prefix)
  - Tổng giường kê thêm (T prefix)
  - Phân bổ giường theo khoa

POST /Location  ← nạp danh mục giường từ HIS
```

---

### Báo Cáo 06 — Tổng Số Ngày Điều Trị ✅

**Tất cả trường đủ từ QĐ 130 + 4750.**  
Không cần bổ sung dữ liệu ngoài. Chỉ cần nạp Bảng 1 XML → `Encounter` FHIR.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← từ Bảng 1 XML (MA_LK, NGAY_VAO, NGAY_RA, SO_NGAY_DTRI, MA_LOAI_KCB...)
POST /Patient      ← từ Bảng 1 XML (MA_BN, HO_TEN, NGAY_SINH, GIOI_TINH...)
POST /Coverage     ← từ Bảng 1 XML (MA_THE_BHYT, GT_THE_TU, GT_THE_DEN...)
```

---

### Báo Cáo 07 — Thống Kê Chi Phí ✅

**Tất cả trường tài chính đủ từ QĐ 130 + 4750.**

#### Endpoint nạp dữ liệu chính

```
POST /Claim         ← từ B1 (MA_LK, T_TONGCHI_BV, T_TONGCHI_BH, NAM_QT, THANG_QT...)
                    ← từ B2 (MA_THUOC, SO_LUONG, DON_GIA, THANH_TIEN_BV, THANH_TIEN_BH...)
                    ← từ B3 (MA_DICH_VU, SO_LUONG, DON_GIA_BV, DON_GIA_BH...)
POST /ClaimResponse ← từ B1 (T_BHTT, T_BNCCT, T_BNTT)
POST /Coverage      ← từ B1 (MA_THE_BHYT, MA_DOITUONG_KCB, MA_KHUVUC, MUC_HUONG)
POST /Invoice       ← tổng hợp chi phí theo đợt
```

---

### Báo Cáo 08 — Lượt BN Vào Ra ✅

**Đủ dữ liệu.** Cải thiện thêm từ QĐ 4750: `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT`.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← B1 + Checkin (NGAY_VAO, NGAY_RA, NGAY_VAO_NOI_TRU, MA_LOAI_KCB,
                     MA_NOI_DI, MA_NOI_DEN, MA_LOAI_RV, LY_DO_VNT, GIAY_CHUYEN_TUYEN)
```

---

### Báo Cáo 09 — BN theo Loại Hình KCB ✅

**Đủ dữ liệu.** Lưu ý QĐ 4750: `MA_DOITUONG_KCB` đổi thành Chuỗi(4) ở Checkin, Chuỗi(3) ở Bảng 1.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← B1 (MA_LOAI_KCB, MA_CSKCB, MA_BN, NGAY_VAO, NGAY_RA)
POST /Coverage     ← B1 (MA_THE_BHYT, MA_DOITUONG_KCB, MA_DKBD)
```

---

### Báo Cáo 10 — Ca Cấp Cứu Tử Vong ⚠️

**Resource FHIR:** `Encounter` (class=EMER) + `Condition` + `Observation` (thiếu)

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `Encounter.class = EMER` | B1(56) | `MA_LOAI_KCB` = 09 hoặc `MA_DOITUONG_KCB` = 2 |
| `dischargeDisposition = exp` | B1(41) | `KET_QUA_DTRI` = 5 |
| `Encounter.period.end` | B1(37) | `NGAY_RA` |
| `Condition.code.coding.code` | B1(27,28) | `MA_BENH_CHINH`, `MA_BENH_KT` |
| `Patient.gender`, `Patient.birthDate` | B1(7,6) | `GIOI_TINH`, `NGAY_SINH` |
| `Procedure.code.coding.code` | B1(30) | `MA_PTTT_QT` (ICD-9CM) |
| `Encounter.reasonCode[1].text` | B1(23), Checkin(15) | `LY_DO_VNT` — QĐ4750 |

#### Trường còn thiếu

| Trường FHIR | Kiểu | Mô tả | Nguồn bổ sung |
|---|---|---|---|
| `Observation.code` (dấu hiệu sinh tồn) | code | **Mạch, huyết áp, SpO2, nhiệt độ** khi vào cấp cứu — là text tự do trong B5.DIEN_BIEN_LS | Chuẩn hóa B5 text → LOINC codes |
| `Observation.valueQuantity` | Quantity | Giá trị số các dấu hiệu sinh tồn | B5 text (cần NLP parse) |
| `Encounter.length` (thời gian cấp cứu) | Duration | Tổng thời gian cấp cứu | Tính từ `NGAY_VAO` → `NGAY_RA` |
| `Procedure.performedDateTime` | dateTime | Thời điểm thực hiện cấp cứu | B3(36) `NGAY_TH_YL` — có trong B3 |

#### Endpoint nạp dữ liệu

```
POST /Encounter    ← B1 (lọc MA_LOAI_KCB=09 hoặc MA_DOITUONG_KCB=2, KET_QUA_DTRI=5)
POST /Condition    ← B1 (MA_BENH_CHINH, MA_BENH_KT — ICD S/T/V-Y + mã nguyên nhân tử vong)
POST /Procedure    ← B3 (MA_PTTT_QT, NGAY_TH_YL)

Tùy chọn (cải thiện chất lượng):
POST /Observation  ← Phân tích B5.DIEN_BIEN_LS để extract sinh tồn (NLP/rule-based)
```

---

### Báo Cáo 11 — Số Hồ Sơ KCB ✅

**Đủ dữ liệu.**

#### Endpoint nạp dữ liệu chính

```
POST /EpisodeOfCare  ← B1 (MA_LK, MA_HSBA, MA_BN, MA_CSKCB, NGAY_VAO, NGAY_RA,
                           MA_LOAI_KCB, MA_BENH_CHINH, KET_QUA_DTRI, MA_TTDV)
POST /Encounter      ← B1 (liên kết về EpisodeOfCare)
```

---

### Báo Cáo 12 — Thống Kê Tai Nạn ⚠️

**Resource FHIR:** `Condition` (ICD S–Y) + `Encounter`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `Condition.code.coding.code` | B1(27) | `MA_BENH_CHINH` — lọc S00–Y99 |
| `Encounter.extension[ma-tai-nan]` | B1(34) | `MA_TAI_NAN` — phân loại TNGT/TNLĐ/TN sinh hoạt/Bạo lực |
| `Patient.gender`, `birthDate` | B1(7,6) | `GIOI_TINH`, `NGAY_SINH` |
| `Patient.address.state/district` | B1(13,14) | `MATINH_CU_TRU`, `MAHUYEN_CU_TRU` |
| `Patient.address.postalCode` | B1(15) | `MAXA_CU_TRU` — Chuỗi(3) theo QĐ4750 |

#### Trường còn thiếu

| Trường FHIR | Kiểu | Mô tả | Giải pháp |
|---|---|---|---|
| `Condition.bodySite` | CodeableConcept | Vị trí tổn thương cụ thể (Vai phải, Đầu gối trái...) | Không có trực tiếp — **Suy luận từ mã ICD S**: `S72.*` = Xương đùi, `S00.*` = Đầu... |
| `Condition.severity` | CodeableConcept | Mức độ: nhẹ/vừa/nặng | **Suy luận từ** `KET_QUA_DTRI` B1(41): 1=Khỏi→mild, 2=Đỡ→moderate, 4/5=Nặng/Tử vong→severe |
| `Condition.onsetDateTime` | dateTime | Thời điểm xảy ra tai nạn | **Xấp xỉ** bằng `NGAY_VAO` B1(35) — thường cùng ngày |
| `Observation.code` (ISS score) | code | Chỉ số nặng chấn thương (Injury Severity Score) | Không có — cần module CĐHA tích hợp |

#### Endpoint nạp dữ liệu

```
POST /Condition    ← B1 (MA_BENH_CHINH lọc S00–Y99 + suy luận bodySite, severity)
POST /Encounter    ← B1 (MA_TAI_NAN là Extension, MA_NOI_DI cho admitSource)
POST /Patient      ← B1 (thông tin nhân thân nạn nhân)

Extension MA_TAI_NAN:
{
  "url": "https://moh.gov.vn/fhir/StructureDefinition/ma-tai-nan",
  "valueCoding": {
    "code": "1",        ← MA_TAI_NAN
    "display": "Tai nạn giao thông"
  }
}
```

---

### Báo Cáo 13 — Thống Kê theo Tuổi ✅

**Đủ dữ liệu.** QĐ 4750 bổ sung thêm `NHOM_MAU`, đổi nhiều trường sang Chuỗi.

#### Endpoint nạp dữ liệu chính

```
POST /Patient      ← B1 (MA_BN, HO_TEN, NGAY_SINH, GIOI_TINH, SO_CCCD,
                         MA_QUOCTICH, MA_DANTOC, MA_NGHE_NGHIEP, DIA_CHI,
                         MATINH_CU_TRU, MAHUYEN_CU_TRU, MAXA_CU_TRU, DIEN_THOAI,
                         NHOM_MAU [QĐ4750])
POST /Encounter    ← B1 (liên kết Patient với đợt điều trị)
```

---

### Báo Cáo 14 — Thống Kê theo Khoa ⚠️

**Resource FHIR:** `Encounter` GROUP BY `serviceProvider`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `Encounter.serviceProvider` (mã) | B1(58) | `MA_CSKCB` |
| `Encounter.location[].location` (mã khoa) | B1(57) | `MA_KHOA` — split ";" |
| `Claim.total.value` | B1(47) | `T_TONGCHI_BV` |
| `Encounter.diagnosis[].condition` | B1(27) | `MA_BENH_CHINH` |

#### Trường còn thiếu

| Trường FHIR | Kiểu | Mô tả | Nguồn bổ sung |
|---|---|---|---|
| `Organization.name` | string | **Tên khoa** — cần hiển thị trên báo cáo | **DMDC QĐ 5937 Phụ lục 5** |
| `Organization.partOf` (tên BV cha) | Reference | **Tên bệnh viện** cha của khoa | DMDC QĐ 5937 Phụ lục 4 |
| Thời gian tại từng khoa | dateTime | Khi BN chuyển nhiều khoa (MA_KHOA split ";"), không biết ngày vào/ra từng khoa | B5.THOI_DIEM_DBLS — xấp xỉ |

#### Endpoint nạp dữ liệu

```
POST /Organization  ← DMDC QĐ 5937 (tên khoa, tên BV) — DỮ LIỆU BỔ SUNG
POST /Encounter     ← B1 (MA_KHOA split ";" → Encounter.location[])
POST /Condition     ← B1 (MA_BENH_CHINH — top bệnh tại khoa)
POST /Claim         ← B1 (T_TONGCHI_BV — chi phí tại khoa)
```

---

### Báo Cáo 15 — Lượt Sử Dụng DVKT ⚠️

**Resource FHIR:** `ServiceRequest` + `Procedure` + `DiagnosticReport`

#### Trường có từ QĐ 130 + 4750

| Trường FHIR | Nguồn XML | Trường XML |
|---|---|---|
| `ServiceRequest.code.coding.code` | B3(3), Checkin(19,23) | `MA_DICH_VU`, `MA_VAT_TU` [QĐ4750] |
| `ServiceRequest.authoredOn` | B3(35) | `NGAY_YL` |
| `ServiceRequest.requester` | B3(33) | `MA_BAC_SI` |
| `ServiceRequest.quantity` | B3(13) | `SO_LUONG` |
| `Procedure.performedDateTime` | B3(36) | `NGAY_TH_YL` |
| `Procedure.performer` | B3(34) | `NGUOI_THUC_HIEN` |
| `DiagnosticReport.code` | B4(3) | `MA_DICH_VU` (CLS) |
| `Observation.code` / `value` | B4(4,6,7) | `MA_CHI_SO`, `GIA_TRI`, `DON_VI_DO` |

#### Trường còn thiếu

| Trường FHIR | Kiểu | Mô tả | Giải pháp |
|---|---|---|---|
| `ServiceRequest.category` | CodeableConcept | **Nhóm dịch vụ** (XN máu/CĐHA/Thủ thuật/Tiền khám/Giường) — quan trọng để GROUP BY | **Suy luận từ tiền tố mã DVKT:** `09.*`=Laboratory; `10.*-28.*`=Imaging; `01.*-08.*`=Procedure; `TG.*`=Giường; `01.010.*`=Tiền khám |
| `ServiceRequest.priority` | code | Độ ưu tiên (routine/urgent) | Mặc định `routine` |
| `Practitioner.name` | string | Tên bác sĩ chỉ định/thực hiện | Module nhân sự HIS |
| `Device.deviceName` | string | Tên máy thực hiện | B3(42) `MA_MAY` — có nhưng mã hóa |

#### Endpoint nạp dữ liệu

```
POST /ServiceRequest  ← B3 (MA_DICH_VU, SO_LUONG, DON_GIA_BH, NGAY_YL, MA_BAC_SI,
                            MA_KHOA, MA_BENH, PP_VO_CAM + suy luận category)
POST /Procedure       ← B3 (NGAY_TH_YL, NGUOI_THUC_HIEN, MA_PTTT_QT, PP_VO_CAM)
POST /DiagnosticReport← B4 (MA_DICH_VU, NGAY_KQ, MA_BS_DOC_KQ, KET_LUAN)
POST /Observation     ← B4 (MA_CHI_SO, GIA_TRI, DON_VI_DO, NGAY_KQ)
POST /Device          ← B3 (MA_MAY, MA_HIEU_SP, TAI_SU_DUNG)
POST /ChargeItem      ← B3 (tổng hợp chi phí từng dịch vụ)

Mapping category từ tiền tố MA_DICH_VU:
  MA_DICH_VU LIKE '09.%'              → category = laboratory (108252007)
  MA_DICH_VU LIKE '10.%' - '28.%'    → category = imaging    (363679005)
  MA_DICH_VU LIKE '01.%' - '08.%'    → category = procedure  (387713003)
  MA_DICH_VU LIKE 'TG.%'             → category = room/bed
  MA_DICH_VU LIKE '01.010.%'         → category = exam (tiền khám)
```

---

### Báo Cáo 16 — Ca Mắc theo ICD ⚠️

**Resource FHIR:** `Condition`

#### Trường có từ QĐ 130 + 4750

Đủ hoàn toàn về mặt dữ liệu bệnh nhân và mã ICD. Chỉ thiếu **tên hiển thị** khi JOIN với CodeSystem.

#### Trường còn thiếu

| Trường FHIR | Kiểu | Mô tả | Nguồn bổ sung |
|---|---|---|---|
| `CodeSystem.concept[].display` | string | **Tên bệnh tiếng Việt** để hiển thị trên báo cáo | **QĐ 4469/QĐ-BYT** |

#### Endpoint nạp dữ liệu

```
POST /Condition    ← B1 (MA_BENH_CHINH, MA_BENH_KT, MA_BENH_YHCT, CHAN_DOAN_RV,
                         KET_QUA_DTRI, MA_BN, MA_LK, NGAY_RA)

Phụ thuộc:
  /CodeSystem/icd-10-vn phải có sẵn (từ BC03)
  để JOIN lấy tên bệnh hiển thị trên Power BI
```

---

### Báo Cáo 17 — Số Đơn Thuốc ✅

**Đủ dữ liệu.** QĐ 4750 bổ sung `MA_THUOC`/`TEN_THUOC` vào Checkin.

#### Endpoint nạp dữ liệu chính

```
POST /MedicationRequest  ← B2 (MA_THUOC, TEN_THUOC, HAM_LUONG, DANG_BAO_CHE,
                                LIEU_DUNG, CACH_DUNG, SO_LUONG, DON_VI_TINH,
                                DUONG_DUNG, NGAY_YL, MA_BAC_SI, MA_KHOA,
                                PHAM_VI, NGUON_CTRA, TT_THAU, SO_DANG_KY)
POST /Medication         ← B2 (MA_THUOC, TEN_THUOC, HAM_LUONG, DANG_BAO_CHE)
```

---

### Báo Cáo 18 — Top 20 Bệnh ICD ⚠️

**Tương tự BC16.** Kế thừa `Condition` — chỉ thiếu tên bệnh ICD tiếng Việt.

#### Trường còn thiếu

| Trường FHIR | Mô tả | Nguồn |
|---|---|---|
| `CodeSystem.concept[].display` | **Tên bệnh tiếng Việt** cho nhãn Top 20 | QĐ 4469/QĐ-BYT |

#### Endpoint nạp dữ liệu

```
Không cần nạp thêm — dùng lại Condition từ BC16.
Cần: /CodeSystem/icd-10-vn đã có (từ BC03)
```

---

### Báo Cáo 19 — Điều Trị Nội Trú ✅

**Đủ dữ liệu.** QĐ 4750 cải thiện thêm `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT`.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← B1 (MA_LOAI_KCB∈{03,04,06}, NGAY_VAO, NGAY_VAO_NOI_TRU,
                         NGAY_RA, SO_NGAY_DTRI, MA_KHOA, MA_CSKCB,
                         MA_NOI_DI, MA_NOI_DEN, MA_LOAI_RV, KET_QUA_DTRI,
                         LY_DO_VNT, MA_LY_DO_VNT, PP_DIEU_TRI, CAN_NANG)
POST /Condition    ← B1 (MA_BENH_CHINH, MA_BENH_KT, CHAN_DOAN_VAO, CHAN_DOAN_RV)
POST /Procedure    ← B1 (MA_PTTT_QT)
                   ← B3 (MA_DICH_VU, NGAY_TH_YL, NGUOI_THUC_HIEN, PP_VO_CAM)
POST /DocumentReference ← B7 (giấy ra viện)
POST /Composition       ← B8 (tóm tắt HSBA — chỉ MA_LOAI_KCB∈{03,04,06})
```

---

### Báo Cáo 20 — Ngày ĐT theo Ngày ✅

**Đủ dữ liệu.** QĐ 4750 cải thiện Census nhờ `NGAY_VAO_NOI_TRU` trong Checkin.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← B1 (MA_LK, NGAY_VAO, NGAY_VAO_NOI_TRU [QĐ4750], NGAY_RA,
                         SO_NGAY_DTRI, MA_LOAI_KCB, MA_CSKCB, MA_KHOA)
DimDate            ← Tạo trong Power BI (không phải FHIR resource)
```

---

### Báo Cáo 21 — Chi Phí theo Ngày ✅

**Đủ dữ liệu.**

#### Endpoint nạp dữ liệu chính

```
POST /ChargeItem   ← B2 (MA_THUOC, SO_LUONG, DON_GIA, THANH_TIEN_BV, NGAY_YL, MA_KHOA)
                   ← B3 (MA_DICH_VU, SO_LUONG, DON_GIA_BV, THANH_TIEN_BV, NGAY_YL, MA_KHOA)
POST /Claim        ← B1 (T_TONGCHI_BV, NGAY_TTOAN, NAM_QT, THANG_QT)
POST /Coverage     ← B1 (MUC_HUONG, T_BNCCT, T_BHTT)
```

---

### Báo Cáo 22 — Nội Trú theo Ngày ✅

**Đủ dữ liệu.** QĐ 4750 cải thiện Census realtime nhờ `NGAY_VAO_NOI_TRU` trong Checkin.

#### Endpoint nạp dữ liệu chính

```
POST /Encounter    ← B1 (MA_LK, NGAY_VAO, NGAY_VAO_NOI_TRU [QĐ4750 Checkin],
                         NGAY_RA, MA_LOAI_KCB∈{03,04,06}, MA_CSKCB, MA_KHOA,
                         MA_LOAI_RV, MA_NOI_DI, LY_DO_VNT [QĐ4750], MA_BENH_CHINH)
```

---

### Báo Cáo 23 — Hồ Sơ KCB theo Ngày Ra ✅

**Đủ dữ liệu.**

#### Endpoint nạp dữ liệu chính

```
POST /Encounter      ← B1 (NGAY_RA, MA_LOAI_KCB, MA_LOAI_RV, MA_BENH_CHINH,
                           MA_BN, MA_CSKCB, NGAY_TTOAN, NAM_QT, THANG_QT,
                           T_TONGCHI_BV, T_BHTT, NGAY_TAI_KHAM)
POST /EpisodeOfCare  ← B1 (MA_LK, MA_HSBA, MA_BN, MA_CSKCB, NGAY_VAO, NGAY_RA)
POST /Claim          ← B1 (T_TONGCHI_BV, T_BHTT, NGAY_TTOAN)
POST /DocumentReference ← B7 (giấy ra viện — liên kết qua MA_LK)
```

---

## Phần III — Tổng Hợp Dữ Liệu Thiếu Theo Nhóm Nguồn

---

### Nhóm 1: Từ DMDC BYT — QĐ 5937/QĐ-BYT

> **Mức độ ưu tiên: 🔴 Cao** — Ảnh hưởng đến BC01, BC02, BC14 (tên BV/khoa hiển thị)

| Dữ liệu cần | Dùng cho BC | Nội dung cần lấy | Endpoint FHIR đích |
|---|---|---|---|
| Tên đầy đủ bệnh viện | 01, 02, 14 | MA_CSKCB → TEN_CSKCB, địa chỉ, hạng BV | `POST /Organization` (type=prov) |
| Tên đầy đủ khoa | 02, 14 | MA_KHOA → TEN_KHOA, mã số khoa BYT | `POST /Organization` (type=dept) |
| Phân cấp BV → Khoa | 02, 14 | `Organization.partOf` chain | `PATCH /Organization/{id}` |

**Cách lấy:** Tải file Excel/CSV Phụ lục 4+5 từ QĐ 5937/QĐ-BYT hoặc từ API Cổng BHXH.

```
Dữ liệu seed cần POST:
  ~1.500 Organization (BV) + ~15.000 Organization (Khoa)

Endpoint:
  POST /Organization   ← từng BV/khoa
  hoặc POST /          ← Transaction Bundle (khuyến nghị cho bulk load)
    { "resourceType": "Bundle", "type": "transaction",
      "entry": [ { "request": { "method": "POST", "url": "Organization" }, "resource": {...} }, ... ]
    }
```

---

### Nhóm 2: Từ QĐ 4469/QĐ-BYT — Bảng mã ICD-10 tiếng Việt

> **Mức độ ưu tiên: 🔴 Cao** — Ảnh hưởng đến BC03, BC16, BC18 (tên bệnh hiển thị)

| Dữ liệu cần | Dùng cho BC | Nội dung | Endpoint FHIR đích |
|---|---|---|---|
| CodeSystem ICD-10 tiếng Việt | 03, 16, 18 | ~14.000 mã ICD-10 + tên tiếng Việt | `PUT /CodeSystem/icd-10-vn` |
| ValueSet ICD-10 active | 03, 16, 18 | Tập mã đang sử dụng | `PUT /ValueSet/icd-10-active` |
| Danh mục mã YHCT | 16 | Mã bệnh Y học cổ truyền | `PUT /CodeSystem/yhct-vn` |

```
Cấu trúc nạp:
  PUT /CodeSystem/icd-10-vn
  {
    "resourceType": "CodeSystem",
    "id": "icd-10-vn",
    "url": "http://hl7.org/fhir/sid/icd-10",
    "version": "QD4469-2020",
    "name": "ICD10VN",
    "title": "ICD-10 Phiên bản Việt Nam (QĐ 4469/QĐ-BYT)",
    "status": "active",
    "content": "complete",
    "concept": [
      { "code": "I21.0", "display": "Nhồi máu cơ tim cấp thành trước", ... },
      { "code": "J02.9", "display": "Viêm họng cấp không đặc hiệu", ... },
      ...
    ]
  }

Khuyến nghị: Dùng FHIR Terminology Server chuyên biệt (Ontoserver, tx.fhir.org)
để host CodeSystem lớn thay vì FHIR server chính.
```

---

### Nhóm 3: Từ HIS Bệnh Viện — Module Nhân Sự & Giường Bệnh

> **Mức độ ưu tiên: 🟡 Trung bình** — Ảnh hưởng đến BC02, BC05, BC10, BC15

| Dữ liệu cần | Dùng cho BC | Nội dung | Endpoint FHIR đích |
|---|---|---|---|
| Danh sách giường kế hoạch | 05 | Tổng số giường, phân bổ theo khoa | `POST /Location` (type=bd) |
| Phân cấp phòng → khoa | 02, 05 | `Location.partOf` chain (giường→phòng→khoa) | `PATCH /Location/{id}` |
| Bác sĩ / nhân viên y tế | 10, 15, 17 | Mã MA_BAC_SI → tên, chuyên khoa | `POST /Practitioner` |
| Vai trò nhân sự | 10, 15 | BS thuộc khoa nào, vị trí chức danh | `POST /PractitionerRole` |

```
Endpoint:
  POST /Location        ← danh mục giường từ HIS
  POST /Practitioner    ← MA_BAC_SI, MA_TTDV → tên BS, mã BHXH
  POST /PractitionerRole← PractitionerRole.organization → Organization(khoa)

Lưu ý:
  MA_BAC_SI trong Bảng 2, 3 = mã định danh y tế (mã BHXH)
  Cần tra cứu từ HIS để lấy HO_TEN bác sĩ
```

---

### Nhóm 4: Từ Cục Quản Lý Dược — Danh Sách Nhà Thuốc

> **Mức độ ưu tiên: 🟢 Thấp** — Chỉ ảnh hưởng đến BC04

| Dữ liệu cần | Dùng cho BC | Nội dung | Endpoint FHIR đích |
|---|---|---|---|
| Danh sách nhà thuốc/khoa dược | 04 | Tên, địa chỉ, giấy phép | `POST /Organization` (type=pharm) |
| Vị trí vật lý nhà thuốc | 04 | Giờ mở cửa, tọa độ | `POST /Location` |

```
Nguồn: https://dav.gov.vn — cơ sở bán lẻ thuốc
       hoặc module kho dược HIS nội bộ

Endpoint:
  POST /Organization   ← nhà thuốc/khoa dược
```

---

### Nhóm 5: Dữ Liệu Suy Luận Từ QĐ 130+4750 (Không Cần Nguồn Ngoài)

> Những trường **có thể tính/suy luận** được từ dữ liệu XML hiện có — không cần nguồn ngoài nhưng cần xử lý logic.

| Trường FHIR | BC | Cách suy luận | Độ chính xác |
|---|---|---|---|
| `ServiceRequest.category` | 15 | Tiền tố mã MA_DICH_VU: `09.*`=Lab, `10-28.*`=Imaging, v.v. | ✅ Cao |
| `Condition.severity` | 12 | KET_QUA_DTRI: 1/2→mild/moderate, 3/4→moderate/severe, 5→fatal | ⚠️ Xấp xỉ |
| `Condition.bodySite` | 12 | Nhóm ICD S: S70-S79→Đùi, S80-S89→Cẳng chân, v.v. | ⚠️ Gần đúng |
| `Condition.onsetDateTime` | 12 | Lấy NGAY_VAO làm xấp xỉ | ⚠️ Xấp xỉ |
| `Encounter.length` | 10, 06 | NGAY_RA − NGAY_VAO hoặc SO_NGAY_DTRI trực tiếp | ✅ Cao |
| `Location.operationalStatus` | 05 | Encounter.status=in-progress → Location.operationalStatus=O | ✅ Cao |
| `Encounter.class` | 06–23 | MA_LOAI_KCB: 01,02,05,07,08→AMB; 03,04,06→IMP; 09→EMER | ✅ Cao |
| `Condition.clinicalStatus` | 16 | KET_QUA_DTRI: 1,2→resolved; 3,4,7→active; 5→inactive; 6→active | ✅ Cao |

---

## Phần IV — Bảng Tổng Hợp Endpoint FHIR Cần Nạp Dữ Liệu

### IV.1 Dữ liệu từ QĐ 130 + 4750 (nạp từ XML)

| Resource | Endpoint | HTTP Method | Nguồn bảng XML | BC sử dụng | Ưu tiên |
|---|---|:---:|---|---|:---:|
| `Patient` | `/Patient` | POST | B1 (STT 1–16 + NHOM_MAU QĐ4750) | 06–23 | 🔴 1 |
| `Encounter` | `/Encounter` | POST | B1 (tất cả trường đợt KBCB) + Checkin | 06–23 | 🔴 1 |
| `Coverage` | `/Coverage` | POST | B1 (MA_THE_BHYT, MA_DKBD, GT_THE_TU/DEN, MA_DOITUONG_KCB) | 07, 09, 17 | 🔴 1 |
| `Condition` | `/Condition` | POST | B1 (MA_BENH_CHINH, MA_BENH_KT, MA_BENH_YHCT, CHAN_DOAN_*) | 10–12, 14–16, 18, 19, 23 | 🔴 1 |
| `Claim` | `/Claim` | POST | B1 (T_TONGCHI_BV, T_TONGCHI_BH, NGAY_TTOAN) + B2 + B3 | 07, 21, 23 | 🔴 1 |
| `ClaimResponse` | `/ClaimResponse` | POST | B1 (T_BHTT, T_BNCCT, T_BNTT) | 07, 23 | 🔴 1 |
| `MedicationRequest` | `/MedicationRequest` | POST | B2 (toàn bộ) + Checkin (MA_THUOC, TEN_THUOC QĐ4750) | 17 | 🔴 1 |
| `Medication` | `/Medication` | POST | B2 (MA_THUOC, TEN_THUOC, HAM_LUONG, DANG_BAO_CHE) | 17 | 🔴 1 |
| `ServiceRequest` | `/ServiceRequest` | POST | B3 (MA_DICH_VU, SO_LUONG, NGAY_YL) + Checkin (MA_VAT_TU, MA_DICH_VU) | 15 | 🟡 2 |
| `Procedure` | `/Procedure` | POST | B3 (MA_PTTT_QT, NGAY_TH_YL, NGUOI_THUC_HIEN, PP_VO_CAM) + B1(30) | 10, 15, 19 | 🟡 2 |
| `DiagnosticReport` | `/DiagnosticReport` | POST | B4 (MA_DICH_VU, NGAY_KQ, KET_LUAN, MA_BS_DOC_KQ) | 15 | 🟡 2 |
| `Observation` | `/Observation` | POST | B4 (MA_CHI_SO, GIA_TRI, DON_VI_DO) | 10, 15 | 🟡 2 |
| `ChargeItem` | `/ChargeItem` | POST | B2 + B3 (SO_LUONG, DON_GIA, THANH_TIEN_BV, NGAY_YL, MA_KHOA) | 21 | 🟡 2 |
| `EpisodeOfCare` | `/EpisodeOfCare` | POST | B1 (MA_LK, MA_HSBA, NGAY_VAO, NGAY_RA, MA_BENH_CHINH) | 11, 23 | 🟡 2 |
| `Location` (giường dùng) | `/Location` | POST | B3 (MA_GIUONG, MA_KHOA) | 05, 19 | 🟡 2 |
| `DocumentReference` | `/DocumentReference` | POST | B7 (giấy ra viện — CHAN_DOAN_RV, PP_DIEUTRI, SO_NGAY_NGHI) | 19, 23 | 🟢 3 |
| `Composition` | `/Composition` | POST | B8 (tóm tắt HSBA — QT_BENHLY, TOMTAT_KQ, PP_DIEUTRI) | 19 | 🟢 3 |
| `ClinicalImpression` | `/ClinicalImpression` | POST | B5 (DIEN_BIEN_LS, GIAI_DOAN_BENH, HOI_CHAN, PHAU_THUAT) | 10 | 🟢 3 |
| `Device` | `/Device` | POST | B3 (MA_MAY, MA_HIEU_SP, TAI_SU_DUNG) | 15 | 🟢 3 |

### IV.2 Dữ liệu từ nguồn ngoài (nạp seed/reference data)

| Resource | Endpoint | HTTP Method | Nguồn bên ngoài | BC sử dụng | Ưu tiên |
|---|---|:---:|---|---|:---:|
| `Organization` (BV) | `/Organization` | POST (bulk) | **DMDC QĐ 5937 Phụ lục 4** | 01, 02, 14 | 🔴 1 |
| `Organization` (Khoa) | `/Organization` | POST (bulk) | **DMDC QĐ 5937 Phụ lục 5** | 02, 14 | 🔴 1 |
| `CodeSystem` (ICD-10) | `/CodeSystem/icd-10-vn` | PUT | **QĐ 4469/QĐ-BYT** | 03, 16, 18 | 🔴 1 |
| `ValueSet` (ICD-10) | `/ValueSet/icd-10-active` | PUT | QĐ 4469/QĐ-BYT | 03, 16, 18 | 🔴 1 |
| `CodeSystem` (YHCT) | `/CodeSystem/yhct-vn` | PUT | QĐ 26/2022/QĐ-BYT | 16 | 🟡 2 |
| `Location` (kế hoạch giường) | `/Location` | POST (bulk) | **HIS — kế hoạch giường BV** | 05 | 🔴 1 |
| `Organization` (Nhà thuốc) | `/Organization` | POST | Cục Quản lý Dược | 04 | 🟢 3 |
| `Practitioner` | `/Practitioner` | POST | HIS — module nhân sự | 10, 15, 17 | 🟡 2 |
| `PractitionerRole` | `/PractitionerRole` | POST | HIS — module nhân sự | 10, 15 | 🟡 2 |

---

## Phần V — Lộ Trình Triển Khai Theo Mức Độ Ưu Tiên

### Giai đoạn 1 — Nạp nền tảng (Prerequisite) 🔴

> Phải hoàn thành trước khi nạp dữ liệu lâm sàng. Không có nhóm này thì JOIN key sẽ thiếu.

| # | Hành động | Resource | Endpoint | Phụ thuộc |
|---|---|---|---|---|
| 1.1 | Nạp danh mục BV từ DMDC | `Organization` (prov) | `POST /Organization` | DMDC QĐ 5937 PL4 |
| 1.2 | Nạp danh mục Khoa từ DMDC | `Organization` (dept) | `POST /Organization` | 1.1 + DMDC QĐ 5937 PL5 |
| 1.3 | Nạp CodeSystem ICD-10 VN | `CodeSystem` | `PUT /CodeSystem/icd-10-vn` | QĐ 4469/QĐ-BYT |
| 1.4 | Nạp kế hoạch giường từ HIS | `Location` | `POST /Location` | 1.2 + HIS |

### Giai đoạn 2 — Nạp dữ liệu lâm sàng cốt lõi 🔴

> Dữ liệu chính từ XML QĐ 130+4750.

| # | Hành động | Resource | Endpoint | Nguồn XML |
|---|---|---|---|---|
| 2.1 | Nạp thông tin bệnh nhân | `Patient` | `POST /Patient` | B1 STT 1–16, NHOM_MAU |
| 2.2 | Nạp đợt điều trị | `Encounter` | `POST /Encounter` | B1 STT 17–65 |
| 2.3 | Nạp thông tin BHYT | `Coverage` | `POST /Coverage` | B1 STT 17–21 |
| 2.4 | Nạp chẩn đoán bệnh | `Condition` | `POST /Condition` | B1 STT 25–29 |
| 2.5 | Nạp chi phí tổng hợp | `Claim` | `POST /Claim` | B1 STT 44–55 |
| 2.6 | Nạp kết quả BHXH | `ClaimResponse` | `POST /ClaimResponse` | B1 STT 49–53 |

### Giai đoạn 3 — Nạp dữ liệu chi tiết lâm sàng 🟡

| # | Hành động | Resource | Endpoint | Nguồn XML |
|---|---|---|---|---|
| 3.1 | Nạp đơn thuốc | `MedicationRequest` | `POST /MedicationRequest` | B2 toàn bộ |
| 3.2 | Nạp danh mục thuốc | `Medication` | `POST /Medication` | B2 (MA_THUOC, TEN_THUOC) |
| 3.3 | Nạp DVKT chi tiết | `ServiceRequest` | `POST /ServiceRequest` | B3 toàn bộ |
| 3.4 | Nạp thực hiện DVKT | `Procedure` | `POST /Procedure` | B3 (NGAY_TH_YL, MA_PTTT_QT) |
| 3.5 | Nạp kết quả CLS | `DiagnosticReport` | `POST /DiagnosticReport` | B4 toàn bộ |
| 3.6 | Nạp chỉ số CLS | `Observation` | `POST /Observation` | B4 (MA_CHI_SO, GIA_TRI) |
| 3.7 | Nạp khoản phí chi tiết | `ChargeItem` | `POST /ChargeItem` | B2 + B3 |
| 3.8 | Nạp hồ sơ KBCB | `EpisodeOfCare` | `POST /EpisodeOfCare` | B1 (MA_HSBA) |
| 3.9 | Nạp nhân sự y tế | `Practitioner` | `POST /Practitioner` | HIS (MA_BAC_SI → tên BS) |

### Giai đoạn 4 — Nạp dữ liệu bổ trợ 🟢

| # | Hành động | Resource | Endpoint | Nguồn |
|---|---|---|---|---|
| 4.1 | Nạp giấy ra viện | `DocumentReference` | `POST /DocumentReference` | B7 |
| 4.2 | Nạp tóm tắt HSBA | `Composition` | `POST /Composition` | B8 |
| 4.3 | Nạp diễn biến LS | `ClinicalImpression` | `POST /ClinicalImpression` | B5 |
| 4.4 | Nạp thiết bị y tế | `Device` | `POST /Device` | B3 (MA_MAY, MA_HIEU_SP) |
| 4.5 | Nạp nhà thuốc | `Organization` (pharm) | `POST /Organization` | Cục QLD |
| 4.6 | Nạp CodeSystem YHCT | `CodeSystem` | `PUT /CodeSystem/yhct-vn` | QĐ 26/2022 |

---

## Phần VI — Tóm Tắt Điều Kiện Chạy Được Từng Báo Cáo

| BC | Tên | Điều kiện tối thiểu để chạy | Điều kiện đầy đủ chất lượng |
|:---:|---|---|---|
| 01 | Danh mục BV | Giai đoạn 1.1 | 1.1 + tên, địa chỉ, hạng từ DMDC |
| 02 | Danh mục Khoa | 1.1 + 1.2 | 1.1 + 1.2 + tên khoa + phân cấp phòng/giường |
| 03 | Danh mục ICD | Giai đoạn 1.3 | 1.3 + cập nhật khi BYT ra phiên bản mới |
| 04 | Danh mục Nhà thuốc | Cục QLD / HIS | Đầy đủ khi tích hợp HIS module dược |
| 05 | Số Giường | 1.4 (kế hoạch giường) | 1.4 + realtime từ Encounter.location |
| 06 | Ngày ĐT | Giai đoạn 2.2 | 2.2 đủ |
| 07 | Chi Phí | 2.5 + 2.6 | 2.5 + 2.6 + 3.7 |
| 08 | Lượt Vào Ra | 2.2 | 2.2 + QĐ4750 fields |
| 09 | Theo Loại Hình | 2.2 + 2.3 | 2.2 + 2.3 |
| 10 | Cấp Cứu Tử Vong | 2.2 + 2.4 | + 3.4 + 3.6 (sinh tồn) |
| 11 | Hồ Sơ KCB | 2.2 + 3.8 | 2.2 + 3.8 |
| 12 | Tai Nạn | 2.2 + 2.4 | + bodySite suy luận |
| 13 | Theo Tuổi | 2.1 + 2.2 | 2.1 + 2.2 (NHOM_MAU QĐ4750) |
| 14 | Theo Khoa | 2.2 + 1.1 + 1.2 | + tên khoa từ DMDC |
| 15 | DVKT | 3.3 + 3.4 + 3.5 + 3.6 | + 3.9 (tên bác sĩ) |
| 16 | Ca Mắc ICD | 2.4 + 1.3 | 2.4 + 1.3 (tên ICD tiếng Việt) |
| 17 | Đơn Thuốc | 3.1 + 3.2 | 3.1 + 3.2 |
| 18 | Top 20 Bệnh | 2.4 + 1.3 | 2.4 + 1.3 (tên ICD tiếng Việt) |
| 19 | Nội Trú | 2.2 + 2.4 | + 3.3 + 3.4 + 4.1 + 4.2 |
| 20 | Ngày ĐT/Ngày | 2.2 | 2.2 + NGAY_VAO_NOI_TRU QĐ4750 |
| 21 | Chi Phí/Ngày | 2.5 + 3.7 | 2.5 + 3.7 |
| 22 | Nội Trú/Ngày | 2.2 | 2.2 + NGAY_VAO_NOI_TRU QĐ4750 |
| 23 | Hồ Sơ/Ngày Ra | 2.2 + 3.8 | 2.2 + 3.8 + 2.5 |

---

*Tài liệu phân tích Gap — Dữ liệu FHIR cần thiết cho 23 Báo cáo Power BI Y tế*  
*Căn cứ: QĐ 130/QĐ-BYT (2023) + QĐ 4750/QĐ-BYT (2023) + HL7 FHIR R4B (4.3.0)*  
*FHIR_R4B_23BaoCao_ChiTiet.md + mapping_xml_to_fhir_v2.md + mapping_fhir_23bc_v3.md*
