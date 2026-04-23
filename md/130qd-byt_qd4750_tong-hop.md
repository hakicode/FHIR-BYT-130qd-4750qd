# TÀI LIỆU TỔNG HỢP DỮ LIỆU XML THEO QĐ 130/QĐ-BYT VÀ QĐ 4750/QĐ-BYT

Bản này lấy [130qd-byt.md](130qd-byt.md) làm gốc và hợp nhất các nội dung sửa đổi, bổ sung tại Quyết định số 4750/QĐ-BYT ngày 29/12/2023. Các trường và bảng không liệt kê lại ở đây được hiểu là giữ nguyên theo file gốc.

## 1. Mốc áp dụng

- Bảng check-in chỉ dùng để thông báo trạng thái khám bệnh, chữa bệnh, không dùng làm căn cứ giám định, thanh toán, quyết toán chi phí BHYT.
- Cơ sở khám bệnh, chữa bệnh gửi Bảng check-in ngay sau khi có phát sinh chi phí khám bệnh, chữa bệnh đầu tiên của người bệnh.
- Đối với trường hợp người bệnh được chỉ định vào điều trị nội trú, nội trú ban ngày hoặc điều trị ngoại trú, cơ sở khám bệnh, chữa bệnh gửi Bảng check-in ngay sau khi có phát sinh chi phí của dịch vụ đầu tiên tại khoa điều trị nội trú, khoa điều trị nội trú ban ngày hoặc khoa điều trị ngoại trú.
- Không cần gửi Bảng check-in trong trường hợp cấp cứu có `MA_DOITUONG_KCB = 2` hoặc cơ sở tiếp nhận người bệnh, mẫu bệnh phẩm để thực hiện dịch vụ cận lâm sàng.
- Việc kiểm thử dữ liệu điện tử theo định dạng XML được thực hiện theo mốc hiệu lực của QĐ 4750; việc gửi và nhận dữ liệu chính thức áp dụng từ ngày 01/07/2024.
- Quyết định số 4210/QĐ-BYT chấm dứt hiệu lực liên quan đến bộ bảng dữ liệu này kể từ ngày 01/07/2024.

## 2. Điều khoản cập nhật

| Điều | Nội dung hợp nhất |
|---|---|
| Điều 2 khoản 1 | Bảng check-in chỉ dùng để thông báo trạng thái, không dùng làm căn cứ giám định, thanh toán, quyết toán BHYT. |
| Điều 3 khoản 1 | Gửi check-in ngay sau khi có phát sinh chi phí đầu tiên; với nội trú, nội trú ban ngày hoặc ngoại trú, gửi ngay sau khi có phát sinh chi phí của dịch vụ đầu tiên tại khoa điều trị tương ứng. |
| Điều 3 khoản 1 (ngoại lệ) | Không gửi check-in cho cấp cứu (`MA_DOITUONG_KCB = 2`) và không gửi cho cơ sở chỉ tiếp nhận người bệnh hoặc mẫu bệnh phẩm để làm cận lâm sàng. |
| Điều 4 khoản 3-5 | Mốc kiểm thử và mốc áp dụng chính thức được cập nhật sang 01/04/2024 và 01/07/2024; Quyết định số 4210/QĐ-BYT dừng từ 01/07/2024. |

## 3. Bảng chỉ tiêu dữ liệu về trạng thái khám bệnh, chữa bệnh

| STT | Chỉ tiêu | QĐ130 | QĐ4750 | Tình trạng | Ghi chú |
|---:|---|---|---|---|---|
| 1 | MA_LK | Chuỗi(100) | Chuỗi(100) | Không đổi | Mã đợt điều trị duy nhất |
| 2 | STT | Số(10) | Số(10) | Không đổi | Số thứ tự gửi dữ liệu |
| 3 | MA_BN | Chuỗi(100) | Chuỗi(100) | Không đổi | Mã người bệnh |
| 4 | HO_TEN | Chuỗi(255) | Chuỗi(255) | Không đổi | Họ tên người bệnh |
| 5 | SO_CCCD | Số(15) | Chuỗi(15) | Sửa kiểu dữ liệu | Giữ số 0 đầu; cho phép dùng mã tài khoản định danh điện tử |
| 6 | NGAY_SINH | Chuỗi(12) | Chuỗi(12) | Không đổi | Định dạng yyyymmddHHMM |
| 7 | GIOI_TINH | Số(1) | Số(1) | Không đổi | 1: Nam; 2: Nữ; 3: Chưa xác định |
| 8 | MA_THE_BHYT | Chuỗi(15) | Chuỗi(15) | Không đổi | Mã thẻ BHYT |
| 9 | MA_DKBD | Chuỗi(5) | Chuỗi(5) | Không đổi | Mã cơ sở đăng ký ban đầu |
| 10 | GT_THE_TU | Chuỗi(8) | Chuỗi(8) | Không đổi | Ngày bắt đầu có giá trị sử dụng |
| 11 | GT_THE_DEN | Chuỗi(8) | Chuỗi(8) | Không đổi | Ngày hết giá trị sử dụng |
| 12 | MA_DOITUONG_KCB | Số(1) | Chuỗi(4) | Sửa kiểu dữ liệu, tăng kích thước | Mã đối tượng đến KBCB |
| 13 | NGAY_VAO | Chuỗi(12) | Chuỗi(12) | Không đổi | Thời điểm người bệnh đến KBCB |
| 14 | NGAY_VAO_NOI_TRU | - | Chuỗi(12) | Trường mới | Thời điểm chỉ định vào điều trị nội trú, nội trú ban ngày hoặc điều trị ngoại trú |
| 15 | LY_DO_VNT | - | Chuỗi(1024) | Trường mới | Lý do vào nội trú hoặc điều trị ngoại trú |
| 16 | MA_LY_DO_VNT | - | Chuỗi(5) | Trường mới | Mã lý do người bệnh vào điều trị nội trú |
| 17 | MA_LOAI_KCB | Số(2) | Chuỗi(2) | Sửa kiểu dữ liệu | Mã hình thức KBCB |
| 18 | MA_CSKCB | Chuỗi(5) | Chuỗi(5) | Không đổi | Mã cơ sở KBCB |
| 19 | MA_DICH_VU | Chuỗi(50) | Chuỗi(50) | Sửa diễn giải | Chỉ ghi khi phát sinh chi phí đầu tiên tại khoa điều trị là DVKT hoặc tiền khám |
| 20 | TEN_DICH_VU | Chuỗi(1024) | Chuỗi(1024) | Sửa diễn giải | Tên tương ứng với MA_DICH_VU |
| 21 | MA_THUOC | - | Chuỗi(255) | Trường mới | Mã hoạt chất của thuốc |
| 22 | TEN_THUOC | - | Chuỗi(1024) | Trường mới | Tên thuốc tương ứng |
| 23 | MA_VAT_TU | - | Chuỗi(255) | Trường mới | Mã vật tư y tế |
| 24 | TEN_VAT_TU | - | Chuỗi(1024) | Trường mới | Tên vật tư y tế |
| 25 | NGAY_YL | Chuỗi(12) | Chuỗi(12) | Không đổi | Thời điểm ra y lệnh |
| 26 | DU_PHONG | - | Chuỗi(n) | Trường mới | Dữ liệu dự phòng |

Các trường 1-4, 6-11, 13, 18 và 25 giữ nguyên. Các trường còn lại của Bảng này không thay đổi so với [130qd-byt.md](130qd-byt.md).

## 4. Bảng 1. Chỉ tiêu tổng hợp khám bệnh, chữa bệnh

> QĐ 4750 chèn thêm trường `NHOM_MAU` ngay sau `GIOI_TINH`, vì vậy thứ tự các trường phía sau dịch xuống một bậc so với QĐ 130.

| STT | Chỉ tiêu | QĐ130 | QĐ4750 | Tình trạng | Ghi chú |
|---:|---|---|---|---|---|
| 1 | MA_LK | Chuỗi(100) | Chuỗi(100) | Không đổi | Mã đợt điều trị duy nhất |
| 2 | STT | Số(10) | Số(10) | Không đổi | Số thứ tự gửi dữ liệu |
| 3 | MA_BN | Chuỗi(100) | Chuỗi(100) | Không đổi | Mã người bệnh |
| 4 | HO_TEN | Chuỗi(255) | Chuỗi(255) | Không đổi | Họ tên người bệnh |
| 5 | SO_CCCD | Số(15) | Chuỗi(15) | Sửa kiểu dữ liệu | Giữ số 0 đầu |
| 6 | NGAY_SINH | Chuỗi(12) | Chuỗi(12) | Không đổi | Định dạng yyyymmddHHMM |
| 7 | GIOI_TINH | Số(1) | Số(1) | Không đổi | 1: Nam; 2: Nữ; 3: Chưa xác định |
| 8 | NHOM_MAU | - | Chuỗi(5) | Trường mới | Nhóm máu của người bệnh nếu có thông tin |
| 9 | MA_QUOCTICH | Số(3) | Chuỗi(3) | Sửa kiểu dữ liệu | Mã quốc tịch |
| 10 | MA_DANTOC | Số(2) | Chuỗi(2) | Sửa kiểu dữ liệu | Mã dân tộc |
| 11 | MA_NGHE_NGHIEP | Số(5) | Chuỗi(5) | Sửa kiểu dữ liệu | Mã nghề nghiệp |
| 12 | DIA_CHI | Chuỗi(1024) | Chuỗi(1024) | Chuẩn hóa diễn giải | Địa chỉ nơi cư trú hiện tại |
| 13 | MATINH_CU_TRU | Chuỗi(3) | Chuỗi(3) | Không đổi | Mã tỉnh cư trú |
| 14 | MAHUYEN_CU_TRU | Chuỗi(3) | Chuỗi(3) | Bổ sung diễn giải | Dùng mã mới khi thành lập hoặc gộp đơn vị hành chính cấp huyện |
| 15 | MAXA_CU_TRU | Chuỗi(5) | Chuỗi(3) | Giảm kích thước tối đa | Dùng mã mới khi thành lập hoặc gộp đơn vị hành chính cấp xã |
| 16 | DIEN_THOAI | Số(15) | Chuỗi(15) | Sửa kiểu dữ liệu | Số điện thoại liên lạc |

Các trường từ STT 17 trở đi của Bảng 1 giữ nguyên theo [130qd-byt.md](130qd-byt.md), gồm cả `MA_THE_BHYT`, `MA_DKBD`, `GT_THE_TU`, `GT_THE_DEN` và toàn bộ phần còn lại của bảng.

## 5. Các bảng 2-12

- Bảng 2, Bảng 3, Bảng 4, Bảng 5, Bảng 6, Bảng 7, Bảng 8, Bảng 9, Bảng 10, Bảng 11 và Bảng 12 không bị sửa đổi bởi QĐ 4750.
- Nội dung chi tiết của các bảng này được giữ nguyên theo [130qd-byt.md](130qd-byt.md).