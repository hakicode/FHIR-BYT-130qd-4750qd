# Mapping Trường Dữ Liệu Chi Tiết: XML (QĐ 130 + QĐ 4750) → FHIR R4B
## 23 Báo cáo Power BI — Field-Level Mapping Document

> **Phiên bản:** 3.0  
> **Nguồn XML:** QĐ 130/QĐ-BYT (18/01/2023) + QĐ 4750/QĐ-BYT (29/12/2023)  
> **Đích:** HL7 FHIR R4B (4.3.0)  
> **Hiệu lực:** 01/07/2024  
>
> **Cấu trúc mỗi báo cáo:**  
> - Bảng mapping: Trường FHIR ↔ Trường XML (tên, bảng nguồn, kiểu DL sau QĐ 4750, ghi chú chuyển đổi)  
> - Bảng resource liên quan  
> - Logic/công thức Power BI  
>
> **Ký hiệu:** ✅ Có đủ | ⚠️ Suy luận/một phần | ❌ Thiếu — cần nguồn ngoài  
> **QĐ 4750:** 🆕 Trường mới | 🔄 Đã sửa kiểu/size | 📝 Sửa diễn giải | ⚠️ Thay đổi nghiệp vụ

---

## Báo cáo 01 — Danh mục Bệnh viện ⚠️

**Resource chính:** `Organization` (type=`prov`)  
**Endpoint FHIR:** `GET /Organization?type=prov&_include=Organization:partof`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Organization.id` | id | ✅ | — | — | — | Tự sinh: `org-{MA_CSKCB}` |
| `Organization.identifier[0].system` | uri | ✅ | — | — | — | Cố định: `https://moh.gov.vn/cskcb` |
| `Organization.identifier[0].value` | string | ✅ | `MA_CSKCB` | B1(58), Checkin(18) | Chuỗi(5) | Mã 5 ký tự do cơ quan thẩm quyền cấp |
| `Organization.active` | boolean | ✅ | — | — | — | Mặc định `true` |
| `Organization.type[0].coding.code` | code | ✅ | — | — | — | Cố định: `prov` |
| `Organization.type[0].coding.display` | string | ✅ | — | — | — | `Healthcare Provider` |
| `Organization.name` | string | ✅ | ❌ | — | — | **THIẾU** — Lấy từ DMDC QĐ 5937/QĐ-BYT |
| `Organization.alias[]` | string[] | ⚪ | ❌ | — | — | **THIẾU** — Tên viết tắt BV |
| `Organization.telecom[].value` | string | ⚪ | ❌ | — | — | **THIẾU** — SĐT, email BV |
| `Organization.address[0].text` | string | ⚪ | ❌ | — | — | **THIẾU** — Địa chỉ BV |
| `Organization.partOf` | Reference | ⚪ | ❌ | — | — | **THIẾU** — BV → Sở Y tế |

### Resource liên quan

| Resource | Liên kết | Mục đích trong báo cáo |
|---|---|---|
| `Location` | `Location.managingOrganization` → `Organization.id` | Địa chỉ vật lý, khu vực BV |
| `Encounter` | `Encounter.serviceProvider` → `Organization.id` | Thống kê lượt khám theo BV |
| `Practitioner` | `PractitionerRole.organization` → `Organization.id` | Nhân sự BV |

### Khoảng cách & Giải pháp

| Trạng thái | Số trường | Giải pháp |
|---|---|---|
| ✅ Từ XML | 1 | `MA_CSKCB` → identifier |
| ❌ Cần nguồn ngoài | 5 | JOIN bảng danh mục CSKCB từ DMDC QĐ 5937/QĐ-BYT hoặc Cổng BHXH |

---

## Báo cáo 02 — Danh mục Khoa ⚠️

**Resource chính:** `Organization` (type=`dept`) + `Location`  
**Endpoint FHIR:** `GET /Organization?type=dept&_include=Organization:partof`

### Mapping trường — `Organization` (Khoa)

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Organization.id` | id | ✅ | `MA_KHOA` | B1(57) | Chuỗi(50) | Tự sinh: `org-khoa-{MA_KHOA}` |
| `Organization.identifier[0].value` | string | ✅ | `MA_KHOA` | B1(57), B2(31), B3(31) | Chuỗi(50) | Phụ lục 5 QĐ 5937/QĐ-BYT |
| `Organization.active` | boolean | ✅ | — | — | — | Mặc định `true` |
| `Organization.type[0].coding.code` | code | ✅ | — | — | — | Cố định: `dept` |
| `Organization.name` | string | ✅ | ❌ | — | — | **THIẾU** — Cần DMDC khoa |
| `Organization.partOf` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | → `Organization/org-{MA_CSKCB}` |

### Mapping trường — `Location` (Phòng/Giường trong khoa)

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Location.id` | id | ✅ | `MA_GIUONG` | B3(32) | Chuỗi(50) | Tự sinh: `loc-{MA_KHOA}-{MA_GIUONG}` |
| `Location.name` | string | ✅ | `MA_GIUONG` | B3(32) | Chuỗi(50) | H001=KH; T001=kê thêm; C001=tự chọn; K001=khác |
| `Location.status` | code | ✅ | — | — | — | Mặc định `active` |
| `Location.physicalType.coding.code` | code | ✅ | — | — | — | `bd` (bed) hoặc `ro` (room) |
| `Location.managingOrganization` | Reference | ✅ | `MA_KHOA` | B3(31) | Chuỗi(20) | → `Organization/org-khoa-{MA_KHOA}` |
| `Location.partOf` | Reference | ⚪ | ❌ | — | — | **THIẾU** — Phòng chứa giường |

### Resource liên quan

| Resource | Liên kết | Mục đích |
|---|---|---|
| `Organization` (BV cha) | `Organization.partOf` → `Organization.id` | Phân cấp BV → Khoa |
| `Encounter` | `Encounter.location[].location` → `Location.id` | BN đang ở khoa/giường nào |
| `PractitionerRole` | `PractitionerRole.organization` → `Organization.id` | Nhân sự trong khoa |

---

## Báo cáo 03 — Danh mục Bệnh theo ICD ❌

**Resource chính:** `CodeSystem` + `ValueSet`  
**Endpoint FHIR:** `GET /CodeSystem?url=http://hl7.org/fhir/sid/icd-10`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `CodeSystem.url` | uri | ✅ | — | — | — | Cố định: `http://hl7.org/fhir/sid/icd-10` |
| `CodeSystem.version` | string | ✅ | — | — | — | `QD4469-2020` theo QĐ 4469/QĐ-BYT |
| `CodeSystem.concept[].code` | code | ✅ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Chỉ là **tham chiếu** — không định nghĩa |
| `CodeSystem.concept[].code` | code | ✅ | `MA_BENH_KT` | B1(28) | Chuỗi(100) | Split ";"; tối đa 12 mã |
| `CodeSystem.concept[].display` | string | ✅ | ❌ | — | — | **THIẾU** — Cần import QĐ 4469/QĐ-BYT |
| `ValueSet.compose.include.concept[].code` | code | ✅ | `MA_BENH_YHCT` | B1(29) | Chuỗi(255) | Mã YHCT song song; system riêng `https://moh.gov.vn/yhct` |

> **Kết luận:** QĐ 130 + QĐ 4750 chỉ **dùng** mã ICD, không định nghĩa CodeSystem.  
> **Giải pháp:** Import riêng bảng ICD-10 tiếng Việt từ QĐ 4469/QĐ-BYT ngày 28/10/2020.

---

## Báo cáo 04 — Danh mục Nhà thuốc ❌

**Resource chính:** `Organization` (type=`pharm`) + `Location`  
**Endpoint FHIR:** `GET /Organization?type=pharm`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Organization.identifier[0].value` | string | ✅ | `MA_CSKCB_THUOC` | B2(5) | Chuỗi(10) | Chỉ là mã CSKCB xuất xứ thuốc đặc biệt — không phải mã nhà thuốc |
| `Organization.name` | string | ✅ | ❌ | — | — | **THIẾU hoàn toàn** |
| `Organization.type` | CodeableConcept | ✅ | ❌ | — | — | **THIẾU** — phân loại nhà thuốc |
| `Organization.address` | Address[] | ✅ | ❌ | — | — | **THIẾU** |
| `Location.hoursOfOperation` | BackboneElement | ⚪ | ❌ | — | — | **THIẾU** |

> **Kết luận:** QĐ 130 + QĐ 4750 không có bảng danh mục nhà thuốc.  
> **Giải pháp:** Lấy từ hệ thống cấp phép Cục Quản lý Dược hoặc module kho dược trong HIS.

---

## Báo cáo 05 — Số Giường ⚠️

**Resource chính:** `Location` (physicalType=`bd`)  
**Endpoint FHIR:** `GET /Location?physicalType=bd&status=active`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Location.id` | id | ✅ | `MA_GIUONG` + `MA_KHOA` | B3(32,31) | Chuỗi(50)+Chuỗi(20) | Tự sinh: `loc-{MA_KHOA}-{MA_GIUONG}` |
| `Location.name` | string | ✅ | `MA_GIUONG` | B3(32) | Chuỗi(50) | H=KH; T=kê thêm; C=tự chọn; K=khác |
| `Location.status` | code | ✅ | — | — | — | Mặc định `active` |
| `Location.operationalStatus` | Coding | ⚪ | ⚠️ Suy luận | B1+B3 | — | Nếu Encounter.status=`in-progress` tại giường này → `O`; còn lại → `U` |
| `Location.physicalType.coding.code` | code | ✅ | — | — | — | Cố định `bd` |
| `Location.managingOrganization` | Reference | ✅ | `MA_KHOA` | B3(31) | Chuỗi(20) | → `Organization/org-khoa-{MA_KHOA}` |
| `Location.partOf` | Reference | ⚪ | ❌ | — | — | **THIẾU** — phòng chứa giường |

### Công thức Power BI

```
TongGiuongKeHoach   = COUNTROWS(FILTER(Location, LEFT(Location[name],1) = "H"))
GiuongDangDung      = COUNTROWS(FILTER(Encounter, Encounter[status] = "in-progress"
                        && Encounter[class] = "IMP"))
GiuongTrong         = TongGiuongKeHoach - GiuongDangDung
TyLeSuDung          = DIVIDE(GiuangDangDung, TongGiuongKeHoach) * 100
```

> **Lưu ý:** Tổng giường kế hoạch chỉ phản ánh giường **đã từng sử dụng** trong dữ liệu.  
> Để có tổng giường theo kế hoạch BV, cần nhập thêm từ HIS (module giường bệnh).

---

## Báo cáo 06 — Tổng Số Ngày Điều Trị ✅

**Resource chính:** `Encounter`  
**Endpoint FHIR:** `GET /Encounter?status=finished&_include=Encounter:subject&_include=Encounter:service-provider`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.id` | id | ✅ | `MA_LK` | B1(1), Checkin(1) | Chuỗi(100) | PRIMARY KEY — mã đợt điều trị duy nhất |
| `Encounter.status` | code | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Có giá trị → `finished`; rỗng → `in-progress` |
| `Encounter.class.code` | code | ✅ | `MA_LOAI_KCB` | B1(56), Checkin(17) 🔄 | Số(2) B1; **Chuỗi(2)** Checkin | 01→`AMB`; 03→`IMP`; 04→`SS`; 09→`EMER` (xem bảng mapping) |
| `Encounter.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | → `Patient/pt-{MA_BN}` |
| `Encounter.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35), Checkin(13) | Chuỗi(12) | `202403100830` → `2024-03-10T08:30:00+07:00` |
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | `202403221000` → `2024-03-22T10:00:00+07:00`; ngoại trú mạn tính → mặc định 23:59 |
| `Encounter.length.value` | decimal | ⚪ | `SO_NGAY_DTRI` | B1(39) | Số(3) | Đã tính sẵn; xem công thức bên dưới |
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | → `Organization/org-{MA_CSKCB}` |
| `Encounter.location[0].location` | Reference | ⚪ | `MA_KHOA` | B1(57) | Chuỗi(50) | Split ";" nếu nhiều khoa → `Location[]` |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ⚪ | `MA_LOAI_RV` + `KET_QUA_DTRI` | B1(42,41) | Số(1) | Xem bảng mapping mã bên dưới |
| `Encounter.hospitalization.origin` | Reference | ⚪ | `MA_NOI_DI` | B1(32) | Chuỗi(5) | Chuyển tuyến đến — `Organization/org-{MA_NOI_DI}` |
| `Encounter.hospitalization.destination` | Reference | ⚪ | `MA_NOI_DEN` | B1(33) | Chuỗi(5) | Chuyển tuyến đi |
| `Encounter.participant[0].individual` | Reference | ⚪ | `MA_TTDV` | B1(65) | Chuỗi(10) | Mã định danh y tế người đứng đầu CSKCB |

### Bảng mapping `MA_LOAI_KCB` → `Encounter.class`

| MA_LOAI_KCB | Tên KCB | FHIR class | SO_NGAY_DTRI |
|:---:|---|---|---|
| 01 | Khám bệnh | `AMB` | 0 |
| 02 | Điều trị ngoại trú | `AMB` | ngày RA − ngày VÀO + 1 |
| 03 | Điều trị nội trú | `IMP` | ngày RA − ngày VÀO + 1 |
| 04 | Nội trú ban ngày | `SS` | ngày RA − ngày VÀO + 1 |
| 05 | Ngoại trú mạn tính + khám + thuốc | `AMB` | số ngày dùng thuốc |
| 06 | Lưu TYT xã / PKĐKKV | `IMP` | ngày RA − ngày VÀO + 1 |
| 07 | Nhận thuốc theo hẹn | `AMB` | 0 |
| 08 | Ngoại trú mạn tính + DVKT | `AMB` | số ngày thực tế có DVKT |
| 09 | Cấp cứu | `EMER` | 0 (khám) hoặc tính như IMP |

### Bảng mapping `MA_LOAI_RV` + `KET_QUA_DTRI` → `dischargeDisposition`

| MA_LOAI_RV | KET_QUA_DTRI | FHIR code | Display |
|:---:|:---:|---|---|
| 1 | 1 hoặc 2 | `home` | Về nhà |
| 1 | 5 | `exp` | Tử vong |
| 2 | bất kỳ | `hosp` | Chuyển tuyến chuyên môn |
| 3 | bất kỳ | `oth` | Trốn viện |
| 4 | bất kỳ | `aadvice` | Xin ra viện |
| 5 | bất kỳ | `other-hcf` | Chuyển tuyến theo BN |
| 1 | 6 | `aadvice` | Tiên lượng nặng xin về |

### Resource liên quan

| Resource | Liên kết FHIR | Mục đích |
|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | Nhân khẩu học BN |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | Thống kê theo BV/khoa |
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | Chẩn đoán trong đợt |
| `EpisodeOfCare` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | Hồ sơ tổng thể |
| `Location` | `Encounter.location[].location` → `Location.id` | Giường/phòng điều trị |

### Công thức Power BI

```dax
SoNgayDieuTri = Encounter[SO_NGAY_DTRI]   -- Lấy trực tiếp từ XML
-- Hoặc tính lại:
SoNgayDieuTri = DATEDIFF(Encounter[period_start], Encounter[period_end], DAY)

TongNgayDieuTri = SUM(FactEncounter[SoNgayDieuTri])
TBNgayDieuTri   = AVERAGE(FactEncounter[SoNgayDieuTri])
```

---

## Báo cáo 07 — Thống Kê Chi Phí ✅

**Resource chính:** `Claim` + `ClaimResponse` + `Coverage`  
**Endpoint FHIR:** `GET /Claim?_include=Claim:patient&_include=Claim:encounter&_include=Claim:insurance`

### Mapping trường — `Claim`

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Claim.id` | id | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | |
| `Claim.status` | code | ✅ | `NGAY_TTOAN` | B1(44) | Chuỗi(12) | Có giá trị → `active`; rỗng → `active` (chưa TT) |
| `Claim.type.coding.code` | code | ✅ | — | — | — | `institutional` |
| `Claim.use` | code | ✅ | — | — | — | `claim` |
| `Claim.patient` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | → `Patient/pt-{MA_BN}` |
| `Claim.created` | dateTime | ✅ | `NGAY_TTOAN` | B1(44) | Chuỗi(12) | yyyymmddHHMM → ISO 8601 |
| `Claim.provider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | → `Organization/org-{MA_CSKCB}` |
| `Claim.encounter` | Reference | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | → `Encounter/{MA_LK}` |
| `Claim.insurance[0].coverage` | Reference | ✅ | `MA_THE_BHYT` | B1(17) | Chuỗi(n) | → `Coverage/cov-{MA_THE_BHYT}` |
| `Claim.insurance[0].focal` | boolean | ✅ | `MA_THE_BHYT` | B1(17) | Chuỗi(n) | `true` khi có thẻ |
| `Claim.total.value` | decimal | ✅ | `T_TONGCHI_BV` | B1(47) | Số(15) | Tổng chi phí BV |
| `Claim.total.currency` | code | ✅ | — | — | — | `VND` |
| `Claim.billablePeriod.start` | date | ⚪ | `THANG_QT` + `NAM_QT` | B1(55,54) | Số(2,4) | Kỳ đề nghị thanh toán |
| `Claim.item[].productOrService.code` | code | ✅ | `MA_DICH_VU` | B3(3) | Chuỗi(50) | Mã DVKT/khám theo DMDC |
| `Claim.item[].quantity.value` | decimal | ⚪ | `SO_LUONG` | B2(18), B3(13) | Số(10) | 3 chữ số thập phân |
| `Claim.item[].unitPrice.value` | decimal | ⚪ | `DON_GIA` / `DON_GIA_BV` | B2(19), B3(14) | Số(15) | |
| `Claim.item[].net.value` | decimal | ✅ | `THANH_TIEN_BV` | B2(20), B3(19) | Số(15) | |

### Mapping trường — Chi tiết tài chính (`ClaimResponse` + `Coverage`)

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Công thức / Ghi chú |
|---|---|---|---|---|---|
| `ClaimResponse.payment.amount.value` | decimal | `T_BHTT` | B1(51) | Số(15) | = T_TONGCHI_BH − T_BNCCT |
| `ClaimResponse.total[benefit].amount` | decimal | `T_TONGCHI_BH` | B1(48) | Số(15) | Tổng trong phạm vi BHYT |
| `Coverage.identifier[0].value` | string | `MA_THE_BHYT` | B1(17) | Chuỗi(n) | Split ";" → nhiều Coverage |
| `Coverage.period.start` | date | `GT_THE_TU` | B1(19) | Chuỗi(n) | yyyymmdd; Split ";" |
| `Coverage.period.end` | date | `GT_THE_DEN` | B1(20) | Chuỗi(n) | yyyymmdd |
| `Coverage.class[0].value` | string | `MA_DKBD` | B1(18) | Chuỗi(n) | CSKCB đăng ký ban đầu |
| `Coverage.type.coding.code` | code | `MA_DOITUONG_KCB` | B1(31) | Chuỗi(3) | Đối tượng KBCB |
| `Coverage.network` | string | `MA_KHUVUC` | B1(59) | Chuỗi(2) | K1/K2/K3 |
| `Coverage.costToBeneficiary[0].value` | Money | `MUC_HUONG` | B2(27), B3(22) | Số(3) | 80/95/100 hoặc trái tuyến |
| `Invoice.totalNet` (T_BNTT) | Money | `T_BNTT` | B1(49) | Số(15) | BN tự trả ngoài BHYT |
| `Coverage.costToBeneficiary[cct]` | Money | `T_BNCCT` | B1(50) | Số(15) | BN cùng chi trả |
| Extension `T_NGUONKHAC` | Extension | `T_NGUONKHAC` | B1(52) | Số(15) | NSNN + viện trợ + trong nước + khác |
| Extension `T_BHTT_GDV` | Extension | `T_BHTT_GDV` | B1(53) | Số(15) | BHYT ngoài định suất/DRG (MA_PTTT=1) |

### Resource liên quan

| Resource | Liên kết FHIR | Mục đích |
|---|---|---|
| `Encounter` | `Claim.encounter` → `Encounter.id` | Lượt khám phát sinh chi phí |
| `Patient` | `Claim.patient` → `Patient.id` | BN chi trả |
| `Coverage` | `Claim.insurance[].coverage` → `Coverage.id` | Thông tin BHYT |
| `ClaimResponse` | `ClaimResponse.request` → `Claim.id` | Kết quả xét duyệt |
| `Organization` | `Claim.provider` → `Organization.id` | Đơn vị lập hồ sơ |

---

## Báo cáo 08 — Lượt Bệnh Nhân Vào Ra ✅

**Resource chính:** `Encounter`  
**Endpoint FHIR:** `GET /Encounter?_include=Encounter:subject&_sort=-date`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.id` | id | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | |
| `Encounter.status` | code | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Có → `finished`; rỗng → `in-progress` |
| `Encounter.class.code` | code | ✅ | `MA_LOAI_KCB` | B1(56) | Số(2) | Xem bảng mapping BC06 |
| `Encounter.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | |
| `Encounter.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35), Checkin(13) | Chuỗi(12) | Metric "Lượt vào" |
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Metric "Lượt ra" |
| `Encounter.location[0].period.start` | dateTime | ✅ | `NGAY_VAO_NOI_TRU` 🆕 | B1(36), Checkin(14) | **Chuỗi(12)** | **QĐ 4750 bổ sung vào Checkin** — thời điểm vào nội trú/ban ngày/ngoại trú chính xác |
| `Encounter.hospitalization.admitSource` | CodeableConcept | ⚪ | `MA_NOI_DI` | B1(32) | Chuỗi(5) | Có giá trị → `hosp`; trống + KCB=cấp cứu → `emd`; khác → `outp` |
| `Encounter.hospitalization.origin` | Reference | ⚪ | `MA_NOI_DI` | B1(32) | Chuỗi(5) | → `Organization/org-{MA_NOI_DI}` |
| `Encounter.hospitalization.destination` | Reference | ⚪ | `MA_NOI_DEN` | B1(33) | Chuỗi(5) | → `Organization/org-{MA_NOI_DEN}` |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ⚪ | `MA_LOAI_RV` | B1(42) | Số(1) | Xem bảng mapping BC06 |
| `Encounter.reasonCode[0].text` | string | ⚪ | `LY_DO_VV` | B1(22) | Chuỗi(n) | Lý do đến KBCB |
| `Encounter.reasonCode[1].text` | string | ⚪ | `LY_DO_VNT` | B1(23), Checkin(15) 🆕 | **Chuỗi(1024)** | **QĐ 4750 bổ sung vào Checkin** |
| `Encounter.reasonCode[1].coding.code` | code | ⚪ | `MA_LY_DO_VNT` 🆕 | B1(24), Checkin(16) | **Chuỗi(5)** | **QĐ 4750 bổ sung vào Checkin** — chờ BYT ban hành danh mục |
| `Encounter.basedOn` | Reference | ⚪ | `GIAY_CHUYEN_TUYEN` | B1(38) | Chuỗi(50) | Số giấy chuyển tuyến / giấy hẹn |
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | |

### Điểm cải thiện từ QĐ 4750

| Trường mới | Lợi ích |
|---|---|
| `NGAY_VAO_NOI_TRU` trong Checkin | Tính chính xác "door-to-bed time"; phân biệt vào viện vs vào nội trú khi qua cấp cứu |
| `LY_DO_VNT` trong Checkin | Có ngay thông tin lý do nhập viện từ khi BN đến khoa, không phải chờ Bảng 1 |
| `MA_DOITUONG_KCB` Chuỗi(4) trong Checkin | Hỗ trợ mã ghép, phân biệt rõ cấp cứu (=`2`) |

### Resource liên quan

| Resource | Liên kết FHIR | Mục đích |
|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | Phân tích lượt theo nhân khẩu |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | Thống kê theo BV/khoa |
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | Bệnh liên quan lượt vào/ra |

### Công thức Power BI

```dax
LuotVao(D)     = COUNTROWS(FILTER(Encounter, DATE(Encounter[period_start]) = D))
LuotRa(D)      = COUNTROWS(FILTER(Encounter, DATE(Encounter[period_end]) = D
                   && Encounter[status] = "finished"))
LuotVaoNoiTru(D) = COUNTROWS(FILTER(Encounter,
                   DATE(Encounter[NGAY_VAO_NOI_TRU]) = D
                   && Encounter[class] IN {"IMP","SS"}))
```

---

## Báo cáo 09 — Số BN theo Loại Hình KCB ✅

**Resource chính:** `Encounter` (GROUP BY class) + `Coverage`  
**Endpoint FHIR:** `GET /Encounter?_include=Encounter:insurance`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.class.code` | code | ✅ | `MA_LOAI_KCB` | B1(56), Checkin(17) 🔄 | Số(2) B1; **Chuỗi(2)** Checkin | Xem bảng mapping mã |
| `Encounter.type[0].coding.code` | code | ⚪ | `MA_LOAI_KCB` | B1(56) | Số(2) | Chi tiết hơn class; dùng mã DMDC |
| `Coverage.type.coding.code` | code | ⚪ | `MA_DOITUONG_KCB` | B1(31), Checkin(12) 🔄 | Chuỗi(3) B1; **Chuỗi(4)** Checkin | Nguồn tài chính; Checkin dùng khi cần nhận diện sớm |
| `Coverage.identifier[0].value` | string | ✅ | `MA_THE_BHYT` | B1(17) | Chuỗi(n) | Xác định có BHYT không |
| `Encounter.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | Đếm số BN unique |
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | Breakdown theo đơn vị |
| `Encounter.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35) | Chuỗi(12) | Lọc theo kỳ báo cáo |

### Phân loại `MA_DOITUONG_KCB` → nguồn tài chính

| Mã (Checkin Chuỗi 4 / B1 Chuỗi 3) | Diễn giải | FHIR Coverage.type |
|---|---|---|
| `1` / `001` | BHYT | `PUBLICPOL` |
| `2` / `002` | Cấp cứu BHYT — **miễn gửi Checkin** theo QĐ 4750 | `PUBLICPOL` + flag EMER |
| `3` / `003` | Miễn phí / Chính sách | `PUBLICPOL` |
| `4` / `004` | Dịch vụ / Tự trả | `pay` |

### Công thức Power BI

```dax
SoBNTheoLoaiHinh =
    SUMMARIZE(FactEncounter, FactEncounter[MA_LOAI_KCB], "SoBN", DISTINCTCOUNT(FactEncounter[MA_BN]))
```

---

## Báo cáo 10 — Số Ca Cấp Cứu Tử Vong ⚠️

**Resource chính:** `Encounter` (class=`EMER`) + `Condition`  
**Endpoint FHIR:** `GET /Encounter?class=EMER&_include=Encounter:diagnosis`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.class.code = EMER` | code | ✅ | `MA_LOAI_KCB`=09 hoặc `MA_DOITUONG_KCB`=`2` | B1(56), Checkin(12) 🔄 | Số(2); **Chuỗi(4)** Checkin | **QĐ 4750:** MA_DOITUONG_KCB=`2` (Chuỗi 4 ký tự) xác định cấp cứu BHYT rõ ràng hơn |
| `Encounter.hospitalization.dischargeDisposition.code = exp` | code | ✅ | `KET_QUA_DTRI`=5 | B1(41) | Số(1) | Mã 5=Tử vong → `exp` |
| `Encounter.status` | code | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Có → `finished` |
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Thời điểm tử vong |
| `Encounter.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | |
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | Thống kê theo đơn vị |
| `Condition.code.coding.code` | code | ✅ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Nguyên nhân tử vong ICD-10 |
| `Condition.code.coding.code` (kèm) | code | ⚪ | `MA_BENH_KT` | B1(28) | Chuỗi(100) | Split ";"; tối đa 12 mã bệnh kèm |
| `Patient.gender` | code | ⚪ | `GIOI_TINH` | B1(7) | Số(1) | 1→`male`; 2→`female`; 3→`unknown` |
| `Patient.birthDate` | date | ⚪ | `NGAY_SINH` | B1(6) | Chuỗi(12) | Tính tuổi tử vong; 8 ký tự đầu |
| `Procedure.code.coding.code` | code | ⚪ | `MA_PTTT_QT` | B1(30) | Chuỗi(125) | ICD-9CM; Split ";" |
| `Observation` (sinh tồn) | — | ❌ | — | — | — | **THIẾU** — B5.DIEN_BIEN_LS là text tự do |

### Logic lọc ca cấp cứu tử vong (cập nhật QĐ 4750)

```
Điều kiện:
  (MA_LOAI_KCB = '09' OR MA_DOITUONG_KCB = '2')   -- Cấp cứu
  AND KET_QUA_DTRI = 5                              -- Tử vong
  AND NGAY_RA IS NOT NULL                           -- Đã kết thúc

Lưu ý QĐ 4750:
  - MA_DOITUONG_KCB trong Checkin là Chuỗi(4), trong B1 là Chuỗi(3)
  - Cấp cứu (MA_DOITUONG_KCB='2') KHÔNG có Checkin → chỉ lấy dữ liệu từ Bảng 1
```

### Khoảng cách dữ liệu

| Thiếu | Tác động | Giải pháp |
|---|---|---|
| Dấu hiệu sinh tồn cuối (`Observation`) | Không phân tích lâm sàng chi tiết | B5.DIEN_BIEN_LS (text tự do) — không chuẩn hóa được |
| Thời gian cấp cứu (door-to-needle) | Không tính được | `NGAY_VAO_NOI_TRU` (QĐ 4750) giúp xấp xỉ |

---

## Báo cáo 11 — Số Hồ Sơ KCB ✅

**Resource chính:** `EpisodeOfCare`  
**Endpoint FHIR:** `GET /EpisodeOfCare?_include=EpisodeOfCare:patient&_include=EpisodeOfCare:care-manager`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `EpisodeOfCare.id` | id | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | 1 MA_LK = 1 đợt điều trị = 1 EpisodeOfCare |
| `EpisodeOfCare.identifier[0].value` | string | ✅ | `MA_HSBA` | B1(64) | Chuỗi(100) | Mã HSBA / phiếu khám ngoại trú |
| `EpisodeOfCare.status` | code | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Có → `finished`; rỗng → `active` |
| `EpisodeOfCare.type[0].coding.code` | code | ⚪ | `MA_LOAI_KCB` | B1(56) | Số(2) | Loại đợt chăm sóc |
| `EpisodeOfCare.patient` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | → `Patient/pt-{MA_BN}` |
| `EpisodeOfCare.managingOrganization` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | → `Organization/org-{MA_CSKCB}` |
| `EpisodeOfCare.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35) | Chuỗi(12) | Ngày mở hồ sơ |
| `EpisodeOfCare.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Ngày đóng hồ sơ |
| `EpisodeOfCare.diagnosis[0].condition` | Reference | ✅ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Chẩn đoán chính → `Condition` |
| `EpisodeOfCare.diagnosis[0].role.code` | code | ⚪ | — | — | — | `CC` (chief complaint) |
| `EpisodeOfCare.careManager` | Reference | ⚪ | `MA_TTDV` | B1(65) | Chuỗi(10) | Mã định danh y tế người đứng đầu CSKCB |

### Metric Power BI

| Metric | Bộ lọc | Công thức |
|---|---|---|
| Tổng hồ sơ mở | Tất cả | `COUNTROWS(EpisodeOfCare)` |
| Hồ sơ nội trú | `MA_LOAI_KCB IN (3,4,6)` | `COUNTROWS(FILTER(...))` |
| Hồ sơ ngoại trú | `MA_LOAI_KCB IN (1,2,5,7,8)` | |
| Hồ sơ đang điều trị | `NGAY_RA` rỗng | `EpisodeOfCare.status = active` |

---

## Báo cáo 12 — Thống Kê Tai Nạn ⚠️

**Resource chính:** `Condition` (ICD S00–Y99) + `Encounter`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Condition.code.coding.code` | code | ✅ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | **Lọc ICD S00–Y99** xác định tai nạn |
| `Condition.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | |
| `Condition.encounter` | Reference | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | |
| `Condition.recordedDate` | dateTime | ⚪ | `NGAY_VAO` | B1(35) | Chuỗi(12) | Xấp xỉ ngày xảy ra tai nạn |
| `Encounter.extension[ma-tai-nan]` | Extension | ✅ | `MA_TAI_NAN` | B1(34) | Số(1) | Phụ lục 4 QĐ 5937: 1=TNGT; 2=TNLĐ; 3=TN sinh hoạt; 4=Bạo lực; 5=Khác |
| `Patient.gender` | code | ⚪ | `GIOI_TINH` | B1(7) | Số(1) | Phân tích giới tính nạn nhân |
| `Patient.birthDate` | date | ⚪ | `NGAY_SINH` | B1(6) | Chuỗi(12) | Tính nhóm tuổi nạn nhân |
| `Patient.address[0].state` | string | ⚪ | `MATINH_CU_TRU` | B1(13) | Chuỗi(3) | Địa bàn xảy ra |
| `Patient.address[0].district` | string | ⚪ | `MAHUYEN_CU_TRU` | B1(14) 📝 | Chuỗi(3) | **QĐ 4750:** Cập nhật mã mới khi gộp đơn vị HC |
| `Encounter.hospitalization.admitSource` | CodeableConcept | ⚪ | `MA_NOI_DI` | B1(32) | Chuỗi(5) | Có → chuyển từ BV khác |
| `Condition.bodySite` | CodeableConcept | ❌ | — | — | — | **THIẾU** — suy luận từ mã ICD S/T theo vùng cơ thể |
| `Condition.severity` | CodeableConcept | ❌ | — | — | — | **THIẾU** — suy luận từ `KET_QUA_DTRI` |
| `Condition.onsetDateTime` | dateTime | ❌ | — | — | — | **THIẾU** — dùng NGAY_VAO làm xấp xỉ |

---

## Báo cáo 13 — Thống Kê theo Tuổi ✅

**Resource chính:** `Patient` + `Encounter`  
**Endpoint FHIR:** `GET /Patient?_include=Patient:general-practitioner`

### Mapping trường dữ liệu — `Patient`

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Patient.id` | id | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | `pt-{MA_BN}` |
| `Patient.identifier[0].system` | uri | ✅ | — | — | — | `https://moh.gov.vn/pid` |
| `Patient.identifier[0].value` | string | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | Mã nội bộ CSKCB |
| `Patient.identifier[1].system` | uri | ✅ | — | — | — | `https://moh.gov.vn/cccd` |
| `Patient.identifier[1].value` | string | ✅ | `SO_CCCD` | B1(5), Checkin(5) 🔄 | **Chuỗi(15)** | **QĐ 4750 đổi Số→Chuỗi** — giữ số 0 đầu |
| `Patient.name[0].text` | string | ✅ | `HO_TEN` | B1(4), Checkin(4) | Chuỗi(255) | |
| `Patient.gender` | code | ✅ | `GIOI_TINH` | B1(7), Checkin(7) | Số(1) | 1→`male`; 2→`female`; 3→`unknown` |
| `Patient.birthDate` | date | ✅ | `NGAY_SINH` | B1(6), Checkin(6) | Chuỗi(12) | 8 ký tự đầu yyyymmdd; `0000`=không xác định |
| `Patient.address[0].text` | string | ⚪ | `DIA_CHI` | B1(12) 🔄 | **Chuỗi(1024)** | **QĐ 4750 đổi Số→Chuỗi** |
| `Patient.address[0].state` | string | ⚪ | `MATINH_CU_TRU` | B1(13) | Chuỗi(3) | |
| `Patient.address[0].district` | string | ⚪ | `MAHUYEN_CU_TRU` | B1(14) 📝 | Chuỗi(3) | **QĐ 4750:** Bổ sung dùng mã mới khi gộp đơn vị HC |
| `Patient.address[0].postalCode` | string | ⚪ | `MAXA_CU_TRU` | B1(15) 🔄 | **Chuỗi(3)** | **QĐ 4750 giảm Size 5→3** |
| `Patient.telecom[0].value` | string | ⚪ | `DIEN_THOAI` | B1(16) 🔄 | **Chuỗi(15)** | **QĐ 4750 đổi Số→Chuỗi** |
| `Patient.extension[blood-type]` | Extension | ⚪ | `NHOM_MAU` 🆕 | B1(8) | **Chuỗi(5)** | **QĐ 4750 TRƯỜNG MỚI** — A/B/AB/O kèm Rh+/- |
| `Patient.extension[nationality]` | Extension | ⚪ | `MA_QUOCTICH` | B1(9) 🔄 | **Chuỗi(3)** | **QĐ 4750 đổi Số→Chuỗi** |
| `Patient.extension[ethnicity]` | Extension | ⚪ | `MA_DANTOC` | B1(10) 🔄 | **Chuỗi(2)** | **QĐ 4750 đổi Số→Chuỗi** |
| `Patient.extension[occupation]` | Extension | ⚪ | `MA_NGHE_NGHIEP` | B1(11) | Chuỗi(5) | QĐ 34/2020/QĐ-TTg; `00000`=không nghề |

### Nhóm tuổi và logic parse NGAY_SINH

```
NGAY_SINH (12 ký tự): yyyymmddHHMM
  birthDate = ký tự 1–8 (yyyymmdd)
  Ngoại lệ: mm=dd='00' → chỉ lưu năm (yyyy)
  Trẻ ≤ 28 ngày: ghi đủ HHmm giờ-phút

Nhóm tuổi BYT:
  < 28 ngày      → Sơ sinh      (neonatal)
  28 ngày–<1 năm → Nhũ nhi      (infant)
  1–<6 tuổi      → Trẻ nhỏ     (toddler)
  6–<15 tuổi     → Trẻ em      (child)
  15–<18 tuổi    → Vị thành niên (adolescent)
  18–59 tuổi     → Người lớn   (adult)
  ≥ 60 tuổi      → Người cao tuổi (elderly)
```

### Cải thiện từ QĐ 4750 cho báo cáo này

| Thay đổi | Tác động phân tích |
|---|---|
| `SO_CCCD` Chuỗi — giữ số 0 đầu | Không sai khi tra cứu/join CCCD bắt đầu bằng 0 |
| `NHOM_MAU` Chuỗi(5) — trường mới | Có thể thêm chiều phân tích nhóm máu trong thống kê BN |
| `MA_QUOCTICH` Chuỗi — giữ `004` | Đúng khi so sánh mã quốc tịch với bảng tra cứu |
| `MAXA_CU_TRU` size 5→3 | **Chú ý:** cần kiểm tra dữ liệu cũ 5 ký tự, cắt ngắn hoặc re-map |

---

## Báo cáo 14 — Thống Kê theo Khoa ✅

**Resource chính:** `Encounter` GROUP BY `serviceProvider` / `location`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | GROUP BY cấp BV |
| `Encounter.location[0].location` | Reference | ✅ | `MA_KHOA` | B1(57) | Chuỗi(50) | GROUP BY cấp Khoa; Split ";" → nhiều Location |
| `Encounter.class.code` | code | ✅ | `MA_LOAI_KCB` | B1(56) | Số(2) | IMP/AMB/SS/EMER |
| `Encounter.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35) | Chuỗi(12) | |
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | |
| `Encounter.length.value` | decimal | ⚪ | `SO_NGAY_DTRI` | B1(39) | Số(3) | Tổng ngày điều trị theo khoa |
| `Encounter.diagnosis[0].condition` | Reference | ⚪ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Top bệnh trong khoa |
| `Encounter.participant[0].individual` | Reference | ⚪ | `MA_BAC_SI` | B2(32), B3(33) | Chuỗi(255) | Nhân sự khoa; split ";" |
| `Claim.total.value` | decimal | ⚪ | `T_TONGCHI_BV` | B1(47) | Số(15) | Chi phí theo khoa |
| `Organization.name` | string | ✅ | ❌ | — | — | **THIẾU** — tên khoa từ DMDC |

### Xử lý nhiều khoa trong một đợt điều trị

```
MA_KHOA = "K01;K02;K03" (phân cách ";")

→ Encounter.location[] = [
    { location: "Location/loc-K01", period: {start: NGAY_VAO, end: ?} },
    { location: "Location/loc-K02", period: {start: ?, end: ?} },
    { location: "Location/loc-K03", period: {start: ?, end: NGAY_RA} }
  ]

Lưu ý: QĐ 130+4750 không lưu ngày chuyển khoa riêng lẻ.
Phân bổ thời gian: Dùng B5.THOI_DIEM_DBLS để ước tính
                   hoặc chia đều số ngày.
```

---

## Báo cáo 15 — Lượt Sử Dụng DVKT ⚠️

**Resource chính:** `ServiceRequest` + `Procedure` + `DiagnosticReport`  
**Endpoint FHIR:** `GET /ServiceRequest?_include=ServiceRequest:subject&_include=ServiceRequest:performer`

### Mapping trường — `ServiceRequest` (từ Bảng 3)

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `ServiceRequest.id` | id | ✅ | `MA_LK`+`STT` | B3(1,2) | Composite | `sr-{MA_LK}-{STT}` |
| `ServiceRequest.status` | code | ✅ | `NGAY_KQ` | B3(37) | Chuỗi(12) | Có → `completed`; rỗng → `active` |
| `ServiceRequest.intent` | code | ✅ | — | — | — | Cố định `order` |
| `ServiceRequest.code.coding.code` | code | ✅ | `MA_DICH_VU` | B3(3), Checkin(19) 📝 | Chuỗi(50) | **QĐ 4750:** Checkin chỉ ghi khi chi phí đầu tiên là DVKT/tiền khám |
| `ServiceRequest.code.text` | string | ✅ | `TEN_DICH_VU` | B3(9), Checkin(20) 📝 | Chuỗi(1024) | Tên tương ứng |
| `ServiceRequest.category` | CodeableConcept | ⚠️ | ⚠️ Suy luận | — | — | Suy luận từ tiền tố mã DVKT (xem bảng bên dưới) |
| `ServiceRequest.subject` | Reference | ✅ | `MA_BN` | B1(3) qua JOIN | Chuỗi(100) | JOIN B3 ← B1 qua MA_LK |
| `ServiceRequest.encounter` | Reference | ✅ | `MA_LK` | B3(1) | Chuỗi(100) | → `Encounter/{MA_LK}` |
| `ServiceRequest.authoredOn` | dateTime | ✅ | `NGAY_YL` | B3(35) | Chuỗi(12) | |
| `ServiceRequest.requester` | Reference | ⚪ | `MA_BAC_SI` | B3(33) | Chuỗi(255) | Split ";" → lấy mã đầu tiên |
| `ServiceRequest.performer[0]` | Reference | ⚪ | `MA_KHOA` | B3(31) | Chuỗi(20) | → `Organization/org-khoa-{MA_KHOA}` |
| `ServiceRequest.quantity.value` | decimal | ⚪ | `SO_LUONG` | B3(13) | Số(10) | 3 chữ số thập phân |
| `ServiceRequest.priority` | code | ❌ | — | — | — | **THIẾU** — không có trong QĐ 130+4750; mặc định `routine` |

### Mapping trường — `ServiceRequest` với VTYT mới từ QĐ 4750

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `ServiceRequest.code.coding.code` | code | `MA_VAT_TU` 🆕 | Checkin(23) | **Chuỗi(255)** | **QĐ 4750 TRƯỜNG MỚI** — ghi khi chi phí đầu tiên là VTYT |
| `ServiceRequest.code.text` | string | `TEN_VAT_TU` 🆕 | Checkin(24) | **Chuỗi(1024)** | **QĐ 4750 TRƯỜNG MỚI** — tên VTYT |
| `Device.identifier[0].value` | string | `MA_VAT_TU` | B3(5) | Chuỗi(255) | Mã VTYT chi tiết đến kích thước (từ Cổng BHXH, QĐ 5086/QĐ-BYT) |
| `Device.deviceName[0].name` | string | `TEN_VAT_TU` | B3(8) | Chuỗi(1024) | Tên thương mại VTYT |
| `Device.identifier[model].value` | string | `MA_HIEU_SP` | B3(43) | Chuỗi(255) | Model/Serial/IMEI — bắt buộc khi có |
| `Device.extension[tai-su-dung]` | Extension | `TAI_SU_DUNG` | B3(44) | Số(1) | `1`=tái sử dụng |

### Mapping trường — `Procedure` (từ Bảng 3)

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `Procedure.code.coding.code` (DVKT) | code | `MA_DICH_VU` | B3(3) | Chuỗi(50) | |
| `Procedure.code.coding.code` (ICD-9) | code | `MA_PTTT_QT` | B3(4) | Chuỗi(255) | Split ";"; ICD-9 CM |
| `Procedure.performedDateTime` | dateTime | `NGAY_TH_YL` | B3(36) | Chuỗi(12) | Thời điểm thực hiện |
| `Procedure.performer[0].actor` | Reference | `NGUOI_THUC_HIEN` | B3(34) | Chuỗi(255) | Mã nhân viên y tế; split ";" |
| `Procedure.extension[pp-vo-cam]` | Extension | `PP_VO_CAM` | B3(40) | Số(1) | 1=Mê; 2=Tê; 3=Châm tê; 4=Khác |
| `Procedure.bodySite.coding.code` | code | `VI_TRI_TH_DVKT` | B3(41) | Số(3) | Vị trí cơ thể (khi BYT ban hành danh mục) |
| `Procedure.note[0].text` | string | `DIEN_BIEN_LS` | B5(3) qua JOIN | Chuỗi(n) | Mô tả thủ thuật (PHAU_THUAT B5(6)) |

### Mapping trường — `DiagnosticReport` + `Observation` (từ Bảng 4)

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `DiagnosticReport.code.coding.code` | code | `MA_DICH_VU` | B4(3) | Chuỗi(15) | Phụ lục 1 QĐ 7603/QĐ-BYT |
| `DiagnosticReport.issued` | instant | `NGAY_KQ` | B4(10) | Chuỗi(12) | ≤30 ngày từ ra viện |
| `DiagnosticReport.resultsInterpreter` | Reference | `MA_BS_DOC_KQ` | B4(11) | Chuỗi(255) | Người đọc/duyệt kết quả |
| `DiagnosticReport.conclusion` | string | `KET_LUAN` | B4(9) | Chuỗi(n) | |
| `Observation.code.coding.code` | code | `MA_CHI_SO` | B4(4) | Chuỗi(50) | Phụ lục 11 QĐ 7603/QĐ-BYT |
| `Observation.code.text` | string | `TEN_CHI_SO` | B4(5) | Chuỗi(255) | |
| `Observation.valueString` / `valueQuantity` | string/Qty | `GIA_TRI` | B4(6) | Chuỗi(50) | Parse số+đơn vị → `valueQuantity`; còn lại → `valueString` |
| `Observation.valueQuantity.unit` | string | `DON_VI_DO` | B4(7) | Chuỗi(50) | Trống → `valueString` |

### Phân loại category DVKT

| Tiền tố mã DVKT | Category FHIR | Display |
|---|---|---|
| `09.*` | `laboratory` | Xét nghiệm |
| `10.*`–`28.*` | `imaging` | Chẩn đoán hình ảnh |
| `01.*`–`08.*` | `procedure` | Thủ thuật/Phẫu thuật |
| `TG.*` | `billing` | Tiền giường |
| `01.010.*` | `billing` | Tiền khám |

---

## Báo cáo 16 — Ca Mắc theo ICD ✅

**Resource chính:** `Condition`  
**Endpoint FHIR:** `GET /Condition?_include=Condition:subject&_include=Condition:encounter`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Condition.id` | id | ✅ | `MA_LK`+`MA_BENH_CHINH` | B1(1,27) | Composite | `cond-{MA_LK}-main` |
| `Condition.clinicalStatus.code` | code | ✅ | `KET_QUA_DTRI` | B1(41) | Số(1) | 1/2→`resolved`; 3/4/7→`active`; 5→`inactive`; 6→`active` |
| `Condition.verificationStatus.code` | code | ✅ | — | — | — | Mặc định `confirmed` (đã qua bác sĩ) |
| `Condition.category[0].code` | code | ✅ | — | — | — | `encounter-diagnosis` (bệnh chính) |
| `Condition.code.coding.system` | uri | ✅ | — | — | — | `http://hl7.org/fhir/sid/icd-10` |
| `Condition.code.coding.code` | code | ✅ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Mã ICD-10 bệnh chính |
| `Condition.code.text` | string | ✅ | `CHAN_DOAN_RV` | B1(26) | Chuỗi(n) | Chẩn đoán xác định đầy đủ |
| `Condition.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | |
| `Condition.encounter` | Reference | ✅ | `MA_LK` | B1(1) | Chuỗi(100) | |
| `Condition.recordedDate` | dateTime | ⚪ | `NGAY_RA` | B1(37) | Chuỗi(12) | Ngày ghi nhận chẩn đoán cuối |
| `Condition.asserter` | Reference | ⚪ | `MA_TTDV` | B1(65) | Chuỗi(10) | Người ký xác nhận |
| `Condition.note[0].text` | string | ⚪ | `CHAN_DOAN_VAO` | B1(25) | Chuỗi(n) | Chẩn đoán sơ bộ khi nhập viện |

### Mapping bệnh kèm theo (nhiều `Condition`)

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `Condition.code.coding.code` | code | `MA_BENH_KT` (split ";") | B1(28) | Chuỗi(100) | Tối đa 12 mã; mỗi mã → 1 Condition (rank≥2) |
| `Condition.category[0].code` | code | — | — | — | `problem-list-item` (phân biệt với bệnh chính) |

### Mapping bệnh YHCT

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `Condition.code.coding.system` | uri | — | — | — | `https://moh.gov.vn/yhct` |
| `Condition.code.coding.code` | code | `MA_BENH_YHCT` | B1(29) | Chuỗi(255) | Song song với ICD-10; split ";" |

---

## Báo cáo 17 — Số Đơn Thuốc ✅

**Resource chính:** `MedicationRequest` + `Medication`  
**Endpoint FHIR:** `GET /MedicationRequest?_include=MedicationRequest:medication&_include=MedicationRequest:requester`

### Mapping trường — `MedicationRequest`

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `MedicationRequest.id` | id | ✅ | `MA_LK`+`STT` | B2(1,2) | Composite | `mr-{MA_LK}-{STT}` |
| `MedicationRequest.status` | code | ✅ | context | B2+B1 | — | Đợt kết thúc → `completed`; đang → `active` |
| `MedicationRequest.intent` | code | ✅ | — | — | — | Cố định `order` |
| `MedicationRequest.medicationCodeableConcept.code` | code | ✅ | `MA_THUOC` | B2(3), Checkin(21) 🆕 | Chuỗi(255) | **QĐ 4750:** Checkin có `MA_THUOC` khi chi phí đầu tiên là thuốc |
| `MedicationRequest.medicationCodeableConcept.text` | string | ✅ | `TEN_THUOC` | B2(7), Checkin(22) 🆕 | Chuỗi(1024) | **QĐ 4750:** Checkin có `TEN_THUOC` tương ứng |
| `MedicationRequest.subject` | Reference | ✅ | `MA_BN` | B1 qua JOIN | Chuỗi(100) | JOIN B2 ← B1 qua MA_LK |
| `MedicationRequest.encounter` | Reference | ✅ | `MA_LK` | B2(1) | Chuỗi(100) | → `Encounter/{MA_LK}` |
| `MedicationRequest.authoredOn` | dateTime | ✅ | `NGAY_YL` | B2(34) | Chuỗi(12) | Ngày ra y lệnh; ngày nghỉ → ngày làm việc trước |
| `MedicationRequest.requester` | Reference | ⚪ | `MA_BAC_SI` | B2(32) | Chuỗi(255) | Split ";"; BS tuyến trên + nhân viên cấp thuốc |
| `MedicationRequest.dosageInstruction[0].text` | string | ⚪ | `LIEU_DUNG` | B2(12) | Chuỗi(1024) | Ngoại trú: SL/lần×lần/ngày×ngày; Nội trú: ×1ngày |
| `MedicationRequest.dosageInstruction[0].route.code` | code | ⚪ | `DUONG_DUNG` | B2(10) | Chuỗi(4) | PO/IV/IM/SC/... |
| `MedicationRequest.dosageInstruction[0].additionalInstruction[0].text` | string | ⚪ | `CACH_DUNG` | B2(13) | Chuỗi(1024) | Lời dặn trên đơn |
| `MedicationRequest.dispenseRequest.quantity.value` | decimal | ⚪ | `SO_LUONG` | B2(18) | Số(10) | 3 chữ số thập phân |
| `MedicationRequest.dispenseRequest.quantity.unit` | string | ⚪ | `DON_VI_TINH` | B2(8) | Chuỗi(50) | viên/ml/UI/... |
| `MedicationRequest.extension[so-dang-ky]` | Extension | ⚪ | `SO_DANG_KY` | B2(14) | Chuỗi(255) | Số đăng ký lưu hành |
| `MedicationRequest.extension[tt-thau]` | Extension | ⚪ | `TT_THAU` | B2(15) | Chuỗi(50) | Số QĐ;Gi;Ni;Năm; áp thầu bổ sung mã đơn vị |
| `MedicationRequest.extension[pham-vi]` | Extension | ⚪ | `PHAM_VI` | B2(16) | Số(1) | 1=trong BHYT; 2=ngoài; 3=quân đội/CA |
| `MedicationRequest.extension[nguon-ctra]` | Extension | ⚪ | `NGUON_CTRA` | B2(36) | Số(1) | 1=BHYT; 2=Dự án; 3=CT mục tiêu; 4=Khác |
| `MedicationRequest.groupIdentifier.value` | string | ⚪ | `MA_LK`+`NGAY_YL` | B2(1,34) | — | 1 đơn = tập dòng cùng MA_LK + ngày YL |

### Mapping trường — `Medication`

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `Medication.code.coding.code` | code | `MA_THUOC` | B2(3) | Chuỗi(255) | Nhiều HĐ phân cách "+" |
| `Medication.code.text` | string | `TEN_THUOC` | B2(7) | Chuỗi(1024) | |
| `Medication.form.text` | string | `DANG_BAO_CHE` | B2(11) | Chuỗi(1024) | |
| `Medication.ingredient[0].strength.numerator` | Quantity | `HAM_LUONG` | B2(9) | Chuỗi(1024) | Nhiều HĐ phân cách "+" |

### Đếm số đơn thuốc

```dax
-- 1 "đơn" = tập dòng B2 cùng MA_LK + cùng ngày NGAY_YL (yyyymmdd)
GroupKey = Concat(B2[MA_LK], "_", LEFT(B2[NGAY_YL], 8))
SoDonThuoc = DISTINCTCOUNT(FactThuoc[GroupKey])
```

---

## Báo cáo 18 — Top 20 Bệnh theo ICD ✅

**Resource chính:** `Condition` (kế thừa BC16)

### Mapping trường dữ liệu (giống BC16, bổ sung logic Top 20)

| Trường FHIR | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Ghi chú |
|---|---|---|---|---|
| `Condition.code.coding.code` | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Chiều phân tích chính |
| `Condition.encounter` → `Encounter.period.end` | `NGAY_RA` | B1(37) | Chuỗi(12) | Lọc theo kỳ báo cáo |
| `Condition.clinicalStatus` | `KET_QUA_DTRI` | B1(41) | Số(1) | Lọc chỉ `confirmed` |
| `CodeSystem.concept[].display` | ❌ | — | — | **THIẾU** — Cần tên ICD từ QĐ 4469/QĐ-BYT |
| `Encounter.serviceProvider` | `MA_CSKCB` | B1(58) | Chuỗi(5) | Breakdown theo BV |

### Logic Top 20

```dax
Top20Benh =
  TOPN(
    20,
    SUMMARIZE(
      FactCondition,
      FactCondition[MA_BENH_CHINH],
      DimICD[ten_benh],     -- JOIN từ bảng ICD ngoài
      "SoCa", COUNTROWS(FactCondition)
    ),
    [SoCa], DESC
  )
```

> **Cấp độ mã:** Top 20 theo mã 3 ký tự (nhóm) cho báo cáo tổng hợp;  
> theo mã đầy đủ (4-7 ký tự) cho báo cáo chi tiết.

---

## Báo cáo 19 — Điều Trị Nội Trú ✅

**Resource chính:** `Encounter` (class=`IMP`)  
**Endpoint FHIR:** `GET /Encounter?class=IMP&_include=Encounter:subject&_include=Encounter:diagnosis`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.class.code = IMP` | code | ✅ | `MA_LOAI_KCB` ∈ {03,04,06} | B1(56) | Số(2) | 03=nội trú; 04=ban ngày; 06=lưu TYT |
| `Encounter.period.start` | dateTime | ✅ | `NGAY_VAO` | B1(35) | Chuỗi(12) | Vào viện |
| `Encounter.location[0].period.start` | dateTime | ✅ | `NGAY_VAO_NOI_TRU` 🆕 | B1(36), Checkin(14) | **Chuỗi(12)** | **QĐ 4750 bổ sung Checkin** — vào khoa điều trị nội trú |
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | Ra viện |
| `Encounter.hospitalization.admitSource` | CodeableConcept | ⚪ | `MA_NOI_DI` + `LY_DO_VNT` | B1(32,23) | Chuỗi(5)+Chuỗi(n) | Nguồn nhập viện |
| `Encounter.hospitalization.origin` | Reference | ⚪ | `MA_NOI_DI` | B1(32) | Chuỗi(5) | BV chuyển đến |
| `Encounter.hospitalization.destination` | Reference | ⚪ | `MA_NOI_DEN` | B1(33) | Chuỗi(5) | BV chuyển đi |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ⚪ | `MA_LOAI_RV` | B1(42) | Số(1) | Xem bảng mapping BC06 |
| `Encounter.diagnosis[0].use.code` | code | ⚪ | — | — | — | `AD` (Admission Diagnosis) |
| `Encounter.diagnosis[0].condition` | Reference | ⚪ | `CHAN_DOAN_VAO` + `MA_BENH_CHINH` | B1(25,27) | Chuỗi | Chẩn đoán nhập viện → `Condition` |
| `Encounter.diagnosis[1].use.code` | code | ⚪ | — | — | — | `DD` (Discharge Diagnosis) |
| `Encounter.diagnosis[1].condition` | Reference | ⚪ | `CHAN_DOAN_RV` + `MA_BENH_CHINH` | B1(26,27) | Chuỗi | Chẩn đoán ra viện |
| `Encounter.reasonCode[0].text` | string | ⚪ | `LY_DO_VNT` | B1(23), Checkin(15) 🆕 | **Chuỗi(1024)** | **QĐ 4750 bổ sung Checkin** |
| `Encounter.reasonCode[0].coding.code` | code | ⚪ | `MA_LY_DO_VNT` 🆕 | B1(24), Checkin(16) | **Chuỗi(5)** | **QĐ 4750 bổ sung Checkin** — chờ BYT ban hành danh mục |
| `Encounter.location[1].location` | Reference | ⚪ | `MA_GIUONG` | B3(32) | Chuỗi(50) | Giường nằm; split ";" nếu nhiều giường |
| `Encounter.extension[can-nang]` | Extension | ⚪ | `CAN_NANG` | B1(60) | Chuỗi(6) | kg, 2 số thập phân |
| `Encounter.extension[can-nang-con]` | Extension | ⚪ | `CAN_NANG_CON` | B1(61) | Chuỗi(100) | gram; sinh đôi phân cách ";" |
| `Encounter.extension[pp-dieu-tri]` | Extension | ⚪ | `PP_DIEU_TRI` | B1(40) | Chuỗi(n) | Phương pháp điều trị (TT 18/2022) |
| `DocumentReference` (giấy ra viện) | — | `MA_LK` → B7 | B7 | — | Bảng 7 liên kết qua MA_LK |
| `Composition` (tóm tắt HSBA) | — | `MA_LK` → B8 | B8 | — | Chỉ khi MA_LOAI_KCB ∈ {03,04,06} |

### Điểm cải thiện từ QĐ 4750

| Trường QĐ 4750 | Bảng | Lợi ích |
|---|---|---|
| `NGAY_VAO_NOI_TRU` trong Checkin | Checkin(14) | Biết ngay thời điểm vào khoa điều trị — tính door-to-bed chính xác |
| `LY_DO_VNT` trong Checkin | Checkin(15) | Có lý do nhập viện ngay khi BN đến khoa, không phải chờ Bảng 1 |
| `MA_LY_DO_VNT` trong Checkin | Checkin(16) | Mã hóa lý do vào điều trị (khi BYT ban hành danh mục) |

---

## Báo cáo 20 — Tổng Số Ngày Điều Trị theo Ngày ✅

**Resource chính:** `Encounter` + DimDate (Power BI)

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|---|---|---|---|
| `Encounter.period.start` | dateTime | `NGAY_VAO` | B1(35) | Chuỗi(12) | Ngày bắt đầu điều trị |
| `Encounter.location[0].period.start` | dateTime | `NGAY_VAO_NOI_TRU` 🆕 | B1(36), Checkin(14) | **Chuỗi(12)** | **QĐ 4750:** Dùng cho Census nội trú chính xác hơn |
| `Encounter.period.end` | dateTime | `NGAY_RA` | B1(37) | Chuỗi(12) | Ngày kết thúc điều trị |
| `Encounter.length.value` | decimal | `SO_NGAY_DTRI` | B1(39) | Số(3) | Đã tính sẵn — dùng để SUM tổng ngày |
| `Encounter.serviceProvider` | Reference | `MA_CSKCB` | B1(58) | Chuỗi(5) | Breakdown theo BV |
| `Encounter.location[].location` | Reference | `MA_KHOA` | B1(57) | Chuỗi(50) | Breakdown theo khoa |
| `Encounter.class` | Coding | `MA_LOAI_KCB` | B1(56) | Số(2) | Filter loại hình KCB |

### Công thức Census theo ngày (cải thiện QĐ 4750)

```dax
-- Dùng NGAY_VAO_NOI_TRU thay NGAY_VAO cho nội trú → Census chính xác hơn
Census_NoiTru(D) =
  COUNTROWS(FILTER(FactEncounter,
    FactEncounter[MA_LOAI_KCB] IN {3,4,6}
    && FactEncounter[NGAY_VAO_NOI_TRU] <= D
    && (ISBLANK(FactEncounter[NGAY_RA]) || FactEncounter[NGAY_RA] >= D)
  ))

TongNgay_TheoThang =
  SUMX(
    DATESBETWEEN(DimDate[Date], [ThangBatDau], [ThangKetThuc]),
    [Census_NoiTru]
  )
```

---

## Báo cáo 21 — Thống Kê Chi Phí theo Ngày ✅

**Resource chính:** `ChargeItem` + `Claim`  
**Endpoint FHIR:** `GET /ChargeItem?_include=ChargeItem:subject&_include=ChargeItem:performing-organization`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `ChargeItem.id` | id | ✅ | `MA_LK`+`STT` | B2/B3(1,2) | Composite | `ci-{MA_LK}-{STT}` |
| `ChargeItem.status` | code | ✅ | — | — | — | Mặc định `billed` khi có NGAY_TTOAN |
| `ChargeItem.code.coding.code` | code | ✅ | `MA_DICH_VU` / `MA_THUOC` / `MA_VAT_TU` | B3(3), B2(3) | Chuỗi(50)/Chuỗi(255) | Theo loại chi phí |
| `ChargeItem.subject` | Reference | ✅ | `MA_BN` | B1 qua JOIN | Chuỗi(100) | |
| `ChargeItem.context` | Reference | ✅ | `MA_LK` | B2/B3(1) | Chuỗi(100) | → `Encounter/{MA_LK}` |
| `ChargeItem.occurrenceDateTime` | dateTime | ✅ | `NGAY_YL` | B2(34), B3(35) | Chuỗi(12) | **Ngày phát sinh chi phí** — trục thời gian |
| `ChargeItem.performingOrganization` | Reference | ⚪ | `MA_KHOA` | B2(31), B3(31) | Chuỗi(15/20) | Khoa phát sinh phí |
| `ChargeItem.quantity.value` | decimal | ⚪ | `SO_LUONG` | B2(18), B3(13) | Số(10) | |
| `ChargeItem.priceOverride.value` | decimal | ⚪ | `DON_GIA` / `DON_GIA_BV` | B2(19), B3(14) | Số(15) | 3 chữ số thập phân |
| `ChargeItem.totalPriceComponent` | Money | ⚪ | `THANH_TIEN_BV` | B2(20), B3(19) | Số(15) | = SO_LUONG × DON_GIA |
| `Claim.created` | dateTime | ✅ | `NGAY_TTOAN` | B1(44) | Chuỗi(12) | Ngày thanh toán (có thể sau ra viện) |
| `Coverage.costToBeneficiary` | Money | ⚪ | `MUC_HUONG` | B2(27), B3(22) | Số(3) | % hưởng BHYT theo ngày |

### Phân tầng chi phí theo ngày

```dax
-- Chi phí theo ngày Y lệnh (khi phát sinh)
ChiPhiTheoNgayYL =
  SUMX(
    FILTER(FactThuoc, DATE(FactThuoc[NGAY_YL]) = [NgayBaoCao]),
    FactThuoc[THANH_TIEN_BV]
  )
  + SUMX(
    FILTER(FactDVKT, DATE(FactDVKT[NGAY_YL]) = [NgayBaoCao]),
    FactDVKT[THANH_TIEN_BV]
  )

-- Chi phí theo ngày thanh toán
ChiPhiTheoNgayTT =
  SUMX(
    FILTER(FactEncounter, DATE(FactEncounter[NGAY_TTOAN]) = [NgayBaoCao]),
    FactEncounter[T_TONGCHI_BV]
  )
```

---

## Báo cáo 22 — Điều Trị Nội Trú theo Ngày ✅

**Resource chính:** `Encounter` (class=`IMP`) theo trục thời gian

### Mapping trường dữ liệu — 3 metric chính

| Metric | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Công thức |
|---|---|---|---|---|
| **Nhập viện (ngày D)** | `NGAY_VAO_NOI_TRU` 🆕 | B1(36), Checkin(14) | **Chuỗi(12)** | `COUNT WHERE DATE(NGAY_VAO_NOI_TRU) = D AND MA_LOAI_KCB ∈ {03,04,06}` |
| **Ra viện (ngày D)** | `NGAY_RA` | B1(37) | Chuỗi(12) | `COUNT WHERE DATE(NGAY_RA) = D AND MA_LOAI_KCB ∈ {03,04,06}` |
| **Census (ngày D)** | `NGAY_VAO_NOI_TRU` + `NGAY_RA` | B1(36,37) | Chuỗi(12) | `COUNT WHERE NGAY_VAO_NOI_TRU ≤ D AND (NGAY_RA IS NULL OR NGAY_RA ≥ D)` |

### Mapping trường bổ sung

| Trường FHIR | Kiểu FHIR | Trường XML | Bảng XML | Kiểu XML | Ghi chú |
|---|---|---|---|---|---|
| `Encounter.hospitalization.admitSource` | CodeableConcept | `MA_NOI_DI` + `LY_DO_VNT` | B1(32,23) | Chuỗi | Phân tích nguồn nhập viện hàng ngày |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | `MA_LOAI_RV` | B1(42) | Số(1) | Phân loại ra viện hàng ngày |
| `Encounter.serviceProvider` | Reference | `MA_CSKCB` | B1(58) | Chuỗi(5) | Breakdown theo BV |
| `Encounter.location[].location` | Reference | `MA_KHOA` | B1(57) | Chuỗi(50) | Breakdown theo khoa |
| `Encounter.diagnosis[].condition` | Reference | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Bệnh liên quan lượt nhập/ra hàng ngày |

### Cải thiện từ QĐ 4750

> Trước QĐ 4750: Chỉ có `NGAY_VAO_NOI_TRU` ở Bảng 1 — không biết sớm.  
> Sau QĐ 4750: `NGAY_VAO_NOI_TRU` **có trong Checkin** → Census realtime ngay khi BN vào khoa,  
> không phải chờ upload Bảng 1 (thường sau khi ra viện).

### Công thức Power BI

```dax
NhapVien(D)  = COUNTROWS(FILTER(FactEncounter,
               DATE(FactEncounter[NGAY_VAO_NOI_TRU]) = D
               && FactEncounter[MA_LOAI_KCB] IN {3,4,6}))

RaVien(D)    = COUNTROWS(FILTER(FactEncounter,
               DATE(FactEncounter[NGAY_RA]) = D
               && FactEncounter[MA_LOAI_KCB] IN {3,4,6}))

Census(D)    = COUNTROWS(FILTER(FactEncounter,
               FactEncounter[MA_LOAI_KCB] IN {3,4,6}
               && FactEncounter[NGAY_VAO_NOI_TRU] <= D
               && (ISBLANK(FactEncounter[NGAY_RA]) || FactEncounter[NGAY_RA] >= D)))
```

---

## Báo cáo 23 — Hồ Sơ KCB theo Ngày Ra Viện ✅

**Resource chính:** `Encounter` + `EpisodeOfCare`  
**Endpoint FHIR:** `GET /Encounter?status=finished&_include=Encounter:subject&_include=Encounter:diagnosis`

### Mapping trường dữ liệu

| Trường FHIR | Kiểu FHIR | Bắt buộc | Trường XML | Bảng XML | Kiểu XML (QĐ 4750) | Chuyển đổi / Ghi chú |
|---|---|:---:|---|---|---|---|
| `Encounter.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | **Chiều GROUP BY chính** — ngày ra viện |
| `Encounter.status = finished` | code | ✅ | `NGAY_RA` có giá trị | B1(37) | Chuỗi(12) | Filter hồ sơ đã kết thúc |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ⚪ | `MA_LOAI_RV` | B1(42) | Số(1) | Xem bảng mapping BC06 |
| `Encounter.class` | Coding | ⚪ | `MA_LOAI_KCB` | B1(56) | Số(2) | IMP/AMB/EMER |
| `Encounter.diagnosis[{rank=1}].condition` | Reference | ⚪ | `MA_BENH_CHINH` | B1(27) | Chuỗi(7) | Chẩn đoán chính ra viện → `Condition` |
| `Encounter.subject` | Reference | ✅ | `MA_BN` | B1(3) | Chuỗi(100) | → `Patient` |
| `Encounter.serviceProvider` | Reference | ✅ | `MA_CSKCB` | B1(58) | Chuỗi(5) | Breakdown theo BV |
| `EpisodeOfCare.status = finished` | code | ✅ | `NGAY_RA` có giá trị | B1(37) | — | Hồ sơ đã đóng |
| `EpisodeOfCare.period.end` | dateTime | ✅ | `NGAY_RA` | B1(37) | Chuỗi(12) | |
| `Claim.created` | dateTime | ⚪ | `NGAY_TTOAN` | B1(44) | Chuỗi(12) | Ngày thanh toán khi ra viện |
| `Claim.billablePeriod` | Period | ⚪ | `NAM_QT` + `THANG_QT` | B1(54,55) | Số(4,2) | Kỳ đề nghị BHXH thanh toán |
| `Encounter.extension[ngay-tai-kham]` | Extension | ⚪ | `NGAY_TAI_KHAM` | B1(63) | Chuỗi(50) | yyyymmdd; nhiều ngày split ";" |
| `DocumentReference` (giấy ra viện) | — | `MA_LK` → B7 | B7 | — | Liên kết qua MA_LK |
| `Composition` (tóm tắt HSBA) | — | `MA_LK` → B8 | B8 | — | MA_LOAI_KCB ∈ {03,04,06} |

### Công thức Power BI

```dax
HoSoRaVienTheoNgay =
  SUMMARIZE(
    FILTER(FactEncounter, NOT(ISBLANK(FactEncounter[NGAY_RA]))),
    DATE(FactEncounter[NGAY_RA]),
    FactEncounter[MA_LOAI_KCB],
    FactEncounter[MA_LOAI_RV],
    "SoHoSo", COUNTROWS(FactEncounter),
    "TongChiPhi", SUM(FactEncounter[T_TONGCHI_BV]),
    "BHXH_TT", SUM(FactEncounter[T_BHTT])
  )
```

---

## Phụ lục A — Tóm tắt tác động QĐ 4750 theo từng báo cáo

| BC | Tên | Trường QĐ 4750 tác động | Mức độ ảnh hưởng |
|:---:|---|---|---|
| 01 | Danh mục BV | Không | — |
| 02 | Danh mục Khoa | Không | — |
| 03 | Danh mục ICD | Không | — |
| 04 | Danh mục Nhà thuốc | Không | — |
| 05 | Số Giường | Không | — |
| 06 | Tổng Ngày ĐT | `NGAY_VAO_NOI_TRU` Checkin | ⚠️ Cần parse Checkin mới |
| 07 | Chi Phí | Không | — |
| 08 | Lượt BN Vào Ra | `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT` Checkin; `MA_DOITUONG_KCB` Chuỗi(4) | 🔄 Nhiều trường mới từ Checkin |
| 09 | BN theo Loại Hình | `MA_DOITUONG_KCB` Chuỗi(4) Checkin; `MA_LOAI_KCB` Chuỗi(2) Checkin | 🔄 Đổi kiểu cần cập nhật logic so sánh |
| 10 | Cấp Cứu Tử Vong | `MA_DOITUONG_KCB`=`2` Chuỗi Checkin xác định cấp cứu | 🔄 Logic lọc chính xác hơn |
| 11 | Số Hồ Sơ | Không | — |
| 12 | Tai Nạn | `MAHUYEN_CU_TRU` bổ sung; `MAXA_CU_TRU` size 5→3 | ⚠️ Kiểm tra dữ liệu cũ |
| 13 | Theo Tuổi | `SO_CCCD` Chuỗi; `NHOM_MAU` mới; `MA_QUOCTICH`/`MA_DANTOC` Chuỗi; `DIA_CHI` Chuỗi; `DIEN_THOAI` Chuỗi; `MAXA_CU_TRU` size 5→3 | 🔄 Nhiều đổi kiểu |
| 14 | Theo Khoa | Không | — |
| 15 | DVKT | `MA_VAT_TU`/`TEN_VAT_TU` mới Checkin; `MA_DICH_VU`/`MA_THUOC` diễn giải mới Checkin | 🆕 VTYT nhận diện sớm từ Checkin |
| 16 | Ca Mắc ICD | Không | — |
| 17 | Đơn Thuốc | `MA_THUOC`/`TEN_THUOC` mới Checkin | 🆕 Thuốc nhận diện sớm từ Checkin |
| 18 | Top 20 Bệnh | Không | — |
| 19 | Nội Trú | `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT` Checkin | 🆕 Dữ liệu nhập viện sớm hơn |
| 20 | Ngày ĐT theo Ngày | `NGAY_VAO_NOI_TRU` Checkin cải thiện Census | 🔄 Census chính xác hơn |
| 21 | Chi Phí theo Ngày | Không | — |
| 22 | Nội Trú theo Ngày | `NGAY_VAO_NOI_TRU` Checkin → Census realtime | 🔄 Census realtime |
| 23 | Hồ Sơ theo Ngày Ra | Không | — |

---

## Phụ lục B — Ma trận Trường XML × Báo cáo sử dụng

| Trường XML (Nguồn QĐ) | Bảng | Kiểu sau QĐ 4750 | BC sử dụng |
|---|---|---|---|
| `MA_LK` | Tất cả | Chuỗi(100) | 06–23 |
| `MA_BN` | B1, Checkin | Chuỗi(100) | 06–23 |
| `HO_TEN` | B1, Checkin | Chuỗi(255) | 08, 13 |
| `SO_CCCD` 🔄 | B1, Checkin | **Chuỗi(15)** | 13 |
| `NGAY_SINH` | B1, Checkin | Chuỗi(12) | 10, 13 |
| `GIOI_TINH` | B1, Checkin | Số(1) | 10, 12, 13 |
| `NHOM_MAU` 🆕 | B1 | **Chuỗi(5)** | 13 |
| `MA_QUOCTICH` 🔄 | B1 | **Chuỗi(3)** | 13 |
| `MA_DANTOC` 🔄 | B1 | **Chuỗi(2)** | 13 |
| `MA_NGHE_NGHIEP` | B1 | Chuỗi(5) | 13 |
| `DIA_CHI` 🔄 | B1 | **Chuỗi(1024)** | 12, 13 |
| `MATINH_CU_TRU` | B1 | Chuỗi(3) | 12, 13 |
| `MAHUYEN_CU_TRU` 📝 | B1 | Chuỗi(3) | 12, 13 |
| `MAXA_CU_TRU` 🔄 | B1 | **Chuỗi(3)** | 12, 13 |
| `DIEN_THOAI` 🔄 | B1 | **Chuỗi(15)** | 13 |
| `MA_THE_BHYT` | B1, Checkin | Chuỗi(n) | 07, 09 |
| `MA_DKBD` | B1 | Chuỗi(n) | 07 |
| `GT_THE_TU` | B1 | Chuỗi(n) | 07 |
| `GT_THE_DEN` | B1 | Chuỗi(n) | 07 |
| `MA_DOITUONG_KCB` 🔄 | B1 Chuỗi(3), Checkin **Chuỗi(4)** | — | 09, 10 |
| `NGAY_VAO` | B1, Checkin | Chuỗi(12) | 06, 08, 11, 19–23 |
| `NGAY_VAO_NOI_TRU` 🆕 | B1, **Checkin** | **Chuỗi(12)** | 08, 19, 20, 22 |
| `LY_DO_VNT` 🆕 | B1, **Checkin** | **Chuỗi(1024)** | 08, 10, 19 |
| `MA_LY_DO_VNT` 🆕 | B1, **Checkin** | **Chuỗi(5)** | 08, 19 |
| `MA_LOAI_KCB` 🔄 | B1 Số(2), **Checkin Chuỗi(2)** | — | 06, 08, 09, 11, 19–23 |
| `NGAY_RA` | B1 | Chuỗi(12) | 06, 08, 10, 11, 16, 18, 20–23 |
| `NGAY_TTOAN` | B1 | Chuỗi(12) | 07, 21, 23 |
| `MA_BENH_CHINH` | B1 | Chuỗi(7) | 10, 12, 14, 16, 18, 19, 23 |
| `MA_BENH_KT` | B1 | Chuỗi(100) | 10, 16 |
| `MA_TAI_NAN` | B1 | Số(1) | 12 |
| `MA_LOAI_RV` | B1 | Số(1) | 06, 08, 10, 22, 23 |
| `KET_QUA_DTRI` | B1 | Số(1) | 06, 10, 16 |
| `SO_NGAY_DTRI` | B1 | Số(3) | 06, 14, 20 |
| `MA_CSKCB` | B1, Checkin | Chuỗi(5) | 01, 06–11, 13–23 |
| `MA_KHOA` | B1, B2, B3 | Chuỗi(50) | 02, 05, 14, 15, 21 |
| `T_THUOC` | B1 | Số(15) | 07 |
| `T_VTYT` | B1 | Số(15) | 07 |
| `T_TONGCHI_BV` | B1 | Số(15) | 07, 14, 21, 23 |
| `T_TONGCHI_BH` | B1 | Số(15) | 07 |
| `T_BNTT` | B1 | Số(15) | 07 |
| `T_BNCCT` | B1 | Số(15) | 07 |
| `T_BHTT` | B1 | Số(15) | 07, 23 |
| `MA_THUOC` | B2, **Checkin** 🆕 | Chuỗi(255) | 17 |
| `TEN_THUOC` | B2, **Checkin** 🆕 | Chuỗi(1024) | 17 |
| `MA_DICH_VU` | B3, Checkin 📝 | Chuỗi(50) | 06, 07, 15, 21 |
| `TEN_DICH_VU` | B3, Checkin 📝 | Chuỗi(1024) | 15 |
| `MA_VAT_TU` | B3, **Checkin** 🆕 | Chuỗi(255) | 15 |
| `TEN_VAT_TU` | B3, **Checkin** 🆕 | Chuỗi(1024) | 15 |
| `THANH_TIEN_BV` | B2, B3 | Số(15) | 07, 21 |
| `NGAY_YL` | B2, B3, Checkin | Chuỗi(12) | 15, 21 |
| `MA_DICH_VU` (CLS) | B4 | Chuỗi(15) | 15 |
| `GIA_TRI` | B4 | Chuỗi(50) | 15 |
| `GIUONG` / `MA_GIUONG` | B3 | Chuỗi(50) | 02, 05, 19 |

---

## Phụ lục C — Quy tắc chuyển đổi kỹ thuật (cập nhật QĐ 4750)

### C1. Kiểu dữ liệu phải xử lý khác sau QĐ 4750

| Trường | Vấn đề kỹ thuật | Giải pháp |
|---|---|---|
| `SO_CCCD` — đổi Số→Chuỗi | Dữ liệu cũ (Số) có thể mất số 0 đầu | Lưu VARCHAR(15); khi nhận dữ liệu cũ: `LPAD(val, 12, '0')` |
| `MA_LOAI_KCB` Checkin — đổi Số→Chuỗi | `01` ≠ `1` khi so sánh | Chuẩn hóa: `LPAD(MA_LOAI_KCB, 2, '0')` trước khi JOIN |
| `MA_DOITUONG_KCB` Checkin — size 1→4 | Mã cũ `1` nay thành `0001` hoặc vẫn `1`? | Cần xác nhận với BYT/BHXH cách padding |
| `MAXA_CU_TRU` — size 5→3 | Mã xã cũ 5 ký tự không khớp mã mới 3 ký tự | Build bảng lookup mã xã cũ → mới |
| `MAHUYEN_CU_TRU` — bổ sung mã mới | Mã huyện cũ sau sáp nhập không còn hợp lệ | Build bảng lookup mã huyện cũ → mới |
| `DIEN_THOAI` — đổi Số→Chuỗi | SĐT đầu `0` bị mất khi lưu kiểu Số | Lưu VARCHAR(15) |

### C2. Định dạng ngày giờ (không thay đổi)

| Format QĐ | Ký tự | FHIR DateTime | Ví dụ |
|---|:---:|---|---|
| `yyyymmddHHMM` | 12 | `yyyy-MM-ddTHH:mm:ss+07:00` | `202403100830` → `2024-03-10T08:30:00+07:00` |
| `yyyymmdd` | 8 | `yyyy-MM-dd` | `20240310` → `2024-03-10` |
| `yyyy00000000` | — | `yyyy` (năm) | `00` tháng/ngày = chỉ biết năm |
| `000000000000` | — | null | Không xác định |

### C3. Mã hóa đặc biệt MA_DICH_VU / MA_THUOC / MA_VAT_TU

| Tiền tố | Ý nghĩa | FHIR Extension |
|---|---|---|
| `VM.XXXXX` | Vận chuyển máu từ CSKCB XXXXX | `extension[van-chuyen-mau]` |
| `BB.XXXXX` | Bao bì thuốc thang | `extension[bao-bi]` |
| `VC.XXXXX` | Vận chuyển BN đến CSKCB XXXXX | `extension[van-chuyen-bn]` |
| `C.XXXXX` | Thuốc chuyển từ CSKCB (thiên tai) | `extension[chuyen-thuoc]` |
| `K.XXXXX` | Thuốc ngoài giá CLS | `extension[thuoc-ngoai-gia]` |
| `M.XXXXX` | Máu từ CSKCB cung cấp XXXXX | `extension[nguon-mau]` |
| `XX.YYYY.ZZZZ.K.WWWWW` | DVKT/CLS chuyển mẫu đến CSKCB WWWWW | `extension[dvkt-chuyen]` |
| `XX.YYYY.ZZZZ_GT` | DVKT có gây tê | `Procedure.extension[vo-cam]` |
| `XX.YYYY.ZZZZ_TB` | DVKT không hoàn thành | `Procedure.status = stopped` |
| `XX.YYYY.0000` | DVKT chưa có giá | `ChargeItem.priceOverride = 0` |

### C4. Nghiệp vụ Checkin mới sau QĐ 4750

```
Quy tắc gửi Checkin:
  GỬI khi:
    → Phát sinh chi phí dịch vụ đầu tiên tại khoa điều trị
      (nội trú | nội trú ban ngày | ngoại trú)

  KHÔNG GỬI khi:
    → MA_DOITUONG_KCB = "2" (cấp cứu BHYT, Khoản 6 Điều 15 NĐ 146/2018)
    → Chỉ nhận BN/mẫu bệnh phẩm để thực hiện CLS
      (Điều 9 TT 30/2020/TT-BYT)

  MỤC ĐÍCH: Chỉ thông báo trạng thái
    → KHÔNG dùng làm căn cứ giám định / thanh toán / quyết toán BHYT

Chọn trường chi phí đầu tiên:
  Chi phí là DVKT/khám → MA_DICH_VU + TEN_DICH_VU; để trống MA_THUOC, MA_VAT_TU
  Chi phí là Thuốc     → MA_THUOC + TEN_THUOC;     để trống MA_DICH_VU, MA_VAT_TU
  Chi phí là VTYT      → MA_VAT_TU + TEN_VAT_TU;   để trống MA_DICH_VU, MA_THUOC
```

---

*Tài liệu kỹ thuật Phiên bản 3.0 — Field-Level Mapping*  
*Căn cứ pháp lý: QĐ 130/QĐ-BYT (18/01/2023) + QĐ 4750/QĐ-BYT (29/12/2023)*  
*Hiệu lực chính thức từ: **01/07/2024***  
*Chuẩn đích: HL7 FHIR R4B (4.3.0) — https://hl7.org/fhir/R4B/*
