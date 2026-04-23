# Phân Tích Mapping Chi Tiết: QĐ 130/QĐ-BYT → FHIR R4B
## 23 Báo cáo Power BI Y Tế

> **Nguồn dữ liệu:** Quyết định số 130/QĐ-BYT ngày 18/01/2023 của Bộ trưởng Bộ Y tế  
> **Chuẩn đích:** HL7 FHIR R4B (4.3.0)  
> **Mục tiêu:** Tài liệu kỹ thuật mapping trường dữ liệu cho triển khai Power BI  
> **Ký hiệu:** ✅ Có đủ | ⚠️ Có một phần / cần xử lý | ❌ Thiếu / cần nguồn ngoài

---

## Mục lục

| # | Báo cáo | Trạng thái |
|---|---|---|
| 01 | Danh mục Bệnh viện | ⚠️ Thiếu danh mục |
| 02 | Danh mục Khoa | ⚠️ Thiếu danh mục |
| 03 | Danh mục Bệnh theo ICD | ❌ Cần nguồn ngoài |
| 04 | Danh mục Nhà thuốc | ❌ Cần nguồn ngoài |
| 05 | Số Giường | ⚠️ Thiếu inventory |
| 06 | Tổng Số Ngày Điều Trị | ✅ Đủ |
| 07 | Thống Kê Chi Phí | ✅ Đủ |
| 08 | Thống Kê Lượt Bệnh Nhân Vào Ra | ✅ Đủ |
| 09 | Số Bệnh Nhân theo Loại Hình KCB | ✅ Đủ |
| 10 | Số Ca Cấp Cứu Tử Vong | ⚠️ Thiếu một phần |
| 11 | Số Hồ Sơ Khám Chữa Bệnh | ✅ Đủ |
| 12 | Thống Kê Tai Nạn | ⚠️ Thiếu một phần |
| 13 | Thống Kê theo Tuổi | ✅ Đủ |
| 14 | Thống Kê theo Khoa | ✅ Đủ |
| 15 | Thống Kê Lượt Sử Dụng DVKT | ⚠️ Thiếu phân loại |
| 16 | Thống Kê Ca Mắc theo ICD | ✅ Đủ |
| 17 | Số Đơn Thuốc | ✅ Đủ |
| 18 | Top 20 Bệnh theo ICD | ✅ Đủ |
| 19 | Điều Trị Nội Trú | ✅ Đủ cơ bản |
| 20 | Tổng Số Ngày Điều Trị theo Ngày | ✅ Đủ |
| 21 | Thống Kê Chi Phí theo Ngày | ✅ Đủ |
| 22 | Điều Trị Nội Trú theo Ngày | ✅ Đủ |
| 23 | Thống Kê Hồ Sơ KCB theo Ngày Ra Viện | ✅ Đủ |

---

## Báo cáo 01 — Danh mục Bệnh viện ⚠️

### Resource FHIR chính: `Organization` (type=prov)

### Mapping trường dữ liệu

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Organization.id` | ✅ | — | — | — | Tự sinh UUID khi import |
| 2 | `Organization.identifier[0].system` | ✅ | — | — | — | Cố định: `https://moh.gov.vn/organization` |
| 3 | `Organization.identifier[0].value` | ✅ | `MA_CSKCB` | Bảng 1, Bảng Check-in | Chuỗi(5) | Mã 5 ký tự do cơ quan thẩm quyền cấp |
| 4 | `Organization.active` | ✅ | — | — | — | Mặc định `true` |
| 5 | `Organization.type[0].coding.code` | ✅ | — | — | — | Cố định: `prov` (Healthcare Provider) |
| 6 | `Organization.name` | ✅ | — | ❌ Không có | — | **THIẾU**: Cần bổ sung từ Bộ mã DMDC |
| 7 | `Organization.alias[]` | ⚪ | — | ❌ Không có | — | **THIẾU**: Tên viết tắt |
| 8 | `Organization.telecom[].system` | ⚪ | — | ❌ Không có | — | **THIẾU**: SĐT bệnh viện |
| 9 | `Organization.address[0].text` | ⚪ | — | ❌ Không có | — | **THIẾU**: Địa chỉ bệnh viện |
| 10 | `Organization.partOf` | ⚪ | — | ❌ Không có | — | **THIẾU**: Phân cấp BV → Sở Y tế |

### Phân tích khoảng cách (Gap)

| Trạng thái | Số trường | Danh sách |
|---|---|---|
| ✅ Có đủ | 2 | `MA_CSKCB` → identifier |
| ⚠️ Tự sinh | 2 | `id`, `active` |
| ❌ Thiếu | 6 | name, alias, telecom, address, partOf, type chi tiết |

**Giải pháp bổ sung:**  
- Nhập danh mục cơ sở KBCB từ **Bộ mã DMDC** (Quyết định 5937/QĐ-BYT) hoặc từ Cổng tiếp nhận dữ liệu BHXH  
- JOIN `MA_CSKCB` từ Bảng 1 với bảng danh mục ngoài để lấy tên, địa chỉ

---

## Báo cáo 02 — Danh mục Khoa ⚠️

### Resource FHIR chính: `Organization` (type=dept) + `Location`

### Mapping trường dữ liệu — `Organization` (Khoa)

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Organization.id` | ✅ | — | — | — | Tự sinh từ `MA_KHOA` |
| 2 | `Organization.identifier[0].value` | ✅ | `MA_KHOA` | Bảng 1 (STT56), Bảng 2 (STT31), Bảng 3 (STT31) | Chuỗi(50) | Mã khoa theo Phụ lục số 5 QĐ 5937/QĐ-BYT |
| 3 | `Organization.active` | ✅ | — | — | — | Mặc định `true` |
| 4 | `Organization.type[0].coding.code` | ✅ | — | — | — | Cố định: `dept` |
| 5 | `Organization.name` | ✅ | — | ❌ Không có | — | **THIẾU**: Cần từ bảng danh mục khoa DMDC |
| 6 | `Organization.partOf` | ✅ | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Reference đến Organization BV cha |

### Mapping trường dữ liệu — `Location` (Phòng/Giường trong khoa)

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Location.id` | ✅ | — | — | — | Tự sinh |
| 2 | `Location.name` | ✅ | `MA_GIUONG` | Bảng 3 (STT32) | Chuỗi(50) | Mã giường 4 ký tự (H001, T001, C001, K001) |
| 3 | `Location.status` | ✅ | — | — | — | Mặc định `active` |
| 4 | `Location.physicalType.coding.code` | ✅ | — | — | — | `bd` (bed) hoặc `ro` (room) |
| 5 | `Location.managingOrganization` | ✅ | `MA_KHOA` | Bảng 3 (STT31) | Chuỗi(20) | Reference đến Organization khoa |

### Phân tích khoảng cách (Gap)

| Trạng thái | Chi tiết |
|---|---|
| ✅ Có | `MA_KHOA` (mã), `MA_CSKCB` (BV cha), `MA_GIUONG` (phòng/giường) |
| ❌ Thiếu | Tên khoa đầy đủ — cần bảng danh mục Phụ lục 5 QĐ 5937/QĐ-BYT |

---

## Báo cáo 03 — Danh mục Bệnh theo ICD ❌

### Resource FHIR chính: `CodeSystem` + `ValueSet`

### Mapping trường dữ liệu

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|
| 1 | `CodeSystem.url` | ✅ | — | ❌ Không có | Cố định: `http://hl7.org/fhir/sid/icd-10` |
| 2 | `CodeSystem.concept[].code` | ✅ | `MA_BENH_CHINH` | Bảng 1 (STT26) | **Chỉ là giá trị tham chiếu**, không phải định nghĩa |
| 3 | `CodeSystem.concept[].display` | ✅ | — | ❌ Không có | QĐ 130 không lưu tên bệnh trong CodeSystem |
| 4 | `CodeSystem.concept[].definition` | ⚪ | — | ❌ Không có | |
| 5 | `ValueSet.compose.include.concept[].code` | ✅ | `MA_BENH_KT` | Bảng 1 (STT27) | Nhiều mã, phân cách ";", tối đa 12 mã |

### Phân tích khoảng cách (Gap)

QĐ 130 **chỉ sử dụng** mã ICD-10 làm giá trị tra cứu (tham chiếu Quyết định 4469/QĐ-BYT ngày 28/10/2020), **không định nghĩa CodeSystem**.

**Giải pháp bổ sung:**
- Import toàn bộ bảng ICD-10 tiếng Việt từ QĐ 4469/QĐ-BYT
- Hoặc dùng CodeSystem ICD-10 quốc tế từ `http://hl7.org/fhir/sid/icd-10` và map với tên Việt Nam qua extension

---

## Báo cáo 04 — Danh mục Nhà thuốc ❌

### Resource FHIR chính: `Organization` (type=pharm) + `Location`

### Mapping trường dữ liệu

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Organization.identifier[0].value` | ✅ | `MA_CSKCB_THUOC` | Bảng 2 (STT5) | Chuỗi(10) | Mã cơ sở cung cấp thuốc — không phải mã nhà thuốc |
| 2 | `Organization.name` | ✅ | — | ❌ Không có | | **THIẾU** hoàn toàn |
| 3 | `Organization.type` | ✅ | — | ❌ Không có | | **THIẾU** — phân loại nhà thuốc |
| 4 | `Organization.address` | ✅ | — | ❌ Không có | | **THIẾU** — địa chỉ |
| 5 | `Organization.telecom` | ⚪ | — | ❌ Không có | | **THIẾU** |
| 6 | `Location.hoursOfOperation` | ⚪ | — | ❌ Không có | | **THIẾU** |

### Phân tích khoảng cách (Gap)

QĐ 130 hoàn toàn không có bảng danh mục nhà thuốc. `MA_CSKCB_THUOC` trong Bảng 2 chỉ là mã cơ sở KCB nơi xuất xứ thuốc (dùng cho trường hợp đặc biệt như thiên tai, chuyển thuốc).

**Giải pháp bổ sung:**
- Lấy từ hệ thống cấp phép dược của Cục Quản lý Dược
- Hoặc từ danh mục nhà thuốc trong phần mềm HIS bệnh viện

---

## Báo cáo 05 — Số Giường ⚠️

### Resource FHIR chính: `Location` (physicalType=bd)

### Mapping trường dữ liệu

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Location.id` | ✅ | — | — | — | Tự sinh từ `MA_GIUONG` + `MA_KHOA` |
| 2 | `Location.name` | ✅ | `MA_GIUONG` | Bảng 3 (STT32) | Chuỗi(50) | Mã giường: H001 (kế hoạch), T001 (kê thêm), C001 (tự chọn), K001 (khác) |
| 3 | `Location.status` | ✅ | — | — | — | Mặc định `active` |
| 4 | `Location.operationalStatus.code` | ⚪ | — | ❌ Không có trực tiếp | — | Suy luận: nếu `Encounter.status=in-progress` → `O` (Occupied); ngược lại → `U` (Unoccupied) |
| 5 | `Location.physicalType.coding.code` | ✅ | — | — | — | Cố định: `bd` (bed) |
| 6 | `Location.managingOrganization` | ✅ | `MA_KHOA` | Bảng 3 (STT31) | Chuỗi(20) | Reference → Organization khoa |
| 7 | `Location.partOf` | ✅ | — | ❌ Không có | — | **THIẾU**: Mã phòng chứa giường không có riêng trong QĐ 130 |

### Metric tính số giường

| Metric | Công thức | Nguồn dữ liệu |
|---|---|---|
| Tổng giường kế hoạch | Đếm `MA_GIUONG` bắt đầu bằng `H` distinct | Bảng 3 — nhưng chỉ từ dữ liệu đã sử dụng |
| Giường đang dùng | Đếm `MA_GIUONG` trong `Encounter` status=`in-progress` | Bảng 3 JOIN Bảng 1 qua `MA_LK` |
| Giường trống | Tổng kế hoạch − Đang dùng | Tính toán |
| Tỷ lệ sử dụng | Đang dùng / Tổng kế hoạch × 100% | Tính toán |

### Phân tích khoảng cách (Gap)

| Vấn đề | Mức độ | Giải pháp |
|---|---|---|
| Không có bảng tổng số giường kế hoạch độc lập | ⚠️ Quan trọng | Cần nhập từ HIS hoặc kế hoạch giường của khoa |
| `operationalStatus` (Occupied/Unoccupied) phải suy luận từ Encounter | ⚠️ Trung bình | JOIN Bảng 3 với Bảng 1 theo `MA_LK` và `MA_KHOA` |
| Không có mã phòng chứa giường riêng | ⚠️ Nhỏ | Tự sinh từ tiền tố mã giường nếu có quy ước |

---

## Báo cáo 06 — Tổng Số Ngày Điều Trị ✅

### Resource FHIR chính: `Encounter`

### Mapping trường dữ liệu đầy đủ

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Encounter.id` | ✅ | `MA_LK` | Bảng 1 (STT1), Bảng Check-in (STT1) | Chuỗi(100) | PRIMARY KEY — mã đợt điều trị duy nhất |
| 2 | `Encounter.status` | ✅ | `MA_LOAI_KCB` + `KET_QUA_DTRI` | Bảng 1 (STT55, STT40) | Số(2), Số(1) | Logic: nếu `NGAY_RA` có giá trị → `finished`; ngược lại → `in-progress` |
| 3 | `Encounter.class.code` | ✅ | `MA_LOAI_KCB` | Bảng 1 (STT55), Bảng Check-in (STT14) | Số(2) | Xem bảng mapping mã bên dưới |
| 4 | `Encounter.subject` | ✅ | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Reference → Patient.identifier |
| 5 | `Encounter.period.start` | ✅ | `NGAY_VAO` | Bảng 1 (STT34) | Chuỗi(12) yyyymmddHHMM | Chuyển định dạng: `202401150830` → `2024-01-15T08:30:00+07:00` |
| 6 | `Encounter.period.end` | ✅ | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) yyyymmddHHMM | Chuyển định dạng tương tự |
| 7 | `Encounter.serviceProvider` | ✅ | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Reference → Organization.identifier |
| 8 | `Encounter.location[0].location` | ⚪ | `MA_KHOA` | Bảng 1 (STT56) | Chuỗi(50) | Reference → Organization khoa; nhiều khoa phân cách ";" |
| 9 | `Encounter.hospitalization.dischargeDisposition` | ⚪ | `MA_LOAI_RV` | Bảng 1 (STT41) | Số(1) | Xem bảng mapping mã bên dưới |

### Mapping mã `MA_LOAI_KCB` → `Encounter.class`

| MA_LOAI_KCB | Tên trong QĐ 130 | FHIR class code | FHIR display |
|---|---|---|---|
| 01 | Khám bệnh | `AMB` | Ambulatory |
| 02 | Điều trị ngoại trú | `AMB` | Ambulatory |
| 03 | Điều trị nội trú | `IMP` | Inpatient |
| 04 | Điều trị nội trú ban ngày | `SS` | Short Stay |
| 05 | Ngoại trú bệnh mạn tính, có khám + lĩnh thuốc | `AMB` | Ambulatory |
| 06 | Điều trị lưu TYT xã, PKĐKKV | `IMP` | Inpatient |
| 07 | Nhận thuốc theo hẹn (không khám) | `AMB` | Ambulatory |
| 08 | Ngoại trú mạn tính, có DVKT | `AMB` | Ambulatory |
| 09 | Cấp cứu (dựa trên ngữ cảnh DMDC) | `EMER` | Emergency |

### Mapping mã `MA_LOAI_RV` → `Encounter.hospitalization.dischargeDisposition`

| MA_LOAI_RV | Tên trong QĐ 130 | FHIR code | FHIR display |
|---|---|---|---|
| 1 | Ra viện | `home` | Home |
| 2 | Chuyển tuyến theo yêu cầu chuyên môn | `hosp` | Hospitalization |
| 3 | Trốn viện | `oth` | Other |
| 4 | Xin ra viện | `aadvice` | Left against advice |
| 5 | Chuyển tuyến theo yêu cầu người bệnh | `other-hcf` | Other healthcare facility |

### Mapping mã `KET_QUA_DTRI` → `Encounter.hospitalization.dischargeDisposition` (bổ sung)

| KET_QUA_DTRI | Tên | Tác động FHIR |
|---|---|---|
| 1 | Khỏi | `dischargeDisposition.code = home` |
| 2 | Đỡ | `dischargeDisposition.code = home` |
| 3 | Không thay đổi | `dischargeDisposition.code = oth` |
| 4 | Nặng hơn | `dischargeDisposition.code = oth` |
| 5 | Tử vong | `dischargeDisposition.code = exp` |
| 6 | Tiên lượng nặng xin về | `dischargeDisposition.code = aadvice` |
| 7 | Chưa xác định | `dischargeDisposition.code = oth` |

### Công thức tính số ngày điều trị

```
SO_NGAY_DTRI (QĐ 130, Bảng 1 STT38):
  - MA_LOAI_KCB ∈ {1, 7, 9} → SO_NGAY_DTRI = 0
  - MA_LOAI_KCB ∈ {2, 3, 4, 6} → SO_NGAY_DTRI = NGAY_RA − NGAY_VAO + 1
  - MA_LOAI_KCB = 5 → SO_NGAY_DTRI = số ngày dùng thuốc
  - MA_LOAI_KCB = 8 → SO_NGAY_DTRI = số ngày thực tế có DVKT

FHIR tương đương:
  DATEDIFF(Encounter.period.start, Encounter.period.end, DAY)
```

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 07 — Thống Kê Chi Phí ✅

### Resource FHIR chính: `Claim` + `ClaimResponse` + `Coverage`

### Mapping trường dữ liệu — `Claim`

| # | Trường FHIR | Bắt buộc FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|:---:|---|---|---|---|
| 1 | `Claim.id` | ✅ | `MA_LK` | Bảng 1 (STT1) | Chuỗi(100) | Dùng `MA_LK` làm Claim ID |
| 2 | `Claim.status` | ✅ | — | — | — | Mặc định `active` |
| 3 | `Claim.type.coding.code` | ✅ | — | — | — | Cố định: `institutional` |
| 4 | `Claim.use` | ✅ | — | — | — | Cố định: `claim` |
| 5 | `Claim.patient` | ✅ | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Reference → Patient |
| 6 | `Claim.created` | ✅ | `NGAY_TTOAN` | Bảng 1 (STT43) | Chuỗi(12) | Ngày thanh toán chi phí |
| 7 | `Claim.provider` | ✅ | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Reference → Organization |
| 8 | `Claim.encounter` | ✅ | `MA_LK` | Bảng 1 (STT1) | Chuỗi(100) | Reference → Encounter |
| 9 | `Claim.insurance[0].coverage` | ✅ | `MA_THE_BHYT` | Bảng 1 (STT16) | Chuỗi(n) | Reference → Coverage |
| 10 | `Claim.insurance[0].focal` | ✅ | — | — | — | `true` nếu có `MA_THE_BHYT` |
| 11 | `Claim.total.value` | ✅ | `T_TONGCHI_BV` | Bảng 1 (STT46) | Số(15) | Tổng chi phí bệnh viện |
| 12 | `Claim.total.currency` | ✅ | — | — | — | Cố định: `VND` |
| 13 | `Claim.item[0].productOrService` | ✅ | `MA_DICH_VU` | Bảng Check-in (STT16) | Chuỗi(50) | Mã dịch vụ DMDC |
| 14 | `Claim.item[0].net.value` | ✅ | `THANH_TIEN_BV` | Bảng 2 (STT20), Bảng 3 (STT19) | Số(15) | Thành tiền theo đơn giá BV |

### Mapping trường dữ liệu — Chi tiết tài chính

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu | Công thức / Ghi chú |
|---|---|---|---|---|---|
| 1 | `ClaimResponse.payment.amount.value` | `T_BHTT` | Bảng 1 (STT50) | Số(15) | = `T_TONGCHI_BH` − `T_BNCCT`; BHXH thanh toán |
| 2 | `Coverage.costToBeneficiary[0].value` (T_BNCCT) | `T_BNCCT` | Bảng 1 (STT49) | Số(15) | Người bệnh cùng chi trả trong phạm vi BHYT |
| 3 | `Invoice.totalNet` (T_BNTT) | `T_BNTT` | Bảng 1 (STT48) | Số(15) | Người bệnh tự trả ngoài phạm vi BHYT |
| 4 | `Claim.total` (T_TONGCHI_BH) | `T_TONGCHI_BH` | Bảng 1 (STT47) | Số(15) | Tổng trong phạm vi quỹ BHYT |
| 5 | Extension `T_NGUONKHAC` | `T_NGUONKHAC` | Bảng 1 (STT51) | Số(15) | Nguồn khác (NSNN, viện trợ ngoài, trong nước) |
| 6 | Extension `T_BHTT_GDV` | `T_BHTT_GDV` | Bảng 1 (STT52) | Số(15) | BHYT thanh toán ngoài định suất/DRG |

### Mapping trường dữ liệu — `Coverage` (Bảo hiểm y tế)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu | Ghi chú |
|---|---|---|---|---|---|
| 1 | `Coverage.identifier[0].value` | `MA_THE_BHYT` | Bảng 1 (STT16) | Chuỗi(n) | Mã thẻ 15 ký tự; nhiều thẻ phân cách ";" |
| 2 | `Coverage.subscriberId` | `MA_THE_BHYT` | Bảng 1 (STT16) | Chuỗi(n) | Số thẻ BHYT |
| 3 | `Coverage.period.start` | `GT_THE_TU` | Bảng 1 (STT18) | Chuỗi(n) yyyymmdd | Ngày thẻ bắt đầu có giá trị |
| 4 | `Coverage.period.end` | `GT_THE_DEN` | Bảng 1 (STT19) | Chuỗi(n) yyyymmdd | Ngày thẻ hết giá trị |
| 5 | `Coverage.class[0].value` | `MA_DKBD` | Bảng 1 (STT17) | Chuỗi(n) | Mã cơ sở KBCB đăng ký ban đầu (5 ký tự) |
| 6 | `Coverage.costToBeneficiary[0].type` | `MUC_HUONG` | Bảng 2 (STT27), Bảng 3 (STT22) | Số(3) | Mức hưởng: 80/95/100 hoặc trái tuyến |
| 7 | `Coverage.type.coding.code` | `MA_DOITUONG_KCB` | Bảng 1 (STT30) | Chuỗi(3) | Đối tượng KBCB theo DMDC |
| 8 | `Coverage.network` | `MA_KHUVUC` | Bảng 1 (STT58) | Chuỗi(2) | K1/K2/K3 — khu vực sinh sống |

### Mapping mã phương thức thanh toán `MA_PTTT`

| MA_PTTT | Tên | FHIR mapping |
|---|---|---|
| 1 | Phí dịch vụ (Fee for service) | `Claim.type = professional` |
| 2 | Định suất (Capitation) | `Claim.type = institutional` + extension |
| 3 | Trường hợp bệnh DRG | `Claim.type = institutional` + extension DRG |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 08 — Thống Kê Lượt Bệnh Nhân Vào Ra ✅

### Resource FHIR chính: `Encounter`

### Mapping trường dữ liệu bổ sung (ngoài BC06)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.hospitalization.admitSource` | `MA_NOI_DI` | Bảng 1 (STT31) | Chuỗi(5) | Nơi chuyển BN đến — nếu có giá trị → chuyển tuyến |
| 2 | `Encounter.hospitalization.origin` | `MA_NOI_DI` | Bảng 1 (STT31) | Chuỗi(5) | Reference → Organization cơ sở chuyển đến |
| 3 | `Encounter.hospitalization.destination` | `MA_NOI_DEN` | Bảng 1 (STT32) | Chuỗi(5) | Reference → Organization cơ sở được chuyển đến |
| 4 | `Encounter.hospitalization.dischargeDisposition` | `MA_LOAI_RV` | Bảng 1 (STT41) | Số(1) | Xem mapping BC06 |
| 5 | `Encounter.reasonCode[0].coding.code` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Lý do vào viện = bệnh chính ICD-10 |
| 6 | `Encounter.reasonCode[0].text` | `LY_DO_VV` | Bảng 1 (STT21) | Chuỗi(n) | Lý do đến KBCB (văn bản tự do) |
| 7 | `Encounter.reasonCode[1].text` | `LY_DO_VNT` | Bảng 1 (STT22) | Chuỗi(n) | Lý do vào nội trú |
| 8 | `Encounter.statusHistory[]` | `NGAY_VAO_NOI_TRU` | Bảng 1 (STT35) | Chuỗi(12) | Thời điểm chuyển sang nội trú nếu khác NGAY_VAO |
| 9 | `Encounter.basedOn` | `GIAY_CHUYEN_TUYEN` | Bảng 1 (STT37) | Chuỗi(50) | Số giấy chuyển tuyến hoặc giấy hẹn khám lại |

### Mapping `admitSource` từ dữ liệu QĐ 130

| Điều kiện từ QĐ 130 | FHIR admitSource code | Display |
|---|---|---|
| `MA_NOI_DI` có giá trị | `hosp` | Transferred from other hospital |
| `MA_LOAI_KCB` = 09 (cấp cứu) | `emd` | From accident/emergency department |
| `MA_LOAI_KCB` = 01 (khám) | `outp` | From outpatient department |
| Các trường hợp còn lại | `gp` | General Practitioner referral |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 09 — Số Bệnh Nhân theo Loại Hình KCB ✅

### Resource FHIR chính: `Encounter` (phân loại theo `class`) + `Coverage`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.class.code` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | Xem bảng mapping BC06 |
| 2 | `Encounter.type[0].coding` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | Chi tiết hơn class — dùng mã DMDC |
| 3 | `Coverage.type.coding.code` | `MA_DOITUONG_KCB` | Bảng 1 (STT30), Bảng Check-in (STT12) | Số(1) | Phân loại nguồn tài chính |
| 4 | `Coverage.subscriberId` | `MA_THE_BHYT` | Bảng 1 (STT16) | Chuỗi(n) | Xác định có BHYT hay không |
| 5 | `Encounter.serviceProvider` | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Cơ sở KCB |

### Phân loại `MA_DOITUONG_KCB` → Nguồn tài chính

| MA_DOITUONG_KCB | Tên (theo DMDC BYT) | FHIR Coverage.type |
|---|---|---|
| 1 | BHYT | `PUBLICPOL` |
| 2 | Tự nguyện / Dịch vụ | `PVTINS` |
| 3 | Miễn phí / Chính sách | `PUBLICPOL` |
| 4 | Khác | `pay` (tự trả) |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 10 — Số Ca Cấp Cứu Tử Vong ⚠️

### Resource FHIR chính: `Encounter` (class=EMER) + `Condition`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.class.code = EMER` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | ⚠️ Cần xác định mã cấp cứu trong DMDC (thường mã 09 hoặc tương đương) |
| 2 | `Encounter.hospitalization.dischargeDisposition.code = exp` | `KET_QUA_DTRI` = 5 | Bảng 1 (STT40) | Số(1) | Mã 5 = Tử vong → map sang `exp` |
| 3 | `Encounter.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Thời điểm tử vong |
| 4 | `Encounter.status` | — | — | — | `finished` khi đã có `NGAY_RA` |
| 5 | `Condition.code.coding.code` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Mã ICD-10 nguyên nhân tử vong |
| 6 | `Condition.code.coding.code` (bệnh kèm) | `MA_BENH_KT` | Bảng 1 (STT27) | Chuỗi(100) | Nhiều mã, phân cách ";", tối đa 12 |
| 7 | `Patient.gender` | `GIOI_TINH` | Bảng 1 / Bảng Check-in (STT7) | Số(1) | 1=Nam, 2=Nữ, 3=Chưa xác định |
| 8 | `Patient.birthDate` | `NGAY_SINH` | Bảng 1 / Bảng Check-in (STT6) | Chuỗi(12) | Tính tuổi khi tử vong |
| 9 | `Observation.code` (dấu hiệu sinh tồn) | — | ❌ Không có | — | **THIẾU**: QĐ 130 không lưu chỉ số lâm sàng cuối |
| 10 | `Procedure.code` (thủ thuật cấp cứu) | `MA_PTTT_QT` | Bảng 1 (STT29) | Chuỗi(125) | Có mã ICD-9 CM thủ thuật; nhiều mã phân cách ";" |

### Logic xác định ca cấp cứu tử vong

```
Điều kiện lọc:
  1. MA_LOAI_KCB = [mã cấp cứu trong DMDC]
     HOẶC LY_DO_VV chứa từ khóa "cấp cứu"
  2. KET_QUA_DTRI = 5 (Tử vong)
     HOẶC MA_LOAI_RV dẫn đến tử vong
  3. NGAY_RA có giá trị (đã kết thúc)
```

### Phân tích khoảng cách (Gap)

| Vấn đề | Mức độ | Giải pháp |
|---|---|---|
| Mã cấp cứu trong `MA_LOAI_KCB` không tường minh trong QĐ 130 | ⚠️ Quan trọng | Tra cứu DMDC để xác định mã cụ thể |
| Thiếu `Observation` (dấu hiệu sinh tồn cuối) | ⚠️ Trung bình | Lấy từ Bảng 5 (DIEN_BIEN_LS) nếu ghi chép đầy đủ |
| Bảng 5 (diễn biến lâm sàng) có `DIEN_BIEN_LS` dạng văn bản | ⚠️ Nhỏ | Không chuẩn hóa thành `Observation.value` được |

### Đánh giá: ⚠️ Đủ cho thống kê số ca, thiếu dữ liệu lâm sàng chi tiết

---

## Báo cáo 11 — Số Hồ Sơ Khám Chữa Bệnh ✅

### Resource FHIR chính: `EpisodeOfCare`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `EpisodeOfCare.id` | `MA_LK` | Bảng 1 (STT1) | Chuỗi(100) | PRIMARY KEY — 1 MA_LK = 1 đợt điều trị = 1 EpisodeOfCare |
| 2 | `EpisodeOfCare.identifier[0].value` | `MA_HSBA` | Bảng 1 (STT63) | Chuỗi(100) | Mã hồ sơ bệnh án hoặc phiếu khám ngoại trú |
| 3 | `EpisodeOfCare.status` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Có `NGAY_RA` → `finished`; không có → `active` |
| 4 | `EpisodeOfCare.type[0].coding` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | Loại đợt chăm sóc |
| 5 | `EpisodeOfCare.patient` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Reference → Patient |
| 6 | `EpisodeOfCare.managingOrganization` | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Reference → Organization BV |
| 7 | `EpisodeOfCare.period.start` | `NGAY_VAO` | Bảng 1 (STT34) | Chuỗi(12) | Ngày mở hồ sơ |
| 8 | `EpisodeOfCare.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Ngày đóng hồ sơ |
| 9 | `EpisodeOfCare.diagnosis[0].condition` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Chẩn đoán bệnh chính (ICD-10) |
| 10 | `EpisodeOfCare.diagnosis[0].role.code` | — | — | — | `CC` (chief complaint) |
| 11 | `EpisodeOfCare.careManager` | `MA_TTDV` | Bảng 1 (STT64) | Chuỗi(10) | Mã định danh y tế người đứng đầu cơ sở |

### Metric tính số hồ sơ

| Metric | Điều kiện lọc | Ghi chú |
|---|---|---|
| Tổng hồ sơ mở | `EpisodeOfCare.status IN (active, finished)` | COUNT(`MA_LK`) |
| Hồ sơ nội trú | `MA_LOAI_KCB IN (3, 4, 6)` | Bảng 8 có dữ liệu tóm tắt |
| Hồ sơ ngoại trú | `MA_LOAI_KCB IN (1, 2, 5, 7, 8)` | |
| Hồ sơ đang điều trị | `NGAY_RA` rỗng | `EpisodeOfCare.status = active` |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 12 — Thống Kê Tai Nạn ⚠️

### Resource FHIR chính: `Condition` (mã ICD nhóm S, T, V–Y) + `Encounter`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Condition.code.coding.code` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Lọc mã ICD S00–Y99 để xác định tai nạn |
| 2 | `Condition.code.coding.code` (phụ) | `MA_BENH_KT` | Bảng 1 (STT27) | Chuỗi(100) | Mã bệnh kèm tai nạn |
| 3 | `Encounter.extension[tai-nan]` | `MA_TAI_NAN` | Bảng 1 (STT33) | Số(1) | **Quan trọng**: Mã tai nạn thương tích theo Phụ lục 4 QĐ 5937/QĐ-BYT |
| 4 | `Condition.subject` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Reference → Patient |
| 5 | `Condition.encounter` | `MA_LK` | Bảng 1 (STT1) | Chuỗi(100) | Reference → Encounter |
| 6 | `Condition.recordedDate` | `NGAY_VAO` | Bảng 1 (STT34) | Chuỗi(12) | Ngày ghi nhận (xấp xỉ) |
| 7 | `Encounter.hospitalization.admitSource` | `MA_NOI_DI` | Bảng 1 (STT31) | Chuỗi(5) | Xem BC08 |
| 8 | `Patient.gender` | `GIOI_TINH` | Bảng 1 (STT7) | Số(1) | Phân tích giới |
| 9 | `Condition.bodySite` | — | ❌ Không có | — | **THIẾU**: Vị trí tổn thương |
| 10 | `Condition.severity` | — | ❌ Không có | — | **THIẾU**: Mức độ nghiêm trọng |
| 11 | `Condition.onsetDateTime` | — | ❌ Không có | — | **THIẾU**: Thời điểm xảy ra tai nạn (≠ thời điểm vào viện) |

### Phân loại mã tai nạn `MA_TAI_NAN`

| MA_TAI_NAN | Loại tai nạn (Phụ lục 4, QĐ 5937) | ICD nhóm tương ứng |
|---|---|---|
| 1 | Tai nạn giao thông | V01–V99 |
| 2 | Tai nạn lao động | W00–W99, X00–X99 |
| 3 | Tai nạn sinh hoạt | W00–W99 |
| 4 | Bạo lực/tự tử | X60–X84, X85–Y09 |
| 5 | Tai nạn khác | T00–T98 còn lại |

### Phân tích khoảng cách (Gap)

| Vấn đề | Mức độ | Giải pháp |
|---|---|---|
| Không có `bodySite` (vị trí tổn thương) | ⚠️ Trung bình | Suy luận từ mã ICD (S00-S99 theo vị trí) |
| Không có `severity` | ⚠️ Trung bình | Suy luận từ `KET_QUA_DTRI` và `SO_NGAY_DTRI` |
| Không có thời điểm xảy ra tai nạn | ⚠️ Nhỏ | Dùng `NGAY_VAO` làm xấp xỉ |

### Đánh giá: ⚠️ Đủ cho thống kê số ca, thiếu chi tiết phân tích tổn thương

---

## Báo cáo 13 — Thống Kê theo Tuổi ✅

### Resource FHIR chính: `Patient` + `Encounter`

### Mapping trường dữ liệu — `Patient`

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Patient.id` | `MA_BN` | Bảng 1 (STT3), Bảng Check-in (STT3) | Chuỗi(100) | ID bệnh nhân theo cơ sở KBCB |
| 2 | `Patient.identifier[0].system` | — | — | — | `https://moh.gov.vn/pid` |
| 3 | `Patient.identifier[0].value` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Mã bệnh nhân nội bộ |
| 4 | `Patient.identifier[1].system` | — | — | — | `https://moh.gov.vn/cccd` |
| 5 | `Patient.identifier[1].value` | `SO_CCCD` | Bảng 1 (STT5) | Số(15) | Số CCCD/CMND/hộ chiếu/định danh điện tử |
| 6 | `Patient.name[0].text` | `HO_TEN` | Bảng 1 (STT4) | Chuỗi(255) | Họ và tên đầy đủ |
| 7 | `Patient.gender` | `GIOI_TINH` | Bảng 1 (STT7), Bảng Check-in (STT7) | Số(1) | 1→`male`, 2→`female`, 3→`unknown` |
| 8 | `Patient.birthDate` | `NGAY_SINH` | Bảng 1 (STT6), Bảng Check-in (STT6) | Chuỗi(12) yyyymmddHHMM | Lấy 8 ký tự đầu yyyymmdd; nếu 0000 → không xác định |
| 9 | `Patient.address[0].text` | `DIA_CHI` | Bảng 1 (STT11) | Chuỗi(1024) | Địa chỉ cư trú đầy đủ |
| 10 | `Patient.address[0].state` | `MATINH_CU_TRU` | Bảng 1 (STT12) | Chuỗi(3) | 2 ký tự cuối mã tỉnh theo TT 07/2016/TT-BCA |
| 11 | `Patient.address[0].district` | `MAHUYEN_CU_TRU` | Bảng 1 (STT13) | Chuỗi(3) | Mã huyện theo QĐ 124/2004/QĐ-TTg |
| 12 | `Patient.address[0].postalCode` | `MAXA_CU_TRU` | Bảng 1 (STT14) | Chuỗi(5) | Mã xã theo QĐ 124/2004/QĐ-TTg |
| 13 | `Patient.telecom[0].value` | `DIEN_THOAI` | Bảng 1 (STT15) | Số(15) | SĐT liên lạc (nếu có) |
| 14 | `Patient.communication[0].language` | — | — | — | Mặc định `vi` (tiếng Việt) |
| 15 | `Patient.extension[dan-toc]` | `MA_DANTOC` | Bảng 1 (STT9) | Số(2) | Mã dân tộc theo QĐ 121-TCTK |
| 16 | `Patient.extension[nghe-nghiep]` | `MA_NGHE_NGHIEP` | Bảng 1 (STT10) | Số(5) | Mã nghề nghiệp theo QĐ 34/2020/QĐ-TTg |
| 17 | `Patient.extension[quoc-tich]` | `MA_QUOCTICH` | Bảng 1 (STT8) | Số(3) | Mã quốc tịch theo TT 07/2016/TT-BCA |

### Mapping `GIOI_TINH` → `Patient.gender`

| GIOI_TINH | FHIR gender | Display |
|---|---|---|
| 1 | `male` | Nam |
| 2 | `female` | Nữ |
| 3 | `unknown` | Chưa xác định |

### Logic tính tuổi và phân nhóm tuổi

```
Từ NGAY_SINH (yyyymmddHHMM):
  birthDate = lấy 8 ký tự đầu → parse thành date

  Trường hợp đặc biệt:
  - NGAY_SINH = "000000000000" → unknown age
  - Trẻ sơ sinh ≤ 28 ngày: dùng đầy đủ yyyymmddHHMM
  - Chỉ có năm (yyyymmdd có mm=00, dd=00): ước tính tuổi từ năm

Nhóm tuổi BYT Việt Nam:
  age < 28 ngày         → neonatal (Sơ sinh)
  28 ngày ≤ age < 1 năm → infant (Nhũ nhi)
  1 ≤ age < 6           → toddler (Trẻ nhỏ)
  6 ≤ age < 15          → child (Trẻ em)
  15 ≤ age < 18         → adolescent (Vị thành niên)
  18 ≤ age < 60         → adult (Người lớn)
  age ≥ 60              → elderly (Người cao tuổi)
```

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 14 — Thống Kê theo Khoa ✅

### Resource FHIR chính: `Encounter` GROUP BY `serviceProvider`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.serviceProvider` | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | BV chính — chiều GROUP BY cấp BV |
| 2 | `Encounter.location[].location` (khoa) | `MA_KHOA` | Bảng 1 (STT56) | Chuỗi(50) | Chiều GROUP BY cấp khoa; nhiều khoa phân cách ";" |
| 3 | `Encounter.class` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | Phân loại nội/ngoại trú trong khoa |
| 4 | `Encounter.period.start` | `NGAY_VAO` | Bảng 1 (STT34) | Chuỗi(12) | Tính ngày điều trị |
| 5 | `Encounter.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Tính ngày điều trị |
| 6 | `Encounter.diagnosis[].condition` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Top bệnh theo khoa |
| 7 | `Encounter.participant[].individual` | `MA_BAC_SI` | Bảng 2 (STT32), Bảng 3 (STT33) | Chuỗi(255) | Mã định danh y tế bác sĩ |
| 8 | `Organization.identifier` | `MA_KHOA` | Bảng 1 (STT56) | Chuỗi(50) | JOIN key với bảng danh mục khoa |
| 9 | `Organization.name` | — | ❌ Cần DMDC | — | Tên khoa từ bảng danh mục |
| 10 | `Organization.partOf` | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Khoa thuộc BV nào |
| 11 | `Claim.total.value` | `T_TONGCHI_BV` | Bảng 1 (STT46) | Số(15) | Chi phí theo khoa |

### Xử lý nhiều khoa trong một đợt điều trị

```
MA_KHOA = "K01;K02;K03" (nhiều khoa phân cách ";")

FHIR xử lý:
  Encounter.location[] = [
    { location: "Organization/K01", period: {start: ..., end: ...} },
    { location: "Organization/K02", period: {start: ..., end: ...} },
    { location: "Organization/K03", period: {start: ..., end: ...} }
  ]

Lưu ý: QĐ 130 không lưu ngày chuyển khoa riêng lẻ
  → Không thể tách chính xác thời gian ở từng khoa
  → Phân bổ đều hoặc dùng Bảng 5 (THOI_DIEM_DBLS) để ước tính
```

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn (tên khoa cần bổ sung từ DMDC)

---

## Báo cáo 15 — Thống Kê Lượt Sử Dụng DVKT ⚠️

### Resource FHIR chính: `ServiceRequest` + `Procedure` + `DiagnosticReport`

### Mapping trường dữ liệu — `ServiceRequest` (từ Bảng 3 QĐ 130)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `ServiceRequest.id` | `MA_LK` + `STT` | Bảng 3 (STT1, STT2) | Chuỗi + Số | Composite key: `MA_LK`-`STT` |
| 2 | `ServiceRequest.status` | `NGAY_KQ` | Bảng 3 (STT37) | Chuỗi(12) | Có `NGAY_KQ` → `completed`; không → `active` |
| 3 | `ServiceRequest.intent` | — | — | — | Cố định: `order` |
| 4 | `ServiceRequest.code.coding.code` | `MA_DICH_VU` | Bảng 3 (STT3) | Chuỗi(50) | Mã DVKT theo DMDC BYT |
| 5 | `ServiceRequest.code.text` | `TEN_DICH_VU` | Bảng 3 (STT9) | Chuỗi(1024) | Tên dịch vụ kỹ thuật |
| 6 | `ServiceRequest.category` | — | ❌ Phải suy luận | — | **THIẾU tường minh**: cần map mã DVKT → nhóm (Lab/Imaging/Procedure) |
| 7 | `ServiceRequest.subject` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Qua JOIN với Bảng 1 theo `MA_LK` |
| 8 | `ServiceRequest.encounter` | `MA_LK` | Bảng 3 (STT1) | Chuỗi(100) | Reference → Encounter |
| 9 | `ServiceRequest.authoredOn` | `NGAY_YL` | Bảng 3 (STT35) | Chuỗi(12) | Thời điểm ra y lệnh |
| 10 | `ServiceRequest.performer` | `MA_KHOA` | Bảng 3 (STT31) | Chuỗi(20) | Khoa thực hiện |
| 11 | `ServiceRequest.requester` | `MA_BAC_SI` | Bảng 3 (STT33) | Chuỗi(255) | Bác sĩ chỉ định; nhiều mã phân cách ";" |
| 12 | `ServiceRequest.quantity` | `SO_LUONG` | Bảng 3 (STT13) | Số(10) | Số lượng DVKT |
| 13 | `ServiceRequest.priority` | — | ❌ Không có | — | **THIẾU**: routine/urgent không có trong QĐ 130 |

### Mapping trường dữ liệu — `Procedure` (thực hiện DVKT)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Procedure.status` | `NGAY_KQ` | Bảng 3 (STT37) | Chuỗi(12) | Có → `completed`; không → `in-progress` |
| 2 | `Procedure.code.coding.code` | `MA_DICH_VU` | Bảng 3 (STT3) | Chuỗi(50) | Mã DVKT |
| 3 | `Procedure.code.coding.code` (ICD-9) | `MA_PTTT_QT` | Bảng 3 (STT4) | Chuỗi(255) | Mã ICD-9 CM phẫu thuật/thủ thuật |
| 4 | `Procedure.subject` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Qua JOIN |
| 5 | `Procedure.encounter` | `MA_LK` | Bảng 3 (STT1) | Chuỗi(100) | Reference → Encounter |
| 6 | `Procedure.performedDateTime` | `NGAY_TH_YL` | Bảng 3 (STT36) | Chuỗi(12) | Thời điểm thực hiện y lệnh |
| 7 | `Procedure.performer[0].actor` | `NGUOI_THUC_HIEN` | Bảng 3 (STT34) | Chuỗi(255) | Mã định danh y tế người thực hiện |
| 8 | `Procedure.usedCode` | `MA_VAT_TU` | Bảng 3 (STT5) | Chuỗi(255) | Vật tư y tế sử dụng kèm |
| 9 | `Procedure.extension[vo-cam]` | `PP_VO_CAM` | Bảng 3 (STT40) | Số(1) | 1=Gây mê, 2=Gây tê, 3=Châm tê, 4=Khác |
| 10 | `Procedure.bodySite` | `VI_TRI_TH_DVKT` | Bảng 3 (STT41) | Số(3) | Vị trí cơ thể thực hiện |
| 11 | `Procedure.extension[may-thuc-hien]` | `MA_MAY` | Bảng 3 (STT42) | Chuỗi(1024) | Mã máy thực hiện theo quy tắc XX.n.YYYYY.Z |

### Mapping trường dữ liệu — `DiagnosticReport` (kết quả CLS, từ Bảng 4)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `DiagnosticReport.code.coding.code` | `MA_DICH_VU` | Bảng 4 (STT3) | Chuỗi(15) | Mã DVKT cận lâm sàng |
| 2 | `DiagnosticReport.issued` | `NGAY_KQ` | Bảng 4 (STT10) | Chuỗi(12) | Thời điểm có kết quả |
| 3 | `DiagnosticReport.result[]` | — | — | — | Reference → Observation |
| 4 | `Observation.code.coding.code` | `MA_CHI_SO` | Bảng 4 (STT4) | Chuỗi(50) | Mã chỉ số xét nghiệm |
| 5 | `Observation.code.text` | `TEN_CHI_SO` | Bảng 4 (STT5) | Chuỗi(255) | Tên chỉ số |
| 6 | `Observation.valueString` | `GIA_TRI` | Bảng 4 (STT6) | Chuỗi(50) | Giá trị kết quả |
| 7 | `Observation.valueQuantity.unit` | `DON_VI_DO` | Bảng 4 (STT7) | Chuỗi(50) | Đơn vị đo |
| 8 | `DiagnosticReport.conclusion` | `KET_LUAN` | Bảng 4 (STT9) | Chuỗi(n) | Kết luận đọc kết quả |
| 9 | `DiagnosticReport.presentedForm[0].data` | `MO_TA` | Bảng 4 (STT8) | Chuỗi(n) | Mô tả kết quả |

### Phân loại category DVKT (cần suy luận)

| Tiền tố mã DVKT (DMDC) | Category FHIR | SNOMED code |
|---|---|---|
| `09.` (xét nghiệm) | Laboratory | `108252007` |
| `18.`-`28.` (CĐHA) | Imaging | `363679005` |
| `01.`-`08.` (thủ thuật) | Procedure | `387713003` |
| Hội chẩn | Consultation | `11429006` |

### Phân tích khoảng cách (Gap)

| Vấn đề | Mức độ | Giải pháp |
|---|---|---|
| Category DVKT phải suy luận từ mã DMDC | ⚠️ Trung bình | Build lookup table mã DVKT → category |
| `priority` không có | ⚠️ Nhỏ | Bỏ qua hoặc mặc định `routine` |
| `Observation.value` kiểu số hóa kém (`GIA_TRI` là chuỗi) | ⚠️ Trung bình | Parse thành `valueQuantity` khi có đơn vị; giữ `valueString` khi không parse được |

### Đánh giá: ⚠️ Đủ nội dung chính, thiếu phân loại category tường minh

---

## Báo cáo 16 — Thống Kê Ca Mắc theo ICD ✅

### Resource FHIR chính: `Condition`

### Mapping trường dữ liệu — `Condition`

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Condition.id` | `MA_LK` + `MA_BENH_CHINH` | Bảng 1 (STT1, STT26) | Composite | Composite key đảm bảo duy nhất |
| 2 | `Condition.clinicalStatus.code` | `KET_QUA_DTRI` | Bảng 1 (STT40) | Số(1) | 1/2→`resolved`; 3/4→`active`; 5→`inactive`; 6/7→`active` |
| 3 | `Condition.verificationStatus.code` | — | — | — | Mặc định `confirmed` (đã qua chẩn đoán bác sĩ) |
| 4 | `Condition.category[0].code` | — | — | — | `encounter-diagnosis` |
| 5 | `Condition.code.coding.system` | — | — | — | `http://hl7.org/fhir/sid/icd-10` |
| 6 | `Condition.code.coding.code` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Mã ICD-10 bệnh chính (QĐ 4469/QĐ-BYT) |
| 7 | `Condition.code.text` | `CHAN_DOAN_RV` | Bảng 1 (STT25) | Chuỗi(n) | Chẩn đoán xác định ra viện đầy đủ |
| 8 | `Condition.subject` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Reference → Patient |
| 9 | `Condition.encounter` | `MA_LK` | Bảng 1 (STT1) | Chuỗi(100) | Reference → Encounter |
| 10 | `Condition.recordedDate` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Ngày ghi nhận chẩn đoán cuối |
| 11 | `Condition.asserter` | `MA_TTDV` | Bảng 1 (STT64) | Chuỗi(10) | Bác sĩ xác nhận (mã định danh y tế) |
| 12 | `Condition.note[0].text` | `CHAN_DOAN_VAO` | Bảng 1 (STT24) | Chuỗi(n) | Chẩn đoán sơ bộ khi vào |

### Mapping bệnh kèm theo — `Condition` (additional)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Condition.code.coding.code` | `MA_BENH_KT` (split ";") | Bảng 1 (STT27) | Chuỗi(100) | Tách chuỗi theo ";", tối đa 12 mã |
| 2 | `Condition.category[0].code` | — | — | — | `problem-list-item` (phân biệt với bệnh chính) |
| 3 | `Encounter.diagnosis[].rank` | — | — | — | rank=1 cho bệnh chính; rank=2,3... cho bệnh kèm |

### Mapping bệnh YHCT — Extension

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Condition.code.coding` (YHCT) | `MA_BENH_YHCT` | Bảng 1 (STT28) | Chuỗi(255) | Mã bệnh YHCT song song với ICD-10 |
| 2 | `Condition.code.coding.system` | — | — | — | `https://moh.gov.vn/yhct` (hệ thống YHCT VN) |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 17 — Số Đơn Thuốc ✅

### Resource FHIR chính: `MedicationRequest` + `Medication`

### Mapping trường dữ liệu — `MedicationRequest`

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `MedicationRequest.id` | `MA_LK` + `STT` | Bảng 2 (STT1, STT2) | Composite | Composite key |
| 2 | `MedicationRequest.status` | `NGAY_YL` + context | Bảng 2 (STT34) | Chuỗi(12) | `completed` nếu đã cấp phát; `active` nếu đang dùng |
| 3 | `MedicationRequest.intent` | — | — | — | Cố định: `order` |
| 4 | `MedicationRequest.medicationCodeableConcept.code` | `MA_THUOC` | Bảng 2 (STT3) | Chuỗi(255) | Mã hoạt chất theo DMDC BYT |
| 5 | `MedicationRequest.medicationCodeableConcept.text` | `TEN_THUOC` | Bảng 2 (STT7) | Chuỗi(1024) | Tên thuốc theo số đăng ký |
| 6 | `MedicationRequest.subject` | `MA_BN` | Bảng 1 (STT3) | Chuỗi(100) | Qua JOIN Bảng 1 theo `MA_LK` |
| 7 | `MedicationRequest.encounter` | `MA_LK` | Bảng 2 (STT1) | Chuỗi(100) | Reference → Encounter |
| 8 | `MedicationRequest.authoredOn` | `NGAY_YL` | Bảng 2 (STT34) | Chuỗi(12) | Ngày ra y lệnh thuốc |
| 9 | `MedicationRequest.requester` | `MA_BAC_SI` | Bảng 2 (STT32) | Chuỗi(255) | Mã bác sĩ kê đơn; nhiều mã phân cách ";" |
| 10 | `MedicationRequest.dosageInstruction[0].text` | `LIEU_DUNG` | Bảng 2 (STT12) | Chuỗi(1024) | Liều dùng chi tiết |
| 11 | `MedicationRequest.dosageInstruction[0].additionalInstruction[0].text` | `CACH_DUNG` | Bảng 2 (STT13) | Chuỗi(1024) | Cách dùng (lời dặn bác sĩ) |
| 12 | `MedicationRequest.dosageInstruction[0].route.coding.code` | `DUONG_DUNG` | Bảng 2 (STT10) | Chuỗi(4) | Mã đường dùng thuốc |
| 13 | `MedicationRequest.dispenseRequest.quantity.value` | `SO_LUONG` | Bảng 2 (STT18) | Số(10) | Số lượng thuốc, 3 chữ số thập phân |
| 14 | `MedicationRequest.dispenseRequest.quantity.unit` | `DON_VI_TINH` | Bảng 2 (STT8) | Chuỗi(50) | Đơn vị tính nhỏ nhất |
| 15 | `MedicationRequest.dispenseRequest.performer` | — | — | — | Suy luận từ `MA_CSKCB_THUOC` Bảng 2 (STT5) |
| 16 | `MedicationRequest.extension[pham-vi]` | `PHAM_VI` | Bảng 2 (STT16) | Số(1) | 1=trong BHYT, 2=ngoài BHYT, 3=quân đội/công an |
| 17 | `MedicationRequest.extension[nguon-chi-tra]` | `NGUON_CTRA` | Bảng 2 (STT36) | Số(1) | 1=BHYT, 2=dự án, 3=CT mục tiêu, 4=khác |

### Mapping trường dữ liệu — `Medication`

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Medication.code.coding.code` | `MA_THUOC` | Bảng 2 (STT3) | Chuỗi(255) | Mã hoạt chất |
| 2 | `Medication.code.text` | `TEN_THUOC` | Bảng 2 (STT7) | Chuỗi(1024) | Tên thương mại |
| 3 | `Medication.form.coding.code` | `DANG_BAO_CHE` | Bảng 2 (STT11) | Chuỗi(1024) | Dạng bào chế |
| 4 | `Medication.ingredient[0].itemCodeableConcept.code` | `MA_THUOC` | Bảng 2 (STT3) | Chuỗi(255) | Hoạt chất; nhiều phân cách "+" |
| 5 | `Medication.ingredient[0].strength.numerator.value` | `HAM_LUONG` | Bảng 2 (STT9) | Chuỗi(1024) | Hàm lượng; nhiều thành phần phân cách "+" |
| 6 | `Medication.extension[so-dang-ky]` | `SO_DANG_KY` | Bảng 2 (STT14) | Chuỗi(255) | Số đăng ký lưu hành |
| 7 | `Medication.extension[thong-tin-thau]` | `TT_THAU` | Bảng 2 (STT15) | Chuỗi(50) | Thông tin gói thầu: số QĐ;Gi;Ni;XXXX |

### Xác định "số đơn thuốc" (groupIdentifier)

```
Một "đơn thuốc" trong QĐ 130 = tập hợp các dòng thuốc (MA_LK + ngày Y lệnh cùng nhau)

FHIR groupIdentifier:
  system: "https://[cskcb]/prescription-group"
  value:  MA_LK + "_" + NGAY_YL (yyyymmdd)

Đếm số đơn = COUNT(DISTINCT groupIdentifier) theo kỳ báo cáo
```

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 18 — Top 20 Bệnh theo ICD ✅

### Resource FHIR chính: `Condition` (kế thừa BC16)

### Logic đặc thù cho Top 20

| Bước | Mô tả | Trường QĐ 130 | Ghi chú |
|---|---|---|---|
| 1 | Lấy tất cả chẩn đoán đã xác định | `MA_BENH_CHINH` (Bảng 1, STT26) | Chỉ bệnh chính (rank=1) |
| 2 | Lọc kỳ báo cáo | `NGAY_RA` (Bảng 1, STT36) | Kỳ báo cáo = khoảng `NGAY_RA` |
| 3 | Lọc theo đơn vị | `MA_CSKCB`, `MA_KHOA` (Bảng 1) | Tuỳ chọn lọc theo BV/khoa |
| 4 | GROUP BY mã ICD | `MA_BENH_CHINH` | Đếm số ca mỗi mã |
| 5 | Lấy tên bệnh đầy đủ | ❌ Cần CodeSystem | JOIN với bảng ICD-10 tiếng Việt (QĐ 4469/QĐ-BYT) |
| 6 | Sắp xếp giảm dần | COUNT(MA_LK) DESC | |
| 7 | Lấy Top 20 | TOPN(20) | Power BI DAX: `TOPN(20, ...)` |

### Xử lý cấp độ mã ICD

```
MA_BENH_CHINH có thể là:
  - Mã 3 ký tự: I21 (nhóm)
  - Mã 4 ký tự: I21.0 (phân nhóm)
  - Mã 5 ký tự: I21.01 (chi tiết)
  - Mã có hậu tố: I21.0X (mở rộng)

Cần quyết định cấp độ group:
  - Top 20 theo mã 3 ký tự: phổ biến cho báo cáo tổng hợp
  - Top 20 theo mã đầy đủ: chi tiết hơn
```

### Đánh giá: ✅ Đủ dữ liệu (cần bổ sung tên ICD tiếng Việt từ CodeSystem)

---

## Báo cáo 19 — Điều Trị Nội Trú ✅

### Resource FHIR chính: `Encounter` (class=IMP)

### Mapping trường dữ liệu đặc thù nội trú

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.class.code = IMP` | `MA_LOAI_KCB` ∈ {3, 4, 6} | Bảng 1 (STT55) | Số(2) | 3=nội trú, 4=nội trú ban ngày, 6=lưu TYT |
| 2 | `Encounter.hospitalization.admitSource` | `MA_NOI_DI`, `LY_DO_VNT` | Bảng 1 (STT31, STT22) | Chuỗi | Xem BC08 |
| 3 | `Encounter.hospitalization.dischargeDisposition` | `MA_LOAI_RV` + `KET_QUA_DTRI` | Bảng 1 (STT41, STT40) | Số(1) | Xem BC06 |
| 4 | `Encounter.hospitalization.origin` | `MA_NOI_DI` | Bảng 1 (STT31) | Chuỗi(5) | Nơi chuyển đến |
| 5 | `Encounter.hospitalization.destination` | `MA_NOI_DEN` | Bảng 1 (STT32) | Chuỗi(5) | Nơi chuyển đi |
| 6 | `Encounter.hospitalization.reAdmission` | — | ❌ Không tường minh | — | Có thể suy luận nếu cùng `MA_BN` nhập viện trong 30 ngày |
| 7 | `Encounter.location[0].location` (giường) | `MA_GIUONG` | Bảng 3 (STT32) | Chuỗi(50) | Mã giường; nhiều giường phân cách ";" |
| 8 | `Encounter.location[0].period.start` | `NGAY_VAO_NOI_TRU` | Bảng 1 (STT35) | Chuỗi(12) | Thời điểm vào nội trú (khác vào viện nếu qua cấp cứu) |
| 9 | `Encounter.diagnosis[0].use.code = AD` | `CHAN_DOAN_VAO` | Bảng 1 (STT24) | Chuỗi(n) | Chẩn đoán khi nhập viện (Admission Diagnosis) |
| 10 | `Encounter.diagnosis[1].use.code = DD` | `CHAN_DOAN_RV` + `MA_BENH_CHINH` | Bảng 1 (STT25, STT26) | Chuỗi(n) + Chuỗi(7) | Chẩn đoán ra viện (Discharge Diagnosis) |
| 11 | `Encounter.diagnosis[].rank` | — | — | — | rank=1 bệnh chính; rank=2+ bệnh kèm |
| 12 | `Encounter.extension[can-nang]` | `CAN_NANG` | Bảng 1 (STT59) | Chuỗi(6) | Cân nặng kg, 2 số thập phân |
| 13 | `Encounter.extension[can-nang-con]` | `CAN_NANG_CON` | Bảng 1 (STT60) | Chuỗi(100) | Cân nặng trẻ sinh (gram); nhiều con phân cách ";" |
| 14 | `Encounter.extension[pp-dieu-tri]` | `PP_DIEU_TRI` | Bảng 1 (STT39) | Chuỗi(n) | Phương pháp điều trị |
| 15 | `Encounter.note[0].text` | `GHI_CHU` | Bảng 1 (STT42) | Chuỗi(n) | Lời dặn bác sĩ khi ra viện |

### Mapping từ Bảng 7 (Giấy ra viện) → `DocumentReference` + `Encounter` bổ sung

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Ghi chú |
|---|---|---|---|---|
| 1 | `DocumentReference.identifier[0].value` | `SO_LUU_TRU` | Bảng 7 (STT2) | Số lưu trữ hồ sơ bệnh án |
| 2 | `DocumentReference.type` | — | — | `discharge-summary` |
| 3 | `DocumentReference.author` | `MA_BS` | Bảng 7 (STT15) | Trưởng khoa ký |
| 4 | `DocumentReference.date` | `NGAY_CT` | Bảng 7 (STT17) | Ngày cấp giấy ra viện |
| 5 | `Encounter.extension[dinh-chi-thai]` | `MA_DINH_CHI_THAI` | Bảng 7 (STT7) | 1=đình chỉ, 0=không |
| 6 | `Encounter.extension[tuoi-thai]` | `TUOI_THAI` | Bảng 7 (STT10) | Tuần tuổi thai 1-42 |

### Mapping từ Bảng 8 (Tóm tắt HSBA) → `EpisodeOfCare` bổ sung

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Ghi chú |
|---|---|---|---|---|
| 1 | `EpisodeOfCare.note[0].text` | `QT_BENHLY` | Bảng 8 (STT11) | Quá trình bệnh lý |
| 2 | `DiagnosticReport.conclusion` | `TOMTAT_KQ` | Bảng 8 (STT12) | Tóm tắt kết quả xét nghiệm |
| 3 | `Observation` (sơ sinh) | `NGAY_SINHCON`, `NGAY_CONCHET`, `SO_CONCHET` | Bảng 8 (STT14-16) | Chỉ dùng khi sinh con |

### Đánh giá: ✅ Đủ dữ liệu cơ bản và chi tiết

---

## Báo cáo 20 — Tổng Số Ngày Điều Trị theo Ngày ✅

### Resource FHIR chính: `Encounter` + DimDate (Power BI)

### Mapping trường dữ liệu (kế thừa BC06)

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Ghi chú |
|---|---|---|---|---|
| 1 | `Encounter.period.start` | `NGAY_VAO` | Bảng 1 (STT34) | Ngày bắt đầu đợt điều trị |
| 2 | `Encounter.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Ngày kết thúc đợt điều trị |
| 3 | `Encounter.serviceProvider` | `MA_CSKCB` | Bảng 1 (STT57) | Breakdown theo đơn vị |
| 4 | `Encounter.location[].location` | `MA_KHOA` | Bảng 1 (STT56) | Breakdown theo khoa |

### Logic tính Census theo ngày

```
Census(D) = COUNT(Encounter WHERE
    class = 'IMP' AND
    NGAY_VAO_NOI_TRU <= D AND
    (NGAY_RA IS NULL OR NGAY_RA >= D)
)

Nguồn: NGAY_VAO_NOI_TRU (Bảng 1, STT35) và NGAY_RA (Bảng 1, STT36)
Lưu ý: Dùng NGAY_VAO_NOI_TRU thay NGAY_VAO để chính xác hơn cho nội trú
```

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 21 — Thống Kê Chi Phí theo Ngày ✅

### Resource FHIR chính: `Claim` + `ChargeItem` + `Invoice`

### Mapping trường dữ liệu — theo chiều thời gian

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `ChargeItem.occurrenceDateTime` | `NGAY_YL` | Bảng 2 (STT34), Bảng 3 (STT35) | Chuỗi(12) | Ngày phát sinh chi phí (ngày ra y lệnh) |
| 2 | `Claim.created` | `NGAY_TTOAN` | Bảng 1 (STT43) | Chuỗi(12) | Ngày thanh toán; có thể sau NGAY_RA |
| 3 | `ChargeItem.quantity.value` | `SO_LUONG` | Bảng 2 (STT18), Bảng 3 (STT13) | Số | Số lượng phát sinh |
| 4 | `ChargeItem.priceOverride.value` | `DON_GIA` | Bảng 2 (STT19), Bảng 3 (STT14) | Số(15) | Đơn giá |
| 5 | `ChargeItem.totalPriceComponent` | `THANH_TIEN_BV` | Bảng 2 (STT20), Bảng 3 (STT19) | Số(15) | = SO_LUONG × DON_GIA |
| 6 | `ChargeItem.performingOrganization` | `MA_KHOA` | Bảng 2 (STT31), Bảng 3 (STT31) | Chuỗi | Khoa phát sinh chi phí |
| 7 | `Coverage.costToBeneficiary` | `MUC_HUONG` | Bảng 2 (STT27), Bảng 3 (STT22) | Số(3) | Mức hưởng BHYT: 80/95/100/trái tuyến |

### Phân tầng chi phí theo ngày

| Tầng | Trường QĐ 130 | Bảng | Ghi chú |
|---|---|---|---|
| Chi phí thuốc theo ngày | `THANH_TIEN_BV` WHERE Bảng 2 | Bảng 2 | Phân tích theo `NGAY_YL` |
| Chi phí DVKT theo ngày | `THANH_TIEN_BV` WHERE Bảng 3 | Bảng 3 | Phân tích theo `NGAY_YL` |
| Chi phí BHYT theo ngày | `THANH_TIEN_BH` | Bảng 2, 3 | = SO_LUONG × DON_GIA × TYLE_TT_BH/100 |
| Tổng thanh toán theo ngày | `T_BHTT` | Bảng 1 | Tổng hợp từ Bảng 1 theo ngày thanh toán |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 22 — Điều Trị Nội Trú theo Ngày ✅

### Resource FHIR chính: `Encounter` (class=IMP) theo trục thời gian

### Mapping 3 metric chính

| Metric | Trường QĐ 130 | Bảng | Công thức |
|---|---|---|---|
| **Nhập viện (ngày D)** | `NGAY_VAO_NOI_TRU` (STT35) | Bảng 1 | `COUNT WHERE DATE(NGAY_VAO_NOI_TRU) = D` |
| **Ra viện (ngày D)** | `NGAY_RA` (STT36) | Bảng 1 | `COUNT WHERE DATE(NGAY_RA) = D AND MA_LOAI_KCB IN (3,4,6)` |
| **Census (ngày D)** | `NGAY_VAO_NOI_TRU` + `NGAY_RA` | Bảng 1 | `COUNT WHERE NGAY_VAO_NOI_TRU ≤ D AND (NGAY_RA IS NULL OR NGAY_RA ≥ D)` |

### Mapping trường bổ sung

| # | Trường FHIR | Trường QĐ 130 | Bảng | Ghi chú |
|---|---|---|---|---|
| 1 | `Encounter.hospitalization.admitSource` | `MA_NOI_DI`, `LY_DO_VNT` | Bảng 1 | Phân tích nguồn nhập viện hàng ngày |
| 2 | `Encounter.hospitalization.dischargeDisposition` | `MA_LOAI_RV` | Bảng 1 | Phân loại ra viện hàng ngày |
| 3 | `Encounter.serviceProvider` | `MA_CSKCB` | Bảng 1 | Breakdown theo BV |
| 4 | `Encounter.location[].location` | `MA_KHOA` | Bảng 1 | Breakdown theo khoa |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Báo cáo 23 — Thống Kê Hồ Sơ KCB theo Ngày Ra Viện ✅

### Resource FHIR chính: `Encounter` + `EpisodeOfCare`

### Mapping trường dữ liệu

| # | Trường FHIR | Trường QĐ 130 | Bảng QĐ 130 | Kiểu QĐ 130 | Ghi chú mapping |
|---|---|---|---|---|---|
| 1 | `Encounter.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | **Chiều GROUP BY chính** — ngày ra viện |
| 2 | `Encounter.status = finished` | `NGAY_RA` có giá trị | Bảng 1 | — | Filter hồ sơ đã kết thúc |
| 3 | `Encounter.hospitalization.dischargeDisposition` | `MA_LOAI_RV` | Bảng 1 (STT41) | Số(1) | Phân loại hình thức ra viện |
| 4 | `Encounter.class` | `MA_LOAI_KCB` | Bảng 1 (STT55) | Số(2) | IMP/AMB/EMER |
| 5 | `Encounter.diagnosis[{rank=1}].condition` | `MA_BENH_CHINH` | Bảng 1 (STT26) | Chuỗi(7) | Chẩn đoán chính ra viện |
| 6 | `EpisodeOfCare.status = finished` | `NGAY_RA` có giá trị | Bảng 1 | — | Hồ sơ đã đóng |
| 7 | `EpisodeOfCare.period.end` | `NGAY_RA` | Bảng 1 (STT36) | Chuỗi(12) | Ngày đóng hồ sơ |
| 8 | `Encounter.serviceProvider` | `MA_CSKCB` | Bảng 1 (STT57) | Chuỗi(5) | Breakdown theo BV |
| 9 | `Claim.created` | `NGAY_TTOAN` | Bảng 1 (STT43) | Chuỗi(12) | Ngày thanh toán khi ra viện |
| 10 | `Encounter.extension[ngay-tai-kham]` | `NGAY_TAI_KHAM` | Bảng 1 (STT62) | Chuỗi(50) | Ngày tái khám; nhiều ngày phân cách ";" |
| 11 | `Encounter.extension[nam-qt]` | `NAM_QT` | Bảng 1 (STT53) | Số(4) | Năm đề nghị thanh toán |
| 12 | `Encounter.extension[thang-qt]` | `THANG_QT` | Bảng 1 (STT54) | Số(2) | Tháng đề nghị thanh toán |

### Phân loại `dischargeDisposition` cho báo cáo

| MA_LOAI_RV | FHIR code | Nhóm thống kê |
|---|---|---|
| 1 | `home` | Ra viện bình thường |
| 2 | `hosp` | Chuyển viện (chuyên môn) |
| 3 | `oth` | Trốn viện |
| 4 | `aadvice` | Xin ra viện |
| 5 | `other-hcf` | Chuyển viện (tự nguyện) |
| — | `exp` | Tử vong (từ KET_QUA_DTRI=5) |

### Đánh giá: ✅ Đủ dữ liệu hoàn toàn

---

## Phụ lục A — Quy tắc chuyển đổi định dạng dữ liệu chung

### A1. Chuyển đổi định dạng ngày giờ

| Định dạng QĐ 130 | Ký tự | FHIR dateTime | Ví dụ |
|---|---|---|---|
| `yyyymmddHHMM` | 12 ký tự | `yyyy-MM-ddTHH:mm:ss+07:00` | `202401150830` → `2024-01-15T08:30:00+07:00` |
| `yyyymmdd` | 8 ký tự | `yyyy-MM-dd` | `20240115` → `2024-01-15` |
| `00000000` | Không xác định ngày | null hoặc chỉ lưu năm | Xử lý ngoại lệ |
| `yyyymm0000` | Thiếu ngày | `yyyy-MM` (partial date) | `202401000000` → `2024-01` |

### A2. Tách chuỗi đa giá trị

| Dấu phân cách | Trường áp dụng | FHIR xử lý |
|---|---|---|
| `;` (chấm phẩy) | `MA_BENH_KT`, `MA_THE_BHYT`, `MA_KHOA`, `MA_BAC_SI`, `NGAY_TAI_KHAM`, `MA_PTTT_QT` | Tách thành array `[]` |
| `+` (dấu cộng) | `MA_THUOC` (đa hoạt chất), `HAM_LUONG` | Tách từng thành phần |
| `.` (dấu chấm) | `MA_CSKCB_THUOC` (C.XXXXX, K.XXXXX) | Parse prefix + mã cơ sở |

### A3. Mã hóa đặc biệt

| Mã đặc biệt | Ý nghĩa | Xử lý FHIR |
|---|---|---|
| `VM.XXXXX` | Vận chuyển máu từ cơ sở XXXXX | `MedicationRequest.extension[van-chuyen-mau]` |
| `BB.XXXXX` | Bao bì thuốc thang từ cơ sở XXXXX | `MedicationRequest.extension[bao-bi]` |
| `VC.XXXXX` | Vận chuyển bệnh nhân đến cơ sở XXXXX | `Procedure.extension[van-chuyen-bn]` |
| `C.XXXXX` | Thuốc chuyển từ cơ sở XXXXX | `MedicationRequest.extension[chuyen-thuoc]` |
| `K.XXXXX` | Thuốc ngoài giá CLS tại cơ sở XXXXX | `MedicationRequest.extension[thuoc-ngoai-gia]` |
| `M.XXXXX` | Máu từ cơ sở cung cấp XXXXX | `MedicationRequest.extension[nguon-mau]` |
| `XX.YYYY.ZZZZ.K.WWWWW` | DVKT/CLS tại cơ sở WWWWW | `ServiceRequest.extension[dvkt-chuyen]` |
| `XX.YYYY.ZZZZ_GT` | DVKT có gây tê | `Procedure.extension[phuong-phap-vo-cam]` |
| `XX.YYYY.ZZZZ_TB` | DVKT bắt đầu nhưng không hoàn thành | `Procedure.status = stopped` |
| `XX.YYYY.0000` | DVKT chưa có giá | `ChargeItem.priceOverride = 0` |

### A4. Trường có giá trị rỗng (để trống)

| Quy tắc QĐ 130 | Trường ví dụ | FHIR xử lý |
|---|---|---|
| Không KBCB BHYT → để trống | `MA_THE_BHYT`, `MA_DKBD`, `GT_THE_TU`, `GT_THE_DEN` | Không tạo `Coverage` resource |
| Không chuyển tuyến → để trống | `MA_NOI_DI`, `MA_NOI_DEN`, `GIAY_CHUYEN_TUYEN` | Không set `admitSource`/`destination` |
| Chưa thanh toán → để trống | `NGAY_TTOAN` | `Claim.status = active` (chưa submitted) |

---

## Phụ lục B — Ma trận Resource × Bảng QĐ 130

| FHIR Resource | Bảng Check-in | Bảng 1 | Bảng 2 | Bảng 3 | Bảng 4 | Bảng 5 | Bảng 6 | Bảng 7 | Bảng 8 | Bảng 9-11 | Bảng 12 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Patient` | ✅ | ✅ | — | — | — | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| `Encounter` | ✅ | ✅ | — | — | — | ✅ | — | ✅ | ✅ | — | — |
| `Condition` | — | ✅ | — | — | — | ✅ | — | — | — | — | — |
| `Coverage` | ✅ | ✅ | — | — | — | — | ✅ | — | — | — | — |
| `Claim` | — | ✅ | ✅ | ✅ | — | — | — | — | — | — | — |
| `MedicationRequest` | — | — | ✅ | — | — | — | — | — | — | — | — |
| `Medication` | — | — | ✅ | — | — | — | — | — | — | — | — |
| `ServiceRequest` | ✅ | — | — | ✅ | — | — | — | — | — | — | — |
| `Procedure` | — | ✅ | — | ✅ | — | — | — | — | — | — | — |
| `DiagnosticReport` | — | — | — | — | ✅ | — | — | — | — | — | — |
| `Observation` | — | — | — | — | ✅ | ✅ | — | — | — | — | — |
| `EpisodeOfCare` | — | ✅ | — | — | — | — | ✅ | ✅ | ✅ | — | — |
| `Organization` | ✅ | ✅ | ✅ | ✅ | — | — | — | — | — | — | — |
| `Location` | — | ✅ | — | ✅ | — | — | — | — | — | — | — |
| `Practitioner` | — | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | ✅ |
| `DocumentReference` | — | — | — | — | — | — | — | ✅ | ✅ | ✅ | — |

---

## Phụ lục C — Tổng hợp khoảng cách (Gap Summary)

### C1. Các trường FHIR thiếu hoàn toàn trong QĐ 130

| Trường FHIR | Dùng cho BC | Mức độ ảnh hưởng | Nguồn bổ sung đề xuất |
|---|---|---|---|
| `Organization.name` (tên BV/khoa) | BC01, BC02, BC14 | ⚠️ Cao | Bộ mã DMDC — Phụ lục 5 QĐ 5937/QĐ-BYT |
| `CodeSystem.concept[].display` (tên ICD) | BC03, BC16, BC18 | ⚠️ Cao | QĐ 4469/QĐ-BYT — bảng ICD-10 tiếng Việt |
| `Organization` (nhà thuốc) | BC04 | ⚠️ Cao | Cục Quản lý Dược / HIS |
| `Location` (tổng số giường KH) | BC05 | ⚠️ Trung bình | Kế hoạch giường BV từ HIS |
| `Condition.bodySite` | BC12 | ⚠️ Thấp | Suy luận từ mã ICD S/T |
| `Condition.severity` | BC12 | ⚠️ Thấp | Suy luận từ `KET_QUA_DTRI` |
| `ServiceRequest.priority` | BC15 | ⚠️ Thấp | Mặc định `routine` |
| `Observation` (sinh tồn lâm sàng) | BC10 | ⚠️ Thấp | Bảng 5 (DIEN_BIEN_LS) không chuẩn hóa |

### C2. Tỷ lệ đáp ứng tổng hợp

| Mức đáp ứng | Số báo cáo | Danh sách BC |
|---|---|---|
| ✅ Đủ hoàn toàn (≥90%) | 15 | BC06, BC07, BC08, BC09, BC11, BC13, BC14, BC16, BC17, BC18, BC19, BC20, BC21, BC22, BC23 |
| ⚠️ Đủ một phần (60-90%) | 6 | BC01, BC02, BC05, BC10, BC12, BC15 |
| ❌ Thiếu nhiều (<60%) | 2 | BC03, BC04 |

---

*Tài liệu kỹ thuật — Phiên bản 1.0*  
*Nguồn: QĐ 130/QĐ-BYT (18/01/2023) | Chuẩn: HL7 FHIR R4B (4.3.0)*  
*Tham chiếu: https://hl7.org/fhir/R4B/*
