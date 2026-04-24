# Báo Cáo Phân Tích FHIR Resource
## Tình trạng dữ liệu sau khi thu thập XML theo QĐ 130 + QĐ 4750

> **Góc nhìn:** Phân tích theo từng FHIR Resource (không phải theo 23 báo cáo)  
> **Câu hỏi trả lời:** Sau khi import toàn bộ XML QĐ 130+4750 vào FHIR server — mỗi Resource có gì, thiếu gì, và nên bổ sung từ đâu?  
> **Chuẩn:** HL7 FHIR R4B (4.3.0)  
> **Căn cứ:** QĐ 130/QĐ-BYT (18/01/2023) + QĐ 4750/QĐ-BYT (29/12/2023)

---

## Quy ước đánh giá

| Ký hiệu | Mức độ quan trọng |
|---|---|
| 🔴 **Thiết yếu** | Không có → Resource không hoạt động / báo cáo sai kết quả hoặc không chạy được |
| 🟠 **Quan trọng** | Không có → báo cáo chạy được nhưng thiếu chiều phân tích chính |
| 🟡 **Nên có** | Không có → báo cáo chạy được, chất lượng phân tích giảm |
| 🟢 **Tốt hơn nếu có** | Không có → không ảnh hưởng báo cáo cốt lõi, chỉ hỗ trợ phân tích nâng cao |

| Ký hiệu nguồn | Diễn giải |
|---|---|
| ✅ **Có từ XML** | Đã có đầy đủ từ QĐ 130 + 4750 |
| ⚠️ **Có một phần** | Có nhưng không đủ hoặc cần xử lý thêm |
| ❌ **Không có** | Hoàn toàn không có trong QĐ 130 + 4750 |

---

## Tổng quan nhanh

| FHIR Resource | Trường có từ XML | Trường thiếu quan trọng | Mức độ hoàn chỉnh |
|---|:---:|:---:|:---:|
| `Patient` | 14 trường | 5 trường | ⬛⬛⬛⬛⬜ 80% |
| `Encounter` | 22 trường | 7 trường | ⬛⬛⬛⬛⬜ 75% |
| `Coverage` | 8 trường | 4 trường | ⬛⬛⬛⬜⬜ 65% |
| `Organization` | 1 trường (chỉ mã) | 6 trường | ⬛⬜⬜⬜⬜ 15% |
| `Location` | 2 trường | 5 trường | ⬛⬜⬜⬜⬜ 25% |
| `Condition` | 7 trường | 5 trường | ⬛⬛⬛⬜⬜ 60% |
| `Claim` | 12 trường | 3 trường | ⬛⬛⬛⬛⬜ 80% |
| `ClaimResponse` | 3 trường | 2 trường | ⬛⬛⬛⬜⬜ 60% |
| `MedicationRequest` | 11 trường | 4 trường | ⬛⬛⬛⬜⬜ 70% |
| `Medication` | 4 trường | 3 trường | ⬛⬛⬜⬜⬜ 55% |
| `ServiceRequest` | 7 trường | 4 trường | ⬛⬛⬛⬜⬜ 60% |
| `Procedure` | 5 trường | 4 trường | ⬛⬛⬜⬜⬜ 55% |
| `DiagnosticReport` | 4 trường | 3 trường | ⬛⬛⬜⬜⬜ 55% |
| `Observation` | 4 trường | 5 trường | ⬛⬛⬜⬜⬜ 45% |
| `EpisodeOfCare` | 6 trường | 3 trường | ⬛⬛⬛⬜⬜ 65% |
| `CodeSystem / ValueSet` | 0 trường | Toàn bộ | ⬜⬜⬜⬜⬜ 0% |
| `Practitioner` | 2 trường (chỉ mã) | 4 trường | ⬛⬜⬜⬜⬜ 20% |
| `ChargeItem` | 5 trường | 3 trường | ⬛⬛⬛⬜⬜ 60% |
| `ClinicalImpression` | 4 trường | 3 trường | ⬛⬛⬜⬜⬜ 55% |
| `DocumentReference` | 8 trường | 3 trường | ⬛⬛⬛⬜⬜ 70% |
| `Composition` | 7 trường | 2 trường | ⬛⬛⬛⬜⬜ 75% |
| `Device` | 3 trường | 3 trường | ⬛⬛⬜⬜⬜ 50% |

---

## 1. Patient

**Nguồn XML:** Bảng Check-in (STT 3–7) + Bảng 1 (STT 1–16)  
**Vai trò:** Dimension trung tâm — mọi Resource lâm sàng đều reference về Patient

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Patient.id` | `MA_BN` B1(3) | Mã nội bộ CSKCB |
| `Patient.identifier[pid]` | `MA_BN` B1(3) | |
| `Patient.identifier[cccd]` | `SO_CCCD` B1(5) — 🔄 Chuỗi(15) QĐ4750 | CCCD/CMND/Hộ chiếu |
| `Patient.name[0].text` | `HO_TEN` B1(4) | |
| `Patient.gender` | `GIOI_TINH` B1(7) | 1→male; 2→female; 3→unknown |
| `Patient.birthDate` | `NGAY_SINH` B1(6) | Parse 8 ký tự đầu |
| `Patient.address[0].text` | `DIA_CHI` B1(12) — 🔄 Chuỗi QĐ4750 | Địa chỉ tự do |
| `Patient.address[0].state` | `MATINH_CU_TRU` B1(13) | Mã tỉnh |
| `Patient.address[0].district` | `MAHUYEN_CU_TRU` B1(14) — 📝 QĐ4750 | Mã huyện |
| `Patient.address[0].postalCode` | `MAXA_CU_TRU` B1(15) — 🔄 Size 5→3 QĐ4750 | Mã xã |
| `Patient.telecom[0]` | `DIEN_THOAI` B1(16) — 🔄 Chuỗi QĐ4750 | SĐT |
| `Patient.extension[nationality]` | `MA_QUOCTICH` B1(9) — 🔄 Chuỗi QĐ4750 | |
| `Patient.extension[ethnicity]` | `MA_DANTOC` B1(10) — 🔄 Chuỗi QĐ4750 | |
| `Patient.extension[occupation]` | `MA_NGHE_NGHIEP` B1(11) | |
| `Patient.extension[blood-type]` | `NHOM_MAU` B1(8N) — 🆕 QĐ4750 | A/B/AB/O + Rh |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động nếu thiếu | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Patient.name[0].family` + `given[]` | 🟠 | QĐ 130 chỉ lưu `HO_TEN` dạng text liền | Không thể tìm kiếm theo họ/tên riêng; FHIR search `family=Nguyen` không hoạt động | Parse `HO_TEN` theo quy tắc tiếng Việt (từ cuối = tên, phần còn lại = họ + đệm) |
| `Patient.identifier[bhxh]` | 🟠 | Mã số BHXH không có trong B1/Checkin | Không liên kết được với cơ sở dữ liệu BHXH; BC07 tài chính thiếu cross-check | Lấy từ B11 (MA_BHXH), B6 (HIV), B12 (GĐYK); hoặc từ cổng BHXH |
| `Patient.active` | 🟡 | Không có trong QĐ 130 + 4750 | Không phân biệt được hồ sơ đang hoạt động / đã xoá | Mặc định `true`; cập nhật khi BN rời khỏi cơ sở |
| `Patient.communication[0].language` | 🟢 | Không có trong QĐ 130 + 4750 | Không ảnh hưởng báo cáo cốt lõi | Mặc định `vi` (tiếng Việt) |
| `Patient.generalPractitioner` | 🟢 | Không có trong QĐ 130 + 4750 | Không có thông tin bác sĩ gia đình / phụ trách | Lấy từ MA_BAC_SI B2/B3 — bác sĩ điều trị chính |

### Nhận xét tổng thể

Patient là resource **hoàn chỉnh nhất** sau khi import QĐ 130+4750. Dữ liệu nhân thân đầy đủ cho báo cáo thống kê. Điểm yếu chính là `name` chưa được tách họ/tên và thiếu mã số BHXH để liên kết hệ thống ngoài.

---

## 2. Encounter

**Nguồn XML:** Bảng Check-in + Bảng 1 (STT 17–65)  
**Vai trò:** Fact table trung tâm — liên kết Patient ↔ Condition ↔ Claim ↔ Procedure ↔ MedicationRequest

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Encounter.id` | `MA_LK` | PRIMARY KEY |
| `Encounter.status` | Suy luận: `NGAY_RA` có giá trị → `finished` | |
| `Encounter.class` | `MA_LOAI_KCB` B1(56) — 🔄 Chuỗi Checkin QĐ4750 | AMB/IMP/SS/EMER |
| `Encounter.period.start` | `NGAY_VAO` B1(35) | |
| `Encounter.period.end` | `NGAY_RA` B1(37) | |
| `Encounter.location[0].period.start` | `NGAY_VAO_NOI_TRU` B1(36), Checkin(14) — 🆕 QĐ4750 | Vào khoa điều trị |
| `Encounter.length` | `SO_NGAY_DTRI` B1(39) | Đã tính sẵn |
| `Encounter.serviceProvider` | `MA_CSKCB` B1(58) | → Organization |
| `Encounter.location[N]` | `MA_KHOA` B1(57) split ";" | → Location (khoa) |
| `Encounter.reasonCode[0].text` | `LY_DO_VV` B1(22) | Lý do đến |
| `Encounter.reasonCode[1].text` | `LY_DO_VNT` B1(23), Checkin(15) — 🆕 QĐ4750 | Lý do vào nội trú |
| `Encounter.reasonCode[1].coding.code` | `MA_LY_DO_VNT` B1(24), Checkin(16) — 🆕 QĐ4750 | Mã lý do |
| `Encounter.hospitalization.origin` | `MA_NOI_DI` B1(32) | CSKCB chuyển đến |
| `Encounter.hospitalization.destination` | `MA_NOI_DEN` B1(33) | CSKCB chuyển đi |
| `Encounter.hospitalization.dischargeDisposition` | `MA_LOAI_RV` + `KET_QUA_DTRI` B1(42,41) | Xem bảng mapping §A.3 |
| `Encounter.basedOn` | `GIAY_CHUYEN_TUYEN` B1(38) | Số giấy chuyển tuyến |
| `Encounter.diagnosis[N].condition` | `MA_BENH_CHINH` + `MA_BENH_KT` B1(27,28) | → Condition |
| `Encounter.serviceType` | `MA_DICH_VU` / `MA_THUOC` / `MA_VAT_TU` Checkin — 🆕 QĐ4750 | Chi phí đầu tiên |
| `Encounter.note[0]` | `GHI_CHU` B1(43) | Lời dặn ra viện |
| `Encounter.extension[pp-dieu-tri]` | `PP_DIEU_TRI` B1(40) | |
| `Encounter.extension[ma-tai-nan]` | `MA_TAI_NAN` B1(34) | |
| `Encounter.participant[attender]` | `MA_TTDV` B1(65) | Người đứng đầu CSKCB |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Encounter.type` | 🟠 | QĐ 130 không có mã loại hình chi tiết hơn class | Không thể GROUP BY theo loại khám (Khám lần đầu / Tái khám / Khám chuyên khoa) | Map từ `MA_LOAI_KCB` + `LY_DO_VV`; hoặc bổ sung từ HIS |
| `Encounter.priority` | 🟡 | Không có trong QĐ 130 + 4750 | Không phân biệt được ca cấp cứu khẩn / bình thường trong cùng class EMER | Suy luận từ `MA_DOITUONG_KCB`=2 → `stat`; còn lại → `routine` |
| `Encounter.participant[N].individual` (bác sĩ chính) | 🟠 | `MA_TTDV` chỉ là người đứng đầu CSKCB, không phải bác sĩ điều trị | Không biết bác sĩ nào trực tiếp điều trị BN → không phân tích được workload theo BS | Lấy `MA_BAC_SI` từ B2/B3 → Practitioner; gán `type = PART` |
| `Encounter.account` | 🟡 | Không có tài khoản thanh toán trong QĐ 130 + 4750 | Không liên kết được Encounter → Account → Invoice theo chuỗi FHIR chuẩn | Tạo Account ảo từ `MA_LK` để liên kết |
| `Encounter.episodeOfCare` | 🟡 | Phải tạo EpisodeOfCare trước rồi mới gán | Không theo dõi được BN tái nhập viện nhiều lần cho cùng một bệnh | Tạo EpisodeOfCare từ `MA_HSBA` B1(64), rồi reference |
| `Encounter.hospitalization.admitSource` (chuẩn hóa) | 🟡 | `MA_NOI_DI` chỉ là mã CSKCB, không phải code admitSource FHIR | Chuỗi filter `admitSource = emd` (từ cấp cứu) hay `hosp` (chuyển từ BV) không chính xác | Map: `MA_NOI_DI` có giá trị + `MA_LOAI_KCB`=03 → `hosp`; `MA_DOITUONG_KCB`=2 → `emd` |
| `Encounter.hospitalization.reAdmission` | 🟢 | Không có trong QĐ 130 + 4750 | Không phân biệt nhập viện lần đầu / tái nhập | Phát hiện bằng logic: cùng `MA_BN` + cùng `MA_BENH_CHINH` trong vòng 30 ngày → tái nhập |

### Nhận xét tổng thể

Encounter là resource **phong phú nhất** về dữ liệu từ QĐ 130+4750, đặc biệt được cải thiện đáng kể bởi QĐ 4750 (thêm `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT`). Điểm yếu chính là **thiếu bác sĩ điều trị trực tiếp** (chỉ có người đứng đầu CSKCB) và **thiếu liên kết EpisodeOfCare** để theo dõi bệnh mạn tính.

---

## 3. Coverage

**Nguồn XML:** Bảng 1 (STT 17–21, 59, 61, 31)  
**Vai trò:** Thông tin bảo hiểm — liên kết Encounter ↔ Claim

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Coverage.identifier[0]` | `MA_THE_BHYT` B1(17) | 15 ký tự; nhiều thẻ split ";" |
| `Coverage.period.start` | `GT_THE_TU` B1(19) | |
| `Coverage.period.end` | `GT_THE_DEN` B1(20) | |
| `Coverage.class[0].value` | `MA_DKBD` B1(18) | CSKCB đăng ký ban đầu |
| `Coverage.type` | `MA_DOITUONG_KCB` B1(31) Chuỗi(3) | Đối tượng KBCB |
| `Coverage.network` | `MA_KHUVUC` B1(59) | K1/K2/K3 |
| `Coverage.costToBeneficiary[exception]` | `NGAY_MIEN_CCT` B1(21) | Miễn cùng chi trả |
| `Coverage.extension[5yr-continuous]` | `NAM_NAM_LIEN_TUC` B1(62) | 5 năm liên tục |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Coverage.subscriber` | 🟠 | QĐ 130 không lưu thông tin người tham gia BHYT (khác BN trong trường hợp phụ thuộc) | Không phân biệt được BN là người tham gia chính hay người phụ thuộc (con/vợ/chồng) → ảnh hưởng phân tích đối tượng BHYT | Lấy từ Cổng BHXH qua API tra cứu thẻ BHYT |
| `Coverage.subscriberId` | 🟠 | Không có mã số BHXH của người đóng | Không liên kết được với hệ thống BHXH để tra cứu lịch sử đóng BHYT | Từ Cổng BHXH hoặc B11 (MA_BHXH cho người nghỉ việc) |
| `Coverage.beneficiary` | 🟠 | Phải reference về Patient nhưng chưa có liên kết tường minh | Coverage hiện tại độc lập, chưa gắn với Patient cụ thể | Tạo Coverage với `Coverage.beneficiary` = `Patient/{MA_BN}` |
| `Coverage.payor` | 🟠 | Không có Organization BHXH tỉnh/huyện | Không biết cơ quan BHXH nào chi trả → không trace được dòng tiền | Tạo Organization(payer) cho từng BHXH tỉnh từ mã 2 ký tự trong `MA_THE_BHYT` |
| `Coverage.costToBeneficiary[0].value` | 🟡 | `MUC_HUONG` chỉ có ở B2/B3 (theo từng dòng chi phí), không có tổng hợp trên Coverage | Không biết ngay mức hưởng tổng quát của BN khi tạo Coverage | Tổng hợp từ `MUC_HUONG` B2/B3 → gán vào Coverage |

---

## 4. Organization

**Nguồn XML:** `MA_CSKCB` B1(58), `MA_KHOA` B1(57)  
**Vai trò:** Master data đơn vị — được reference bởi hầu hết mọi Resource

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Organization.identifier[0].value` | `MA_CSKCB` B1(58) — 5 ký tự | Chỉ có mã |
| `Organization.identifier[0].value` (khoa) | `MA_KHOA` B1(57) | Chỉ có mã khoa |

### Trường còn thiếu — CỐT LÕI NHẤT

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Organization.name` | 🔴 **Thiết yếu** | QĐ 130+4750 chỉ truyền mã, không truyền tên | **Toàn bộ báo cáo hiển thị mã BV/Khoa thay vì tên** — không dùng được trong thực tế | **DMDC QĐ 5937/QĐ-BYT** — Phụ lục 4 (BV) + Phụ lục 5 (Khoa) |
| `Organization.type` (hạng BV) | 🔴 **Thiết yếu** | Không có | Không phân loại được BV hạng I/II/III/IV, tuyến TW/tỉnh/huyện | DMDC QĐ 5937 + Phân hạng BYT |
| `Organization.address` | 🟠 | Không có địa chỉ BV trong QĐ 130+4750 | Không lọc được theo địa lý (tỉnh/vùng) | DMDC QĐ 5937 |
| `Organization.partOf` (BV → Sở YT) | 🟠 | Không có phân cấp | Không drill-down được BV → Sở YT → Bộ YT | DMDC QĐ 5937 + cấu trúc hành chính y tế |
| `Organization.telecom` | 🟡 | Không có | Không có thông tin liên hệ | DMDC QĐ 5937 |
| `Organization.active` | 🟡 | Không có | Không biết BV còn hoạt động không | DMDC QĐ 5937 + cập nhật định kỳ |

### Nhận xét tổng thể

Organization là resource **thiếu nhất và quan trọng nhất** trong toàn bộ hệ thống. Sau khi import QĐ 130+4750, mọi reference đến Organization chỉ có **mã số** — không có tên, không có địa chỉ, không có phân cấp. Đây là điều kiện tiên quyết phải bổ sung trước khi bất kỳ báo cáo nào có thể hiển thị nhãn có nghĩa.

---

## 5. Location

**Nguồn XML:** `MA_GIUONG` B3(32), `MA_KHOA` B1(57), B3(31)  
**Vai trò:** Giường bệnh, phòng, khoa — phân tích tình trạng sử dụng giường

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Location.id` | `MA_GIUONG` + `MA_KHOA` composite | Tự sinh |
| `Location.name` | `MA_GIUONG` B3(32) | H001, T001, C001, K001... |
| `Location.managingOrganization` | `MA_KHOA` B3(31) | → Organization(khoa) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| **Tổng số giường kế hoạch** | 🔴 **Thiết yếu** | QĐ 130+4750 chỉ biết giường **đã có BN dùng** trong kỳ báo cáo — không biết tổng giường được phân bổ | Tỷ lệ sử dụng giường = BN đang nằm / Tổng giường → mẫu số = 0 → chia không được | **HIS module quản lý giường** — danh sách kế hoạch giường theo khoa |
| `Location.physicalType` | 🟠 | Mã MA_GIUONG chỉ là tên viết tắt | Không phân biệt được giường (bd) / phòng (ro) / tầng (lvl) / khoa (wa) | Suy luận: tiền tố H/T/C/K → `bd`; nếu không có MA_GIUONG → `wa` (khoa) |
| `Location.partOf` (giường → phòng → khoa) | 🟠 | Không có phân cấp vị trí vật lý | Không drill-down được từ khoa → phòng → giường | HIS cung cấp cây phân cấp vị trí |
| `Location.status` | 🟡 | Không có trong QĐ 130+4750 | Không biết giường `active` hay `suspended` (sửa chữa) | Mặc định `active`; HIS cập nhật khi bảo trì |
| `Location.operationalStatus` | 🟡 | Chỉ suy luận được từ Encounter | Real-time occupancy không chính xác 100% | Cập nhật từ Encounter.status = in-progress → `O` (Occupied) |

---

## 6. Condition

**Nguồn XML:** Bảng 1 (STT 25–30)  
**Vai trò:** Chẩn đoán bệnh — liên kết tới ICD-10

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Condition.code.coding.code` | `MA_BENH_CHINH` B1(27) | ICD-10 bệnh chính |
| `Condition.code.text` | `CHAN_DOAN_RV` B1(26) | Chẩn đoán đầy đủ bằng chữ |
| `Condition.note[0].text` | `CHAN_DOAN_VAO` B1(25) | Chẩn đoán sơ bộ khi vào |
| `Condition.code.coding[]` (bệnh kèm) | `MA_BENH_KT` B1(28) split ";" | Tối đa 12 mã |
| `Condition.code.coding[]` (YHCT) | `MA_BENH_YHCT` B1(29) | System riêng |
| `Condition.stage[0].summary` | `GIAI_DOAN_BENH` B5(4) | Text tự do |
| `Condition.recordedDate` | `NGAY_RA` B1(37) | Ngày ghi nhận chẩn đoán cuối |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Condition.code.coding.display` | 🔴 **Thiết yếu** | CodeSystem ICD-10 tiếng Việt không có trong QĐ 130+4750 | **Tên bệnh tiếng Việt bị thiếu** → báo cáo chỉ hiển thị mã `I21.0` thay vì `Nhồi máu cơ tim cấp thành trước` | **QĐ 4469/QĐ-BYT** — import CodeSystem ICD-10 tiếng Việt |
| `Condition.verificationStatus` | 🟠 | Không có trong QĐ 130+4750 | Không phân biệt `confirmed` / `provisional` → FHIR query `?verification-status=confirmed` trả kết quả sai | Mặc định `confirmed` cho chẩn đoán ra viện; `provisional` cho chẩn đoán vào |
| `Condition.clinicalStatus` | 🟠 | Không tường minh | FHIR yêu cầu clinicalStatus khi Condition không phải encounter-diagnosis | Map từ `KET_QUA_DTRI`: 1/2→`resolved`; 3/4/7→`active`; 5→`inactive`; 6→`active` |
| `Condition.severity` | 🟡 | Không có trong QĐ 130+4750 | Không phân tích được bệnh nhẹ/vừa/nặng | Suy luận từ `KET_QUA_DTRI` + `MA_LOAI_RV`; hoặc từ B5.DIEN_BIEN_LS (NLP) |
| `Condition.onsetDateTime` | 🟡 | Không có ngày khởi phát bệnh | Không tính được thời gian từ khởi phát đến nhập viện | Xấp xỉ bằng `NGAY_VAO` — không chính xác cho bệnh mạn tính |
| `Condition.asserter` | 🟢 | `MA_TTDV` chỉ là người đứng đầu, không phải BS chẩn đoán | Không trace được BS nào đưa ra chẩn đoán | Lấy từ `MA_BAC_SI` B2/B3 hoặc `NGUOI_THUC_HIEN` B3 |

### Nhận xét tổng thể

Condition có đủ mã ICD để phân tích dịch tễ cơ bản. Vấn đề lớn nhất là **thiếu tên bệnh** (cần CodeSystem) và **không có clinicalStatus tường minh** (phải suy luận). Điều này làm cho FHIR query chuẩn không trả đúng kết quả mà không qua lớp xử lý trung gian.

---

## 7. Claim + ClaimResponse

**Nguồn XML:** Bảng 1 (STT 44–55) + Bảng 2 + Bảng 3  
**Vai trò:** Thanh toán BHYT — dòng tiền từ BV → BHXH

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Claim.total` | `T_TONGCHI_BV` B1(47) | Tổng chi phí BV |
| `Claim.item[].net` (thuốc) | `THANH_TIEN_BV` B2(20) | Từng dòng thuốc |
| `Claim.item[].net` (DVKT) | `THANH_TIEN_BV` B3(19) | Từng dòng DVKT/VTYT |
| `Claim.item[].adjudication[benefit]` | `THANH_TIEN_BH` B2(21), B3(20) | Phần BHYT |
| `Claim.item[].adjudication[nsnn/vtnn/vttn/other]` | `T_NGUONKHAC_*` B2(22–26), B3(23–27) | Nguồn khác |
| `ClaimResponse.payment.amount` | `T_BHTT` B1(51) | BHXH thanh toán |
| `Coverage.costToBeneficiary` | `T_BNCCT` B1(50) | BN cùng chi trả |
| `Invoice.totalNet` | `T_BNTT` B1(49) | BN tự trả |
| `Claim.extension[bhtt-gdv]` | `T_BHTT_GDV` B1(53) | Ngoài định suất/DRG |
| `Claim.billablePeriod` | `NAM_QT` + `THANG_QT` B1(54,55) | Kỳ thanh toán |
| `Claim.extension[tt-thau]` | `TT_THAU` B2(15), B3(16) | Thông tin thầu |
| `Claim.extension[pham-vi]` | `PHAM_VI` B2(16), B3(12) | Phạm vi BHYT |
| `Claim.extension[tran-tt]` | `T_TRANTT` B3(21) | Trần thanh toán VTYT |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Claim.status` (phê duyệt / từ chối) | 🟠 | QĐ 130+4750 là dữ liệu gửi lên — kết quả phê duyệt từ BHXH không có trong XML | Không biết Claim nào bị từ chối/điều chỉnh sau khi BHXH xét duyệt | Nhận `ClaimResponse` từ Cổng BHXH sau quyết toán |
| `Claim.item[].adjudication[deductible]` | 🟡 | Không tách riêng phần khấu trừ | Không phân tích được bệnh lý nào có mức khấu trừ cao | Tính toán: `T_BNCCT` / `THANH_TIEN_BH` → tỷ lệ khấu trừ |
| `ClaimResponse.processNote` | 🟡 | Lý do từ chối / điều chỉnh từ BHXH | Không giải thích được tại sao Claim bị giảm | Từ Cổng BHXH sau quyết toán |
| `Claim.diagnosis[].diagnosisCodeableConcept` | 🟡 | Không có reference từ Claim về Condition | Claim và Condition không liên kết → khó join trong Power BI | Bổ sung khi tạo Claim: copy `MA_BENH_CHINH` → `Claim.diagnosis` |

---

## 8. MedicationRequest + Medication

**Nguồn XML:** Bảng 2 (38 trường)  
**Vai trò:** Đơn thuốc, danh mục thuốc

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `Medication.code.coding.code` | `MA_THUOC` B2(3) |
| `Medication.code.text` | `TEN_THUOC` B2(7) |
| `Medication.form` | `DANG_BAO_CHE` B2(11) |
| `Medication.ingredient[].strength` | `HAM_LUONG` B2(9) |
| `MedicationRequest.dosageInstruction[0].text` | `LIEU_DUNG` B2(12) |
| `MedicationRequest.dosageInstruction[0].route` | `DUONG_DUNG` B2(10) |
| `MedicationRequest.dosageInstruction[0].additionalInstruction` | `CACH_DUNG` B2(13) |
| `MedicationRequest.dispenseRequest.quantity` | `SO_LUONG` B2(18) |
| `MedicationRequest.dispenseRequest.unitPrice` | `DON_GIA` B2(19) |
| `MedicationRequest.authoredOn` | `NGAY_YL` B2(34) |
| `MedicationRequest.requester` | `MA_BAC_SI` B2(32) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Medication.code.coding.system` (ATC) | 🟠 | QĐ 130 dùng mã hoạt chất DMDC BYT, không dùng ATC quốc tế | Không thể so sánh / tra cứu quốc tế; không tích hợp được với hệ thống drug database | Map mã DMDC → ATC qua bảng tra cứu; hoặc bổ sung song song coding ATC |
| `Medication.code.coding.display` (tên INN) | 🟠 | Chỉ có tên thương mại, không có tên INN (International Nonproprietary Name) | Thuốc cùng hoạt chất từ các nhà sản xuất khác nhau không nhóm được | Lấy tên INN từ DMDC Cục QLD hoặc WHO drug database |
| `Medication.manufacturer` | 🟡 | Không có trong QĐ 130+4750 | Không phân tích được tỷ lệ thuốc ngoại/nội | Từ `SO_DANG_KY` B2(14) → tra cứu Cục QLD |
| `MedicationRequest.status` | 🟡 | Không tường minh trong QĐ 130+4750 | FHIR query `?status=completed` không chuẩn | Suy luận từ `NGAY_RA` B1(37): có → `completed`; không → `active` |
| `MedicationRequest.dosageInstruction[0].doseAndRate` (structured) | 🟢 | `LIEU_DUNG` là text tự do (vd: "2 viên/lần × 3 lần/ngày × 7 ngày") | Không tính được tổng liều hay so sánh liều chuẩn tự động | Parse text `LIEU_DUNG` theo regex → `doseQuantity` + `frequency` + `duration` |

---

## 9. ServiceRequest

**Nguồn XML:** Bảng 3 (STT 1–9, 11–13, 33, 35) + Checkin (MA_VAT_TU, MA_DICH_VU — QĐ4750)  
**Vai trò:** Chỉ định dịch vụ kỹ thuật, VTYT

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `ServiceRequest.code` | `MA_DICH_VU` B3(3) |
| `ServiceRequest.code.text` | `TEN_DICH_VU` B3(9) |
| `ServiceRequest.quantity` | `SO_LUONG` B3(13) |
| `ServiceRequest.authoredOn` | `NGAY_YL` B3(35) |
| `ServiceRequest.requester` | `MA_BAC_SI` B3(33) |
| `ServiceRequest.reasonCode` | `MA_BENH` B3 | Bệnh cần DVKT |
| `ServiceRequest.code` (VTYT) | `MA_VAT_TU` Checkin(23) — 🆕 QĐ4750 | |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `ServiceRequest.category` | 🔴 **Thiết yếu** | QĐ 130 không phân loại DVKT vào nhóm Lab/Imaging/Procedure | **Không GROUP BY được loại dịch vụ** (XN máu / CĐHA / Thủ thuật / Tiền khám / Tiền giường) | **Suy luận từ tiền tố MA_DICH_VU**: `09.*`→Laboratory; `10-28.*`→Imaging; `01-08.*`→Procedure; `TG.*`→Giường; `01.010.*`→Tiền khám |
| `ServiceRequest.code.coding.display` | 🟠 | QĐ 130+4750 không đi kèm tên DVKT trong `MA_DICH_VU` — chỉ có `TEN_DICH_VU` text | Tên DVKT có thể không nhất quán giữa các cơ sở | Chuẩn hóa từ DMDC QĐ 7603/QĐ-BYT (Phụ lục 1) |
| `ServiceRequest.intent` | 🟡 | Không có — tất cả đều là y lệnh thực tế | FHIR yêu cầu intent; thiếu → validation fail | Mặc định `order` |
| `ServiceRequest.priority` | 🟡 | Không có | Không phân biệt DVKT thường / khẩn | Suy luận: `MA_DOITUONG_KCB`=2 → `urgent`; còn lại → `routine` |

---

## 10. Procedure

**Nguồn XML:** Bảng 3 (STT 4, 34, 36–41) + Bảng 1 (STT 30)  
**Vai trò:** Phẫu thuật, thủ thuật đã thực hiện

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `Procedure.code.coding` (ICD-9CM) | `MA_PTTT_QT` B1(30), B3(4) |
| `Procedure.performer[0].actor` | `NGUOI_THUC_HIEN` B3(34) |
| `Procedure.performedDateTime` | `NGAY_TH_YL` B3(36) |
| `Procedure.extension[pp-vo-cam]` | `PP_VO_CAM` B3(40) | Gây mê/tê/châm tê |
| `Procedure.bodySite` | `VI_TRI_TH_DVKT` B3(41) | Vị trí thực hiện |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Procedure.code.coding.display` | 🔴 **Thiết yếu** | Mã ICD-9CM không có tên đi kèm | Báo cáo PT/TT chỉ hiển thị mã số | Import CodeSystem ICD-9-CM từ QĐ 4440/QĐ-BYT |
| `Procedure.outcome` | 🟠 | Không có kết quả PT/TT trong QĐ 130+4750 | Không phân tích được tỷ lệ thành công PT | Suy luận từ `KET_QUA_DTRI` B1(41) — chỉ xấp xỉ |
| `Procedure.complication[]` | 🟠 | Không có trong QĐ 130+4750 | Không theo dõi được biến chứng PT | Từ B5.DIEN_BIEN_LS (text tự do → NLP) hoặc mã ICD kèm Y83-Y84 |
| `Procedure.note[0].text` (kỹ thuật) | 🟡 | `PHAU_THUAT` B5(6) có nhưng là text tự do, không chuẩn hóa | Không search/filter được theo kỹ thuật mổ | Chuẩn hóa B5.PHAU_THUAT theo template PT/TT |
| `Procedure.usedCode` (VTYT dùng trong PT) | 🟡 | Phải JOIN B3(MA_DICH_VU) với B3(MA_VAT_TU) trong cùng MA_LK + GOI_VTYT | Không liên kết tường minh VTYT → PT | JOIN B3 theo `MA_LK` + `GOI_VTYT` để gán VTYT vào Procedure |

---

## 11. DiagnosticReport + Observation

**Nguồn XML:** Bảng 4 (12 trường)  
**Vai trò:** Kết quả xét nghiệm, CĐHA, thăm dò chức năng

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `DiagnosticReport.code` | `MA_DICH_VU` B4(3) |
| `DiagnosticReport.issued` | `NGAY_KQ` B4(10) |
| `DiagnosticReport.conclusion` | `KET_LUAN` B4(9) |
| `DiagnosticReport.resultsInterpreter` | `MA_BS_DOC_KQ` B4(11) |
| `Observation.code` | `MA_CHI_SO` B4(4) |
| `Observation.code.text` | `TEN_CHI_SO` B4(5) |
| `Observation.valueString` / `valueQuantity` | `GIA_TRI` B4(6) |
| `Observation.valueQuantity.unit` | `DON_VI_DO` B4(7) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Observation.referenceRange[]` | 🟠 | QĐ 130+4750 không lưu giá trị bình thường tham chiếu | Không tự động flag kết quả bất thường; không alert được | Từ máy xét nghiệm HIS (middleware LIS) kèm theo kết quả |
| `Observation.interpretation` | 🟠 | Không có flag H/L/N (cao/thấp/bình thường) | Power BI không tự phân loại được kết quả bất thường | Suy luận từ `referenceRange` khi có; hoặc từ LIS middleware |
| `DiagnosticReport.presentedForm` (file PDF/ảnh) | 🟡 | QĐ 130+4750 chỉ lưu text, không có file hình ảnh | Không attach được ảnh CĐHA, phim XQ, CT vào FHIR | PACS/DICOM server → `ImagingStudy` resource + DiagnosticReport.imagingStudy |
| `Observation.subject` + `encounter` | 🟡 | Phải JOIN qua `MA_LK` từ B4 lên B1 | Observation không tự link được về Patient / Encounter | Bổ sung khi tạo: `Observation.encounter = Encounter/{MA_LK}` |
| `Observation.effectiveDateTime` | 🟡 | `NGAY_KQ` là ngày có kết quả, không phải ngày lấy mẫu | Không tính được TAT (Turnaround Time) từ lấy mẫu đến có kết quả | Bổ sung `NGAY_TH_YL` B3(36) làm `effectiveDateTime`; `NGAY_KQ` làm `issued` |
| `ImagingStudy` (hình ảnh học) | 🟢 | Không có trong QĐ 130+4750 | Không liên kết được kết quả CĐHA với file hình ảnh DICOM | PACS server → `ImagingStudy` FHIR resource |

---

## 12. EpisodeOfCare

**Nguồn XML:** Bảng 1 (MA_LK, MA_HSBA, MA_BN, MA_CSKCB, NGAY_VAO, NGAY_RA, MA_BENH_CHINH)  
**Vai trò:** Hồ sơ bệnh án tổng thể — theo dõi BN qua nhiều đợt khám

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `EpisodeOfCare.id` | `MA_LK` B1(1) |
| `EpisodeOfCare.identifier[0]` | `MA_HSBA` B1(64) |
| `EpisodeOfCare.patient` | `MA_BN` B1(3) |
| `EpisodeOfCare.managingOrganization` | `MA_CSKCB` B1(58) |
| `EpisodeOfCare.period.start` | `NGAY_VAO` B1(35) |
| `EpisodeOfCare.period.end` | `NGAY_RA` B1(37) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `EpisodeOfCare.type` | 🟠 | Không có loại đợt chăm sóc chuẩn hóa | Không phân biệt EpisodeOfCare nội trú / ngoại trú / mạn tính | Map từ `MA_LOAI_KCB` → `EpisodeOfCare.type` |
| `EpisodeOfCare.team` | 🟡 | Không có reference đến CareTeam | Không biết đội điều trị của đợt bệnh | Lấy BS từ B2/B3 → tạo CareTeam |
| `EpisodeOfCare.account` | 🟡 | Không có tài khoản thanh toán liên kết | Khó trace chuỗi tài chính EpisodeOfCare → Account → Invoice | Tạo Account từ MA_LK + T_TONGCHI_BV |
| **EpisodeOfCare liên tục (bệnh mạn)** | 🟠 | Mỗi MA_LK tạo ra 1 EpisodeOfCare riêng — không có cơ chế nhóm nhiều đợt khám của cùng một bệnh | Không theo dõi được bệnh mạn tính (ĐTĐ, THA, ung thư...) qua nhiều lần KBCB | Thêm logic: cùng MA_BN + MA_BENH_CHINH trong vòng N ngày → link về 1 EpisodeOfCare gốc |

---

## 13. CodeSystem / ValueSet

**Nguồn XML:** Không có  
**Vai trò:** Nền tảng terminology — tất cả mã (ICD, DVKT, thuốc, VTYT) cần display name

### Trường còn thiếu — hoàn toàn

| CodeSystem | Mức độ | Mô tả thiếu | Nguồn bổ sung |
|---|:---:|---|---|
| **ICD-10 tiếng Việt** | 🔴 **Thiết yếu** | Toàn bộ tên bệnh tiếng Việt (~14.000 mã) | **QĐ 4469/QĐ-BYT** (28/10/2020) |
| **ICD-9-CM** (PT/TT) | 🔴 **Thiết yếu** | Tên phẫu thuật/thủ thuật quốc tế | **QĐ 4440/QĐ-BYT** |
| **DMDC DVKT** (QĐ 7603) | 🟠 | Tên chuẩn 30.000+ dịch vụ kỹ thuật | **QĐ 7603/QĐ-BYT** (Phụ lục 1) |
| **DMDC thuốc/hoạt chất** | 🟠 | Tên INN, ATC code, nhà sản xuất | **Cục Quản lý Dược** / WHO ATC |
| **DMDC VTYT** (QĐ 5086) | 🟡 | Tên chuẩn VTYT, nhóm VTYT | **QĐ 5086/QĐ-BYT** |
| **DMDC mã khoa** (QĐ 5937 PL5) | 🟠 | Tên đầy đủ 200+ khoa lâm sàng | **QĐ 5937/QĐ-BYT Phụ lục 5** |
| **DMDC mã BV** (QĐ 5937 PL4) | 🔴 **Thiết yếu** | Tên đầy đủ ~1.500 CSKCB | **QĐ 5937/QĐ-BYT Phụ lục 4** |
| **YHCT** | 🟡 | Tên bệnh Y học cổ truyền | **QĐ 26/2022/QĐ-BYT** |
| **Mã dân tộc** | 🟡 | Tên 54 dân tộc | QĐ 121-TCTK/PPCĐ |
| **Mã nghề nghiệp** | 🟢 | Tên nghề nghiệp | QĐ 34/2020/QĐ-TTg |

### Nhận xét tổng thể

CodeSystem/ValueSet là **nhóm thiếu có tác động lan rộng nhất**. Không có CodeSystem → mọi mã trong hệ thống (bệnh, DVKT, thuốc, BV, khoa) chỉ là chuỗi số/ký tự không có nghĩa hiển thị. Đây là điều kiện nền tảng phải có trước khi vận hành hệ thống.

---

## 14. Practitioner

**Nguồn XML:** `MA_BAC_SI` B2(32), B3(33) / `NGUOI_THUC_HIEN` B3(34) / `MA_BS_DOC_KQ` B4(11) / `MA_TTDV` B1(65)  
**Vai trò:** Nhân sự y tế — bác sĩ kê đơn, thực hiện, ký chứng từ

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn | Ghi chú |
|---|---|---|
| `Practitioner.identifier[bhxh].value` | `MA_BAC_SI` B2/B3, `MA_TTDV` B1 | Chỉ có mã định danh y tế (mã BHXH) |
| `Practitioner.identifier[bhxh].value` | `MA_BS_DOC_KQ` B4 | Bác sĩ đọc KQ |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Practitioner.name` | 🔴 **Thiết yếu** | QĐ 130+4750 chỉ truyền mã BHXH của bác sĩ | Báo cáo hiển thị mã số BS thay vì tên — không dùng được | **HIS module nhân sự** — tra cứu mã BS → tên đầy đủ |
| `Practitioner.qualification` | 🟠 | Không có bằng cấp, chuyên khoa trong QĐ 130+4750 | Không phân tích được theo chuyên khoa BS; không biết BS có thẩm quyền gì | HIS / Cục QLKCB (Bộ YT) — dữ liệu hành nghề |
| `PractitionerRole` | 🟠 | Không có role: BS thuộc khoa nào, chức danh gì | Không biết BS thuộc khoa Tim mạch hay Ngoại khoa → không phân tích workload theo khoa | HIS: `PractitionerRole.organization` = MA_KHOA; `PractitionerRole.code` = chức danh |
| `Practitioner.telecom` | 🟢 | Không có | Không có thông tin liên hệ BS | HIS module nhân sự |

---

## 15. ChargeItem

**Nguồn XML:** Bảng 2 + Bảng 3 (trường giá, số lượng, ngày phát sinh)  
**Vai trò:** Khoản phí chi tiết theo ngày — phân tích chi phí time-series

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `ChargeItem.occurrenceDateTime` | `NGAY_YL` B2(34), B3(35) |
| `ChargeItem.quantity` | `SO_LUONG` B2(18), B3(13) |
| `ChargeItem.priceOverride` | `DON_GIA_BV` B3(14), `DON_GIA` B2(19) |
| `ChargeItem.totalPriceComponent` | `THANH_TIEN_BV` B2(20), B3(19) |
| `ChargeItem.performingOrganization` | `MA_KHOA` B2(31), B3(31) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `ChargeItem.definitionUri` | 🟡 | Không có link đến định nghĩa dịch vụ | Không lookup được thông tin chi tiết DVKT từ ChargeItem | Link đến `ServiceRequest.id` cùng MA_LK + STT |
| `ChargeItem.factorOverride` | 🟡 | `TYLE_TT_DV` B3(17) chỉ là tỷ lệ đặc biệt (nằm ghép, khám lần 2...) | Không encode được hệ số điều chỉnh giá theo FHIR chuẩn | Map `TYLE_TT_DV` → `ChargeItem.factorOverride` khi ≠ 100 |
| `ChargeItem.account` | 🟡 | Không có | Không liên kết ChargeItem → Account → Invoice chuỗi FHIR chuẩn | Tạo Account từ MA_LK; gán `ChargeItem.account` = Account |

---

## 16. DocumentReference + Composition

**Nguồn XML:** Bảng 7 (giấy ra viện) + Bảng 8 (tóm tắt HSBA)  
**Vai trò:** Tài liệu lâm sàng — discharge summary

### Trường đã có từ XML

| Trường FHIR | Trường XML nguồn |
|---|---|
| `DocumentReference.description` | `CHAN_DOAN_RV` B7(11) |
| `DocumentReference.extension[pp-dieu-tri]` | `PP_DIEUTRI` B7(12) |
| `DocumentReference.note` | `GHI_CHU` B7(13) |
| `DocumentReference.date` | `NGAY_CT` B7(17) |
| `Composition.section[clinical-history]` | `QT_BENHLY` B8(11) |
| `Composition.section[discharge]` | `CHAN_DOAN_RV` B8(10) |
| `Composition.section[treatment]` | `PP_DIEUTRI` B8(13) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `DocumentReference.content[0].attachment.data` | 🟡 | QĐ 130+4750 chỉ lưu text; không lưu file PDF giấy ra viện có chữ ký số | Không có bản điện tử đầy đủ pháp lý | HIS xuất PDF có chữ ký số → base64 → `attachment.data` |
| `DocumentReference.securityLabel` | 🟡 | Không có nhãn bảo mật (đặc biệt B6 HIV) | Dữ liệu HIV nhạy cảm không có mã bảo mật | Thêm `securityLabel = restricted` cho Bảng 6 (HIV/AIDS) |
| `Composition.author` (bác sĩ ký HSBA) | 🟠 | `MA_TTDV` B8(19) là người đứng đầu, `MA_BS` B7(15) là BS ký | Chưa tách rõ author theo từng section | Gán `Composition.author` = Practitioner/{MA_BS} từ B7/B8 |

---

## 17. Device

**Nguồn XML:** Bảng 3 (MA_MAY, MA_HIEU_SP, TAI_SU_DUNG)  
**Vai trò:** Thiết bị y tế, VTYT

### Trường đã có từ XML QĐ 130 + 4750

| Trường FHIR | Trường XML nguồn |
|---|---|
| `Device.identifier[serial]` | `MA_MAY` B3(42) |
| `Device.identifier[model]` | `MA_HIEU_SP` B3(43) |
| `Device.extension[tai-su-dung]` | `TAI_SU_DUNG` B3(44) |

### Trường còn thiếu

| Trường FHIR | Mức độ | Lý do thiếu | Tác động | Đề xuất bổ sung |
|---|:---:|---|---|---|
| `Device.type` (loại thiết bị) | 🟠 | `MA_MAY` mã hóa loại trong tiền tố (HH/SA/XQ/MRI...) nhưng không tường minh | Không phân loại được thiết bị → không thống kê lượt sử dụng theo loại máy | Parse tiền tố MA_MAY: `HH.*`=Huyết học; `SA.*`=Siêu âm; `XQ.*`=XQ; `MRI.*`=MRI; `CL.*`=CLS |
| `Device.status` | 🟡 | Không có trạng thái máy | Không biết máy đang active hay ngừng sử dụng | Mặc định `active`; HIS cập nhật khi bảo dưỡng |
| `Device.owner` | 🟡 | `MA_MAY` có mã nguồn kinh phí (NSNN/XHH) nhưng không có Organization owner | Không biết thiết bị thuộc BV nào, khoa nào | Parse `MA_MAY`: `n=1`→NSNN, `n=2`→XHH, `n=3`→khác; `YYYYY`=mã BV → `Device.owner` |
| `Device.expirationDate` | 🟢 | Không có trong QĐ 130+4750 | Không cảnh báo VTYT hết hạn sử dụng | Từ module kho vật tư HIS |

---

## Phần Tổng Hợp — Ma Trận Ưu Tiên Bổ Sung

### Nhóm A — Bắt buộc bổ sung (Không có → hệ thống không vận hành được)

| Dữ liệu cần bổ sung | Resource FHIR đích | Nguồn | Phương thức nạp |
|---|---|---|---|
| **Tên BV đầy đủ + hạng BV** | `Organization.name` + `Organization.type` | DMDC QĐ 5937/QĐ-BYT Phụ lục 4 | `POST /Organization` bulk transaction |
| **Tên Khoa đầy đủ** | `Organization.name` (dept) | DMDC QĐ 5937/QĐ-BYT Phụ lục 5 | `POST /Organization` bulk transaction |
| **CodeSystem ICD-10 tiếng Việt** (~14.000 mã) | `CodeSystem` + `ValueSet` | QĐ 4469/QĐ-BYT | `PUT /CodeSystem/icd-10-vn` |
| **Tổng số giường kế hoạch** | `Location` (physicalType=bd) | HIS module quản lý giường | `POST /Location` bulk |

### Nhóm B — Quan trọng (Không có → báo cáo thiếu chiều phân tích chính)

| Dữ liệu cần bổ sung | Resource FHIR đích | Nguồn | Phương thức nạp |
|---|---|---|---|
| **CodeSystem ICD-9-CM** (PT/TT) | `CodeSystem` | QĐ 4440/QĐ-BYT | `PUT /CodeSystem/icd-9-cm-vn` |
| **Tên DVKT chuẩn** (~30.000 dịch vụ) | `CodeSystem` / `ServiceRequest.code.display` | DMDC QĐ 7603/QĐ-BYT Phụ lục 1 | `PUT /CodeSystem/dvkt-vn` |
| **Tên BS + chuyên khoa** | `Practitioner.name` + `PractitionerRole` | HIS module nhân sự | `POST /Practitioner` + `POST /PractitionerRole` |
| **Tên thuốc INN + mã ATC** | `Medication.code.coding` (ATC) | Cục Quản lý Dược / WHO ATC | `PATCH /Medication/{id}` |
| **Coverage.beneficiary + payor** | `Coverage` (hoàn chỉnh) | Cổng BHXH API | `PATCH /Coverage/{id}` |
| **ServiceRequest.category** | `ServiceRequest` | Suy luận từ tiền tố MA_DICH_VU | Transform khi nạp B3 |

### Nhóm C — Nên có (Báo cáo chạy được nhưng chất lượng thấp hơn)

| Dữ liệu cần bổ sung | Resource FHIR đích | Nguồn | Phương thức nạp |
|---|---|---|---|
| Tên VTYT chuẩn (QĐ 5086) | `Device.type` / `ServiceRequest.code.display` | DMDC QĐ 5086/QĐ-BYT | `PUT /CodeSystem/vtyt-vn` |
| Kết quả phê duyệt BHXH | `ClaimResponse.status` + `processNote` | Cổng BHXH sau quyết toán | `PUT /ClaimResponse/{id}` |
| Observation.referenceRange | `Observation` (XN) | LIS middleware | `PATCH /Observation/{id}` |
| Phân cấp giường → phòng → khoa | `Location.partOf` chain | HIS cây phân cấp vị trí | `PATCH /Location/{id}` |
| Patient.name tách họ/tên | `Patient.name.family` + `given[]` | Xử lý NLP/regex từ HO_TEN | Transform khi nạp B1 |
| CodeSystem YHCT | `CodeSystem` | QĐ 26/2022/QĐ-BYT | `PUT /CodeSystem/yhct-vn` |
| EpisodeOfCare liên tục (bệnh mạn) | `EpisodeOfCare` | Logic: cùng MA_BN + MA_BENH_CHINH | Xử lý sau khi nạp B1 |

### Nhóm D — Tốt hơn nếu có (Phân tích nâng cao)

| Dữ liệu cần bổ sung | Resource FHIR đích | Nguồn | Ghi chú |
|---|---|---|---|
| Hình ảnh DICOM từ PACS | `ImagingStudy` | PACS/DICOM server | Cần tích hợp PACS với FHIR server |
| Dấu hiệu sinh tồn chuẩn hóa | `Observation` (LOINC) | Parse B5.DIEN_BIEN_LS (NLP) hoặc HIS | Khó — B5 là text tự do |
| File PDF giấy ra viện có chữ ký số | `DocumentReference.attachment` | HIS xuất PDF | PKI/chữ ký số |
| Biến chứng PT | `Condition` (complication) | B5 text → NLP hoặc ICD Y83-Y84 | Cần đầu tư NLP |
| Lịch sử bệnh mạn tính nhiều năm | `Condition` (chronic) | Hệ thống HIS lịch sử + cổng dữ liệu y tế quốc gia | Phụ thuộc tích hợp ngoài BV |

---

## Kết Luận

Sau khi import toàn bộ XML QĐ 130+4750, hệ thống FHIR có **dữ liệu lâm sàng giao dịch đầy đủ** nhưng **thiếu nền tảng terminology và master data**. Cụ thể:

**Điểm mạnh từ QĐ 130 + 4750:**
- `Patient`, `Encounter`, `Claim`, `MedicationRequest` đạt mức hoàn chỉnh 70–80%
- QĐ 4750 bổ sung đáng kể: `NGAY_VAO_NOI_TRU` cải thiện Census nội trú; `LY_DO_VNT` + `MA_LY_DO_VNT` chuẩn hóa lý do nhập viện; `NHOM_MAU` thêm chiều phân tích mới; 5 trường chi phí đầu tiên giúp nhận diện sớm loại KBCB qua Checkin

**Hai khoảng trống cốt lõi cần giải quyết:**
1. **Terminology** — Không có tên hiển thị cho bất kỳ mã nào (ICD, DVKT, thuốc, BV, khoa). Đây là vấn đề nền tảng ảnh hưởng đến toàn bộ 23 báo cáo.
2. **Master data tổ chức** — `Organization` và `Location` chỉ có mã, không có tên, không có phân cấp. Không thể làm báo cáo có nhãn có nghĩa.

**Thứ tự ưu tiên hành động:**
```
1. Nạp Organization (BV + Khoa) từ DMDC QĐ 5937       → unlock 18/23 báo cáo
2. Nạp CodeSystem ICD-10 từ QĐ 4469                    → unlock BC03, BC16, BC18
3. Nạp Location kế hoạch giường từ HIS                 → unlock BC05
4. Nạp Practitioner từ HIS nhân sự                     → cải thiện BC10, BC15, BC17
5. Nạp CodeSystem ICD-9-CM, DVKT, thuốc ATC             → nâng chất lượng toàn hệ thống
```

---

*Báo cáo phân tích FHIR Resource — Góc nhìn kỹ thuật*  
*Căn cứ: QĐ 130/QĐ-BYT (2023) + QĐ 4750/QĐ-BYT (2023) + HL7 FHIR R4B (4.3.0)*
