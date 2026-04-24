# Mapping Dữ Liệu: QĐ 130/QĐ-BYT + QĐ 4750/QĐ-BYT → HL7 FHIR R4B

> **Mục đích tài liệu:** Ánh xạ từng trường dữ liệu trong các Bảng XML (theo QĐ 130 đã được sửa đổi bổ sung bởi QĐ 4750) sang phần tử tương ứng trong chuẩn HL7 FHIR R4B.  
> **Phạm vi:** 13 Bảng XML (Bảng Check-in + Bảng 1–12)  
> **Chuẩn đích:** HL7 FHIR R4B (4.3.0) — https://hl7.org/fhir/R4B/  
> **Căn cứ pháp lý:** QĐ 130/QĐ-BYT ngày 18/01/2023 + QĐ 4750/QĐ-BYT ngày 29/12/2023  
> **Hiệu lực:** Từ 01/07/2024

---

### Ký hiệu và quy ước

| Ký hiệu | Ý nghĩa |
|---|---|
| 🆕 | Trường **mới hoàn toàn** do QĐ 4750 bổ sung |
| 🔄 | Trường **sửa đổi** kiểu dữ liệu hoặc kích thước theo QĐ 4750 |
| 📝 | Trường **sửa đổi diễn giải/nghiệp vụ** theo QĐ 4750 |
| `R` | Required — bắt buộc trong FHIR |
| `O` | Optional — tùy chọn trong FHIR |
| `C` | Conditional — có điều kiện |
| `1:1` | Ánh xạ trực tiếp một-một |
| `1:N` | Một trường XML → nhiều phần tử FHIR |
| `N:1` | Nhiều trường XML → một phần tử FHIR |
| `CONST` | Giá trị cố định, không lấy từ XML |
| `DERIVE` | Giá trị tính toán/suy luận từ XML |

---

## 1. Bảng Check-in — Trạng thái khám bệnh, chữa bệnh

**FHIR Resource chính ánh xạ:** `Encounter` (trạng thái) + `Patient` (định danh) + `Coverage` (BHYT)

> **Lưu ý nghiệp vụ QĐ 4750:**  
> - Bảng Check-in **chỉ dùng để thông báo trạng thái**, không làm căn cứ giám định/thanh toán.  
> - **Không gửi** khi `MA_DOITUONG_KCB = 2` (cấp cứu).  
> - **Không gửi** khi cơ sở chỉ tiếp nhận mẫu bệnh phẩm để thực hiện CLS.  
> - Gửi ngay sau khi phát sinh chi phí **dịch vụ đầu tiên tại khoa điều trị**.

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | Bắt buộc | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | 130 | `Encounter` | `Encounter.id` | id | R | 1:1 | Mã đợt điều trị duy nhất — PRIMARY KEY liên kết tất cả bảng |
| 2 | `STT` | Số | 10 | 130 | — | — | — | — | — | Số thứ tự gửi dữ liệu, không ánh xạ sang FHIR |
| 3 | `MA_BN` | Chuỗi | 100 | 130 | `Patient` | `Patient.identifier[pid].value` | string | R | 1:1 | system = `https://[cskcb]/patient-id` |
| 4 | `HO_TEN` | Chuỗi | 255 | 130 | `Patient` | `Patient.name[0].text` | string | R | 1:1 | Họ và tên đầy đủ |
| 5 🔄 | `SO_CCCD` | **Chuỗi** | 15 | **4750** | `Patient` | `Patient.identifier[cccd].value` | string | O | 1:1 | **QĐ 4750 đổi Số→Chuỗi** để giữ số 0 đầu. system = `https://moh.gov.vn/cccd` |
| 6 | `NGAY_SINH` | Chuỗi | 12 | 130 | `Patient` | `Patient.birthDate` | date | R | 1:1 | Lấy 8 ký tự đầu (yyyymmdd). `mm=00` hoặc `dd=00` → partial date. Trẻ ≤28 ngày ghi đủ yyyymmddHHMM |
| 7 | `GIOI_TINH` | Số | 1 | 130 | `Patient` | `Patient.gender` | code | R | 1:1 | `1`→`male`; `2`→`female`; `3`→`unknown` |
| 8 | `MA_THE_BHYT` | Chuỗi | 15 | 130 | `Coverage` | `Coverage.identifier[0].value` | string | C | 1:1 | Để trống nếu không KBCB BHYT. 15 ký tự/thẻ |
| 9 | `MA_DKBD` | Chuỗi | 5 | 130 | `Coverage` | `Coverage.class[0].value` | string | C | 1:1 | Mã CSKCB đăng ký ban đầu. Để trống nếu không BHYT |
| 10 | `GT_THE_TU` | Chuỗi | 8 | 130 | `Coverage` | `Coverage.period.start` | date | C | 1:1 | yyyymmdd. Để trống nếu không BHYT |
| 11 | `GT_THE_DEN` | Chuỗi | 8 | 130 | `Coverage` | `Coverage.period.end` | date | C | 1:1 | yyyymmdd. Để trống nếu không BHYT |
| 12 🔄 | `MA_DOITUONG_KCB` | **Chuỗi** | **4** | **4750** | `Coverage` | `Coverage.type.coding.code` | code | R | 1:1 | **QĐ 4750 đổi Số(1)→Chuỗi(4).** Khi =`2` (cấp cứu) → không gửi Bảng Check-in |
| 13 | `NGAY_VAO` | Chuỗi | 12 | 130 | `Encounter` | `Encounter.period.start` | dateTime | R | 1:1 | yyyymmddHHMM → `yyyy-MM-ddTHH:mm:ss+07:00` |
| 14 🆕 | `NGAY_VAO_NOI_TRU` | Chuỗi | 12 | **4750** | `Encounter` | `Encounter.location[0].period.start` | dateTime | C | 1:1 | **Trường mới QĐ 4750.** Thời điểm được chỉ định vào nội trú/ban ngày/ngoại trú. yyyymmddHHMM |
| 15 🆕 | `LY_DO_VNT` | Chuỗi | 1024 | **4750** | `Encounter` | `Encounter.reasonCode[0].text` | string | C | 1:1 | **Trường mới QĐ 4750.** Lý do vào nội trú/ngoại trú. Áp dụng nội trú, ban ngày, ngoại trú |
| 16 🆕 | `MA_LY_DO_VNT` | Chuỗi | 5 | **4750** | `Encounter` | `Encounter.reasonCode[0].coding.code` | code | C | 1:1 | **Trường mới QĐ 4750.** Bắt buộc khi BYT ban hành danh mục mã. system = `https://moh.gov.vn/ly-do-vnt` |
| 17 🔄 | `MA_LOAI_KCB` | **Chuỗi** | 2 | **4750** | `Encounter` | `Encounter.class.code` | code | R | 1:1 | **QĐ 4750 đổi Số→Chuỗi.** `01`→`AMB`; `03`→`IMP`; `04`→`SS`; `09`→`EMER` (xem bảng mapping §A.1) |
| 18 | `MA_CSKCB` | Chuỗi | 5 | 130 | `Encounter` | `Encounter.serviceProvider` | Reference(Organization) | R | 1:1 | → `Organization.identifier.value` |
| 19 📝 | `MA_DICH_VU` | Chuỗi | 50 | **4750** | `Encounter` | `Encounter.serviceType.coding.code` | code | C | 1:1 | **QĐ 4750 sửa diễn giải:** Chỉ ghi khi chi phí đầu tiên tại khoa là DVKT/tiền khám. Để trống nếu chi phí đầu tiên là thuốc hoặc VTYT |
| 20 📝 | `TEN_DICH_VU` | Chuỗi | 1024 | **4750** | `Encounter` | `Encounter.serviceType.text` | string | C | 1:1 | **QĐ 4750 sửa diễn giải:** Tên tương ứng với MA_DICH_VU khi chi phí đầu tiên là DVKT/tiền khám |
| 21 🆕 | `MA_THUOC` | Chuỗi | 255 | **4750** | `MedicationRequest` | `MedicationRequest.medicationCodeableConcept.coding.code` | code | C | 1:1 | **Trường mới QĐ 4750.** Ghi khi chi phí đầu tiên tại khoa là thuốc. Mã hoạt chất theo DMDC BYT |
| 22 🆕 | `TEN_THUOC` | Chuỗi | 1024 | **4750** | `MedicationRequest` | `MedicationRequest.medicationCodeableConcept.text` | string | C | 1:1 | **Trường mới QĐ 4750.** Tên thuốc tương ứng khi chi phí đầu tiên là thuốc |
| 23 🆕 | `MA_VAT_TU` | Chuỗi | 255 | **4750** | `ServiceRequest` | `ServiceRequest.code.coding.code` | code | C | 1:1 | **Trường mới QĐ 4750.** Ghi khi chi phí đầu tiên là VTYT. Mã VTYT theo QĐ 5086/QĐ-BYT |
| 24 🆕 | `TEN_VAT_TU` | Chuỗi | 1024 | **4750** | `ServiceRequest` | `ServiceRequest.code.text` | string | C | 1:1 | **Trường mới QĐ 4750.** Tên VTYT tương ứng |
| 25 | `NGAY_YL` | Chuỗi | 12 | 130 | `ServiceRequest` | `ServiceRequest.authoredOn` | dateTime | R | 1:1 | yyyymmddHHMM → ISO 8601. Thời điểm ra y lệnh |
| 26 🆕 | `DU_PHONG` | Chuỗi | n | **4750** | — | `Encounter.extension[du-phong].valueString` | string | O | 1:1 | **Trường mới QĐ 4750.** Dữ liệu dự phòng |

### Quy tắc chọn trường chi phí đầu tiên (QĐ 4750)

```
Chi phí đầu tiên tại khoa là:
  DVKT hoặc tiền khám → ghi MA_DICH_VU + TEN_DICH_VU; để trống MA_THUOC, TEN_THUOC, MA_VAT_TU, TEN_VAT_TU
  Thuốc               → ghi MA_THUOC   + TEN_THUOC;   để trống MA_DICH_VU, TEN_DICH_VU, MA_VAT_TU, TEN_VAT_TU
  VTYT                → ghi MA_VAT_TU  + TEN_VAT_TU;  để trống MA_DICH_VU, TEN_DICH_VU, MA_THUOC, TEN_THUOC
```

---

## 2. Bảng 1 — Chỉ tiêu tổng hợp khám bệnh, chữa bệnh

**FHIR Resource chính ánh xạ:** `Encounter` · `Patient` · `Coverage` · `Condition` · `Claim`

### 2.1 Nhóm định danh đợt điều trị

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | 130 | `Encounter` | `Encounter.id` | id | R | 1:1 | PRIMARY KEY — liên kết tất cả bảng trong một đợt KBCB |
| 2 | `STT` | Số | 10 | 130 | — | — | — | — | — | Số thứ tự gửi, không ánh xạ |
| 3 | `MA_BN` | Chuỗi | 100 | 130 | `Patient` | `Patient.identifier[pid].value` | string | R | 1:1 | Mã nội bộ CSKCB |
| 63 | `MA_HSBA` | Chuỗi | 100 | 130 | `EpisodeOfCare` | `EpisodeOfCare.identifier[0].value` | string | O | 1:1 | Mã hồ sơ bệnh án / phiếu khám ngoại trú |

### 2.2 Nhóm nhân thân bệnh nhân (STT 4–16, có thay đổi QĐ 4750)

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 4 | `HO_TEN` | Chuỗi | 255 | 130 | `Patient` | `Patient.name[0].text` | string | R | 1:1 | Trẻ sơ sinh chưa có tên: ghi theo TT 30/2020 |
| 5 🔄 | `SO_CCCD` | **Chuỗi** | 15 | **4750** | `Patient` | `Patient.identifier[cccd].value` | string | O | 1:1 | **QĐ 4750: Số→Chuỗi** — giữ số 0 đầu; system = `https://moh.gov.vn/cccd` |
| 6 | `NGAY_SINH` | Chuỗi | 12 | 130 | `Patient` | `Patient.birthDate` | date | R | 1:1 | yyyymmddHHMM. Lấy 8 ký tự đầu; `0000` → partial; trẻ ≤28 ngày ghi đủ |
| 7 | `GIOI_TINH` | Số | 1 | 130 | `Patient` | `Patient.gender` | code | R | 1:1 | `1`→`male`; `2`→`female`; `3`→`unknown` |
| 8 🆕 | `NHOM_MAU` | **Chuỗi** | **5** | **4750** | `Patient` | `Patient.extension[blood-type].valueString` | string | O | 1:1 | **Trường mới QĐ 4750.** Nhóm máu (A/B/AB/O kèm Rh+/-). Ghi khi có thông tin |
| 9 🔄 | `MA_QUOCTICH` | **Chuỗi** | 3 | **4750** | `Patient` | `Patient.extension[nationality].valueCoding.code` | code | O | 1:1 | **QĐ 4750: Số→Chuỗi.** Theo Phụ lục 2 TT 07/2016/TT-BCA. system = `https://moh.gov.vn/nationality` |
| 10 🔄 | `MA_DANTOC` | **Chuỗi** | 2 | **4750** | `Patient` | `Patient.extension[ethnicity].valueCoding.code` | code | O | 1:1 | **QĐ 4750: Số→Chuỗi.** Theo QĐ 121-TCTK/PPCĐ. system = `https://moh.gov.vn/ethnicity` |
| 11 | `MA_NGHE_NGHIEP` | Chuỗi | 5 | 130 | `Patient` | `Patient.extension[occupation].valueCoding.code` | code | O | 1:1 | Theo QĐ 34/2020/QĐ-TTg. `00000` = không nghề |
| 12 🔄 | `DIA_CHI` | **Chuỗi** | 1024 | **4750** | `Patient` | `Patient.address[0].text` | string | O | 1:1 | **QĐ 4750: Số→Chuỗi** (lỗi kiểu DL trong QĐ 130 đã được sửa) |
| 13 | `MATINH_CU_TRU` | Chuỗi | 3 | 130 | `Patient` | `Patient.address[0].state` | string | O | 1:1 | 2 ký tự cuối mã tỉnh theo TT 07/2016/TT-BCA |
| 14 📝 | `MAHUYEN_CU_TRU` | Chuỗi | 3 | **4750** | `Patient` | `Patient.address[0].district` | string | O | 1:1 | **QĐ 4750 bổ sung:** Dùng mã mới khi thành lập/gộp đơn vị hành chính |
| 15 🔄 | `MAXA_CU_TRU` | Chuỗi | **3** | **4750** | `Patient` | `Patient.address[0].postalCode` | string | O | 1:1 | **QĐ 4750 giảm size 5→3.** Bổ sung: dùng mã mới khi thành lập/gộp đơn vị HC |
| 16 🔄 | `DIEN_THOAI` | **Chuỗi** | 15 | **4750** | `Patient` | `Patient.telecom[0].value` | string | O | 1:1 | **QĐ 4750: Số→Chuỗi** — giữ số 0 đầu; system = `phone`; Ghi khi BN cung cấp |

### 2.3 Nhóm thẻ BHYT

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 17 | `MA_THE_BHYT` | Chuỗi | n | 130 | `Coverage` | `Coverage.identifier[0].value` | string | C | 1:N | 15 ký tự/thẻ; nhiều thẻ phân cách `;` → tạo nhiều Coverage |
| 18 | `MA_DKBD` | Chuỗi | n | 130 | `Coverage` | `Coverage.class[0].value` | string | C | 1:1 | 5 ký tự mã CSKCB đăng ký ban đầu; nhiều phân cách `;` |
| 19 | `GT_THE_TU` | Chuỗi | n | 130 | `Coverage` | `Coverage.period.start` | date | C | 1:1 | yyyymmdd; nhiều phân cách `;` tương ứng từng thẻ |
| 20 | `GT_THE_DEN` | Chuỗi | n | 130 | `Coverage` | `Coverage.period.end` | date | C | 1:1 | yyyymmdd; để trống nếu không tra cứu được (QN/HC/LS/XK/CY/CA) |
| 21 | `NGAY_MIEN_CCT` | Chuỗi | 12 | 130 | `Coverage` | `Coverage.costToBeneficiary[0].exception[0].period.start` | dateTime | C | 1:1 | 8 ký tự yyyymmdd nếu có giấy; 12 ký tự yyyymmddHHMM nếu tính tự động |
| 61 | `NAM_NAM_LIEN_TUC` | Chuỗi | 8 | 130 | `Coverage` | `Coverage.extension[5yr-continuous].valueDate` | date | O | 1:1 | yyyymmdd — Ngày đủ 5 năm tham gia BHYT liên tục |
| 58 | `MA_KHUVUC` | Chuỗi | 2 | 130 | `Coverage` | `Coverage.network` | string | O | 1:1 | K1/K2/K3 — khu vực ghi trên thẻ BHYT |
| 31 | `MA_DOITUONG_KCB` | Chuỗi | 3 | 130 | `Coverage` | `Coverage.type.coding.code` | code | R | 1:1 | Đối tượng KBCB theo DMDC BYT *(lưu ý: Bảng 1 giữ Chuỗi(3), Checkin là Chuỗi(4))* |

### 2.4 Nhóm thông tin đợt KBCB

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 56 | `MA_LOAI_KCB` | Số | 2 | 130 | `Encounter` | `Encounter.class.code` | code | R | 1:1 | Xem bảng mapping §A.1 |
| 57 | `MA_KHOA` | Chuỗi | 50 | 130 | `Encounter` | `Encounter.location[].location` | Reference(Location) | O | 1:N | Nhiều khoa phân cách `;` → `Encounter.location[]` |
| 58 | `MA_CSKCB` | Chuỗi | 5 | 130 | `Encounter` | `Encounter.serviceProvider` | Reference(Organization) | R | 1:1 | |
| 35 | `NGAY_VAO` | Chuỗi | 12 | 130 | `Encounter` | `Encounter.period.start` | dateTime | R | 1:1 | yyyymmddHHMM → ISO 8601+07:00 |
| 36 | `NGAY_VAO_NOI_TRU` | Chuỗi | 12 | 130 | `Encounter` | `Encounter.location[0].period.start` | dateTime | C | 1:1 | Thời điểm vào nội trú/ban ngày (có thể sau NGAY_VAO nếu qua cấp cứu) |
| 37 | `NGAY_RA` | Chuỗi | 12 | 130 | `Encounter` | `Encounter.period.end` | dateTime | C | 1:1 | Ngoại trú mạn tính: mặc định 23:59. Tử vong = thời điểm tử vong |
| 39 | `SO_NGAY_DTRI` | Số | 3 | 130 | `Encounter` | `Encounter.length.value` | decimal | O | 1:1 | Đơn vị: ngày. Xem công thức §A.2 |
| 38 | `GIAY_CHUYEN_TUYEN` | Chuỗi | 50 | 130 | `Encounter` | `Encounter.basedOn[0].identifier.value` | string | C | 1:1 | Số giấy chuyển tuyến hoặc giấy hẹn tái khám |
| 32 | `MA_NOI_DI` | Chuỗi | 5 | 130 | `Encounter` | `Encounter.hospitalization.origin` | Reference(Organization) | C | 1:1 | CSKCB chuyển BN đến; để trống nếu không chuyển tuyến |
| 33 | `MA_NOI_DEN` | Chuỗi | 5 | 130 | `Encounter` | `Encounter.hospitalization.destination` | Reference(Organization) | C | 1:1 | CSKCB BN được chuyển đến |
| 34 | `MA_TAI_NAN` | Số | 1 | 130 | `Encounter` | `Encounter.extension[tai-nan].valueCoding.code` | code | C | 1:1 | Phụ lục 4 QĐ 5937/QĐ-BYT. `1`=TNGT; `2`=TNLĐ; `3`=TN sinh hoạt; `4`=Bạo lực |
| 60 | `CAN_NANG` | Chuỗi | 6 | 130 | `Observation` | `Observation.valueQuantity.value` | decimal | O | 1:1 | kg; 2 số thập phân. `Observation.code` = LOINC `29463-7` (body weight) |
| 61 | `CAN_NANG_CON` | Chuỗi | 100 | 130 | `Observation` | `Observation.valueQuantity.value` | decimal | C | 1:N | gram; nhiều con phân cách `;` → nhiều Observation. Chỉ ghi khi sinh con |
| 62 | `NGAY_TAI_KHAM` | Chuỗi | 50 | 130 | `Appointment` | `Appointment.start` | dateTime | O | 1:N | yyyymmdd; nhiều ngày phân cách `;` → nhiều Appointment |
| 65 | `MA_TTDV` | Chuỗi | 10 | 130 | `Encounter` | `Encounter.participant[attender].individual` | Reference(Practitioner) | O | 1:1 | Mã định danh y tế (mã BHXH) người đứng đầu CSKCB hoặc người được ủy quyền |

### 2.5 Nhóm lý do và chẩn đoán

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 22 | `LY_DO_VV` | Chuỗi | n | 130 | `Encounter` | `Encounter.reasonCode[0].text` | string | O | 1:1 | Lý do đến KBCB; thiên tai/dịch bệnh ghi theo hướng dẫn BYT |
| 23 | `LY_DO_VNT` | Chuỗi | n | 130 | `Encounter` | `Encounter.reasonCode[1].text` | string | C | 1:1 | Lý do vào nội trú/ban ngày; có triệu chứng lâm sàng |
| 24 | `MA_LY_DO_VNT` | Chuỗi | 5 | 130 | `Encounter` | `Encounter.reasonCode[1].coding.code` | code | C | 1:1 | Bắt buộc khi BYT ban hành danh mục |
| 25 | `CHAN_DOAN_VAO` | Chuỗi | n | 130 | `Condition` | `Condition.note[0].text` | string | O | 1:1 | Chẩn đoán sơ bộ khi tiếp nhận. `Condition.category` = `encounter-diagnosis` |
| 26 | `CHAN_DOAN_RV` | Chuỗi | n | 130 | `Condition` | `Condition.code.text` | string | R | 1:1 | Chẩn đoán xác định đầy đủ khi ra viện. Mã bệnh dài ngày theo TT 46/2016 |
| 27 | `MA_BENH_CHINH` | Chuỗi | 7 | 130 | `Condition` | `Condition.code.coding[0].code` | code | R | 1:1 | ICD-10 QĐ 4469/QĐ-BYT. system=`http://hl7.org/fhir/sid/icd-10`. 1 mã duy nhất |
| 28 | `MA_BENH_KT` | Chuỗi | 100 | 130 | `Condition` | `Condition.code.coding[N].code` | code | O | 1:N | ICD-10 bệnh kèm; nhiều mã phân cách `;`; tối đa 12 mã → mỗi mã = 1 Condition riêng |
| 29 | `MA_BENH_YHCT` | Chuỗi | 255 | 130 | `Condition` | `Condition.code.coding[].code` | code | O | 1:N | Mã YHCT song song ICD-10. system=`https://moh.gov.vn/yhct`. Split `;` |
| 30 | `MA_PTTT_QT` | Chuỗi | 125 | 130 | `Procedure` | `Procedure.code.coding[0].code` | code | C | 1:N | ICD-9 CM QĐ 4440/QĐ-BYT. Split `;`. Chỉ ghi khi có PT/TT |

### 2.6 Nhóm kết quả điều trị

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 41 | `KET_QUA_DTRI` | Số | 1 | 130 | `Encounter` | `Encounter.hospitalization.dischargeDisposition.coding.code` | code | O | 1:1 | Xem bảng mapping §A.3 |
| 42 | `MA_LOAI_RV` | Số | 1 | 130 | `Encounter` | `Encounter.hospitalization.dischargeDisposition.coding.code` | code | O | N:1 | Kết hợp với KET_QUA_DTRI. Xem §A.3 |
| 40 | `PP_DIEU_TRI` | Chuỗi | n | 130 | `Encounter` | `Encounter.extension[pp-dieu-tri].valueString` | string | O | 1:1 | Phương pháp điều trị theo TT 18/2022 |
| 43 | `GHI_CHU` | Chuỗi | n | 130 | `Encounter` | `Encounter.note[0].text` | string | O | 1:1 | Lời dặn bác sĩ khi ra viện |

### 2.7 Nhóm thanh toán

| STT | Trường XML | Kiểu XML | Size | QĐ | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 44 | `NGAY_TTOAN` | Chuỗi | 12 | 130 | `Claim` | `Claim.created` | dateTime | C | 1:1 | Để trống → chưa thanh toán |
| 45 | `T_THUOC` | Số | 15 | 130 | `Claim` | `Claim.item[nhom-thuoc].net.value` | decimal | O | 1:1 | Tổng THANH_TIEN_BV Bảng 2 (thuốc+oxy+máu+dịch truyền) |
| 46 | `T_VTYT` | Số | 15 | 130 | `Claim` | `Claim.item[nhom-vtyt].net.value` | decimal | O | 1:1 | Tổng THANH_TIEN_BV VTYT từ Bảng 3 |
| 47 | `T_TONGCHI_BV` | Số | 15 | 130 | `Claim` | `Claim.total.value` | decimal | R | 1:1 | Tổng chi phí BV = SUM(B2+B3).THANH_TIEN_BV |
| 48 | `T_TONGCHI_BH` | Số | 15 | 130 | `Claim` | `Claim.item[benefit].adjudication[benefit].amount.value` | decimal | O | 1:1 | Tổng trong phạm vi BHYT = SUM(B2+B3).THANH_TIEN_BH |
| 49 | `T_BNTT` | Số | 15 | 130 | `Invoice` | `Invoice.totalNet.value` | decimal | O | 1:1 | BN tự trả ngoài BHYT |
| 50 | `T_BNCCT` | Số | 15 | 130 | `Coverage` | `Coverage.costToBeneficiary[cct].value.value` | decimal | O | 1:1 | BN cùng chi trả trong BHYT |
| 51 | `T_BHTT` | Số | 15 | 130 | `ClaimResponse` | `ClaimResponse.payment.amount.value` | decimal | R | DERIVE | = T_TONGCHI_BH − T_BNCCT |
| 52 | `T_NGUONKHAC` | Số | 15 | 130 | `Claim` | `Claim.item[other-src].adjudication[other].amount.value` | decimal | O | 1:1 | Tổng nguồn khác (NSNN + viện trợ + trong nước + CL) |
| 53 | `T_BHTT_GDV` | Số | 15 | 130 | `Claim` | `Claim.extension[bhtt-gdv].valueMoney.value` | decimal | O | 1:1 | BHYT ngoài định suất/DRG (MA_PTTT=1) |
| 54 | `NAM_QT` | Số | 4 | 130 | `Claim` | `Claim.billablePeriod.start` (năm) | date | R | N:1 | Kết hợp với THANG_QT → `yyyy-MM-01` |
| 55 | `THANG_QT` | Số | 2 | 130 | `Claim` | `Claim.billablePeriod.start` (tháng) | date | R | N:1 | |
| 66 | `DU_PHONG` | Chuỗi | n | 130 | — | `Encounter.extension[du-phong].valueString` | string | O | 1:1 | Trường dự phòng khi cần thiết |

---

## 3. Bảng 2 — Chỉ tiêu chi tiết thuốc

**FHIR Resource chính ánh xạ:** `MedicationRequest` · `Medication`

> Bảng 2 **không bị sửa đổi** bởi QĐ 4750 — toàn bộ giữ nguyên theo QĐ 130.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `MedicationRequest` | `MedicationRequest.encounter` | Reference(Encounter) | R | N:1 | Liên kết về Bảng 1 |
| 2 | `STT` | Số | 10 | — | — | — | — | — | Số thứ tự, không ánh xạ |
| 3 | `MA_THUOC` | Chuỗi | 255 | `Medication` | `Medication.code.coding[0].code` | code | R | 1:1 | Mã hoạt chất DMDC BYT. Nhiều HĐ phân cách `+` → `Medication.ingredient[]`. Mã đặc biệt: `40.17`=Oxy; `40.573`=NO; `VM.XXXXX`=vận chuyển máu; `BB.XXXXX`=bao bì thuốc thang |
| 4 | `MA_PP_CHEBIEN` | Chuỗi | 255 | `Medication` | `Medication.extension[pp-che-bien].valueCodeableConcept.code` | code | C | 1:1 | Chỉ áp dụng thuốc cổ truyền. Nhiều PP phân cách `;` |
| 5 | `MA_CSKCB_THUOC` | Chuỗi | 10 | `MedicationRequest` | `MedicationRequest.extension[cskcb-thuoc].valueString` | string | C | 1:1 | Chỉ trường hợp đặc biệt: `C.XXXXX`=chuyển thuốc thiên tai; `K.XXXXX`=ngoài giá CLS; `M.XXXXX`=máu |
| 6 | `MA_NHOM` | Số | 2 | `MedicationRequest` | `MedicationRequest.category[0].coding.code` | code | R | 1:1 | Nhóm chi phí Phụ lục 3 QĐ 5937/QĐ-BYT |
| 7 | `TEN_THUOC` | Chuỗi | 1024 | `Medication` | `Medication.code.text` | string | R | 1:1 | Tên theo số ĐKLH Cục QLD/YDCT |
| 8 | `DON_VI_TINH` | Chuỗi | 50 | `MedicationRequest` | `MedicationRequest.dispenseRequest.quantity.unit` | string | R | 1:1 | Đơn vị nhỏ nhất; chai/lọ chia theo UI/ml → ghi UI/ml |
| 9 | `HAM_LUONG` | Chuỗi | 1024 | `Medication` | `Medication.ingredient[0].strength.numerator.value` | string | O | 1:N | Nhiều HĐ phân cách `+` → `ingredient[]` |
| 10 | `DUONG_DUNG` | Chuỗi | 4 | `MedicationRequest` | `MedicationRequest.dosageInstruction[0].route.coding.code` | code | R | 1:1 | PO/IV/IM/SC/... Theo ĐKLH |
| 11 | `DANG_BAO_CHE` | Chuỗi | 1024 | `Medication` | `Medication.form.text` | string | O | 1:1 | Dạng bào chế theo ĐKLH |
| 12 | `LIEU_DUNG` | Chuỗi | 1024 | `MedicationRequest` | `MedicationRequest.dosageInstruction[0].text` | string | O | 1:1 | Ngoại trú: SL/lần×lần/ngày×ngày; Nội trú: SL/lần×lần/ngày×1ngày |
| 13 | `CACH_DUNG` | Chuỗi | 1024 | `MedicationRequest` | `MedicationRequest.dosageInstruction[0].additionalInstruction[0].text` | string | O | 1:1 | Lời dặn trên đơn thuốc |
| 14 | `SO_DANG_KY` | Chuỗi | 255 | `Medication` | `Medication.extension[so-dang-ky].valueString` | string | C | 1:1 | Số ĐKLH; không bắt buộc: Oxy, NO, máu, thuốc thang, phóng xạ. Tự bào chế: `HD./CP./VT.{maBV}.{năm}.{STT}` |
| 15 | `TT_THAU` | Chuỗi | 50 | `MedicationRequest` | `MedicationRequest.extension[tt-thau].valueString` | string | R | 1:1 | Số QĐ;Gi;Ni;Năm. Áp thầu thêm mã đơn vị. Tự bào chế: số văn bản;XXXX |
| 16 | `PHAM_VI` | Số | 1 | `MedicationRequest` | `MedicationRequest.extension[pham-vi].valueCoding.code` | code | R | 1:1 | `1`=trong BHYT; `2`=ngoài BHYT; `3`=quân đội/CA (NĐ 70/2015) |
| 17 | `TYLE_TT_BH` | Số | 3 | `Coverage` | `Coverage.costToBeneficiary[tyle-bh].value.value` | decimal | R | 1:1 | % nguyên dương. Không quy định=100; ngoài BHYT=0 |
| 18 | `SO_LUONG` | Số | 10 | `MedicationRequest` | `MedicationRequest.dispenseRequest.quantity.value` | decimal | R | 1:1 | 3 chữ số thập phân; dấu `.` |
| 19 | `DON_GIA` | Số | 15 | `MedicationRequest` | `MedicationRequest.dispenseRequest.unitPrice.value` | decimal | R | 1:1 | Giá hóa đơn mua vào; 3 chữ số thập phân |
| 20 | `THANH_TIEN_BV` | Số | 15 | `Claim` | `Claim.item[].net.value` | decimal | R | DERIVE | = SO_LUONG × DON_GIA |
| 21 | `THANH_TIEN_BH` | Số | 15 | `Claim` | `Claim.item[].adjudication[benefit].amount.value` | decimal | R | DERIVE | = SO_LUONG × DON_GIA × TYLE_TT_BH/100 |
| 22 | `T_NGUONKHAC_NSNN` | Số | 15 | `Claim` | `Claim.item[].adjudication[nsnn].amount.value` | decimal | O | 1:1 | Ngân sách nhà nước TW/ĐP |
| 23 | `T_NGUONKHAC_VTNN` | Số | 15 | `Claim` | `Claim.item[].adjudication[vtnn].amount.value` | decimal | O | 1:1 | Tổ chức/cá nhân ngoài lãnh thổ VN |
| 24 | `T_NGUONKHAC_VTTN` | Số | 15 | `Claim` | `Claim.item[].adjudication[vttn].amount.value` | decimal | O | 1:1 | Tổ chức/cá nhân trong lãnh thổ VN |
| 25 | `T_NGUONKHAC_CL` | Số | 15 | `Claim` | `Claim.item[].adjudication[other-src].amount.value` | decimal | O | 1:1 | Nguồn khác còn lại |
| 26 | `T_NGUONKHAC` | Số | 15 | `Claim` | `Claim.item[].adjudication[total-other].amount.value` | decimal | O | DERIVE | = NSNN + VTNN + VTTN + CL |
| 27 | `MUC_HUONG` | Số | 3 | `Coverage` | `Coverage.costToBeneficiary[muc-huong].type.coding.code` | code | R | 1:1 | Đúng tuyến: 80/95/100. Trái tuyến: mức × tỷ lệ trái tuyến. Miễn CCT=100 |
| 28 | `T_BNTT` | Số | 15 | `Invoice` | `Invoice.lineItem[].priceComponent[self-pay].amount.value` | decimal | R | DERIVE | BN tự trả ngoài BHYT; xem công thức §B.1 |
| 29 | `T_BNCCT` | Số | 15 | `Coverage` | `Coverage.costToBeneficiary[cct].value.value` | decimal | R | DERIVE | BN cùng chi trả; xem công thức §B.1 |
| 30 | `T_BHTT` | Số | 15 | `ClaimResponse` | `ClaimResponse.addItem[].adjudication[benefit].amount.value` | decimal | R | DERIVE | BHXH thanh toán; xem công thức §B.1 |
| 31 | `MA_KHOA` | Chuỗi | 15 | `MedicationRequest` | `MedicationRequest.dispenseRequest.performer` | Reference(Organization) | O | 1:1 | Khoa chỉ định thuốc |
| 32 | `MA_BAC_SI` | Chuỗi | 255 | `MedicationRequest` | `MedicationRequest.requester` | Reference(Practitioner) | O | 1:N | Mã định danh y tế; split `;`. BS tuyến trên + nhân viên cấp thuốc phân cách `;` |
| 33 | `MA_DICH_VU` | Chuỗi | 255 | `ServiceRequest` | `ServiceRequest.code.coding.code` | code | C | 1:1 | Bắt buộc khi thuốc dùng trong DVKT tính riêng; XN ngoài giá máu; thuốc ngoài giá CLS. Cấu trúc đặc biệt `XX.YYYY.ZZZZ.K.WWWWW`; `_GT`; `_TB`; `0000` |
| 34 | `NGAY_YL` | Chuỗi | 12 | `MedicationRequest` | `MedicationRequest.authoredOn` | dateTime | R | 1:1 | Ngày nghỉ → mặc định ngày làm việc liền kề trước (trừ cấp cứu) |
| 35 | `MA_PTTT` | Số | 1 | `Claim` | `Claim.type.extension[pttt].valueCoding.code` | code | R | 1:1 | `1`=Phí dịch vụ; `2`=Định suất; `3`=DRG |
| 36 | `NGUON_CTRA` | Số | 1 | `MedicationRequest` | `MedicationRequest.extension[nguon-ctra].valueCoding.code` | code | R | 1:1 | `1`=BHYT; `2`=Dự án/viện trợ; `3`=CT mục tiêu QG; `4`=Khác |
| 37 | `VET_THUONG_TP` | Số | 1 | `MedicationRequest` | `MedicationRequest.extension[vet-thuong-tp].valueBoolean` | boolean | C | 1:1 | `1`=thuốc điều trị vết thương tái phát thương binh/bệnh binh |
| 38 | `DU_PHONG` | Chuỗi | n | — | `MedicationRequest.extension[du-phong].valueString` | string | O | 1:1 | Dự phòng |

---

## 4. Bảng 3 — Chỉ tiêu chi tiết dịch vụ kỹ thuật và vật tư y tế

**FHIR Resource chính ánh xạ:** `ServiceRequest` · `Procedure` · `Device` · `Location`

> Bảng 3 **không bị sửa đổi** bởi QĐ 4750 — toàn bộ giữ nguyên theo QĐ 130.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `ServiceRequest` | `ServiceRequest.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `STT` | Số | 10 | — | — | — | — | — | |
| 3 | `MA_DICH_VU` | Chuỗi | 50 | `ServiceRequest` | `ServiceRequest.code.coding[0].code` | code | R | 1:1 | DMDC BYT. `VC.XXXXX`=vận chuyển BN; `XX.YYYY.ZZZZ.K.WWWWW`=chuyển mẫu; `_GT`=gây tê; `_TB`=không hoàn thành; `XX.YYYY.0000`=chưa có giá |
| 4 | `MA_PTTT_QT` | Chuỗi | 255 | `Procedure` | `Procedure.code.coding[0].code` | code | C | 1:N | ICD-9 CM QĐ 4440/QĐ-BYT; split `;` |
| 5 | `MA_VAT_TU` | Chuỗi | 255 | `Device` | `Device.identifier[0].value` | string | C | 1:1 | Mã VTYT đến kích thước cụ thể; cấp tự động Cổng BHXH (QĐ 5086/QĐ-BYT). Chỉ VTYT chưa trong cơ cấu giá |
| 6 | `MA_NHOM` | Số | 2 | `ChargeItem` | `ChargeItem.code.coding.code` | code | R | 1:1 | Nhóm chi phí Phụ lục 3 QĐ 5937 |
| 7 | `GOI_VTYT` | Chuỗi | 3 | `ChargeItem` | `ChargeItem.extension[goi-vtyt].valueString` | string | C | 1:1 | G1/G2/... — Gói VTYT theo lần thực hiện DVKT |
| 8 | `TEN_VAT_TU` | Chuỗi | 1024 | `Device` | `Device.deviceName[0].name` | string | C | 1:1 | Tên thương mại VTYT |
| 9 | `TEN_DICH_VU` | Chuỗi | 1024 | `ServiceRequest` | `ServiceRequest.code.text` | string | R | 1:1 | Gây tê → bổ sung `[gây tê]`; chi tiết trong `[]` |
| 10 | `MA_XANG_DAU` | Chuỗi | 20 | `ServiceRequest` | `ServiceRequest.extension[xang-dau].valueCoding.code` | code | C | 1:1 | Chỉ dùng khi vận chuyển BN |
| 11 | `DON_VI_TINH` | Chuỗi | 50 | `ChargeItem` | `ChargeItem.quantity.unit` | string | R | 1:1 | |
| 12 | `PHAM_VI` | Số | 1 | `ServiceRequest` | `ServiceRequest.extension[pham-vi].valueCoding.code` | code | R | 1:1 | `1`=trong BHYT; `2`=ngoài; `3`=quân đội/CA |
| 13 | `SO_LUONG` | Số | 10 | `ServiceRequest` | `ServiceRequest.quantity.value` | decimal | R | 1:1 | 3 chữ số thập phân |
| 14 | `DON_GIA_BV` | Số | 15 | `ChargeItem` | `ChargeItem.priceOverride.value` | decimal | R | 1:1 | 3 chữ số thập phân. VTYT tái sử dụng: DON_GIA_BV = DON_GIA_BH |
| 15 | `DON_GIA_BH` | Số | 15 | `ChargeItem` | `ChargeItem.extension[don-gia-bh].valueMoney.value` | decimal | R | 1:1 | Giá BHYT; VTYT tái sử dụng: gồm chi phí tái sử dụng |
| 16 | `TT_THAU` | Chuỗi | 25 | `ServiceRequest` | `ServiceRequest.extension[tt-thau].valueString` | string | R | 1:1 | Số QĐ.Mã đơn vị;Gi;Ni;XXXX. TTMSTT=`00`. VTYT trước TT 14/2020: Số QĐ.Mã;Gi;XXXX |
| 17 | `TYLE_TT_DV` | Số | 3 | `ChargeItem` | `ChargeItem.extension[tyle-tt-dv].valueDecimal` | decimal | C | 1:1 | Tỷ lệ đặc biệt: nằm ghép/khám nhiều lần/PT nhiều can thiệp. Xem §B.2 |
| 18 | `TYLE_TT_BH` | Số | 3 | `Coverage` | `Coverage.costToBeneficiary[tyle-bh].value.value` | decimal | R | 1:1 | % BHYT; không quy định=100; ngoài BHYT=0 |
| 19 | `THANH_TIEN_BV` | Số | 15 | `Claim` | `Claim.item[].net.value` | decimal | R | DERIVE | = SO_LUONG × DON_GIA_BV |
| 20 | `THANH_TIEN_BH` | Số | 15 | `Claim` | `Claim.item[].adjudication[benefit].amount.value` | decimal | R | DERIVE | Thường: SO_LUONG × DON_GIA_BH × TYLE_TT_BH/100. Có TYLE_TT_DV: × TYLE_TT_DV/100 thêm. Xem §B.2 |
| 21 | `T_TRANTT` | Số | 15 | `Claim` | `Claim.item[].extension[tran-tt].valueMoney.value` | decimal | C | 1:1 | Trần 45 tháng lương cơ sở VTYT (TT 04/2017). Để trống nếu không có |
| 22 | `MUC_HUONG` | Số | 3 | `Coverage` | `Coverage.costToBeneficiary[muc-huong].type.coding.code` | code | R | 1:1 | Như Bảng 2 |
| 23 | `T_NGUONKHAC_NSNN` | Số | 15 | `Claim` | `Claim.item[].adjudication[nsnn].amount.value` | decimal | O | 1:1 | Tiền ngân sách nhà nước TW/ĐP hỗ trợ |
| 24 | `T_NGUONKHAC_VTNN` | Số | 15 | `Claim` | `Claim.item[].adjudication[vtnn].amount.value` | decimal | O | 1:1 | Tiền tổ chức/cá nhân ngoài lãnh thổ VN |
| 25 | `T_NGUONKHAC_VTTN` | Số | 15 | `Claim` | `Claim.item[].adjudication[vttn].amount.value` | decimal | O | 1:1 | Tiền tổ chức/cá nhân trong lãnh thổ VN |
| 26 | `T_NGUONKHAC_CL` | Số | 15 | `Claim` | `Claim.item[].adjudication[other-src].amount.value` | decimal | O | 1:1 | Nguồn khác còn lại (không thuộc NSNN, VTNN, VTTN) |
| 27 | `T_NGUONKHAC` | Số | 15 | `Claim` | `Claim.item[].adjudication[total-other].amount.value` | decimal | O | DERIVE | = NSNN + VTNN + VTTN + CL |
| 28 | `T_BNTT` | Số | 15 | `Invoice` | `Invoice.lineItem[].priceComponent[self-pay].amount.value` | decimal | R | DERIVE | Xem §B.2 |
| 29 | `T_BNCCT` | Số | 15 | `Coverage` | `Coverage.costToBeneficiary[cct].value.value` | decimal | R | DERIVE | |
| 30 | `T_BHTT` | Số | 15 | `ClaimResponse` | `ClaimResponse.addItem[].adjudication[benefit].amount.value` | decimal | R | DERIVE | |
| 31 | `MA_KHOA` | Chuỗi | 20 | `ServiceRequest` | `ServiceRequest.performer[0]` | Reference(Organization) | O | 1:1 | Khoa cung cấp DVKT/VTYT/giường |
| 32 | `MA_GIUONG` | Chuỗi | 50 | `Location` | `Location.identifier[0].value` | string | C | 1:N | 4 ký tự. H=KH; T=kê thêm; C=tự chọn; K=khác. Nhiều giường split `;` → nhiều Location |
| 33 | `MA_BAC_SI` | Chuỗi | 255 | `ServiceRequest` | `ServiceRequest.requester` | Reference(Practitioner) | O | 1:1 | Huy động phòng dịch: `MA_BAC_SI.C.XXXXX` |
| 34 | `NGUOI_THUC_HIEN` | Chuỗi | 255 | `Procedure` | `Procedure.performer[0].actor` | Reference(Practitioner) | O | 1:N | Split `;` → nhiều performer |
| — | `MA_BENH` | Chuỗi | 100 | `ServiceRequest` | `ServiceRequest.reasonCode[0].coding.code` | code | C | 1:1 | ICD-10 bệnh cần DVKT bổ sung (ngoài bệnh chính). Trống → điều trị bệnh chính |
| — | `MA_BENH_YHCT` | Chuỗi | 255 | `ServiceRequest` | `ServiceRequest.reasonCode[0].extension[yhct].valueCoding.code` | code | C | 1:1 | |
| 35 | `NGAY_YL` | Chuỗi | 12 | `ServiceRequest` | `ServiceRequest.authoredOn` | dateTime | R | 1:1 | Giường bệnh: ngày bắt đầu/thay đổi loại. VTYT: ngày PT/TT có dùng |
| 36 | `NGAY_TH_YL` | Chuỗi | 12 | `Procedure` | `Procedure.performedDateTime` | dateTime | O | 1:1 | Thời điểm thực hiện y lệnh |
| 37 | `NGAY_KQ` | Chuỗi | 12 | `Procedure` | `Procedure.performedPeriod.end` | dateTime | C | 1:1 | PT/TT: kết thúc; giường: kết thúc từng loại. Sau 7 ngày: nhập Cổng BHXH (tối đa 30 ngày) |
| 38 | `MA_PTTT` | Số | 1 | `Claim` | `Claim.type.extension[pttt].valueCoding.code` | code | R | 1:1 | Như Bảng 2 |
| 39 | `VET_THUONG_TP` | Số | 1 | `ServiceRequest` | `ServiceRequest.extension[vet-thuong-tp].valueBoolean` | boolean | C | 1:1 | Như Bảng 2 |
| 40 | `PP_VO_CAM` | Số | 1 | `Procedure` | `Procedure.extension[pp-vo-cam].valueCoding.code` | code | C | 1:1 | Bắt buộc khi PT/TT. `1`=Mê; `2`=Tê; `3`=Châm tê; `4`=Khác |
| 41 | `VI_TRI_TH_DVKT` | Số | 3 | `Procedure` | `Procedure.bodySite[0].coding.code` | code | C | 1:1 | Khi BYT ban hành danh mục vị trí cơ thể |
| 42 | `MA_MAY` | Chuỗi | 1024 | `Device` | `Device.identifier[serial].value` | string | C | 1:1 | Format: `XX.n.YYYYY.Z`. XX=nhóm máy; n=nguồn KP (1=NSNN;2=XHH;3=khác); YYYYY=mã BV; Z=serial. Nhiều serial split `;` |
| 43 | `MA_HIEU_SP` | Chuỗi | 255 | `Device` | `Device.identifier[model].value` | string | C | 1:1 | Model/Serial/IMEI trên VTYT; bắt buộc khi có |
| 44 | `TAI_SU_DUNG` | Số | 1 | `Device` | `Device.extension[tai-su-dung].valueBoolean` | boolean | C | 1:1 | `1`=tái sử dụng |
| 45 | `DU_PHONG` | Chuỗi | n | — | `ServiceRequest.extension[du-phong].valueString` | string | O | 1:1 | |

---

## 5. Bảng 4 — Chỉ tiêu chi tiết dịch vụ cận lâm sàng

**FHIR Resource chính ánh xạ:** `DiagnosticReport` · `Observation`

> Bảng 4 **không bị sửa đổi** bởi QĐ 4750. Chỉ gửi khi người bệnh có thực hiện CLS.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `DiagnosticReport` | `DiagnosticReport.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `STT` | Số | 10 | — | — | — | — | — | |
| 3 | `MA_DICH_VU` | Chuỗi | 15 | `DiagnosticReport` | `DiagnosticReport.code.coding[0].code` | code | R | 1:1 | Phụ lục 1 QĐ 7603/QĐ-BYT |
| 4 | `MA_CHI_SO` | Chuỗi | 50 | `Observation` | `Observation.code.coding[0].code` | code | R | 1:1 | Phụ lục 11 QĐ 7603/QĐ-BYT. Mỗi chỉ số = 1 Observation |
| 5 | `TEN_CHI_SO` | Chuỗi | 255 | `Observation` | `Observation.code.text` | string | R | 1:1 | |
| 6 | `GIA_TRI` | Chuỗi | 50 | `Observation` | `Observation.valueQuantity.value` / `Observation.valueString` | decimal / string | C | 1:1 | Nếu parse được số+đơn vị → `valueQuantity`; còn lại → `valueString`. Để trống nếu chưa có KQ |
| 7 | `DON_VI_DO` | Chuỗi | 50 | `Observation` | `Observation.valueQuantity.unit` | string | C | 1:1 | Phụ lục 11; không có đơn vị → để trống |
| 8 | `MO_TA` | Chuỗi | n | `DiagnosticReport` | `DiagnosticReport.presentedForm[0].data` | base64Binary | C | 1:1 | Mô tả của người đọc. Để trống nếu chưa có KQ |
| 9 | `KET_LUAN` | Chuỗi | n | `DiagnosticReport` | `DiagnosticReport.conclusion` | string | C | 1:1 | Kết luận đọc KQ |
| 10 | `NGAY_KQ` | Chuỗi | 12 | `DiagnosticReport` | `DiagnosticReport.issued` | instant | C | 1:1 | yyyymmddHHMM. Sau 7 ngày: nhập Cổng BHXH; tối đa 30 ngày từ ra viện |
| 11 | `MA_BS_DOC_KQ` | Chuỗi | 255 | `DiagnosticReport` | `DiagnosticReport.resultsInterpreter[0]` | Reference(Practitioner) | O | 1:1 | Mã định danh y tế người đọc/duyệt KQ |
| 12 | `DU_PHONG` | Chuỗi | n | — | Extension | string | O | 1:1 | |

---

## 6. Bảng 5 — Chỉ tiêu chi tiết diễn biến lâm sàng

**FHIR Resource chính ánh xạ:** `ClinicalImpression` · `Procedure` (PT/TT)

> Bảng 5 **không bị sửa đổi** bởi QĐ 4750.  
> Chỉ gửi khi: ngoại trú (MA_LOAI_KCB ∈ {02,05,08}), nội trú, ban ngày, lưu TYT xã, nội trú dưới 4 giờ.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `ClinicalImpression` | `ClinicalImpression.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `STT` | Số | 10 | — | — | — | — | — | |
| 3 | `DIEN_BIEN_LS` | Chuỗi | n | `ClinicalImpression` | `ClinicalImpression.note[0].text` | string | R | 1:1 | Diễn biến lâm sàng và/hoặc nội dung chăm sóc |
| 4 | `GIAI_DOAN_BENH` | Chuỗi | n | `Condition` | `Condition.stage[0].summary.text` | string | C | 1:1 | Khi cơ sở đã xác định giai đoạn bệnh |
| 5 | `HOI_CHAN` | Chuỗi | n | `ClinicalImpression` | `ClinicalImpression.investigation[0].item[0].display` | string | C | 1:1 | Kết quả hội chẩn |
| 6 | `PHAU_THUAT` | Chuỗi | n | `Procedure` | `Procedure.note[0].text` | string | C | 1:1 | Mô tả cách thức PT/TT |
| 7 | `THOI_DIEM_DBLS` | Chuỗi | 12 | `ClinicalImpression` | `ClinicalImpression.date` | dateTime | R | 1:1 | yyyymmddHHMM → ISO 8601 |
| 8 | `NGUOI_THUC_HIEN` | Chuỗi | 255 | `ClinicalImpression` | `ClinicalImpression.assessor` | Reference(Practitioner) | O | 1:1 | Ghi người thực hiện chính trước; split `;` → lấy đầu tiên |
| 9 | `DU_PHONG` | Chuỗi | n | — | Extension | string | O | 1:1 | |

---

## 7. Bảng 6 — Chỉ tiêu hồ sơ bệnh án HIV/AIDS

**FHIR Resource chính ánh xạ:** `EpisodeOfCare` · `CarePlan` · `Observation` · `MedicationRequest`

> Bảng 6 **không bị sửa đổi** bởi QĐ 4750.  
> Gửi đồng thời lên Cổng BHXH (TT 48/2017) **và** Cổng HMED (https://dieutri.arv.vn).

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `EpisodeOfCare` | `EpisodeOfCare.id` | id | R | 1:1 | |
| 2 | `MA_THE_BHYT` | Chuỗi | n | `Coverage` | `Coverage.identifier[0].value` | string | C | 1:N | Như Bảng 1 |
| 3 | `SO_CCCD` | Số | 15 | `Patient` | `Patient.identifier[cccd].value` | string | O | 1:1 | |
| 4 | `NGAYKD_HIV` | Chuỗi | 8 | `Condition` | `Condition.onsetDateTime` | dateTime | C | 1:1 | yyyymmdd. Để trống nếu điều trị phơi nhiễm |
| 5 | `BDDT_ARV` | Chuỗi | 8 | `MedicationRequest` | `MedicationRequest.authoredOn` | dateTime | C | 1:1 | yyyymmdd — ngày đầu tiên nhận ARV trong chương trình |
| 6 | `MA_PHAC_DO_DIEU_TRI_BD` | Chuỗi | 200 | `MedicationRequest` | `MedicationRequest.extension[phac-do-bd].valueString` | string | O | 1:1 | Phụ lục 10 QĐ 5937/QĐ-BYT |
| 7 | `MA_BAC_PHAC_DO_BD` | Số | 1 | `MedicationRequest` | `MedicationRequest.extension[bac-phac-do-bd].valueCoding.code` | code | C | 1:1 | `1`=bậc1; `2`=bậc2; `3`=bậc3. Khi PĐ = "Khác" |
| 8 | `MA_LYDO_DTRI` | Số | 1 | `EpisodeOfCare` | `EpisodeOfCare.extension[ly-do-dk].valueCoding.code` | code | R | 1:1 | `1`=Mới ĐK; `2`=Chưa ARV CĐ; `3`=Đã ARV CĐ; `4`=Đã ARV điều trị lại; `5`=Chưa ARV ĐK lại |
| 9 | `LOAI_DTRI_LAO` | Số | 1 | `Condition` | `Condition.extension[loai-dtri-lao].valueCoding.code` | code | R | 1:1 | `0`=Không; `1`=Lao tiềm ẩn; `2`=Lao; `3`=Lao kháng thuốc |
| 10 | `PHACDO_DTRI_LAO` | Số | 2 | `MedicationRequest` | `MedicationRequest.extension[phac-do-lao].valueCoding.code` | code | C | 1:1 | Mã 1–5: PĐ lao; Mã 6–12: PĐ lao tiềm ẩn |
| 11 | `NGAYBD_DTRI_LAO` | Chuỗi | 8 | `MedicationRequest` | `MedicationRequest.dispenseRequest.validityPeriod.start` | date | C | 1:1 | yyyymmdd |
| 12 | `NGAYKT_DTRI_LAO` | Chuỗi | 8 | `MedicationRequest` | `MedicationRequest.dispenseRequest.validityPeriod.end` | date | C | 1:1 | yyyymmdd. Để trống nếu chưa kết thúc |
| 13 | `MA_LYDO_XNTL_VR` | Số | 1 | `Observation` | `Observation.extension[ly-do-xn].valueCoding.code` | code | C | 1:1 | `1`=Thường quy; `2`=Nghi thất bại; `3`=Khác |
| 14 | `NGAY_XN_TLVR` | Chuỗi | 8 | `Observation` | `Observation.effectiveDateTime` | dateTime | C | 1:1 | yyyymmdd — ngày lấy mẫu TLVR |
| 15 | `KQ_XNTL_VR` | Số | 1 | `Observation` | `Observation.valueCodeableConcept.coding.code` | code | C | 1:1 | `1`=KPH; `2`=<50; `3`=50–<200; `4`=200–1000; `5`=>1000 bản sao/ml |
| 16 | `NGAY_KQ_XN_TLVR` | Chuỗi | 8 | `Observation` | `Observation.issued` | instant | C | 1:1 | yyyymmdd |
| 17 | `MA_LOAI_BN` | Số | 1 | `EpisodeOfCare` | `EpisodeOfCare.type[0].coding.code` | code | R | 1:1 | `1`=Nhiễm HIV; `2`=Trẻ phơi nhiễm; `3`=PrEP; `4`=PEP; `5`=Khác |
| 18 | `MA_TINH_TRANG_DK` | Chuỗi | 18 | `EpisodeOfCare` | `EpisodeOfCare.extension[tinh-trang].valueString` | string | O | 1:1 | Nhiều mã phân cách `;` (thai, lao, viêm gan, nghiện chích...) |
| 19 | `LAN_XN_PCR` | Số | 1 | `Observation` | `Observation.extension[lan-xn-pcr].valueInteger` | integer | C | 1:1 | Chỉ trẻ <18 tháng phơi nhiễm |
| 20 | `NGAY_XN_PCR` | Chuỗi | 8 | `Observation` | `Observation.effectiveDateTime` (PCR) | dateTime | C | 1:1 | yyyymmdd; chỉ trẻ <18 tháng |
| 21 | `NGAY_KQ_XN_PCR` | Chuỗi | 8 | `Observation` | `Observation.issued` (PCR) | instant | C | 1:1 | yyyymmdd |
| 22 | `MA_KQ_XN_PCR` | Số | 1 | `Observation` | `Observation.valueBoolean` | boolean | C | 1:1 | `0`=Âm tính; `1`=Dương tính |
| 23 | `NGAY_NHAN_TT_MANG_THAI` | Chuỗi | 8 | `Condition` | `Condition.extension[ngay-mang-thai].valueDate` | date | C | 1:1 | yyyymmdd |
| 24 | `NGAY_BAT_DAU_DT_CTX` | Chuỗi | 8 | `MedicationRequest` | `MedicationRequest.authoredOn` (CTX) | dateTime | C | 1:1 | yyyymmdd |
| 25 | `MA_XU_TRI` | Số | 1 | `CarePlan` | `CarePlan.activity[].detail.code.coding.code` | code | R | 1:N | `1`=ARV; `2`=Lao; `3`=DPhòng lao; `4`=CTX; `5`=PLTMC; `6`=Viêm gan; `7`=Khác; nhiều split `;` |
| 26 | `NGAY_BAT_DAU_XU_TRI` | Chuỗi | 8 | `CarePlan` | `CarePlan.period.start` | date | R | 1:1 | yyyymmdd — ngày bắt đầu đợt ARV |
| 27 | `NGAY_KET_THUC_XU_TRI` | Chuỗi | 8 | `CarePlan` | `CarePlan.period.end` | date | R | 1:1 | yyyymmdd |
| 28 | `MA_PHAC_DO_DIEU_TRI` | Chuỗi | 200 | `MedicationRequest` | `MedicationRequest.extension[phac-do-hientai].valueString` | string | R | 1:1 | Phụ lục 10 QĐ 5937 — phác đồ đợt này |
| 29 | `MA_BAC_PHAC_DO` | Số | 1 | `MedicationRequest` | `MedicationRequest.extension[bac-phac-do].valueCoding.code` | code | C | 1:1 | Khi PĐ = "Khác" |
| 30 | `SO_NGAY_CAP_THUOC_ARV` | Số | 3 | `MedicationRequest` | `MedicationRequest.dispenseRequest.validityPeriod` | Period | R | DERIVE | ≤ NGAYKT − NGAYBD (số ngày) |
| 31 | `DU_PHONG` | Chuỗi | n | — | Extension | string | O | 1:1 | |

---

## 8. Bảng 7 — Chỉ tiêu dữ liệu giấy ra viện

**FHIR Resource chính ánh xạ:** `DocumentReference` (type=`discharge-summary`) · `Encounter`

> Bảng 7 **không bị sửa đổi** bởi QĐ 4750. Sinh đôi/nhiều → gửi riêng từng trẻ.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `DocumentReference` | `DocumentReference.context.encounter[0]` | Reference(Encounter) | R | N:1 | |
| 2 | `SO_LUU_TRU` | Chuỗi | 200 | `DocumentReference` | `DocumentReference.identifier[0].value` | string | R | 1:1 | Số HSBA |
| 3 | `MA_YTE` | Chuỗi | 200 | `Patient` | `Patient.identifier[MA_BN].value` | string | R | 1:1 | = MA_BN Bảng 1 |
| 4 | `MA_KHOA_RV` | Chuỗi | 200 | `Organization` | `Organization.identifier.value` (khoa tổng kết) | string | R | 1:1 | |
| 5 | `NGAY_VAO` | Chuỗi | 12 | `Encounter` | `Encounter.period.start` | dateTime | R | 1:1 | |
| 6 | `NGAY_RA` | Chuỗi | 12 | `Encounter` | `Encounter.period.end` | dateTime | R | 1:1 | |
| 7 | `MA_DINH_CHI_THAI` | Số | 1 | `Encounter` | `Encounter.extension[dinh-chi-thai].valueBoolean` | boolean | R | 1:1 | `0`=Không; `1`=Có |
| 8 | `NGUYENNHAN_DINHCHI` | Chuỗi | n | `Encounter` | `Encounter.extension[nguyen-nhan-dinh-chi].valueString` | string | C | 1:1 | Bắt buộc khi MA_DINH_CHI_THAI=1 |
| 9 | `THOIGIAN_DINHCHI` | Chuỗi | 12 | `Encounter` | `Encounter.extension[thoi-gian-dinh-chi].valueDateTime` | dateTime | C | 1:1 | yyyymmddHHMM; bắt buộc khi =1 |
| 10 | `TUOI_THAI` | Số | 2 | `Encounter` | `Encounter.extension[tuoi-thai].valueInteger` | integer | C | 1:1 | Tuần tuổi thai 1–42; bắt buộc khi =1 |
| 11 | `CHAN_DOAN_RV` | Chuỗi | 1500 | `DocumentReference` | `DocumentReference.description` | string | R | 1:1 | Theo TT 18/2022; mã bệnh dài ngày theo TT 46/2016 |
| 12 | `PP_DIEUTRI` | Chuỗi | 1500 | `DocumentReference` | `DocumentReference.extension[pp-dieu-tri].valueString` | string | R | 1:1 | Theo TT 18/2022 |
| 13 | `GHI_CHU` | Chuỗi | 1500 | `DocumentReference` | `DocumentReference.note[0].text` | string | C | 1:1 | Phụ lục 3 TT 18/2022 |
| 14 | `MA_TTDV` | Chuỗi | 10 | `Practitioner` | `Practitioner.identifier[bhxh].value` (người đứng đầu) | string | R | 1:1 | |
| 15 | `MA_BS` | Chuỗi | 200 | `Practitioner` | `Practitioner.identifier[bhxh].value` (trưởng/phó khoa) | string | R | 1:1 | |
| 16 | `TEN_BS` | Chuỗi | 255 | `Practitioner` | `Practitioner.name[0].text` | string | R | 1:1 | |
| 17 | `NGAY_CT` | Chuỗi | 8 | `DocumentReference` | `DocumentReference.date` | instant | R | 1:1 | yyyymmdd; = ngày ra viện |
| 18 | `MA_CHA` | Chuỗi | 10 | `RelatedPerson` | `RelatedPerson.identifier[bhxh].value` (cha) | string | C | 1:1 | Trẻ <16 tuổi. Để trống nếu không có |
| 19 | `MA_ME` | Chuỗi | 10 | `RelatedPerson` | `RelatedPerson.identifier[bhxh].value` (mẹ) | string | C | 1:1 | Trẻ <16 tuổi |
| 20 | `MA_THE_TAM` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[tam].value` | string | C | 1:1 | Thẻ BHYT tạm cho trẻ/người hiến tạng |
| 21 | `HO_TEN_CHA` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (cha) | string | C | 1:1 | Phụ lục 3 TT 56/2017 |
| 22 | `HO_TEN_ME` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (mẹ) | string | C | 1:1 | |
| 23 | `SO_NGAY_NGHI` | Số | 2 | `Claim` | `Claim.extension[so-ngay-nghi].valueInteger` | integer | C | 1:1 | Ngày nghỉ ngoại trú sau ra viện |
| 24 | `NGOAITRU_TUNGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.start` (ngoại trú) | date | C | 1:1 | yyyymmdd |
| 25 | `NGOAITRU_DENNGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.end` (ngoại trú) | date | C | 1:1 | yyyymmdd |

---

## 9. Bảng 8 — Chỉ tiêu dữ liệu tóm tắt hồ sơ bệnh án

**FHIR Resource chính ánh xạ:** `Composition` (type=`discharge-summary`)

> Bảng 8 **không bị sửa đổi** bởi QĐ 4750.  
> Chỉ gửi khi MA_LOAI_KCB ∈ {03 (nội trú), 04 (ban ngày), 06 (lưu TYT xã)}.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `Composition` | `Composition.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `MA_LOAI_KCB` | Số | 2 | `Encounter` | `Encounter.class.code` | code | R | 1:1 | `02`/`03`/`04` |
| 3 | `HO_TEN_CHA` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (cha) | string | C | 1:1 | Nếu có |
| 4 | `HO_TEN_ME` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (mẹ) | string | C | 1:1 | |
| 5 | `NGUOI_GIAM_HO` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (giám hộ) | string | C | 1:1 | |
| 6 | `DON_VI` | Chuỗi | 1024 | `Organization` | `Organization.name` (nơi làm việc BN) | string | O | 1:1 | Con ốm: ghi đơn vị cha/mẹ |
| 7 | `NGAY_VAO` | Chuỗi | 12 | `Encounter` | `Encounter.period.start` | dateTime | R | 1:1 | |
| 8 | `NGAY_RA` | Chuỗi | 12 | `Encounter` | `Encounter.period.end` | dateTime | R | 1:1 | |
| 9 | `CHAN_DOAN_VAO` | Chuỗi | n | `Composition` | `Composition.section[admission].text.div` | xhtml | O | 1:1 | Chẩn đoán khi nhập viện |
| 10 | `CHAN_DOAN_RV` | Chuỗi | n | `Composition` | `Composition.section[discharge].text.div` | xhtml | R | 1:1 | Theo TT 18/2022 |
| 11 | `QT_BENHLY` | Chuỗi | n | `Composition` | `Composition.section[clinical-history].text.div` | xhtml | R | 1:1 | Quá trình bệnh lý và diễn biến lâm sàng |
| 12 | `TOMTAT_KQ` | Chuỗi | n | `DiagnosticReport` | `DiagnosticReport.conclusion` | string | O | 1:1 | Tóm tắt kết quả XN có giá trị chẩn đoán |
| 13 | `PP_DIEUTRI` | Chuỗi | n | `Composition` | `Composition.section[treatment].text.div` | xhtml | R | 1:1 | Theo TT 18/2022 |
| 14 | `NGAY_SINHCON` | Chuỗi | 8 | `Patient` | `Patient.birthDate` (con) | date | C | 1:1 | yyyymmdd. Khi con chết sau sinh |
| 15 | `NGAY_CONCHET` | Chuỗi | 8 | `Patient` | `Patient.deceasedDateTime` | dateTime | C | 1:1 | yyyymmdd |
| 16 | `SO_CONCHET` | Số | 2 | `Observation` | `Observation.valueInteger` (death-count) | integer | C | 1:1 | |
| 17 | `KET_QUA_DTRI` | Số | 1 | `Encounter` | `Encounter.hospitalization.dischargeDisposition.coding.code` | code | O | 1:1 | `1`–`7` |
| 18 | `GHI_CHU` | Chuỗi | n | `Composition` | `Composition.note[0].text` | string | C | 1:1 | Phụ lục 4 TT 18/2022: người giám hộ/NLHVDS |
| 19 | `MA_TTDV` | Số | 10 | `Practitioner` | `Practitioner.identifier[bhxh].value` (người đứng đầu) | string | R | 1:1 | |
| 20 | `NGAY_CT` | Chuỗi | 8 | `Composition` | `Composition.date` | dateTime | R | 1:1 | yyyymmdd |
| 21 | `MA_THE_TAM` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[tam].value` | string | C | 1:1 | |
| 22 | `DU_PHONG` | Chuỗi | n | — | Extension | string | O | 1:1 | |

---

## 10. Bảng 9 — Chỉ tiêu dữ liệu giấy chứng sinh

**FHIR Resource chính ánh xạ:** `Patient` (trẻ) · `RelatedPerson` (mẹ/cha) · `DocumentReference`

> Bảng 9 **không bị sửa đổi** bởi QĐ 4750. Sinh đôi/nhiều → gửi riêng từng trẻ.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `Encounter` | `Encounter.id` (đợt sinh) | id | R | 1:1 | |
| 2 | `MA_BHXH_NND` | Số | 10 | `RelatedPerson` | `RelatedPerson.identifier[bhxh].value` (mẹ/NND) | string | C | 1:1 | Nếu có |
| 3 | `MA_THE_NND` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[0].value` (mẹ) | string | C | 1:1 | |
| 4 | `HO_TEN_NND` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (mẹ/NND) | string | R | 1:1 | |
| 5 | `NGAYSINH_NND` | Chuỗi | 8 | `RelatedPerson` | `RelatedPerson.birthDate` | date | O | 1:1 | yyyymmdd |
| 6 | `MA_DANTOC_NND` | Số | 2 | `RelatedPerson` | `RelatedPerson.extension[ethnicity].valueCoding.code` | code | O | 1:1 | QĐ 121-TCTK |
| 7 | `SO_CCCD_NND` | Số | 15 | `RelatedPerson` | `RelatedPerson.identifier[cccd].value` | string | O | 1:1 | |
| 8 | `NGAYCAP_CCCD_NND` | Chuỗi | 8 | `RelatedPerson` | `RelatedPerson.identifier[cccd].period.start` | date | O | 1:1 | |
| 9 | `NOICAP_CCCD_NND` | Chuỗi | 1024 | `RelatedPerson` | `RelatedPerson.identifier[cccd].assigner.display` | string | O | 1:1 | |
| 10 | `NOI_CU_TRU_NND` | Chuỗi | 1024 | `RelatedPerson` | `RelatedPerson.address[0].text` | string | O | 1:1 | |
| 11 | `MA_QUOCTICH` | Số | 3 | `RelatedPerson` | `RelatedPerson.extension[nationality].valueCoding.code` | code | O | 1:1 | TT 07/2016/TT-BCA |
| 12 | `MATINH_CU_TRU` | Chuỗi | 3 | `RelatedPerson` | `RelatedPerson.address[0].state` | string | O | 1:1 | |
| 13 | `MAHUYEN_CU_TRU` | Chuỗi | 3 | `RelatedPerson` | `RelatedPerson.address[0].district` | string | O | 1:1 | |
| 14 | `MAXA_CU_TRU` | Chuỗi | 5 | `RelatedPerson` | `RelatedPerson.address[0].postalCode` | string | O | 1:1 | |
| 15 | `HO_TEN_CHA` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (cha) | string | C | 1:1 | |
| 16 | `MA_THE_TAM` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[tam].value` (trẻ) | string | C | 1:1 | Thẻ BHYT tạm của trẻ |
| 17 | `HO_TEN_CON` | Chuỗi | 255 | `Patient` | `Patient.name[0].text` | string | C | 1:1 | Tên dự kiến (nếu có) |
| 18 | `GIOI_TINH_CON` | Số | 1 | `Patient` | `Patient.gender` | code | R | 1:1 | `1`→`male`; `2`→`female`; `3`→`unknown` |
| 19 | `SO_CON` | Số | 2 | `Observation` | `Observation.valueInteger` (birth-count) | integer | R | 1:1 | Số con trong lần sinh này |
| 20 | `LAN_SINH` | Số | 2 | `Observation` | `Observation.extension[lan-sinh].valueInteger` | integer | O | 1:1 | Số lần sinh (tính cả lần này) |
| 21 | `SO_CON_SONG` | Số | 2 | `Observation` | `Observation.extension[con-song].valueInteger` | integer | O | 1:1 | Số con hiện đang sống |
| 22 | `CAN_NANG_CON` | Số | 10 | `Observation` | `Observation.valueQuantity.value` | decimal | R | 1:1 | gram; LOINC `8339-4` (birth weight) |
| 23 | `NGAY_SINH_CON` | Chuỗi | 12 | `Patient` | `Patient.birthDate` | dateTime | R | 1:1 | yyyymmddHHMM — giờ phút bắt buộc |
| 24 | `NOI_SINH_CON` | Chuỗi | 1024 | `Encounter` | `Encounter.location[0].location.display` | string | R | 1:1 | |
| 25 | `TINH_TRANG_CON` | Chuỗi | n | `Observation` | `Observation.note[0].text` | string | R | 1:1 | APGAR, dị tật nếu có |
| 26 | `SINHCON_PHAUTHUAT` | Số | 1 | `Procedure` | `Procedure.code.coding.code` (C-section) | code | R | 1:1 | `1`=Sinh mổ; `0`=Sinh thường |
| 27 | `SINHCON_DUOI32TUAN` | Số | 1 | `Patient` | `Patient.extension[premature].valueBoolean` | boolean | R | 1:1 | `1`=Dưới 32 tuần |
| 28 | `GHI_CHU` | Chuỗi | n | `DocumentReference` | `DocumentReference.note[0].text` | string | C | 1:1 | Ghi "Sinh mổ" / "Dưới 32 tuần" / cả hai |
| 29 | `NGUOI_DO_DE` | Chuỗi | 255 | `Procedure` | `Procedure.performer[0].actor.display` | string | O | 1:1 | |
| 30 | `NGUOI_GHI_PHIEU` | Chuỗi | 255 | `DocumentReference` | `DocumentReference.author[0].display` | string | O | 1:1 | |
| 31 | `NGAY_CT` | Chuỗi | 8 | `DocumentReference` | `DocumentReference.date` | instant | R | 1:1 | yyyymmdd |
| 32 | `SO` | Chuỗi | 200 | `DocumentReference` | `DocumentReference.identifier[so].value` | string | R | 1:1 | Số GCS tại CSKCB |
| 33 | `QUYEN_SO` | Chuỗi | 200 | `DocumentReference` | `DocumentReference.identifier[quyen].value` | string | O | 1:1 | |
| 34 | `MA_TTDV` | Số | 10 | `Practitioner` | `Practitioner.identifier[bhxh].value` | string | R | 1:1 | Thủ trưởng CSKCB |

---

## 11. Bảng 10 — Chỉ tiêu dữ liệu giấy chứng nhận nghỉ dưỡng thai

**FHIR Resource chính ánh xạ:** `Claim` (type=`oral`) · `Condition`

> Bảng 10 **không bị sửa đổi** bởi QĐ 4750.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `Claim` | `Claim.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `SO_SERI` | Chuỗi | 200 | `Claim` | `Claim.identifier[seri].value` | string | R | 1:1 | Phụ lục 6 TT 56/2017 |
| 3 | `SO_CT` | Chuỗi | 200 | `Claim` | `Claim.identifier[so-ct].value` | string | O | 1:1 | Quản lý nội bộ CSKCB |
| 4 | `SO_NGAY` | Số | 3 | `Claim` | `Claim.extension[so-ngay].valueInteger` | integer | R | DERIVE | = DEN_NGAY − TU_NGAY |
| 5 | `DON_VI` | Chuỗi | 1024 | `Organization` | `Organization.name` (nơi BN làm việc) | string | O | 1:1 | |
| 6 | `CHAN_DOAN_RV` | Chuỗi | n | `Condition` | `Condition.code.text` | string | R | 1:1 | Theo TT 56/2017 |
| 7 | `TU_NGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.start` | date | R | 1:1 | yyyymmdd; = ngày khám |
| 8 | `DEN_NGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.end` | date | R | 1:1 | yyyymmdd |
| 9 | `MA_TTDV` | Số | 10 | `Practitioner` | `Practitioner.identifier[bhxh].value` | string | R | 1:1 | |
| 10 | `TEN_BS` | Chuỗi | 255 | `Practitioner` | `Practitioner.name[0].text` | string | R | 1:1 | |
| 11 | `MA_BS` | Chuỗi | 200 | `Practitioner` | `Practitioner.identifier[bhxh].value` (BS ký) | string | R | 1:1 | |
| 12 | `NGAY_CT` | Chuỗi | 8 | `Claim` | `Claim.created` | dateTime | R | 1:1 | yyyymmdd |

---

## 12. Bảng 11 — Chỉ tiêu dữ liệu giấy chứng nhận nghỉ việc hưởng BHXH

**FHIR Resource chính ánh xạ:** `Claim` (type=`professional`) · `Condition`

> Bảng 11 **không bị sửa đổi** bởi QĐ 4750.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `MA_LK` | Chuỗi | 100 | `Claim` | `Claim.encounter` | Reference(Encounter) | R | N:1 | |
| 2 | `SO_CT` | Chuỗi | 200 | `Claim` | `Claim.identifier[so-ct].value` | string | O | 1:1 | |
| 3 | `SO_SERI` | Chuỗi | 200 | `Claim` | `Claim.identifier[seri].value` | string | O | 1:1 | CT07 |
| 4 | `SO_KCB` | Chuỗi | 200 | `Claim` | `Claim.identifier[so-kcb].value` | string | O | 1:1 | Phụ lục 07 TT 18/2022 |
| 5 | `DON_VI` | Chuỗi | 1024 | `Organization` | `Organization.name` (nơi BN làm việc) | string | O | 1:1 | Con ốm: ghi đơn vị cha/mẹ |
| 6 | `MA_BHXH` | Số | 10 | `Patient` | `Patient.identifier[bhxh].value` | string | R | 1:1 | |
| 7 | `MA_THE_BHYT` | Chuỗi | n | `Coverage` | `Coverage.identifier[0].value` | string | C | 1:1 | |
| 8 | `CHAN_DOAN_RV` | Chuỗi | n | `Condition` | `Condition.code.text` | string | R | 1:1 | Theo TT 18/2022; mã bệnh dài ngày |
| 9 | `PP_DIEUTRI` | Chuỗi | n | `Claim` | `Claim.extension[pp-dieu-tri].valueString` | string | O | 1:1 | |
| 10 | `MA_DINH_CHI_THAI` | Số | 1 | `Encounter` | `Encounter.extension[dinh-chi-thai].valueBoolean` | boolean | O | 1:1 | |
| 11 | `NGUYENNHAN_DINHCHI` | Chuỗi | n | `Encounter` | `Encounter.extension[nguyen-nhan-dinh-chi].valueString` | string | C | 1:1 | Bắt buộc khi =1 |
| 12 | `TUOI_THAI` | Số | 2 | `Encounter` | `Encounter.extension[tuoi-thai].valueInteger` | integer | C | 1:1 | Tuần 1–42; bắt buộc khi =1 |
| 13 | `SO_NGAY_NGHI` | Số | 3 | `Claim` | `Claim.extension[so-ngay-nghi].valueInteger` | integer | R | 1:1 | Tối đa 30 ngày/lần; lao ≤180 ngày; sảy/phá thai từ 13 tuần ≤50 ngày |
| 14 | `TU_NGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.start` | date | R | 1:1 | yyyymmdd; = ngày khám |
| 15 | `DEN_NGAY` | Chuỗi | 8 | `Claim` | `Claim.billablePeriod.end` | date | R | 1:1 | yyyymmdd |
| 16 | `HO_TEN_CHA` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (cha) | string | C | 1:1 | Trẻ <7 tuổi; Phụ lục 7 TT 18/2022 |
| 17 | `HO_TEN_ME` | Chuỗi | 255 | `RelatedPerson` | `RelatedPerson.name[0].text` (mẹ) | string | C | 1:1 | Trẻ <7 tuổi |
| 18 | `MA_TTDV` | Số | 10 | `Practitioner` | `Practitioner.identifier[bhxh].value` | string | R | 1:1 | |
| 19 | `MA_BS` | Chuỗi | 200 | `Practitioner` | `Practitioner.identifier[bhxh].value` (BS ký) | string | R | 1:1 | |
| 20 | `NGAY_CT` | Chuỗi | 8 | `Claim` | `Claim.created` | dateTime | R | 1:1 | yyyymmdd; = ngày khám (hoặc ngày cuối đợt khám) |
| 21 | `MA_THE_TAM` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[tam].value` | string | C | 1:1 | |
| 22 | `MAU_SO` | Chuỗi | 5 | `Claim` | `Claim.extension[mau-so].valueString` | string | O | 1:1 | Mặc định `CT07` |

---

## 13. Bảng 12 — Chỉ tiêu dữ liệu giám định y khoa

**FHIR Resource chính ánh xạ:** `Claim` (type=`institutional`) · `Patient` · `ClinicalImpression`

> Bảng 12 **không bị sửa đổi** bởi QĐ 4750.  
> Nhập trực tiếp trên Cổng BHXH — hiện chưa liên thông HIS.  
> Không áp dụng giám định pháp y.

| STT | Trường XML | Kiểu XML | Size | FHIR Resource | FHIR Path | Kiểu FHIR | B/b | Quan hệ | Ghi chú chuyển đổi |
|:---:|---|:---:|:---:|---|---|:---:|:---:|:---:|---|
| 1 | `NGUOI_CHU_TRI` | Chuỗi | 255 | `CareTeam` | `CareTeam.participant[lead].member.display` | string | R | 1:1 | Trong danh mục Cổng BHXH |
| 2 | `CHUC_VU` | Số | 1 | `CareTeam` | `CareTeam.participant[lead].role[0].coding.code` | code | R | 1:1 | `1`=Chủ tịch; `2`=Ký thay |
| 3 | `NGAY_HOP` | Chuỗi | 8 | `CareTeam` | `CareTeam.period.start` | date | R | 1:1 | yyyymmdd |
| 4 | `HO_TEN` | Chuỗi | 255 | `Patient` | `Patient.name[0].text` | string | R | 1:1 | Người được GĐYK |
| 5 | `NGAY_SINH` | Chuỗi | 8 | `Patient` | `Patient.birthDate` | date | R | 1:1 | yyyymmdd |
| 6 | `SO_CCCD` | Số | 15 | `Patient` | `Patient.identifier[cccd].value` | string | O | 1:1 | |
| 7 | `NGAY_CAP_CCCD` | Chuỗi | 8 | `Patient` | `Patient.identifier[cccd].period.start` | date | O | 1:1 | yyyymmdd |
| 8 | `NOI_CAP_CCCD` | Chuỗi | 1024 | `Patient` | `Patient.identifier[cccd].assigner.display` | string | O | 1:1 | |
| 9 | `DIA_CHI` | Chuỗi | 1024 | `Patient` | `Patient.address[0].text` | string | O | 1:1 | |
| 10 | `MATINH_CU_TRU` | Chuỗi | 3 | `Patient` | `Patient.address[0].state` | string | O | 1:1 | |
| 11 | `MAHUYEN_CU_TRU` | Chuỗi | 3 | `Patient` | `Patient.address[0].district` | string | O | 1:1 | |
| 12 | `MAXA_CU_TRU` | Chuỗi | 5 | `Patient` | `Patient.address[0].postalCode` | string | O | 1:1 | |
| 13 | `MA_BHXH` | Số | 10 | `Patient` | `Patient.identifier[bhxh].value` | string | R | 1:1 | |
| 14 | `MA_THE_BHYT` | Chuỗi | 15 | `Coverage` | `Coverage.identifier[0].value` | string | C | 1:1 | Nếu có |
| 15 | `NGHE_NGHIEP` | Chuỗi | 100 | `Patient` | `Patient.extension[occupation-text].valueString` | string | C | 1:1 | |
| 16 | `DIEN_THOAI` | Chuỗi | 15 | `Patient` | `Patient.telecom[0].value` | string | C | 1:1 | |
| 17 | `MA_DOI_TUONG` | Chuỗi | 20 | `Claim` | `Claim.type.coding.code` | code | R | 1:1 | BB/BHXH1L/BNN/CĐHH/NKT/TB/TH/TNLĐ/... Nhiều split `;` |
| 18 | `KHAM_GIAM_DINH` | Số | 1 | `Claim` | `Claim.extension[loai-kham-gd].valueCoding.code` | code | R | 1:1 | `1`=Lần đầu; `2`=Lại; `3`=Tái phát; `4`=Phúc quyết; `5`=PQ lần cuối; `6`=Bổ sung; `7`=Vết thương sót; `8`=Tổng hợp |
| 19 | `SO_BIEN_BAN` | Chuỗi | 200 | `Claim` | `Claim.identifier[bien-ban].value` | string | R | 1:1 | |
| 20 | `TYLE_TTCT_CU` | Số | 3 | `Claim` | `Claim.extension[ty-le-cu].valueDecimal` | decimal | C | 1:1 | Để trống nếu lần đầu |
| 21 | `DANG_HUONG_CHE_DO` | Số | 3 | `Coverage` | `Coverage.extension[che-do-dang-huong].valueString` | string | C | 1:1 | `1`–`7`; nhiều split `;`. Để trống nếu chưa hưởng |
| 22 | `NGAY_CHUNG_TU` | Chuỗi | 8 | `Claim` | `Claim.created` | dateTime | R | 1:1 | yyyymmdd; = ngày họp HĐGĐYK |
| 23 | `SO_GIAY_GIOI_THIEU` | Chuỗi | 200 | `Claim` | `Claim.referral.identifier.value` | string | O | 1:1 | |
| 24 | `NGAY_DE_NGHI` | Chuỗi | 8 | `Claim` | `Claim.extension[ngay-de-nghi].valueDate` | date | O | 1:1 | yyyymmdd |
| 25 | `MA_DONVI` | Chuỗi | 200 | `Organization` | `Organization.identifier.value` (giới thiệu) | string | O | 1:1 | Cơ quan quản lý/giới thiệu |
| 26 | `GIOI_THIEU_CUA` | Chuỗi | 1024 | `Organization` | `Organization.name` (giới thiệu) | string | O | 1:1 | |
| 27 | `KET_QUA_KHAM` | Chuỗi | n | `ClinicalImpression` | `ClinicalImpression.finding[0].itemCodeableConcept.text` | string | R | 1:1 | Kết quả HĐGĐYK trong biên bản |
| 28 | `SO_VAN_BAN_CAN_CU` | Chuỗi | 200 | `Claim` | `Claim.extension[van-ban-can-cu].valueString` | string | R | 1:1 | Nhiều văn bản split `;` |
| 29 | `TYLE_TTCT_MOI` | Số | 3 | `Claim` | `Claim.extension[ty-le-moi].valueDecimal` | decimal | R | 1:1 | % tổn thương lần này |
| 30 | `TONG_TYLE_TTCT` | Số | 3 | `Claim` | `Claim.extension[tong-ty-le].valueDecimal` | decimal | C | 1:1 | Chỉ ghi khi GĐTG/bổ sung/vết thương sót |
| 31 | `DANG_KHUYETTAT` | Số | 1 | `Condition` | `Condition.code.coding.code` (disability-type) | code | C | 1:1 | `1`–`6`. Chỉ khi GĐYK NKT. TT 01/2019/TT-BLĐTBXH |
| 32 | `MUC_DO_KHUYETTAT` | Số | 1 | `Condition` | `Condition.severity.coding.code` | code | C | 1:1 | `1`=Thực hiện được; `2`=Cần trợ giúp; `3`=Không TH được; `4`=Không XĐ |
| 33 | `DE_NGHI` | Chuỗi | n | `Claim` | `Claim.note[0].text` | string | R | 1:1 | Nội dung đề nghị |
| 34 | `DUOC_XACDINH` | Chuỗi | n | `Claim` | `Claim.extension[duoc-xac-dinh].valueString` | string | C | 1:1 | Khoản 2 Điều 4 TT 56/2017: người không tự phục vụ |
| 35 | `DU_PHONG` | Chuỗi | n | — | Extension | string | O | 1:1 | |

---

## Phụ lục A — Bảng mapping mã

### A.1 `MA_LOAI_KCB` → `Encounter.class`

| Giá trị XML | Tên hình thức | FHIR class code | system |
|:---:|---|:---:|---|
| `01` | Khám bệnh | `AMB` | `http://terminology.hl7.org/CodeSystem/v3-ActCode` |
| `02` | Điều trị ngoại trú | `AMB` | |
| `03` | Điều trị nội trú | `IMP` | |
| `04` | Điều trị nội trú ban ngày | `SS` | |
| `05` | Ngoại trú mạn tính + khám + thuốc | `AMB` | |
| `06` | Lưu TYT xã / PKĐKKV | `IMP` | |
| `07` | Nhận thuốc theo hẹn | `AMB` | |
| `08` | Ngoại trú mạn tính + DVKT | `AMB` | |
| `09` | Cấp cứu | `EMER` | |

### A.2 Công thức `SO_NGAY_DTRI` → `Encounter.length`

| MA_LOAI_KCB | Công thức |
|:---:|---|
| 01, 07, 09 | `= 0` |
| 02, 03, 04, 06 | `= ngày(NGAY_RA) − ngày(NGAY_VAO) + 1` |
| 05 | `= số ngày dùng thuốc` |
| 08 | `= số ngày thực tế có DVKT` |

### A.3 `KET_QUA_DTRI` + `MA_LOAI_RV` → `Encounter.hospitalization.dischargeDisposition`

| MA_LOAI_RV | KET_QUA_DTRI | FHIR code | Display |
|:---:|:---:|:---:|---|
| `1` | `1` hoặc `2` | `home` | Về nhà |
| `1` | `5` | `exp` | Tử vong |
| `1` | `6` | `aadvice` | Tiên lượng nặng xin về |
| `2` | bất kỳ | `hosp` | Chuyển tuyến (chuyên môn) |
| `3` | bất kỳ | `oth` | Trốn viện |
| `4` | bất kỳ | `aadvice` | Xin ra viện |
| `5` | bất kỳ | `other-hcf` | Chuyển tuyến (theo BN) |

### A.4 `GIOI_TINH` → `Patient.gender`

| Giá trị XML | FHIR code |
|:---:|:---:|
| `1` | `male` |
| `2` | `female` |
| `3` | `unknown` |

---

## Phụ lục B — Công thức tính tài chính

### B.1 Công thức T_BNTT / T_BNCCT / T_BHTT (Bảng 2 & Bảng 3)

```
Bước 1 — Tính tạm thời:
  T_BNTT_tm  = THANH_TIEN_BV − THANH_TIEN_BH
  T_BHTT_tm  = THANH_TIEN_BH × MUC_HUONG / 100
  T_BNCCT_tm = THANH_TIEN_BH − T_BHTT_tm

Bước 2 — Điều chỉnh khi T_NGUONKHAC > 0 và hỗ trợ riêng cá nhân BN:
  Nếu T_NGUONKHAC ≤ T_BNTT_tm:
    T_BNTT  = T_BNTT_tm − T_NGUONKHAC
    T_BNCCT = T_BNCCT_tm
    T_BHTT  = T_BHTT_tm

  Nếu T_NGUONKHAC > T_BNTT_tm:
    T_BNTT  = 0
    Du      = T_NGUONKHAC − T_BNTT_tm
    Nếu Du ≤ T_BNCCT_tm:
      T_BNCCT = T_BNCCT_tm − Du
      T_BHTT  = T_BHTT_tm
    Nếu Du > T_BNCCT_tm:
      T_BNCCT = 0
      T_BHTT  = T_BHTT_tm − (Du − T_BNCCT_tm)

Trường hợp đặc biệt (thuốc ARV):
  T_NGUONKHAC = T_BNCCT_tm → T_BNCCT = 0; T_BHTT = T_BHTT_tm
```

### B.2 Công thức THANH_TIEN_BH (Bảng 3 — trường hợp có TYLE_TT_DV)

```
Thông thường:
  THANH_TIEN_BH = SO_LUONG × DON_GIA_BH × TYLE_TT_BH / 100

Khi có TYLE_TT_DV (nằm ghép / khám nhiều lần / PT nhiều can thiệp):
  THANH_TIEN_BH = SO_LUONG × DON_GIA_BH × TYLE_TT_DV/100 × TYLE_TT_BH/100

Bảng TYLE_TT_DV đặc biệt:
  ─────────────────────────────────────────────────────────────────
  Tình huống                                  TYLE_TT_DV  SO_LUONG
  Chuyển ≥2 khoa/ngày (cao+thấp nhất)            100       0.500
  Chuyển ≥2 khoa/ngày + nằm ghép 2 người          50       0.500
  Chuyển ≥2 khoa/ngày + nằm ghép ≥3 người         33       0.330
  Nằm 1 người/giường                              100       1.000
  Tiền khám lần 1                                 100       1.000
  Tiền khám lần 2–4                                30       1.000
  Tiền khám lần 5                                  10       1.000
  Tiền khám lần ≥6                                  0       1.000
  PT ≥2 can thiệp cùng kíp (từ lần 2)             50       1.000
  PT ≥2 can thiệp kíp khác (từ lần 2)             80       1.000
  Thủ thuật phát sinh trong PT                     80       1.000
```

---

## Phụ lục C — Quy tắc chuyển đổi định dạng

### C.1 Ngày giờ

| Định dạng XML | Ký tự | FHIR Type | FHIR Format | Ví dụ chuyển đổi |
|---|:---:|---|---|---|
| `yyyymmddHHMM` | 12 | `dateTime` | `yyyy-MM-ddTHH:mm:ss+07:00` | `202403100830` → `2024-03-10T08:30:00+07:00` |
| `yyyymmdd` | 8 | `date` | `yyyy-MM-dd` | `20240310` → `2024-03-10` |
| `yyyymm0000` | 12 | `date` (partial) | `yyyy-MM` | Chỉ biết năm-tháng |
| `yyyy00000000` | 12 | `date` (partial) | `yyyy` | Chỉ biết năm |
| `000000000000` | 12 | null | — | Không xác định |

### C.2 Xử lý giá trị Số → Chuỗi (thay đổi QĐ 4750)

| Trường | Vấn đề kỹ thuật | Giải pháp |
|---|---|---|
| `SO_CCCD` (B1, Checkin) | Kiểu Số → mất số 0 đầu | Lưu `VARCHAR(15)`; khi đọc dữ liệu cũ: `LPAD(val, 12, '0')` |
| `MA_LOAI_KCB` (Checkin) | `1` → phải là `01` | `LPAD(val, 2, '0')` |
| `MA_DOITUONG_KCB` (Checkin) | `1` → `0001` hoặc `1` (cần xác nhận BYT/BHXH) | Build lookup cũ→mới |
| `MA_QUOCTICH`, `MA_DANTOC` | Mất số 0 đầu | `LPAD(MA_QUOCTICH, 3, '0')`; `LPAD(MA_DANTOC, 2, '0')` |
| `DIEN_THOAI` | SĐT bắt đầu `0` bị mất | Lưu `VARCHAR(15)` |
| `DIA_CHI` | Kiểu Số (lỗi QĐ 130) → Chuỗi | Không có vấn đề chuyển đổi, đã là text |

### C.3 Xử lý giảm size `MAXA_CU_TRU` (5→3 theo QĐ 4750)

```
QĐ 130: MAXA_CU_TRU Chuỗi(5) theo QĐ 124/2004/QĐ-TTg
QĐ 4750: MAXA_CU_TRU Chuỗi(3) — dùng mã mới khi thành lập/gộp đơn vị HC

Xử lý migration:
  - Mã xã cũ 5 ký tự: cần build bảng lookup mã xã cũ → mã mới 3 ký tự
  - Mã xã mới sau sáp nhập: dùng trực tiếp (đã là 3 ký tự)
  - FHIR path: Patient.address[0].postalCode — VARCHAR(5) để tương thích cả hai
```

### C.4 Xử lý đa giá trị (phân cách `;`)

| Trường | Cách xử lý FHIR |
|---|---|
| `MA_THE_BHYT` nhiều thẻ | Tạo nhiều `Coverage` resource; mỗi thẻ = 1 Coverage |
| `MA_BENH_KT` nhiều mã | Tạo nhiều `Condition` resource (rank ≥ 2); mỗi mã = 1 Condition |
| `MA_KHOA` nhiều khoa | Tạo `Encounter.location[]` nhiều phần tử |
| `MA_BAC_SI` nhiều bác sĩ | `ServiceRequest.requester` + `MedicationRequest.requester` split `;` → dùng mã đầu tiên làm requester chính |
| `MA_GIUONG` nhiều giường | `Encounter.location[]` nhiều phần tử |
| `NGAY_TAI_KHAM` nhiều ngày | Tạo nhiều `Appointment` resource |
| `MA_XU_TRI` nhiều xử trí | Tạo nhiều `CarePlan.activity[]` |

### C.5 Mã đặc biệt trong MA_THUOC / MA_DICH_VU / MA_VAT_TU

| Mã / Tiền tố | Ý nghĩa | FHIR xử lý |
|---|---|---|
| `40.17` | Khí Oxy | `Medication.code.coding.code = 40.17`; LOINC `57010-5` |
| `40.573` | Khí NO | `Medication.code.coding.code = 40.573` |
| `{mã}.KT` | Máu + XN kháng thể bất thường | Extension `[kt-xn]` = true |
| `{mã}.NAT` | Máu + XN acid nucleic | Extension `[nat-xn]` = true |
| `{mã}.KTNAT` | Máu + cả hai XN | Extensions KT + NAT |
| `VM.XXXXX` | Vận chuyển máu từ CSKCB XXXXX | `Extension[van-chuyen-mau].valueString = XXXXX` |
| `BB.XXXXX` | Bao bì thuốc thang | `Extension[bao-bi].valueString = XXXXX` |
| `VC.XXXXX` | Vận chuyển BN đến XXXXX | `ServiceRequest.code = VC`; performer = Org XXXXX |
| `C.XXXXX` | Thuốc chuyển từ CSKCB XXXXX | `Extension[cskcb-thuoc] = C.XXXXX` |
| `K.XXXXX` | Thuốc ngoài giá CLS tại XXXXX | `Extension[cskcb-thuoc] = K.XXXXX` |
| `M.XXXXX` | Máu từ CSKCB XXXXX | `Extension[cskcb-thuoc] = M.XXXXX` |
| `XX.YYYY.ZZZZ.K.WWWWW` | DVKT/CLS chuyển đến CSKCB WWWWW | Parse: code=`XX.YYYY.ZZZZ`; performer=Org WWWWW |
| `XX.YYYY.ZZZZ_GT` | DVKT có gây tê | code = `XX.YYYY.ZZZZ`; `PP_VO_CAM` = 2 |
| `XX.YYYY.ZZZZ_TB` | DVKT không hoàn thành | `Procedure.status = stopped`; DON_GIA_BH=0 |
| `XX.YYYY.0000` | DVKT chưa có giá | code = `XX.YYYY.0000`; `ChargeItem.priceOverride = 0` |

---

*Phiên bản 2.0 — Mapping thuần túy Bảng XML → FHIR Resource*  
*Căn cứ: QĐ 130/QĐ-BYT (18/01/2023) + QĐ 4750/QĐ-BYT (29/12/2023)*  
*Hiệu lực: 01/07/2024*  
*Chuẩn đích: HL7 FHIR R4B (4.3.0)*
