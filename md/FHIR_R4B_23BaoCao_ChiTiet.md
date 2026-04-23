# Phân tích Chi Tiết FHIR R4B Resources — 23 Báo cáo Power BI Y Tế

> **Chuẩn:** HL7 FHIR R4B (4.3.0) | **Mục tiêu:** Tài liệu kỹ thuật đầy đủ cho triển khai Power BI

---

## Báo cáo 01 — Danh mục Bệnh viện

### Resource chính: `Organization`

**Endpoint:** `GET /Organization?type=prov&_include=Organization:partof&_include=Location:organization`

### Bảng trường dữ liệu

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Organization.id` | id | ✅ | ID định danh nội bộ FHIR | `org-bvbachmai-001` |
| `Organization.identifier` | Identifier[] | ✅ | Mã bệnh viện theo Bộ Y tế | system: `https://moh.gov.vn/org`, value: `01023` |
| `Organization.active` | boolean | ✅ | Trạng thái hoạt động | `true` |
| `Organization.type` | CodeableConcept[] | ✅ | Loại tổ chức | code: `prov`, display: `Healthcare Provider` |
| `Organization.name` | string | ✅ | Tên bệnh viện | `Bệnh viện Bạch Mai` |
| `Organization.alias` | string[] | ⚪ | Tên viết tắt/bí danh | `BVBM` |
| `Organization.telecom` | ContactPoint[] | ⚪ | SĐT, email, website | system: `phone`, value: `024-3869-3731` |
| `Organization.address` | Address[] | ⚪ | Địa chỉ | 78 Giải Phóng, Đống Đa, Hà Nội |
| `Organization.partOf` | Reference(Organization) | ⚪ | Tổ chức cha (nếu là chi nhánh) | `Organization/so-y-te-hn` |
| `Organization.contact` | BackboneElement[] | ⚪ | Người liên hệ đầu mối | name, telecom, address |
| `Organization.endpoint` | Reference(Endpoint)[] | ⚪ | URL kết nối HIS/API | `Endpoint/his-bachmai` |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích trong báo cáo |
|---|---|---|---|
| `Location` | `Location.managingOrganization` → `Organization.id` | 1:N (một BV có nhiều Location) | Địa chỉ vật lý, tòa nhà, khu vực |
| `OrganizationAffiliation` | `OrganizationAffiliation.organization` → `Organization.id` | N:M | Liên kết BV vệ tinh, chuyển viện |
| `HealthcareService` | `HealthcareService.providedBy` → `Organization.id` | 1:N | Danh sách dịch vụ y tế cung cấp |
| `PractitionerRole` | `PractitionerRole.organization` → `Organization.id` | N:1 | Nhân sự thuộc bệnh viện |
| `Endpoint` | `Organization.endpoint` → `Endpoint.id` | 1:N | Thông tin kết nối hệ thống |

---

## Báo cáo 02 — Danh mục Khoa

### Resource chính: `Organization` (type=dept) + `Location`

**Endpoint:** `GET /Organization?type=dept&_include=Organization:partof`

### Bảng trường dữ liệu — `Organization` (Khoa)

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Organization.id` | id | ✅ | ID khoa | `org-khoa-noitim-001` |
| `Organization.identifier` | Identifier[] | ✅ | Mã khoa theo BYT | value: `K001` |
| `Organization.active` | boolean | ✅ | Trạng thái hoạt động | `true` |
| `Organization.type` | CodeableConcept[] | ✅ | Loại = khoa | code: `dept` |
| `Organization.name` | string | ✅ | Tên khoa | `Khoa Nội Tim mạch` |
| `Organization.partOf` | Reference(Organization) | ✅ | Bệnh viện chủ quản | `Organization/org-bvbachmai-001` |
| `Organization.telecom` | ContactPoint[] | ⚪ | SĐT nội bộ khoa | |

### Bảng trường dữ liệu — `Location` (Phòng/Khu vực trong khoa)

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Location.id` | id | ✅ | ID phòng | `loc-phong-201` |
| `Location.status` | code | ✅ | active/suspended/inactive | `active` |
| `Location.name` | string | ✅ | Tên phòng | `Phòng 201 - Nội Tim mạch` |
| `Location.physicalType` | CodeableConcept | ✅ | Loại vật lý | code: `ro` (room) hoặc `wa` (ward) |
| `Location.managingOrganization` | Reference(Organization) | ✅ | Khoa quản lý | `Organization/org-khoa-noitim-001` |
| `Location.partOf` | Reference(Location) | ⚪ | Phòng thuộc khu/tầng | `Location/loc-tang2` |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Organization` (BV cha) | `Organization.partOf` → `Organization.id` | N:1 | Phân cấp BV→Khoa |
| `Location` | `Location.managingOrganization` → `Organization.id` | 1:N | Phòng/giường thuộc khoa |
| `PractitionerRole` | `PractitionerRole.organization` → `Organization.id` | N:1 | Nhân sự trong khoa |
| `Encounter` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Lượt khám tại khoa |
| `HealthcareService` | `HealthcareService.providedBy` → `Organization.id` | 1:N | Dịch vụ của khoa |

---

## Báo cáo 03 — Danh mục Bệnh theo ICD

### Resource chính: `CodeSystem` + `ValueSet`

**Endpoint:** `GET /CodeSystem?url=http://hl7.org/fhir/sid/icd-10`
**Expand:** `POST /ValueSet/$expand` với body chứa ValueSet ICD

### Bảng trường dữ liệu — `CodeSystem`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `CodeSystem.id` | id | ✅ | ID hệ thống mã | `icd-10-cm` |
| `CodeSystem.url` | uri | ✅ | Canonical URL định danh | `http://hl7.org/fhir/sid/icd-10` |
| `CodeSystem.version` | string | ✅ | Phiên bản | `2023` |
| `CodeSystem.name` | string | ✅ | Tên | `ICD-10` |
| `CodeSystem.status` | code | ✅ | active/draft/retired | `active` |
| `CodeSystem.content` | code | ✅ | complete/fragment/not-present | `complete` |
| `CodeSystem.concept[].code` | code | ✅ | Mã bệnh | `I21` |
| `CodeSystem.concept[].display` | string | ✅ | Tên bệnh (tiếng Anh) | `Acute myocardial infarction` |
| `CodeSystem.concept[].definition` | string | ⚪ | Mô tả định nghĩa | |
| `CodeSystem.concept[].property[]` | BackboneElement | ⚪ | Thuộc tính mở rộng (chương, nhóm) | |
| `CodeSystem.concept[].concept[]` | BackboneElement | ⚪ | Mã con (phân nhóm ICD) | I21.0, I21.1... |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `ValueSet` | `ValueSet.compose.include.system` → `CodeSystem.url` | N:1 | Tập con ICD dùng trong từng chuyên khoa |
| `ConceptMap` | `ConceptMap.group.source/target` → `CodeSystem.url` | N:N | Ánh xạ ICD-10 ↔ ICD-11 |
| `Condition` | `Condition.code.coding.system` → `CodeSystem.url` | N:1 | Chẩn đoán thực tế tham chiếu mã ICD |
| `Encounter` | `Encounter.reasonCode.coding.system` → `CodeSystem.url` | N:1 | Lý do vào viện dùng mã ICD |

---

## Báo cáo 04 — Danh mục Nhà thuốc

### Resource chính: `Organization` (type=pharm) + `Location`

**Endpoint:** `GET /Organization?type=pharm&_include=Location:organization`

### Bảng trường dữ liệu

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Organization.id` | id | ✅ | ID nhà thuốc | `org-nhathuoc-bvbm` |
| `Organization.identifier` | Identifier[] | ✅ | Số giấy phép kinh doanh dược | value: `GP-0123/BYT` |
| `Organization.type` | CodeableConcept[] | ✅ | code: `pharm` | Nhà thuốc |
| `Organization.name` | string | ✅ | Tên nhà thuốc | `Nhà thuốc BV Bạch Mai` |
| `Organization.partOf` | Reference(Organization) | ⚪ | BV/khoa dược chủ quản | `Organization/khoa-duoc-bvbm` |
| `Organization.telecom` | ContactPoint[] | ⚪ | SĐT, giờ mở cửa | |
| `Organization.address` | Address[] | ✅ | Địa chỉ nhà thuốc | |
| `Location.hoursOfOperation` | BackboneElement[] | ⚪ | Giờ mở cửa chi tiết | Mon-Fri 7:00-20:00 |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Location` | `Location.managingOrganization` → `Organization.id` | 1:1 | Vị trí vật lý của nhà thuốc |
| `MedicationDispense` | `MedicationDispense.performer.actor` → `Organization.id` | N:1 | Lịch sử cấp phát thuốc |
| `MedicationRequest` | `MedicationRequest.dispenseRequest.performer` → `Organization.id` | N:1 | Đơn thuốc gửi về nhà thuốc |
| `PractitionerRole` | `PractitionerRole.organization` → `Organization.id` | N:1 | Dược sĩ làm việc tại đây |
| `Medication` | `MedicationDispense.medication[x]` | N:1 | Danh mục thuốc tại nhà thuốc |

---

## Báo cáo 05 — Số Giường

### Resource chính: `Location` (physicalType=bd)

**Endpoint:** `GET /Location?physicalType=bd&_include=Location:partof&status=active`

### Bảng trường dữ liệu

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Location.id` | id | ✅ | ID giường | `bed-201a` |
| `Location.status` | code | ✅ | active/suspended/inactive | `active` |
| `Location.operationalStatus` | Coding | ⚪ | Trạng thái vận hành | code: `O` (Occupied), `U` (Unoccupied) |
| `Location.name` | string | ✅ | Tên/số giường | `Giường 201A` |
| `Location.alias` | string[] | ⚪ | Tên rút gọn | `201A` |
| `Location.physicalType` | CodeableConcept | ✅ | Loại vật lý = giường | code: `bd`, system: `.../location-physical-type` |
| `Location.managingOrganization` | Reference(Organization) | ✅ | Khoa quản lý giường | `Organization/khoa-noitim` |
| `Location.partOf` | Reference(Location) | ✅ | Phòng chứa giường | `Location/phong-201` |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Location` (phòng) | `Location.partOf` → `Location.id` | N:1 | Giường thuộc phòng |
| `Location` (khoa/tầng) | `Location.partOf` (nhiều cấp) | N:1 | Phân cấp địa lý |
| `Organization` | `Location.managingOrganization` → `Organization.id` | N:1 | Khoa quản lý |
| `Encounter` | `Encounter.location[].location` → `Location.id` | N:1 | Bệnh nhân đang chiếm giường |
| `Schedule` | `Schedule.actor` → `Location.id` | 1:1 | Lịch đặt giường |

### Công thức Power BI
- **Tổng giường:** `COUNTROWS(FILTER(Location, Location[status] = "active"))`
- **Giường đang sử dụng:** JOIN với `Encounter` có `status = in-progress`
- **Tỷ lệ sử dụng:** `Giường đang dùng / Tổng giường × 100%`

---

## Báo cáo 06 — Tổng Số Ngày Điều Trị

### Resource chính: `Encounter`

**Endpoint:** `GET /Encounter?class=IMP&status=finished&_include=Encounter:subject&_include=Encounter:service-provider`

### Bảng trường dữ liệu

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Encounter.id` | id | ✅ | ID lượt điều trị | `enc-20240115-001` |
| `Encounter.status` | code | ✅ | planned/in-progress/finished/... | `finished` |
| `Encounter.class` | Coding | ✅ | AMB/IMP/EMER/HH | code: `IMP` |
| `Encounter.type` | CodeableConcept[] | ⚪ | Loại điều trị chi tiết | |
| `Encounter.subject` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-nguyen-van-a` |
| `Encounter.period.start` | dateTime | ✅ | Ngày giờ vào viện | `2024-01-15T08:30:00+07:00` |
| `Encounter.period.end` | dateTime | ✅ | Ngày giờ ra viện | `2024-01-22T10:00:00+07:00` |
| `Encounter.serviceProvider` | Reference(Organization) | ✅ | Khoa/BV điều trị | `Organization/khoa-noitim` |
| `Encounter.location[].location` | Reference(Location) | ⚪ | Giường/phòng điều trị | `Location/bed-201a` |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ⚪ | Hình thức ra viện | code: `home` |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Thông tin nhân khẩu bệnh nhân |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Thống kê theo khoa/BV |
| `Location` | `Encounter.location[].location` → `Location.id` | N:N | Giường/phòng sử dụng |
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | 1:N | Chẩn đoán trong đợt điều trị |
| `EpisodeOfCare` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | N:1 | Đợt chăm sóc tổng thể |

### Công thức Power BI
```
SoNgayDieuTri = DATEDIFF(Encounter[period_start], Encounter[period_end], DAY)
TongNgayDieuTri = SUM(FactEncounter[SoNgayDieuTri])
TrungBinhNgay = AVERAGE(FactEncounter[SoNgayDieuTri])
```

---

## Báo cáo 07 — Thống Kê Chi Phí

### Resource chính: `Claim` + `ClaimResponse` + `Invoice`

**Endpoint:** `GET /Claim?_include=Claim:patient&_include=Claim:encounter&_include=Claim:insurance`

### Bảng trường dữ liệu — `Claim`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Claim.id` | id | ✅ | ID hồ sơ thanh toán | `claim-20240115-001` |
| `Claim.status` | code | ✅ | active/cancelled/draft/entered-in-error | `active` |
| `Claim.type` | CodeableConcept | ✅ | Loại claim (institutional/professional) | code: `institutional` |
| `Claim.use` | code | ✅ | claim/preauthorization/predetermination | `claim` |
| `Claim.patient` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `Claim.created` | dateTime | ✅ | Ngày tạo claim | `2024-01-22` |
| `Claim.provider` | Reference(Organization/Practitioner) | ✅ | Đơn vị lập hóa đơn | `Organization/bvbachmai` |
| `Claim.encounter` | Reference(Encounter)[] | ✅ | Lượt khám liên quan | `Encounter/enc-001` |
| `Claim.insurance[].coverage` | Reference(Coverage) | ✅ | Bảo hiểm | `Coverage/bhyt-001` |
| `Claim.insurance[].focal` | boolean | ✅ | Bảo hiểm chính | `true` |
| `Claim.total` | Money | ✅ | Tổng giá trị yêu cầu | value: `5000000`, currency: `VND` |
| `Claim.item[].sequence` | positiveInt | ✅ | Số thứ tự dòng | `1` |
| `Claim.item[].productOrService` | CodeableConcept | ✅ | Dịch vụ/thuốc | |
| `Claim.item[].quantity` | Quantity | ⚪ | Số lượng | |
| `Claim.item[].unitPrice` | Money | ⚪ | Đơn giá | |
| `Claim.item[].net` | Money | ✅ | Thành tiền | |

### Bảng trường dữ liệu — `ClaimResponse`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `ClaimResponse.request` | Reference(Claim) | ✅ | Claim gốc | `Claim/claim-001` |
| `ClaimResponse.outcome` | code | ✅ | queued/complete/error/partial | `complete` |
| `ClaimResponse.payment.amount` | Money | ✅ | Số tiền được thanh toán | value: `4500000` |
| `ClaimResponse.total[].category` | CodeableConcept | ✅ | Loại tổng (submitted/benefit) | |
| `ClaimResponse.total[].amount` | Money | ✅ | Giá trị từng loại | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Encounter` | `Claim.encounter` → `Encounter.id` | N:1 | Lượt khám phát sinh chi phí |
| `Patient` | `Claim.patient` → `Patient.id` | N:1 | Bệnh nhân chi trả |
| `Coverage` | `Claim.insurance[].coverage` → `Coverage.id` | N:1 | Thông tin BHYT |
| `ClaimResponse` | `ClaimResponse.request` → `Claim.id` | 1:1 | Kết quả xét duyệt |
| `ChargeItem` | `Invoice.lineItem.chargeItem` → `ChargeItem.id` | 1:N | Chi tiết từng khoản phí |
| `Organization` | `Claim.provider` → `Organization.id` | N:1 | Đơn vị lập hóa đơn |
| `MedicationRequest` | Qua `Claim.item` | N:N | Chi phí thuốc trong claim |
| `Procedure` | `Claim.procedure[].procedure[x]` → `Procedure.id` | N:N | Chi phí thủ thuật |

---

## Báo cáo 08 — Thống Kê Lượt Bệnh Nhân Vào Ra

### Resource chính: `Encounter`

**Endpoint:** `GET /Encounter?date=ge[start]&date=le[end]&_include=Encounter:subject`

### Bảng trường dữ liệu bổ sung (ngoài Báo cáo 06)

| Trường FHIR | Mô tả | Vai trò trong báo cáo |
|---|---|---|
| `Encounter.status` | in-progress (đang điều trị), finished (đã ra) | Phân biệt vào/đang/ra |
| `Encounter.class` | AMB/IMP/EMER | Phân loại luồng bệnh nhân |
| `Encounter.period.start` | Timestamp vào viện | Metric "Lượt vào" |
| `Encounter.period.end` | Timestamp ra viện | Metric "Lượt ra" |
| `Encounter.hospitalization.admitSource` | Nguồn nhập viện | Chuyển viện/tự đến/cấp cứu |
| `Encounter.hospitalization.dischargeDisposition` | Hình thức ra viện | Khỏi/chuyển/tử vong |
| `Encounter.reasonCode` | Lý do vào viện (ICD) | Phân tích nguyên nhân |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Thông tin bệnh nhân |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Thống kê theo đơn vị |
| `Location` | `Encounter.location[].location` → `Location.id` | N:N | Địa điểm điều trị |
| `Condition` | `Condition.encounter` → `Encounter.id` | 1:N | Bệnh lý vào/ra viện |
| `EpisodeOfCare` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | N:1 | Theo dõi đợt bệnh liên tục |

---

## Báo cáo 09 — Số Bệnh Nhân theo Loại Hình KCB

### Resource chính: `Encounter` (phân loại theo `class`)

**Endpoint:** `GET /Encounter?_include=Encounter:subject&_include=Encounter:insurance`

### Phân loại `Encounter.class`

| Code | Display | Mô tả | Ghi chú |
|---|---|---|---|
| `AMB` | Ambulatory | Ngoại trú | Khám trong ngày, không lưu đêm |
| `IMP` | Inpatient | Nội trú | Lưu trú qua đêm |
| `EMER` | Emergency | Cấp cứu | Khẩn cấp 24/7 |
| `HH` | Home Health | Chăm sóc tại nhà | Y tế cộng đồng |
| `SS` | Short Stay | Lưu ngắn ngày | Quan sát/điều trị <24h |
| `OBSENC` | Observation | Theo dõi | Chờ quyết định nhập viện |
| `PRENC` | Pre-Admission | Tiền nhập viện | Chuẩn bị phẫu thuật |

### Bảng trường dữ liệu bổ sung

| Trường FHIR | Mô tả | Ví dụ |
|---|---|---|
| `Encounter.type` | Loại hình chi tiết hơn class | Khám lần đầu, tái khám, khám chuyên khoa |
| `Encounter.serviceType` | Dịch vụ cụ thể | Nội soi, siêu âm, xét nghiệm |
| `Encounter.priority` | Độ ưu tiên | routine/urgent/asap/stat |
| `Coverage.type` | Loại bảo hiểm | BHYT/dịch vụ/miễn phí |
| `Coverage.subscriberId` | Số thẻ BHYT | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Thông tin bệnh nhân |
| `Coverage` | Qua `Encounter.account` → `Account.coverage` | N:N | Phân loại nguồn tài chính |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Đơn vị thực hiện |
| `Practitioner` | `Encounter.participant[].individual` → `Practitioner.id` | N:N | Bác sĩ tiếp nhận |

---

## Báo cáo 10 — Số Ca Cấp Cứu Tử Vong

### Resource chính: `Encounter` (class=EMER) + `Condition`

**Endpoint:** `GET /Encounter?class=EMER&_include=Encounter:diagnosis&_include=Encounter:subject`

### Bảng trường dữ liệu — Xác định ca tử vong

| Trường FHIR | Giá trị lọc | Mô tả |
|---|---|---|
| `Encounter.class` | `EMER` | Lọc chỉ lượt cấp cứu |
| `Encounter.hospitalization.dischargeDisposition.coding.code` | `exp` (expired) | Ca tử vong tại BV |
| `Encounter.hospitalization.dischargeDisposition.coding.system` | `.../discharge-disposition` | Hệ thống mã |
| `Encounter.period.end` | Ngày tử vong | Thời điểm tử vong |
| `Encounter.status` | `finished` | Lượt đã kết thúc |

### Các mã `dischargeDisposition` cần lưu ý

| Code | Mô tả |
|---|---|
| `exp` | Expired — Tử vong |
| `home` | Về nhà bình thường |
| `other-hcf` | Chuyển cơ sở khác |
| `hosp` | Chuyển bệnh viện |
| `aadvice` | Xuất viện theo yêu cầu |

### Bảng trường dữ liệu bổ sung

| Trường FHIR | Mô tả | Ví dụ |
|---|---|---|
| `Condition.code` | Mã ICD nguyên nhân tử vong | `I21` — Nhồi máu cơ tim cấp |
| `Condition.verificationStatus` | confirmed | Chẩn đoán đã xác nhận |
| `Observation.code` | Dấu hiệu sinh tồn cuối | Nhịp tim, huyết áp, SpO2 |
| `Procedure.code` | Thủ thuật cấp cứu đã làm | CPR, thở máy, sốc điện |
| `Patient.gender` | Giới tính | Phân tích theo giới |
| `Patient.birthDate` | Tuổi khi tử vong | Phân tích theo tuổi |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | 1:N | Nguyên nhân tử vong (ICD) |
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Nhân khẩu học người tử vong |
| `Procedure` | `Procedure.encounter` → `Encounter.id` | N:1 | Thủ thuật cấp cứu đã thực hiện |
| `Observation` | `Observation.encounter` → `Encounter.id` | N:1 | Chỉ số lâm sàng cuối cùng |
| `Practitioner` | `Encounter.participant[].individual` → `Practitioner.id` | N:N | Êkip cấp cứu |

---

## Báo cáo 11 — Số Hồ Sơ Khám Chữa Bệnh

### Resource chính: `EpisodeOfCare`

**Endpoint:** `GET /EpisodeOfCare?_include=EpisodeOfCare:patient&_include=EpisodeOfCare:organization`

### Bảng trường dữ liệu

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `EpisodeOfCare.id` | id | ✅ | ID hồ sơ | `eoc-2024-bachmai-001` |
| `EpisodeOfCare.status` | code | ✅ | planned/active/finished/... | `finished` |
| `EpisodeOfCare.type` | CodeableConcept[] | ⚪ | Loại đợt chăm sóc | Nội trú/Ngoại trú |
| `EpisodeOfCare.patient` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `EpisodeOfCare.managingOrganization` | Reference(Organization) | ✅ | BV/đơn vị quản lý | `Organization/bvbachmai` |
| `EpisodeOfCare.period.start` | dateTime | ✅ | Ngày mở hồ sơ | `2024-01-15` |
| `EpisodeOfCare.period.end` | dateTime | ⚪ | Ngày đóng hồ sơ | `2024-01-22` |
| `EpisodeOfCare.diagnosis[].condition` | Reference(Condition) | ⚪ | Chẩn đoán chính | `Condition/cond-001` |
| `EpisodeOfCare.diagnosis[].role` | CodeableConcept | ⚪ | Vai trò chẩn đoán | chief-complaint/CC |
| `EpisodeOfCare.careManager` | Reference(Practitioner) | ⚪ | Bác sĩ phụ trách | `Practitioner/dr-001` |
| `EpisodeOfCare.team` | Reference(CareTeam)[] | ⚪ | Đội điều trị | |
| `EpisodeOfCare.account` | Reference(Account)[] | ⚪ | Tài khoản thanh toán | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `EpisodeOfCare.patient` → `Patient.id` | N:1 | Bệnh nhân có hồ sơ |
| `Organization` | `EpisodeOfCare.managingOrganization` → `Organization.id` | N:1 | Đơn vị quản lý hồ sơ |
| `Encounter` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | 1:N (reverse) | Các lượt khám trong hồ sơ |
| `Condition` | `EpisodeOfCare.diagnosis[].condition` → `Condition.id` | N:N | Bệnh lý trong hồ sơ |
| `Practitioner` | `EpisodeOfCare.careManager` → `Practitioner.id` | N:1 | Bác sĩ quản lý |
| `DocumentReference` | `DocumentReference.context.encounter` → Encounter (trong EoC) | N:N | Tài liệu y tế |

---

## Báo cáo 12 — Thống Kê Tai Nạn

### Resource chính: `Condition` (mã ICD nhóm S, T, V-Y) + `Encounter`

**Endpoint:** `GET /Condition?code=S00-Y99&_include=Condition:encounter&_include=Condition:subject`

### Phân loại mã ICD tai nạn

| Nhóm ICD | Loại tai nạn | Ví dụ mã |
|---|---|---|
| S00–S99 | Chấn thương theo vị trí cơ thể | S72 = Gãy xương đùi |
| T00–T98 | Chấn thương nhiều vị trí, ngộ độc | T39 = Ngộ độc thuốc giảm đau |
| V01–V99 | Tai nạn giao thông | V40 = Va chạm ô tô |
| W00–W99 | Tai nạn sinh hoạt | W18 = Ngã |
| X00–X99 | Tai nạn do tác nhân bên ngoài | X10 = Bỏng |
| Y00–Y34 | Tai nạn không rõ nguyên nhân | |
| Y35–Y84 | Biến chứng chăm sóc y tế | |
| Y85–Y99 | Hoàn cảnh bổ sung | |

### Bảng trường dữ liệu bổ sung

| Trường FHIR | Mô tả | Ví dụ |
|---|---|---|
| `Condition.code` | Mã ICD tai nạn | S72.0 |
| `Condition.bodySite` | Vị trí tổn thương | Xương đùi phải |
| `Condition.severity` | Mức độ nghiêm trọng | severe/moderate/mild |
| `Condition.onsetDateTime` | Thời điểm xảy ra tai nạn | |
| `Encounter.reasonCode` | Lý do vào viện | Tai nạn giao thông |
| `Encounter.hospitalization.admitSource` | Đến từ đâu | Cấp cứu/tự đến |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Encounter` | `Condition.encounter` → `Encounter.id` | N:1 | Lượt điều trị tai nạn |
| `Patient` | `Condition.subject` → `Patient.id` | N:1 | Nạn nhân tai nạn |
| `Procedure` | `Procedure.encounter` → `Encounter.id` | N:1 | Xử lý chấn thương |
| `Observation` | `Observation.encounter` → `Encounter.id` | N:1 | Đánh giá mức độ thương tích |
| `ImagingStudy` | `ImagingStudy.encounter` → `Encounter.id` | N:1 | X-Quang, CT chấn thương |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Cơ sở tiếp nhận |

---

## Báo cáo 13 — Thống Kê theo Tuổi

### Resource chính: `Patient` + `Encounter`

**Endpoint:** `GET /Patient?_revinclude=Encounter:subject&birthdate=le[date]`

### Bảng trường dữ liệu — `Patient`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Patient.id` | id | ✅ | ID bệnh nhân | `pt-nguyen-van-a` |
| `Patient.identifier` | Identifier[] | ✅ | CCCD, số BN | system: `https://moh.gov.vn/pid` |
| `Patient.active` | boolean | ✅ | Hồ sơ còn hoạt động | `true` |
| `Patient.name` | HumanName[] | ✅ | Họ tên | family: Nguyễn, given: Văn A |
| `Patient.gender` | code | ✅ | male/female/other/unknown | `male` |
| `Patient.birthDate` | date | ✅ | Ngày sinh | `1985-03-20` |
| `Patient.address` | Address[] | ⚪ | Địa chỉ thường trú | Quận Đống Đa, Hà Nội |
| `Patient.telecom` | ContactPoint[] | ⚪ | SĐT | |
| `Patient.communication` | BackboneElement[] | ⚪ | Ngôn ngữ | vi (tiếng Việt) |

### Nhóm tuổi chuẩn Bộ Y tế Việt Nam

| Nhóm | Khoảng tuổi | Mã |
|---|---|---|
| Sơ sinh | < 28 ngày | `neonatal` |
| Nhũ nhi | 28 ngày – < 12 tháng | `infant` |
| Trẻ nhỏ | 1 – < 6 tuổi | `toddler` |
| Trẻ em | 6 – < 15 tuổi | `child` |
| Vị thành niên | 15 – < 18 tuổi | `adolescent` |
| Người lớn | 18 – 59 tuổi | `adult` |
| Người cao tuổi | ≥ 60 tuổi | `elderly` |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Encounter` | `Encounter.subject` → `Patient.id` | 1:N | Lượt khám của bệnh nhân |
| `Condition` | `Condition.subject` → `Patient.id` | 1:N | Bệnh lý theo nhóm tuổi |
| `MedicationRequest` | `MedicationRequest.subject` → `Patient.id` | 1:N | Thuốc theo nhóm tuổi |
| `Procedure` | `Procedure.subject` → `Patient.id` | 1:N | Dịch vụ kỹ thuật theo tuổi |
| `Observation` | `Observation.subject` → `Patient.id` | 1:N | Chỉ số sinh tồn, chiều cao, cân nặng |

---

## Báo cáo 14 — Thống Kê theo Khoa

### Resource chính: `Encounter` (GROUP BY serviceProvider)

**Endpoint:** `GET /Encounter?_include=Encounter:service-provider&_include=Encounter:diagnosis`

### Bảng trường dữ liệu tập trung

| Trường FHIR | Mô tả | Vai trò |
|---|---|---|
| `Encounter.serviceProvider` | Reference → Organization (khoa) | Chiều GROUP BY chính |
| `Encounter.class` | AMB/IMP/EMER | Phân loại loại hình tại khoa |
| `Encounter.period.start/.end` | Ngày vào/ra | Tính ngày điều trị |
| `Encounter.diagnosis[].condition` | Condition (ICD) | Top bệnh tại khoa |
| `Encounter.participant[].individual` | Practitioner | Nhân sự khoa |
| `Organization.identifier` | Mã khoa | Join key |
| `Organization.name` | Tên khoa | Label trong báo cáo |
| `Organization.partOf` | BV cha | Phân cấp báo cáo |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Metric cần tính |
|---|---|---|---|
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Nhóm theo khoa |
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Số bệnh nhân/khoa |
| `Condition` | `Encounter.diagnosis` → `Condition.id` | 1:N | Bệnh lý tại khoa |
| `Claim` | `Claim.encounter` → `Encounter.id` | 1:1 | Chi phí/khoa |
| `MedicationRequest` | `MedicationRequest.encounter` → `Encounter.id` | 1:N | Đơn thuốc/khoa |
| `Procedure` | `Procedure.encounter` → `Encounter.id` | 1:N | Dịch vụ kỹ thuật/khoa |
| `Location` | `Encounter.location[].location` → `Location.id` | N:N | Giường sử dụng/khoa |

---

## Báo cáo 15 — Thống Kê Lượt Sử Dụng Dịch Vụ Kỹ Thuật

### Resource chính: `ServiceRequest` + `Procedure` + `DiagnosticReport`

**Endpoint:** `GET /ServiceRequest?_include=ServiceRequest:encounter&_include=ServiceRequest:subject`

### Bảng trường dữ liệu — `ServiceRequest`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `ServiceRequest.id` | id | ✅ | ID chỉ định | `sr-xn-001` |
| `ServiceRequest.status` | code | ✅ | draft/active/completed/revoked | `completed` |
| `ServiceRequest.intent` | code | ✅ | order/plan/proposal | `order` |
| `ServiceRequest.category` | CodeableConcept[] | ✅ | Nhóm dịch vụ | Laboratory/Imaging/Procedure |
| `ServiceRequest.code` | CodeableConcept | ✅ | Mã dịch vụ cụ thể | LOINC/SNOMED |
| `ServiceRequest.subject` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `ServiceRequest.encounter` | Reference(Encounter) | ✅ | Lượt khám chỉ định | `Encounter/enc-001` |
| `ServiceRequest.requester` | Reference(Practitioner) | ✅ | Bác sĩ chỉ định | `Practitioner/dr-001` |
| `ServiceRequest.performer` | Reference(Organization)[] | ⚪ | Khoa/phòng thực hiện | `Organization/phong-xn` |
| `ServiceRequest.authoredOn` | dateTime | ✅ | Thời điểm chỉ định | `2024-01-15T09:00:00` |
| `ServiceRequest.priority` | code | ⚪ | routine/urgent/asap/stat | `routine` |

### Phân loại dịch vụ kỹ thuật

| Category | Code | Mô tả |
|---|---|---|
| Laboratory | `108252007` (SNOMED) | Xét nghiệm: máu, nước tiểu, vi sinh |
| Imaging | `363679005` (SNOMED) | X-Quang, CT, MRI, Siêu âm |
| Procedure | `387713003` (SNOMED) | Thủ thuật: nội soi, sinh thiết |
| Consultation | `11429006` (SNOMED) | Hội chẩn chuyên khoa |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Encounter` | `ServiceRequest.encounter` → `Encounter.id` | N:1 | Lượt khám chỉ định |
| `Patient` | `ServiceRequest.subject` → `Patient.id` | N:1 | Bệnh nhân thụ hưởng |
| `Procedure` | `Procedure.basedOn` → `ServiceRequest.id` | 1:1 | Thực hiện dịch vụ |
| `DiagnosticReport` | `DiagnosticReport.basedOn` → `ServiceRequest.id` | 1:1 | Kết quả trả về |
| `Observation` | `DiagnosticReport.result` → `Observation.id` | 1:N | Kết quả chi tiết |
| `ImagingStudy` | `DiagnosticReport.imagingStudy` → `ImagingStudy.id` | 1:N | Hình ảnh học |
| `Practitioner` | `ServiceRequest.requester` → `Practitioner.id` | N:1 | Bác sĩ chỉ định |
| `Organization` | `ServiceRequest.performer` → `Organization.id` | N:1 | Khoa thực hiện |
| `ChargeItem` | `ChargeItem.service` → `ServiceRequest.id` | 1:1 | Chi phí dịch vụ |

---

## Báo cáo 16 — Thống Kê Ca Mắc theo ICD

### Resource chính: `Condition`

**Endpoint:** `GET /Condition?verification-status=confirmed&_include=Condition:subject&_include=Condition:encounter`

### Bảng trường dữ liệu — `Condition`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Condition.id` | id | ✅ | ID chẩn đoán | `cond-i21-001` |
| `Condition.clinicalStatus` | CodeableConcept | ✅ | active/resolved/inactive/recurrence | code: `active` |
| `Condition.verificationStatus` | CodeableConcept | ✅ | confirmed/provisional/differential | code: `confirmed` |
| `Condition.category` | CodeableConcept[] | ✅ | encounter-diagnosis/problem-list-item | |
| `Condition.severity` | CodeableConcept | ⚪ | mild/moderate/severe | |
| `Condition.code` | CodeableConcept | ✅ | Mã ICD | coding: system ICD-10, code: `I21.0` |
| `Condition.bodySite` | CodeableConcept[] | ⚪ | Vị trí giải phẫu | |
| `Condition.subject` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `Condition.encounter` | Reference(Encounter) | ⚪ | Lượt khám ghi nhận | `Encounter/enc-001` |
| `Condition.onsetDateTime` | dateTime | ⚪ | Thời điểm khởi phát | `2024-01-10` |
| `Condition.recordedDate` | dateTime | ✅ | Ngày ghi nhận | `2024-01-15` |
| `Condition.asserter` | Reference(Practitioner) | ⚪ | Bác sĩ chẩn đoán | `Practitioner/dr-001` |
| `Condition.note` | Annotation[] | ⚪ | Ghi chú lâm sàng | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `Condition.subject` → `Patient.id` | N:1 | Bệnh nhân mắc bệnh |
| `Encounter` | `Condition.encounter` → `Encounter.id` | N:1 | Lượt khám ghi nhận chẩn đoán |
| `Practitioner` | `Condition.asserter` → `Practitioner.id` | N:1 | Bác sĩ chẩn đoán |
| `Organization` | Qua `Encounter.serviceProvider` | N:1 | Nơi ghi nhận chẩn đoán |
| `CodeSystem` (ICD) | `Condition.code.coding.system` | N:1 | Hệ thống mã bệnh |

---

## Báo cáo 17 — Số Đơn Thuốc

### Resource chính: `MedicationRequest`

**Endpoint:** `GET /MedicationRequest?status=active,completed&intent=order&_include=MedicationRequest:subject&_include=MedicationRequest:medication`

### Bảng trường dữ liệu — `MedicationRequest`

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `MedicationRequest.id` | id | ✅ | ID dòng thuốc | `mr-001` |
| `MedicationRequest.status` | code | ✅ | active/completed/cancelled/on-hold | `completed` |
| `MedicationRequest.intent` | code | ✅ | order/proposal/plan/instance-order | `order` |
| `MedicationRequest.medication[x]` | CodeableConcept hoặc Reference | ✅ | Thuốc kê | `Medication/med-paracetamol` |
| `MedicationRequest.subject` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `MedicationRequest.encounter` | Reference(Encounter) | ✅ | Lượt khám kê đơn | `Encounter/enc-001` |
| `MedicationRequest.authoredOn` | dateTime | ✅ | Ngày kê đơn | `2024-01-15T10:30:00` |
| `MedicationRequest.requester` | Reference(Practitioner) | ✅ | Bác sĩ kê đơn | `Practitioner/dr-001` |
| `MedicationRequest.groupIdentifier` | Identifier | ⚪ | Nhóm đơn thuốc (1 đơn = N dòng) | value: `rx-20240115-001` |
| `MedicationRequest.dosageInstruction` | Dosage[] | ✅ | Liều dùng, cách dùng | |
| `MedicationRequest.dispenseRequest.quantity` | Quantity | ⚪ | Số lượng cấp phát | |
| `MedicationRequest.dispenseRequest.performer` | Reference(Organization) | ⚪ | Nhà thuốc cấp phát | `Organization/nhathuoc-bvbm` |
| `MedicationRequest.note` | Annotation[] | ⚪ | Ghi chú cho dược sĩ | |

### Bảng trường dữ liệu — `Medication`

| Trường FHIR | Mô tả | Ví dụ |
|---|---|---|
| `Medication.code` | Mã thuốc | ATC code: `N02BE01` |
| `Medication.status` | active/inactive | `active` |
| `Medication.manufacturer` | Nhà sản xuất | `Organization/nsx-001` |
| `Medication.form` | Dạng bào chế | tablet/capsule/injection |
| `Medication.ingredient[].item[x]` | Hoạt chất | Paracetamol 500mg |
| `Medication.ingredient[].strength` | Hàm lượng | 500 mg/tablet |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Medication` | `MedicationRequest.medicationReference` → `Medication.id` | N:1 | Chi tiết thuốc |
| `Patient` | `MedicationRequest.subject` → `Patient.id` | N:1 | Bệnh nhân nhận đơn |
| `Encounter` | `MedicationRequest.encounter` → `Encounter.id` | N:1 | Lượt khám kê đơn |
| `Practitioner` | `MedicationRequest.requester` → `Practitioner.id` | N:1 | Bác sĩ kê đơn |
| `MedicationDispense` | `MedicationDispense.authorizingPrescription` → `MedicationRequest.id` | 1:1 | Cấp phát thực tế |
| `Organization` | `MedicationRequest.dispenseRequest.performer` → `Organization.id` | N:1 | Nhà thuốc cấp phát |

---

## Báo cáo 18 — Top 20 Bệnh theo ICD

*Kế thừa hoàn toàn từ Báo cáo 16 — `Condition`*

### Logic đặc thù

| Bước | Mô tả | FHIR/DAX |
|---|---|---|
| 1. Lấy dữ liệu | Tất cả `Condition` đã confirmed | `verificationStatus = confirmed` |
| 2. Lọc thời gian | Trong kỳ báo cáo | `recordedDate >= [start] AND <= [end]` |
| 3. Group | Theo `Condition.code` (mã ICD) | GROUP BY `code.coding.code` |
| 4. Đếm | Số ca mắc mỗi mã | COUNT(Condition.id) |
| 5. Sắp xếp | Giảm dần | ORDER BY count DESC |
| 6. Lấy top | Top 20 | TOPN(20, ...) |
| 7. Enrich | Lấy tên bệnh đầy đủ | JOIN với CodeSystem ICD |

### Bảng Resource liên quan

| Resource | Mục đích cụ thể |
|---|---|
| `Condition` | Nguồn dữ liệu chính |
| `CodeSystem` (ICD-10) | Lấy tên đầy đủ của từng mã bệnh |
| `Encounter` | Lọc theo khoa/BV/loại hình điều trị |
| `Patient` | Phân tích demographic của top bệnh |
| `Organization` | Breakdown top bệnh theo đơn vị |

---

## Báo cáo 19 — Điều Trị Nội Trú

### Resource chính: `Encounter` (class=IMP) — Fact Table trung tâm

**Endpoint:** `GET /Encounter?class=IMP&_include=Encounter:subject&_include=Encounter:diagnosis&_include=Encounter:service-provider&_include=Encounter:location`

### Bảng trường dữ liệu đầy đủ

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `Encounter.hospitalization.preAdmissionIdentifier` | Identifier | ⚪ | Mã tiền nhập viện | |
| `Encounter.hospitalization.origin` | Reference(Location) | ⚪ | Đến từ đâu (phòng khám/cấp cứu) | |
| `Encounter.hospitalization.admitSource` | CodeableConcept | ✅ | Nguồn nhập viện | emd/outp/born/gp/mp/nursing/... |
| `Encounter.hospitalization.reAdmission` | CodeableConcept | ⚪ | Tái nhập viện | |
| `Encounter.hospitalization.dietPreference` | CodeableConcept[] | ⚪ | Chế độ ăn | |
| `Encounter.hospitalization.specialArrangement` | CodeableConcept[] | ⚪ | Sắp xếp đặc biệt | xe lăn, thông dịch |
| `Encounter.hospitalization.destination` | Reference(Location) | ⚪ | Chuyển đến đâu khi ra | |
| `Encounter.hospitalization.dischargeDisposition` | CodeableConcept | ✅ | Hình thức ra viện | home/hosp/other-hcf/exp |
| `Encounter.diagnosis[].condition` | Reference(Condition) | ✅ | Chẩn đoán | `Condition/cond-001` |
| `Encounter.diagnosis[].use` | CodeableConcept | ✅ | AD (nhập viện)/DD (ra viện)/CC (chính) | |
| `Encounter.diagnosis[].rank` | positiveInt | ⚪ | Thứ tự chẩn đoán | `1` = chính |

### Bảng Resource liên quan (đầy đủ)

| Resource | Trường tham chiếu | Loại quan hệ | Metric/Mục đích |
|---|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Nhân khẩu học bệnh nhân nội trú |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Khoa/BV điều trị |
| `Location` | `Encounter.location[].location` → `Location.id` | N:N | Giường/phòng |
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | 1:N | Chẩn đoán vào/ra viện |
| `Procedure` | `Procedure.encounter` → `Encounter.id` | 1:N | Phẫu thuật/thủ thuật |
| `MedicationRequest` | `MedicationRequest.encounter` → `Encounter.id` | 1:N | Thuốc trong đợt nội trú |
| `Claim` / `Invoice` | `Claim.encounter` → `Encounter.id` | 1:1 | Chi phí nội trú |
| `Observation` | `Observation.encounter` → `Encounter.id` | 1:N | Dấu hiệu sinh tồn, theo dõi |
| `DiagnosticReport` | `DiagnosticReport.encounter` → `Encounter.id` | 1:N | Kết quả xét nghiệm/CĐHA |
| `ServiceRequest` | `ServiceRequest.encounter` → `Encounter.id` | 1:N | Dịch vụ kỹ thuật được chỉ định |
| `AllergyIntolerance` | `AllergyIntolerance.patient` → `Patient.id` | 1:N | Dị ứng thuốc |
| `NutritionOrder` | `NutritionOrder.encounter` → `Encounter.id` | 1:1 | Chế độ ăn nội trú |
| `EpisodeOfCare` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | N:1 | Đợt chăm sóc tổng thể |

---

## Báo cáo 20 — Tổng Số Ngày Điều Trị theo Ngày

### Resource chính: `Encounter` + `DimDate`

### Bảng trường dữ liệu

| Trường FHIR | Mô tả | Vai trò |
|---|---|---|
| `Encounter.period.start` | Ngày vào viện | Tính Census từ ngày này |
| `Encounter.period.end` | Ngày ra viện | Tính Census đến ngày này |
| `Encounter.class` | IMP | Filter nội trú |
| `Encounter.status` | in-progress/finished | Tính tổng đang điều trị |
| `Encounter.serviceProvider` | Khoa/BV | Breakdown theo đơn vị |

### Logic tính Census (số bệnh nhân đang điều trị tại ngày D)

```
Census(D) = COUNT(Encounter WHERE
    class = 'IMP' AND
    period.start <= D AND
    (period.end IS NULL OR period.end >= D)
)
```

### Bảng Resource liên quan

| Resource | Mục đích |
|---|---|
| `Encounter` | Nguồn dữ liệu chính |
| `Organization` | Breakdown Census theo khoa |
| `Location` | Census theo phòng/giường |
| `DimDate` (Power BI) | Calendar table — trục X của biểu đồ |

---

## Báo cáo 21 — Thống Kê Chi Phí theo Ngày

### Resource chính: `Claim` + `Invoice` + `ChargeItem`

### Bảng trường dữ liệu — `ChargeItem` (chi tiết nhất)

| Trường FHIR | Kiểu dữ liệu | Bắt buộc | Mô tả | Ví dụ |
|---|---|:---:|---|---|
| `ChargeItem.id` | id | ✅ | ID khoản phí | `ci-001` |
| `ChargeItem.status` | code | ✅ | planned/billable/billed/... | `billed` |
| `ChargeItem.code` | CodeableConcept | ✅ | Mã dịch vụ tính phí | |
| `ChargeItem.subject` | Reference(Patient) | ✅ | Bệnh nhân | `Patient/pt-001` |
| `ChargeItem.context` | Reference(Encounter) | ✅ | Lượt khám | `Encounter/enc-001` |
| `ChargeItem.occurrenceDateTime` | dateTime | ✅ | Ngày phát sinh phí | `2024-01-16T14:00:00` |
| `ChargeItem.performer[].actor` | Reference | ⚪ | Người thực hiện | |
| `ChargeItem.performingOrganization` | Reference(Organization) | ⚪ | Khoa tính phí | |
| `ChargeItem.quantity` | Quantity | ⚪ | Số lượng | |
| `ChargeItem.priceOverride` | Money | ⚪ | Giá ghi đè | |
| `ChargeItem.factorOverride` | decimal | ⚪ | Hệ số điều chỉnh | |
| `ChargeItem.totalPriceComponent` | MoneyQuantity | ⚪ | Thành tiền | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Encounter` | `Claim.encounter` → `Encounter.id` | N:1 | Ngày phát sinh chi phí |
| `Patient` | `Claim.patient` → `Patient.id` | N:1 | Phân tích chi phí theo bệnh nhân |
| `Coverage` | `Claim.insurance[].coverage` → `Coverage.id` | N:1 | Tỷ lệ BHYT/tự trả theo ngày |
| `ClaimResponse` | `ClaimResponse.request` → `Claim.id` | 1:1 | Số tiền thực chi |
| `ChargeItem` | `Invoice.lineItem.chargeItem` → `ChargeItem.id` | N:1 | Chi tiết dòng phí |
| `Organization` | `Claim.provider` → `Organization.id` | N:1 | Chi phí theo đơn vị |

---

## Báo cáo 22 — Điều Trị Nội Trú theo Ngày

### Resource chính: `Encounter` (class=IMP)

### Bảng 3 metric chính

| Metric | Định nghĩa FHIR | Công thức |
|---|---|---|
| **Nhập viện (D)** | Encounter IMP có `period.start` trong ngày D | `COUNT WHERE DATE(start) = D` |
| **Ra viện (D)** | Encounter IMP có `period.end` trong ngày D | `COUNT WHERE DATE(end) = D` |
| **Census (D)** | Encounter IMP đang `in-progress` cuối ngày D | `COUNT WHERE start ≤ D AND (end IS NULL OR end > D)` |

### Bảng trường dữ liệu bổ sung

| Trường FHIR | Mô tả | Ví dụ |
|---|---|---|
| `Encounter.hospitalization.admitSource` | Nguồn nhập viện hôm nay | emd/outp/born/... |
| `Encounter.hospitalization.dischargeDisposition` | Lý do ra viện hôm nay | home/hosp/exp/... |
| `Encounter.serviceProvider` | Khoa tiếp nhận | `Organization/khoa-noi` |
| `Encounter.diagnosis[].condition` | Chẩn đoán nhập viện | ICD tương ứng |

### Bảng Resource liên quan

| Resource | Mục đích |
|---|---|
| `Patient` | Phân tích demographic dòng nhập/ra |
| `Organization` | Breakdown 3 metric theo khoa |
| `Location` | Theo dõi tình trạng giường theo ngày |
| `Condition` | Bệnh lý liên quan dòng nhập/ra theo ngày |
| `DimDate` | Trục thời gian |

---

## Báo cáo 23 — Thống Kê Hồ Sơ KCB theo Ngày Ra Viện

### Resource chính: `Encounter` + `EpisodeOfCare`

**Endpoint:** `GET /Encounter?status=finished&_include=Encounter:subject&_include=Encounter:diagnosis`

### Bảng trường dữ liệu — tập trung vào ngày ra viện

| Trường FHIR | Mô tả | Vai trò |
|---|---|---|
| `Encounter.period.end` | **Ngày ra viện** — chiều GROUP BY chính | Trục X biểu đồ |
| `Encounter.status` | `finished` — đã hoàn tất | Filter |
| `Encounter.hospitalization.dischargeDisposition` | Hình thức ra viện | Phân loại |
| `Encounter.class` | IMP/AMB/EMER | Loại hình KCB |
| `Encounter.diagnosis[{rank=1}].condition` | **Chẩn đoán chính ra viện** | Thống kê bệnh ra viện |
| `EpisodeOfCare.status` | `finished` | Hồ sơ đã đóng |
| `EpisodeOfCare.period.end` | Ngày đóng hồ sơ | Ngày ra viện ở level EoC |

### Phân loại `dischargeDisposition`

| Code | Tên | Ý nghĩa |
|---|---|---|
| `home` | Về nhà | Điều trị thành công |
| `hosp` | Chuyển BV | Chuyển tuyến trên |
| `other-hcf` | Chuyển cơ sở khác | Chuyển tuyến dưới/cùng |
| `exp` | Tử vong | Tử vong tại BV |
| `aadvice` | Xin về | Bệnh nhân tự xin ra |
| `oth` | Khác | |

### Bảng Resource liên quan

| Resource | Trường tham chiếu | Loại quan hệ | Mục đích |
|---|---|---|---|
| `Patient` | `Encounter.subject` → `Patient.id` | N:1 | Nhân khẩu học bệnh nhân ra viện |
| `Condition` | `Encounter.diagnosis[].condition` → `Condition.id` | 1:N | Chẩn đoán ra viện (ICD) |
| `Organization` | `Encounter.serviceProvider` → `Organization.id` | N:1 | Thống kê theo đơn vị |
| `Claim` | `Claim.encounter` → `Encounter.id` | 1:1 | Thanh toán khi ra viện |
| `DocumentReference` | Qua `Encounter` | N:1 | Giấy ra viện, tóm tắt bệnh án |
| `MedicationRequest` | `MedicationRequest.encounter` → `Encounter.id` | 1:N | Đơn thuốc mang về |
| `EpisodeOfCare` | `Encounter.episodeOfCare` → `EpisodeOfCare.id` | N:1 | Hồ sơ tổng thể |

---

## Phụ lục — Tổng hợp tất cả Resource được sử dụng

| Resource | Số báo cáo sử dụng | Vai trò chủ yếu |
|---|---|---|
| `Encounter` | 20/23 | Fact table trung tâm |
| `Patient` | 18/23 | Dimension bệnh nhân |
| `Organization` | 18/23 | Dimension đơn vị (BV/Khoa) |
| `Condition` | 14/23 | Chẩn đoán/bệnh lý |
| `Location` | 10/23 | Giường/phòng/khoa vật lý |
| `Claim` | 6/23 | Thanh toán, chi phí |
| `MedicationRequest` | 5/23 | Đơn thuốc |
| `Procedure` | 6/23 | Thủ thuật, dịch vụ kỹ thuật |
| `ServiceRequest` | 3/23 | Chỉ định dịch vụ |
| `DiagnosticReport` | 3/23 | Kết quả xét nghiệm |
| `EpisodeOfCare` | 4/23 | Hồ sơ bệnh án |
| `CodeSystem/ValueSet` | 3/23 | Danh mục ICD |
| `Coverage` | 4/23 | Bảo hiểm y tế |
| `Invoice/ChargeItem` | 3/23 | Chi tiết phí |
| `ClaimResponse` | 2/23 | Kết quả xét duyệt BHYT |
| `Observation` | 4/23 | Dấu hiệu lâm sàng |
| `Medication` | 2/23 | Danh mục thuốc |
| `MedicationDispense` | 2/23 | Cấp phát thuốc |
| `Practitioner/PractitionerRole` | 5/23 | Nhân sự y tế |
| `DocumentReference` | 2/23 | Tài liệu y tế |

---

*Tài liệu kỹ thuật — HL7 FHIR R4B (4.3.0) | https://hl7.org/fhir/R4B/*
