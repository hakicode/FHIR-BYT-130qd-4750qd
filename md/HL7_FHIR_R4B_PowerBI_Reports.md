# Phân tích FHIR R4B Resources cho 23 Báo cáo Power BI – Lĩnh vực Y Tế

> **Chuẩn tham chiếu:** HL7 FHIR R4B (4.3.0)  
> **Mục tiêu:** Xác định Resource chính và các Resource liên quan cho từng báo cáo Power BI trong hệ thống thống kê dữ liệu bệnh viện.

---

## Quy ước chung

| Ký hiệu | Ý nghĩa |
|---|---|
| **Resource chính** | Resource trực tiếp chứa dữ liệu cốt lõi của báo cáo |
| **Resource liên quan** | Resource được tham chiếu (reference) hoặc bổ sung ngữ cảnh |
| `$include` | Tham số `_include` khi gọi FHIR API để kéo thêm resource |
| `_revinclude` | Tham số để kéo resource ngược chiều (reverse reference) |

---

## 1. Danh mục Bệnh viện

### Resource chính
**`Organization`**

### Mô tả
Resource `Organization` trong FHIR đại diện cho một tổ chức y tế — bao gồm bệnh viện, phòng khám, trung tâm y tế. Mỗi bệnh viện là một `Organization` với `type` được mã hoá theo hệ thống chuẩn (ví dụ: `http://terminology.hl7.org/CodeSystem/organization-type`, code `prov` = Healthcare Provider).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Location` | `Location.managingOrganization` | Địa chỉ vật lý, toạ độ, thông tin cơ sở vật chất của bệnh viện |
| `HealthcareService` | `HealthcareService.providedBy` | Các dịch vụ y tế mà bệnh viện cung cấp |
| `OrganizationAffiliation` | `OrganizationAffiliation.organization` | Quan hệ liên kết giữa các bệnh viện (ví dụ: bệnh viện vệ tinh) |
| `Endpoint` | `Organization.endpoint` | Thông tin kết nối hệ thống HIS/EMR của bệnh viện |
| `Practitioner` / `PractitionerRole` | `PractitionerRole.organization` | Đội ngũ y bác sĩ thuộc bệnh viện |

### Ghi chú Power BI
- Dùng `Organization?type=prov&_include=Organization:partof` để lấy phân cấp bệnh viện → khoa → phòng.
- Trường `Organization.identifier` thường chứa mã bệnh viện theo quy định của Bộ Y tế.

---

## 2. Danh mục Khoa

### Resource chính
**`Organization`** (với `type = dept`) hoặc **`Location`** (tùy mô hình triển khai)

### Mô tả
Khoa (Department) trong FHIR R4B có thể được mô hình hoá theo hai cách:
1. `Organization` với `type = dept` và `partOf` trỏ về bệnh viện cha.
2. `Location` với `physicalType = wa` (ward) và `managingOrganization` trỏ về bệnh viện.

Trong thực tế triển khai Việt Nam, **`Organization` dạng cây phân cấp** phổ biến hơn.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Organization` (cha) | `Organization.partOf` | Bệnh viện chủ quản của khoa |
| `Location` | `Location.managingOrganization` | Phòng vật lý, giường bệnh thuộc khoa |
| `PractitionerRole` | `PractitionerRole.organization` | Nhân sự được phân công tại khoa |
| `HealthcareService` | `HealthcareService.providedBy` | Dịch vụ được thực hiện tại khoa |
| `Encounter` | `Encounter.serviceProvider` | Lượt khám gắn với khoa |

### Ghi chú Power BI
- Query: `Organization?type=dept&_include=Organization:partof` để dựng cây bệnh viện → khoa.
- Kết hợp với `Location?_include=Location:organization` để lấy số phòng, số giường.

---

## 3. Danh mục Bệnh theo ICD

### Resource chính
**`CodeSystem`** + **`ValueSet`** (ICD-10 / ICD-11)

### Mô tả
FHIR không lưu trữ danh mục ICD dưới dạng clinical resource mà sử dụng **Terminology Resources**:
- `CodeSystem`: Định nghĩa các mã ICD và thuộc tính (code, display, định nghĩa).
- `ValueSet`: Tập hợp các mã ICD được phép dùng trong hệ thống.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `ValueSet` | `ValueSet.compose.include.system` | Danh sách mã ICD cho từng chuyên khoa |
| `ConceptMap` | `ConceptMap.group.source/target` | Ánh xạ giữa ICD-10 và ICD-11 |
| `Condition` | `Condition.code.coding.system` | Chẩn đoán thực tế dùng mã ICD |
| `Encounter` | `Encounter.reasonCode` | Lý do vào viện dùng mã ICD |

### Ghi chú Power BI
- Endpoint: `GET /CodeSystem?url=http://hl7.org/fhir/sid/icd-10`
- Dùng `ValueSet/$expand` để expand toàn bộ danh mục ICD ra dạng bảng phẳng.
- Kết hợp với `Condition` để thống kê tần suất từng mã bệnh.

---

## 4. Danh mục Nhà thuốc

### Resource chính
**`Organization`** (với `type = pharmacy`) + **`Location`**

### Mô tả
Nhà thuốc trong FHIR là một `Organization` với `type` = `pharm` (pharmacy). Nếu cần thêm thông tin vị trí, giờ mở cửa, dịch vụ → bổ sung `Location` và `HealthcareService`.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Location` | `Location.managingOrganization` | Địa chỉ, toạ độ, giờ hoạt động của nhà thuốc |
| `HealthcareService` | `HealthcareService.providedBy` | Dịch vụ phân phối thuốc |
| `MedicationDispense` | `MedicationDispense.performer.actor` | Lịch sử cấp phát thuốc tại nhà thuốc |
| `MedicationRequest` | `MedicationRequest.dispenseRequest.performer` | Đơn thuốc gửi đến nhà thuốc |
| `PractitionerRole` | `PractitionerRole.organization` | Dược sĩ làm việc tại nhà thuốc |

### Ghi chú Power BI
- Query: `Organization?type=pharm&_include=Organization:endpoint&_include=Location:organization`

---

## 5. Số Giường

### Resource chính
**`Location`** (với `physicalType = bd` – bed)

### Mô tả
Mỗi giường bệnh là một `Location` riêng biệt với:
- `physicalType.coding.code = bd` (bed) theo hệ thống `http://terminology.hl7.org/CodeSystem/location-physical-type`
- `partOf` trỏ về phòng → khoa → bệnh viện.
- `status`: `active | suspended | inactive` (giường đang hoạt động / tạm dừng / ngừng).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Location` (phòng) | `Location.partOf` | Phòng chứa giường |
| `Organization` | `Location.managingOrganization` | Khoa/bệnh viện quản lý giường |
| `Encounter` | `Encounter.location.location` | Lượt nội trú đang chiếm giường |
| `Schedule` / `Slot` | `Schedule.actor` | Lịch đặt giường trước |

### Ghi chú Power BI
- Query: `Location?physicalType=bd&_include=Location:partof&_include=Location:organization`
- Đếm `Location.status = active` → tổng giường hoạt động.
- `LEFT JOIN` với `Encounter` đang `in-progress` để tính **tỷ lệ sử dụng giường**.

---

## 6. Tổng Số Ngày Điều Trị

### Resource chính
**`Encounter`**

### Mô tả
Mỗi lượt điều trị nội trú là một `Encounter` với:
- `class = IMP` (inpatient) theo `ActCode`.
- `period.start` và `period.end` → tính số ngày = `(end - start)` theo ngày.
- `status = finished` cho các lượt đã hoàn thành.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Bệnh nhân điều trị |
| `Organization` | `Encounter.serviceProvider` | Khoa/bệnh viện điều trị |
| `Location` | `Encounter.location.location` | Giường/phòng được sử dụng |
| `Condition` | `Encounter.diagnosis.condition` | Chẩn đoán trong đợt điều trị |
| `EpisodeOfCare` | `Encounter.episodeOfCare` | Đợt chăm sóc dài hạn (nếu có) |

### Ghi chú Power BI
- Query: `Encounter?class=IMP&status=finished&date=ge[startDate]&date=le[endDate]`
- Tính `SUM(period.end - period.start)` → tổng ngày điều trị.
- Group by `serviceProvider` để thống kê theo khoa/bệnh viện.

---

## 7. Thống Kê Chi Phí

### Resource chính
**`Claim`** + **`ClaimResponse`** + **`Invoice`**

### Mô tả
- `Claim`: Hồ sơ yêu cầu thanh toán gửi đi (bảo hiểm y tế, tự trả).
- `ClaimResponse`: Kết quả xét duyệt, số tiền được chấp nhận.
- `Invoice`: Hoá đơn chi tiết các khoản phí (dịch vụ, thuốc, vật tư).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Claim.encounter` | Lượt khám/điều trị phát sinh chi phí |
| `Patient` | `Claim.patient` | Bệnh nhân chi trả |
| `Coverage` | `Claim.insurance.coverage` | Thông tin bảo hiểm y tế |
| `MedicationRequest` | `Claim.item.encounter` | Chi phí thuốc |
| `ServiceRequest` | `Claim.item` | Chi phí dịch vụ kỹ thuật |
| `Procedure` | `Claim.procedure` | Thủ thuật/phẫu thuật phát sinh chi phí |
| `ChargeItem` | `Invoice.lineItem.chargeItem` | Chi tiết từng khoản phí |

### Ghi chú Power BI
- Dùng `ClaimResponse` để lấy số tiền **thực được thanh toán** sau xét duyệt.
- `Invoice` cho chi tiết dòng phí → phù hợp báo cáo chi phí chi tiết theo dịch vụ.
- Kết hợp `Coverage` để phân tích tỷ lệ BHYT / tự trả.

---

## 8. Thống Kê Lượt Bệnh Nhân Vào Ra

### Resource chính
**`Encounter`**

### Mô tả
Thống kê dòng chảy bệnh nhân (patient flow): số vào viện (`status = in-progress`), số ra viện (`status = finished`), số đang điều trị. Sử dụng `period.start` (ngày vào) và `period.end` (ngày ra).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Thông tin bệnh nhân |
| `Organization` | `Encounter.serviceProvider` | Bệnh viện/khoa tiếp nhận |
| `Location` | `Encounter.location` | Địa điểm điều trị |
| `Condition` | `Encounter.reasonCode` hoặc `diagnosis` | Lý do vào viện |
| `EpisodeOfCare` | `Encounter.episodeOfCare` | Theo dõi liên tục một đợt bệnh |

### Ghi chú Power BI
- Tách thành 2 metric: **Lượt vào** (đếm theo `period.start`) và **Lượt ra** (đếm theo `period.end`).
- Filter `class` để phân biệt ngoại trú (AMB), nội trú (IMP), cấp cứu (EMER).

---

## 9. Số Bệnh Nhân theo Loại Hình Khám Chữa Bệnh

### Resource chính
**`Encounter`** (phân loại theo `class` và `type`)

### Mô tả
FHIR phân loại lượt khám qua:
- `Encounter.class`: `AMB` (ngoại trú), `IMP` (nội trú), `EMER` (cấp cứu), `HH` (tại nhà), `SS` (short stay).
- `Encounter.type`: Loại hình chi tiết hơn (khám lần đầu, tái khám, khám chuyên khoa...).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Thông tin bệnh nhân |
| `Organization` | `Encounter.serviceProvider` | Đơn vị thực hiện |
| `Practitioner` | `Encounter.participant.individual` | Bác sĩ điều trị |
| `Coverage` | `Encounter.account → Account.coverage` | Loại hình bảo hiểm |
| `ServiceType` (embedded) | `Encounter.serviceType` | Dịch vụ khám cụ thể |

### Ghi chú Power BI
- Group by `Encounter.class` để tạo bảng phân loại loại hình KCB.
- Kết hợp `Coverage.type` để biết tỷ lệ BHYT, dịch vụ, miễn phí.

---

## 10. Số Ca Cấp Cứu Tử Vong

### Resource chính
**`Encounter`** (class = EMER) + **`Condition`** (với verificationStatus = confirmed, về tử vong)

### Mô tả
Ca cấp cứu tử vong = `Encounter.class = EMER` + `Encounter.hospitalization.dischargeDisposition` có code chỉ tử vong (ví dụ: `exp` = expired theo `http://terminology.hl7.org/CodeSystem/discharge-disposition`).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Thông tin bệnh nhân tử vong |
| `Condition` | `Encounter.diagnosis` | Chẩn đoán khi tử vong (ICD) |
| `Observation` | `Observation.encounter` | Dấu hiệu sinh tồn cuối cùng |
| `Procedure` | `Procedure.encounter` | Thủ thuật cấp cứu đã thực hiện |
| `Organization` | `Encounter.serviceProvider` | Khoa cấp cứu |
| `Practitioner` | `Encounter.participant` | Bác sĩ/điều dưỡng trực tiếp |

### Ghi chú Power BI
- Filter: `Encounter?class=EMER&_include=Encounter:diagnosis`
- Lọc `hospitalization.dischargeDisposition.coding.code = exp`
- Kết hợp `Condition.code` (ICD) → top nguyên nhân tử vong tại cấp cứu.

---

## 11. Số Hồ Sơ Khám Chữa Bệnh

### Resource chính
**`EpisodeOfCare`** hoặc **`Encounter`**

### Mô tả
- `EpisodeOfCare`: Đại diện cho **một đợt chăm sóc** liên tục (một hồ sơ bệnh án). Một EpisodeOfCare có thể chứa nhiều Encounter.
- `Encounter`: Nếu hệ thống không dùng EpisodeOfCare, mỗi Encounter là một hồ sơ riêng.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `EpisodeOfCare.patient` | Bệnh nhân |
| `Organization` | `EpisodeOfCare.managingOrganization` | Đơn vị quản lý hồ sơ |
| `Encounter` | `Encounter.episodeOfCare` | Các lượt khám trong hồ sơ |
| `Condition` | `EpisodeOfCare.diagnosis.condition` | Chẩn đoán chính của hồ sơ |
| `Practitioner` | `EpisodeOfCare.careManager` | Bác sĩ phụ trách hồ sơ |
| `DocumentReference` | `DocumentReference.context.encounter` | Tài liệu y tế đính kèm hồ sơ |

### Ghi chú Power BI
- Đếm `EpisodeOfCare` để có số hồ sơ duy nhất (không bị trùng khi bệnh nhân tái khám nhiều lần).
- Group by `managingOrganization` và `period` để phân tích theo đơn vị và thời gian.

---

## 12. Thống Kê Tai Nạn

### Resource chính
**`Condition`** + **`Encounter`**

### Mô tả
Tai nạn trong FHIR được xác định qua:
- `Condition.code`: Mã ICD-10 nhóm S (Injuries), T (Poisonings/External causes), V–Y (External causes of morbidity).
- `Condition.category`: `encounter-diagnosis`.
- `Encounter.reasonCode`: Mã lý do vào viện do tai nạn.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Condition.encounter` | Lượt điều trị do tai nạn |
| `Patient` | `Condition.subject` | Bệnh nhân bị tai nạn |
| `Procedure` | `Procedure.encounter` | Phẫu thuật/xử lý vết thương |
| `Observation` | `Observation.encounter` | Ghi nhận mức độ chấn thương |
| `Organization` | `Encounter.serviceProvider` | Nơi tiếp nhận |
| `Location` | `Encounter.location` | Địa điểm tiếp nhận (cấp cứu, phòng mổ) |

### Ghi chú Power BI
- Filter `Condition.code` theo dải ICD: `S00–S99`, `T00–T98`, `V00–Y99`.
- Phân loại: Tai nạn giao thông (V01–V99), Tai nạn lao động (W00–W99), Tai nạn sinh hoạt.

---

## 13. Thống Kê theo Tuổi

### Resource chính
**`Patient`** + **`Encounter`**

### Mô tả
Tính tuổi bệnh nhân từ `Patient.birthDate` so với ngày khám (`Encounter.period.start`). Phân nhóm tuổi theo chuẩn của Bộ Y tế Việt Nam hoặc WHO (0–5, 6–14, 15–60, >60...).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Encounter.subject` | Lượt khám của bệnh nhân |
| `Condition` | `Condition.subject` | Bệnh theo nhóm tuổi |
| `Observation` | `Observation.subject` | Chỉ số lâm sàng theo tuổi |
| `MedicationRequest` | `MedicationRequest.subject` | Thuốc theo nhóm tuổi |
| `Procedure` | `Procedure.subject` | Dịch vụ kỹ thuật theo tuổi |

### Ghi chú Power BI
- Tạo cột tính tuổi: `DATEDIFF(Patient.birthDate, Encounter.period.start, YEAR)`
- Tạo nhóm tuổi bằng DAX: `SWITCH(TRUE(), age < 1, "Sơ sinh", age <= 5, "0-5", ...)`
- Cross join với `Condition` để có ma trận **Tuổi × Bệnh**.

---

## 14. Thống Kê theo Khoa

### Resource chính
**`Encounter`** (group by `serviceProvider` hoặc `location`)

### Mô tả
Thống kê các chỉ số (lượt khám, ngày điều trị, chi phí, bệnh nhân) theo từng khoa trong bệnh viện. Khoa được xác định qua `Encounter.serviceProvider` (trỏ về `Organization` khoa) hoặc `Encounter.location` (trỏ về `Location` thuộc khoa).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Organization` | `Encounter.serviceProvider` | Định danh khoa |
| `Location` | `Encounter.location.location` | Phòng/giường trong khoa |
| `Patient` | `Encounter.subject` | Bệnh nhân trong khoa |
| `Condition` | `Encounter.diagnosis` | Bệnh điều trị tại khoa |
| `Claim` | `Claim.encounter` | Chi phí phát sinh tại khoa |
| `Practitioner` | `Encounter.participant` | Nhân sự khoa |

### Ghi chú Power BI
- Dựng `Encounter` → JOIN với `Organization` (khoa) → GROUP BY.
- Tạo bảng pivot: **Khoa × Tháng × Chỉ số**.

---

## 15. Thống Kê Lượt Sử Dụng Dịch Vụ Kỹ Thuật

### Resource chính
**`ServiceRequest`** + **`Procedure`** + **`DiagnosticReport`**

### Mô tả
- `ServiceRequest`: Chỉ định dịch vụ kỹ thuật (xét nghiệm, chẩn đoán hình ảnh, thủ thuật).
- `Procedure`: Ghi nhận dịch vụ đã được thực hiện.
- `DiagnosticReport`: Kết quả xét nghiệm, CĐHA đã trả.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `ServiceRequest.encounter` | Lượt khám chỉ định dịch vụ |
| `Patient` | `ServiceRequest.subject` | Bệnh nhân thụ hưởng |
| `Observation` | `DiagnosticReport.result` | Kết quả chi tiết xét nghiệm |
| `ImagingStudy` | `DiagnosticReport.imagingStudy` | Hình ảnh học (X-Quang, MRI, CT) |
| `Practitioner` | `ServiceRequest.requester` | Bác sĩ chỉ định |
| `Organization` | `ServiceRequest.performer` | Khoa/phòng thực hiện |
| `ChargeItem` | `ChargeItem.service` | Chi phí dịch vụ kỹ thuật |

### Ghi chú Power BI
- Đếm `ServiceRequest` theo `code` → top dịch vụ được chỉ định nhiều nhất.
- Đếm `Procedure.status = completed` → dịch vụ đã thực hiện.
- Tỷ lệ hoàn thành = `Procedure.completed / ServiceRequest.total`.

---

## 16. Thống Kê Ca Mắc theo ICD

### Resource chính
**`Condition`**

### Mô tả
Mỗi chẩn đoán bệnh là một `Condition` với:
- `Condition.code.coding`: Mã ICD-10/11 + tên bệnh.
- `Condition.clinicalStatus`: `active | resolved | inactive`.
- `Condition.verificationStatus`: `confirmed | provisional`.
- `Condition.category`: `encounter-diagnosis` (chẩn đoán tại khám) hoặc `problem-list-item` (bệnh mãn tính).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Condition.encounter` | Lượt khám ghi nhận bệnh |
| `Patient` | `Condition.subject` | Bệnh nhân mắc bệnh |
| `Organization` | `Encounter.serviceProvider` | Nơi ghi nhận |
| `Practitioner` | `Condition.asserter` | Bác sĩ chẩn đoán |
| `CodeSystem` (ICD) | `Condition.code.coding.system` | Hệ thống mã bệnh |

### Ghi chú Power BI
- Group by `Condition.code` → đếm số ca mắc mỗi mã ICD.
- Filter `verificationStatus = confirmed` để loại chẩn đoán tạm thời.
- Phân tích theo `Condition.onsetDateTime` để vẽ xu hướng dịch bệnh.

---

## 17. Số Đơn Thuốc

### Resource chính
**`MedicationRequest`**

### Mô tả
Mỗi đơn thuốc là một hoặc nhiều `MedicationRequest` liên kết cùng một `Encounter`. `MedicationRequest.groupIdentifier` dùng để nhóm các thuốc trong cùng một đơn.
- `status`: `active | completed | cancelled | on-hold`.
- `intent`: `order` (đơn chính thức).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `MedicationRequest.encounter` | Lượt khám kê đơn |
| `Patient` | `MedicationRequest.subject` | Bệnh nhân nhận đơn |
| `Medication` | `MedicationRequest.medicationReference` | Chi tiết thuốc (tên, hoạt chất, dạng bào chế) |
| `Practitioner` | `MedicationRequest.requester` | Bác sĩ kê đơn |
| `MedicationDispense` | `MedicationDispense.authorizingPrescription` | Thông tin cấp phát thực tế |
| `Organization` | `MedicationRequest.dispenseRequest.performer` | Nhà thuốc/khoa dược |

### Ghi chú Power BI
- Đếm `MedicationRequest.groupIdentifier` (unique) → số đơn thuốc.
- Đếm `MedicationRequest` (total) → tổng số dòng thuốc.
- Tỷ lệ cấp phát = `MedicationDispense / MedicationRequest`.

---

## 18. Top 20 Bệnh theo ICD

### Resource chính
**`Condition`**

### Mô tả
Tương tự báo cáo #16 nhưng áp dụng `TOPN(20)` theo tần suất mã ICD. Lấy toàn bộ `Condition.code` đã xác nhận (`verificationStatus = confirmed`), đếm tần suất, sắp xếp giảm dần.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Condition.encounter` | Thêm ngữ cảnh lâm sàng |
| `Patient` | `Condition.subject` | Phân tích theo nhóm dân số |
| `Organization` | `Encounter.serviceProvider` | Lọc theo bệnh viện/khoa |
| `CodeSystem` (ICD) | `Condition.code` | Lấy tên đầy đủ của bệnh |

### Ghi chú Power BI
- DAX: `TOPN(20, SUMMARIZE(Condition, Condition[code], "Count", COUNTROWS(Condition)), [Count], DESC)`
- Dùng Bar Chart nằm ngang, hiển thị cả mã ICD và tên bệnh.

---

## 19. Điều Trị Nội Trú

### Resource chính
**`Encounter`** (class = IMP – Inpatient)

### Mô tả
Điều trị nội trú là `Encounter` với `class = IMP`. Cần khai thác đầy đủ: ngày vào, ngày ra, khoa điều trị, chẩn đoán, chi phí, thủ thuật và kết quả điều trị.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Bệnh nhân nội trú |
| `Condition` | `Encounter.diagnosis` | Chẩn đoán vào viện / ra viện |
| `Procedure` | `Procedure.encounter` | Phẫu thuật/thủ thuật trong nội trú |
| `MedicationRequest` | `MedicationRequest.encounter` | Thuốc kê trong đợt nội trú |
| `Location` | `Encounter.location` | Giường/phòng/khoa |
| `Organization` | `Encounter.serviceProvider` | Khoa điều trị |
| `Claim` / `Invoice` | `Claim.encounter` | Chi phí nội trú |
| `Observation` | `Observation.encounter` | Dấu hiệu sinh tồn, theo dõi |
| `AllergyIntolerance` | `AllergyIntolerance.patient` | Dị ứng của bệnh nhân |
| `DiagnosticReport` | `DiagnosticReport.encounter` | Kết quả xét nghiệm/CĐHA |

### Ghi chú Power BI
- Là báo cáo **tổng hợp nhất**, cần dựng Star Schema với `Encounter(IMP)` làm fact table trung tâm.
- Tính: số ngày nằm viện trung bình, chi phí trung bình, tỷ lệ tái nhập viện trong 30 ngày.

---

## 20. Tổng Số Ngày Điều Trị theo Ngày

### Resource chính
**`Encounter`**

### Mô tả
Mở rộng của báo cáo #6, thêm chiều thời gian theo **ngày** (time series). Mỗi điểm dữ liệu = tổng ngày điều trị tích lũy hoặc tổng ngày điều trị phát sinh trong ngày đó.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Organization` | `Encounter.serviceProvider` | Lọc theo khoa/bệnh viện |
| `Location` | `Encounter.location` | Lọc theo phòng/giường |
| `Patient` | `Encounter.subject` | Phân tích nhân khẩu học |

### Ghi chú Power BI
- Tạo **Date Dimension Table** từ min(`period.start`) đến max(`period.end`).
- Với mỗi ngày D: đếm Encounter đang `in-progress` (start ≤ D ≤ end) → số giường đang chiếm.
- Vẽ Line Chart theo ngày → xu hướng tải bệnh viện.

---

## 21. Thống Kê Chi Phí theo Ngày

### Resource chính
**`Claim`** + **`Invoice`**

### Mô tả
Phân tích chi phí theo trục thời gian (ngày). Sử dụng `Claim.created` hoặc `Invoice.date` làm trục ngày. Phân tích: tổng chi phí theo ngày, chi phí BHYT vs. tự trả, chi phí trung bình mỗi lượt khám.

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Encounter` | `Claim.encounter` | Lượt khám phát sinh chi phí |
| `Patient` | `Claim.patient` | Bệnh nhân |
| `Coverage` | `Claim.insurance.coverage` | Phân loại nguồn thanh toán |
| `Organization` | `Claim.provider` | Đơn vị lập hoá đơn |
| `ChargeItem` | `Invoice.lineItem` | Chi tiết dòng phí theo ngày |

### Ghi chú Power BI
- Group `Claim.created` theo ngày → tổng `Claim.total.value`.
- Kết hợp `ClaimResponse` để lấy số tiền thực chi (sau khi BHYT xét duyệt).
- Vẽ Stacked Bar Chart: BHYT + Tự trả + Miễn phí theo ngày.

---

## 22. Điều Trị Nội Trú theo Ngày

### Resource chính
**`Encounter`** (class = IMP)

### Mô tả
Tương tự báo cáo #19 nhưng thêm chiều thời gian theo ngày: số bệnh nhân nội trú mới nhập viện mỗi ngày, số ra viện mỗi ngày, số đang điều trị tại thời điểm cuối ngày (Census).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Thông tin bệnh nhân |
| `Organization` | `Encounter.serviceProvider` | Khoa điều trị |
| `Location` | `Encounter.location` | Giường bệnh |
| `Condition` | `Encounter.diagnosis` | Chẩn đoán nội trú |

### Ghi chú Power BI
- Metric 1 (Nhập viện): `COUNT(Encounter WHERE DATE(period.start) = D AND class = IMP)`
- Metric 2 (Ra viện): `COUNT(Encounter WHERE DATE(period.end) = D AND class = IMP)`
- Metric 3 (Census): `COUNT(Encounter WHERE period.start ≤ D AND (period.end IS NULL OR period.end > D))`
- Vẽ 3 đường trên cùng một Line Chart → phân tích luồng nội trú.

---

## 23. Thống Kê Hồ Sơ KCB theo Ngày Ra Viện

### Resource chính
**`Encounter`** + **`EpisodeOfCare`**

### Mô tả
Thống kê số hồ sơ KCB được đóng (bệnh nhân ra viện) theo từng ngày. `Encounter.period.end` là ngày ra viện. `Encounter.hospitalization.dischargeDisposition` ghi nhận hình thức ra viện (khỏi, chuyển viện, xin về, tử vong...).

### Các Resource liên quan

| Resource | Trường tham chiếu | Vai trò |
|---|---|---|
| `Patient` | `Encounter.subject` | Bệnh nhân ra viện |
| `Organization` | `Encounter.serviceProvider` | Khoa/bệnh viện |
| `Condition` | `Encounter.diagnosis` | Chẩn đoán ra viện (ICD) |
| `Claim` | `Claim.encounter` | Thanh toán khi ra viện |
| `DocumentReference` | `DocumentReference.context.encounter` | Giấy ra viện, tóm tắt bệnh án |
| `MedicationRequest` | `MedicationRequest.encounter` | Đơn thuốc mang về khi ra viện |

### Ghi chú Power BI
- Filter `Encounter.status = finished` và group by `DATE(period.end)`.
- Phân nhóm `dischargeDisposition`: Khỏi bệnh / Đỡ / Nặng hơn / Xin về / Tử vong / Chuyển viện.
- Kết hợp `Condition.code` → chẩn đoán ra viện phổ biến theo ngày.

---

## Tổng Hợp Resource Map

| # | Báo cáo | Resource Chính | Resource Hỗ Trợ Quan Trọng |
|---|---|---|---|
| 1 | Danh mục Bệnh viện | `Organization` | `Location`, `HealthcareService` |
| 2 | Danh mục Khoa | `Organization` (dept) | `Location`, `PractitionerRole` |
| 3 | Danh mục Bệnh ICD | `CodeSystem`, `ValueSet` | `Condition`, `ConceptMap` |
| 4 | Danh mục Nhà thuốc | `Organization` (pharm) | `Location`, `MedicationDispense` |
| 5 | Số giường | `Location` (bed) | `Encounter`, `Organization` |
| 6 | Tổng ngày điều trị | `Encounter` | `Patient`, `Organization`, `Location` |
| 7 | Thống kê chi phí | `Claim`, `Invoice` | `Coverage`, `ChargeItem`, `Encounter` |
| 8 | Lượt BN vào ra | `Encounter` | `Patient`, `Organization`, `Condition` |
| 9 | BN theo loại hình KCB | `Encounter` | `Coverage`, `Organization` |
| 10 | Ca cấp cứu tử vong | `Encounter` (EMER) | `Condition`, `Procedure`, `Patient` |
| 11 | Số hồ sơ KCB | `EpisodeOfCare` | `Encounter`, `Condition`, `Patient` |
| 12 | Thống kê tai nạn | `Condition`, `Encounter` | `Procedure`, `Patient` |
| 13 | Thống kê theo tuổi | `Patient`, `Encounter` | `Condition`, `MedicationRequest` |
| 14 | Thống kê theo khoa | `Encounter` | `Organization`, `Location`, `Claim` |
| 15 | Lượt dịch vụ kỹ thuật | `ServiceRequest`, `Procedure` | `DiagnosticReport`, `Encounter` |
| 16 | Ca mắc theo ICD | `Condition` | `Encounter`, `Patient`, `CodeSystem` |
| 17 | Số đơn thuốc | `MedicationRequest` | `Medication`, `MedicationDispense` |
| 18 | Top 20 bệnh ICD | `Condition` | `Encounter`, `Patient` |
| 19 | Điều trị nội trú | `Encounter` (IMP) | `Condition`, `Procedure`, `Claim`, `Observation` |
| 20 | Ngày điều trị theo ngày | `Encounter` | `Organization`, `Location` |
| 21 | Chi phí theo ngày | `Claim`, `Invoice` | `Coverage`, `ChargeItem` |
| 22 | Nội trú theo ngày | `Encounter` (IMP) | `Patient`, `Organization`, `Location` |
| 23 | Hồ sơ KCB theo ngày ra viện | `Encounter` | `Patient`, `Condition`, `DocumentReference` |

---

## Gợi Ý Kiến Trúc Power BI

### Star Schema khuyến nghị

```
                    DimPatient (Patient)
                         |
DimOrganization ── FactEncounter ── DimCondition (ICD)
(Organization)       (Encounter)         |
     |                   |          DimCodeSystem
DimLocation         FactClaim
(Location)          (Claim/Invoice)
                         |
                    DimCoverage (Coverage)
```

### Các bảng Fact chính
| Fact Table | FHIR Resource | Granularity |
|---|---|---|
| `FactEncounter` | `Encounter` | 1 dòng / lượt khám |
| `FactCondition` | `Condition` | 1 dòng / chẩn đoán |
| `FactClaim` | `Claim` + `ChargeItem` | 1 dòng / dòng phí |
| `FactMedication` | `MedicationRequest` | 1 dòng / dòng thuốc |
| `FactProcedure` | `Procedure` | 1 dòng / thủ thuật |
| `FactServiceRequest` | `ServiceRequest` | 1 dòng / chỉ định |

### Các bảng Dimension chính
| Dimension | FHIR Resource | Mô tả |
|---|---|---|
| `DimPatient` | `Patient` | Nhân khẩu học bệnh nhân |
| `DimOrganization` | `Organization` | Cây bệnh viện → khoa → phòng |
| `DimLocation` | `Location` | Phòng, giường |
| `DimICD` | `CodeSystem` (ICD) | Danh mục bệnh |
| `DimDate` | Tạo thủ công | Calendar table |
| `DimPractitioner` | `Practitioner` | Bác sĩ, điều dưỡng |
| `DimCoverage` | `Coverage` | Loại bảo hiểm |

---

*Tài liệu được tạo dựa trên chuẩn HL7 FHIR R4B (4.3.0) – https://hl7.org/fhir/R4B/*
