# Báo Cáo Mapping Trường Dữ Liệu XML BHYT
## Đối chiếu với Quyết định 130/QĐ-BYT (hợp nhất QĐ 4750/QĐ-BYT)

> **Phạm vi:** So sánh danh sách thẻ XML trong từng file XML với danh sách chỉ tiêu dữ liệu trong bảng quyết định tương ứng.  
> **Cơ sở pháp lý:** Quyết định số 130/QĐ-BYT ngày 18/01/2023 và Quyết định số 4750/QĐ-BYT ngày 29/12/2023.  
> **Quy ước trạng thái:** ✅ Khớp | ⚠️ Lệch (có trường thừa/thiếu) | ❌ Không có bảng quy định tương ứng

---

## Tổng quan kết quả

| File XML | Tên | Bảng QĐ | Số trường QĐ | Số trường XML | Trạng thái |
|---|---|---|:---:|:---:|:---:|
| XML0 | Trạng thái KCB (Check-in) | Bảng Check-in | 26 | 26 | ✅ |
| XML1 | Tổng hợp KCB | Bảng 1 | 66 | 66 | ✅ |
| XML2 | Chi tiết thuốc | Bảng 2 | 38 | 38 | ✅ |
| XML3 | Chi tiết DVKT & VTYT | Bảng 3 | 45+2* | 45 | ✅ |
| XML4 | Chi tiết cận lâm sàng | Bảng 4 | 12 | 12 | ✅ |
| XML5 | Diễn biến lâm sàng | Bảng 5 | 9 | 9 | ✅ |
| XML6 | Hồ sơ HIV/AIDS | Bảng 6 | 31 | 45 | ⚠️ |
| XML7 | Giấy ra viện | Bảng 7 | 25 | 25 | ✅ |
| XML8 | Tóm tắt hồ sơ bệnh án | Bảng 8 | 22 | 22 | ✅ |
| XML9 | Giấy chứng sinh | Bảng 9 | 34 | 34 | ✅ |
| XML10 | Giấy nghỉ dưỡng thai | Bảng 10 | 12 | 13 | ⚠️ |
| XML11 | Giấy nghỉ hưởng BHXH | Bảng 11 | 22 | 22 | ✅ |
| XML13 | Giấy chuyển tuyến | — | — | — | ❌ |
| XML14 | Giấy hẹn khám lại | — | — | — | ❌ |
| XML15 | Chi tiết điều trị bệnh lao | — | — | — | ❌ |

> *2 trường bổ sung theo QĐ4750 được đánh dấu `—` thay vì số thứ tự trong bảng quyết định.

---

## XML0 — Bảng Check-in (Trạng thái KCB)

**Kết quả: ✅ Khớp hoàn toàn (26/26 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML0 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | STT | Số | 10 | ✅ |
| 3 | MA_BN | Chuỗi | 100 | ✅ |
| 4 | HO_TEN | Chuỗi | 255 | ✅ |
| 5 | SO_CCCD | Chuỗi | 15 | ✅ |
| 6 | NGAY_SINH | Chuỗi | 12 | ✅ |
| 7 | GIOI_TINH | Số | 1 | ✅ |
| 8 | MA_THE_BHYT | Chuỗi | 15 | ✅ |
| 9 | MA_DKBD | Chuỗi | 5 | ✅ |
| 10 | GT_THE_TU | Chuỗi | 8 | ✅ |
| 11 | GT_THE_DEN | Chuỗi | 8 | ✅ |
| 12 | MA_DOITUONG_KCB | Chuỗi | 4 | ✅ |
| 13 | NGAY_VAO | Chuỗi | 12 | ✅ |
| 14 | NGAY_VAO_NOI_TRU | Chuỗi | 12 | ✅ |
| 15 | LY_DO_VNT | Chuỗi | 1024 | ✅ |
| 16 | MA_LY_DO_VNT | Chuỗi | 5 | ✅ |
| 17 | MA_LOAI_KCB | Chuỗi | 2 | ✅ |
| 18 | MA_CSKCB | Chuỗi | 5 | ✅ |
| 19 | MA_DICH_VU | Chuỗi | 50 | ✅ |
| 20 | TEN_DICH_VU | Chuỗi | 1024 | ✅ |
| 21 | MA_THUOC | Chuỗi | 255 | ✅ |
| 22 | TEN_THUOC | Chuỗi | 1024 | ✅ |
| 23 | MA_VAT_TU | Chuỗi | 255 | ✅ |
| 24 | TEN_VAT_TU | Chuỗi | 1024 | ✅ |
| 25 | NGAY_YL | Chuỗi | 12 | ✅ |
| 26 | DU_PHONG | Chuỗi | n | ✅ |

---

## XML1 — Bảng 1 (Tổng hợp KCB)

**Kết quả: ✅ Khớp hoàn toàn (66/66 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML1 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | STT | Số | 10 | ✅ |
| 3 | MA_BN | Chuỗi | 100 | ✅ |
| 4 | HO_TEN | Chuỗi | 255 | ✅ |
| 5 | SO_CCCD | Chuỗi | 15 | ✅ |
| 6 | NGAY_SINH | Chuỗi | 12 | ✅ |
| 7 | GIOI_TINH | Số | 1 | ✅ |
| 8 | NHOM_MAU | Chuỗi | 5 | ✅ |
| 9 | MA_QUOCTICH | Chuỗi | 3 | ✅ |
| 10 | MA_DANTOC | Chuỗi | 2 | ✅ |
| 11 | MA_NGHE_NGHIEP | Chuỗi | 5 | ✅ |
| 12 | DIA_CHI | Chuỗi | 1024 | ✅ |
| 13 | MATINH_CU_TRU | Chuỗi | 3 | ✅ |
| 14 | MAHUYEN_CU_TRU | Chuỗi | 3 | ✅ |
| 15 | MAXA_CU_TRU | Chuỗi | 3 | ✅ |
| 16 | DIEN_THOAI | Chuỗi | 15 | ✅ |
| 17 | MA_THE_BHYT | Chuỗi | n | ✅ |
| 18 | MA_DKBD | Chuỗi | n | ✅ |
| 19 | GT_THE_TU | Chuỗi | n | ✅ |
| 20 | GT_THE_DEN | Chuỗi | n | ✅ |
| 21 | NGAY_MIEN_CCT | Chuỗi | 12 | ✅ |
| 22 | LY_DO_VV | Chuỗi | n | ✅ |
| 23 | LY_DO_VNT | Chuỗi | n | ✅ |
| 24 | MA_LY_DO_VNT | Chuỗi | 5 | ✅ |
| 25 | CHAN_DOAN_VAO | Chuỗi | n | ✅ |
| 26 | CHAN_DOAN_RV | Chuỗi | n | ✅ |
| 27 | MA_BENH_CHINH | Chuỗi | 7 | ✅ |
| 28 | MA_BENH_KT | Chuỗi | 100 | ✅ |
| 29 | MA_BENH_YHCT | Chuỗi | 255 | ✅ |
| 30 | MA_PTTT_QT | Chuỗi | 125 | ✅ |
| 31 | MA_DOITUONG_KCB | Chuỗi | 3 | ✅ |
| 32 | MA_NOI_DI | Chuỗi | 5 | ✅ |
| 33 | MA_NOI_DEN | Chuỗi | 5 | ✅ |
| 34 | MA_TAI_NAN | Số | 1 | ✅ |
| 35 | NGAY_VAO | Chuỗi | 12 | ✅ |
| 36 | NGAY_VAO_NOI_TRU | Chuỗi | 12 | ✅ |
| 37 | NGAY_RA | Chuỗi | 12 | ✅ |
| 38 | GIAY_CHUYEN_TUYEN | Chuỗi | 50 | ✅ |
| 39 | SO_NGAY_DTRI | Số | 3 | ✅ |
| 40 | PP_DIEU_TRI | Chuỗi | n | ✅ |
| 41 | KET_QUA_DTRI | Số | 1 | ✅ |
| 42 | MA_LOAI_RV | Số | 1 | ✅ |
| 43 | GHI_CHU | Chuỗi | n | ✅ |
| 44 | NGAY_TTOAN | Chuỗi | 12 | ✅ |
| 45 | T_THUOC | Số | 15 | ✅ |
| 46 | T_VTYT | Số | 15 | ✅ |
| 47 | T_TONGCHI_BV | Số | 15 | ✅ |
| 48 | T_TONGCHI_BH | Số | 15 | ✅ |
| 49 | T_BNTT | Số | 15 | ✅ |
| 50 | T_BNCCT | Số | 15 | ✅ |
| 51 | T_BHTT | Số | 15 | ✅ |
| 52 | T_NGUONKHAC | Số | 15 | ✅ |
| 53 | T_BHTT_GDV | Số | 15 | ✅ |
| 54 | NAM_QT | Số | 4 | ✅ |
| 55 | THANG_QT | Số | 2 | ✅ |
| 56 | MA_LOAI_KCB | Số | 2 | ✅ |
| 57 | MA_KHOA | Chuỗi | 50 | ✅ |
| 58 | MA_CSKCB | Chuỗi | 5 | ✅ |
| 59 | MA_KHUVUC | Chuỗi | 2 | ✅ |
| 60 | CAN_NANG | Chuỗi | 6 | ✅ |
| 61 | CAN_NANG_CON | Chuỗi | 100 | ✅ |
| 62 | NAM_NAM_LIEN_TUC | Chuỗi | 8 | ✅ |
| 63 | NGAY_TAI_KHAM | Chuỗi | 50 | ✅ |
| 64 | MA_HSBA | Chuỗi | 100 | ✅ |
| 65 | MA_TTDV | Chuỗi | 10 | ✅ |
| 66 | DU_PHONG | Chuỗi | n | ✅ |

---

## XML2 — Bảng 2 (Chi tiết thuốc)

**Kết quả: ✅ Khớp hoàn toàn (38/38 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML2 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | STT | Số | 10 | ✅ |
| 3 | MA_THUOC | Chuỗi | 255 | ✅ |
| 4 | MA_PP_CHEBIEN | Chuỗi | 255 | ✅ |
| 5 | MA_CSKCB_THUOC | Chuỗi | 10 | ✅ |
| 6 | MA_NHOM | Số | 2 | ✅ |
| 7 | TEN_THUOC | Chuỗi | 1024 | ✅ |
| 8 | DON_VI_TINH | Chuỗi | 50 | ✅ |
| 9 | HAM_LUONG | Chuỗi | 1024 | ✅ |
| 10 | DUONG_DUNG | Chuỗi | 4 | ✅ |
| 11 | DANG_BAO_CHE | Chuỗi | 1024 | ✅ |
| 12 | LIEU_DUNG | Chuỗi | 1024 | ✅ |
| 13 | CACH_DUNG | Chuỗi | 1024 | ✅ |
| 14 | SO_DANG_KY | Chuỗi | 255 | ✅ |
| 15 | TT_THAU | Chuỗi | 50 | ✅ |
| 16 | PHAM_VI | Số | 1 | ✅ |
| 17 | TYLE_TT_BH | Số | 3 | ✅ |
| 18 | SO_LUONG | Số | 10 | ✅ |
| 19 | DON_GIA | Số | 15 | ✅ |
| 20 | THANH_TIEN_BV | Số | 15 | ✅ |
| 21 | THANH_TIEN_BH | Số | 15 | ✅ |
| 22 | T_NGUONKHAC_NSNN | Số | 15 | ✅ |
| 23 | T_NGUONKHAC_VTNN | Số | 15 | ✅ |
| 24 | T_NGUONKHAC_VTTN | Số | 15 | ✅ |
| 25 | T_NGUONKHAC_CL | Số | 15 | ✅ |
| 26 | T_NGUONKHAC | Số | 15 | ✅ |
| 27 | MUC_HUONG | Số | 3 | ✅ |
| 28 | T_BNTT | Số | 15 | ✅ |
| 29 | T_BNCCT | Số | 15 | ✅ |
| 30 | T_BHTT | Số | 15 | ✅ |
| 31 | MA_KHOA | Chuỗi | 15 | ✅ |
| 32 | MA_BAC_SI | Chuỗi | 255 | ✅ |
| 33 | MA_DICH_VU | Chuỗi | 255 | ✅ |
| 34 | NGAY_YL | Chuỗi | 12 | ✅ |
| 35 | NGAY_TH_YL | Chuỗi | 12 | ✅ |
| 36 | MA_PTTT | Số | 1 | ✅ |
| 37 | NGUON_CTRA | Số | 1 | ✅ |
| 38 | VET_THUONG_TP | Số | 1 | ✅ |
| — | DU_PHONG | Chuỗi | n | ✅ |

> **Ghi chú:** Trường `DU_PHONG` trong XML2 là trường dự phòng chuẩn, không được đánh STT riêng trong Bảng 2 của quyết định nhưng vẫn được xem là hợp lệ theo thông lệ chung.

---

## XML3 — Bảng 3 (Chi tiết DVKT & VTYT)

**Kết quả: ✅ Khớp (45 trường quy định + 2 trường bổ sung từ QĐ4750)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML3 | Ghi chú |
|:---:|---|---|:---:|:---:|---|
| 1 | MA_LK | Chuỗi | 100 | ✅ | |
| 2 | STT | Số | 10 | ✅ | |
| 3 | MA_DICH_VU | Chuỗi | 50 | ✅ | |
| 4 | MA_PTTT_QT | Chuỗi | 255 | ✅ | |
| 5 | MA_VAT_TU | Chuỗi | 255 | ✅ | |
| 6 | MA_NHOM | Số | 2 | ✅ | |
| 7 | GOI_VTYT | Chuỗi | 3 | ✅ | |
| 8 | TEN_VAT_TU | Chuỗi | 1024 | ✅ | |
| 9 | TEN_DICH_VU | Chuỗi | 1024 | ✅ | |
| 10 | MA_XANG_DAU | Chuỗi | 20 | ✅ | |
| 11 | DON_VI_TINH | Chuỗi | 50 | ✅ | |
| 12 | PHAM_VI | Số | 1 | ✅ | |
| 13 | SO_LUONG | Số | 10 | ✅ | |
| 14 | DON_GIA_BV | Số | 15 | ✅ | |
| 15 | DON_GIA_BH | Số | 15 | ✅ | |
| 16 | TT_THAU | Chuỗi | 25 | ✅ | |
| 17 | TYLE_TT_DV | Số | 3 | ✅ | |
| 18 | TYLE_TT_BH | Số | 3 | ✅ | |
| 19 | THANH_TIEN_BV | Số | 15 | ✅ | |
| 20 | THANH_TIEN_BH | Số | 15 | ✅ | |
| 21 | T_TRANTT | Số | 15 | ✅ | |
| 22 | MUC_HUONG | Số | 3 | ✅ | |
| 23 | T_NGUONKHAC_NSNN | Số | 15 | ✅ | |
| 24 | T_NGUONKHAC_VTNN | Số | 15 | ✅ | |
| 25 | T_NGUONKHAC_VTTN | Số | 15 | ✅ | |
| 26 | T_NGUONKHAC_CL | Số | 15 | ✅ | |
| 27 | T_NGUONKHAC | Số | 15 | ✅ | |
| 28 | T_BNTT | Số | 15 | ✅ | |
| 29 | T_BNCCT | Số | 15 | ✅ | |
| 30 | T_BHTT | Số | 15 | ✅ | |
| 31 | MA_KHOA | Chuỗi | 20 | ✅ | |
| 32 | MA_GIUONG | Chuỗi | 50 | ✅ | |
| 33 | MA_BAC_SI | Chuỗi | 255 | ✅ | |
| 34 | NGUOI_THUC_HIEN | Chuỗi | 255 | ✅ | |
| — | MA_BENH | Chuỗi | 100 | ✅ | Bổ sung QĐ4750, không đánh STT |
| — | MA_BENH_YHCT | Chuỗi | 255 | ✅ | Bổ sung QĐ4750, không đánh STT |
| 35 | NGAY_YL | Chuỗi | 12 | ✅ | |
| 36 | NGAY_TH_YL | Chuỗi | 12 | ✅ | |
| 37 | NGAY_KQ | Chuỗi | 12 | ✅ | |
| 38 | MA_PTTT | Số | 1 | ✅ | |
| 39 | VET_THUONG_TP | Số | 1 | ✅ | |
| 40 | PP_VO_CAM | Số | 1 | ✅ | |
| 41 | VI_TRI_TH_DVKT | Số | 3 | ✅ | |
| 42 | MA_MAY | Chuỗi | 1024 | ✅ | |
| 43 | MA_HIEU_SP | Chuỗi | 255 | ✅ | |
| 44 | TAI_SU_DUNG | Số | 1 | ✅ | |
| 45 | DU_PHONG | Chuỗi | n | ✅ | |

---

## XML4 — Bảng 4 (Chi tiết cận lâm sàng)

**Kết quả: ✅ Khớp hoàn toàn (12/12 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML4 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | STT | Số | 10 | ✅ |
| 3 | MA_DICH_VU | Chuỗi | 15 | ✅ |
| 4 | MA_CHI_SO | Chuỗi | 50 | ✅ |
| 5 | TEN_CHI_SO | Chuỗi | 255 | ✅ |
| 6 | GIA_TRI | Chuỗi | 50 | ✅ |
| 7 | DON_VI_DO | Chuỗi | 50 | ✅ |
| 8 | MO_TA | Chuỗi | n | ✅ |
| 9 | KET_LUAN | Chuỗi | n | ✅ |
| 10 | NGAY_KQ | Chuỗi | 12 | ✅ |
| 11 | MA_BS_DOC_KQ | Chuỗi | 255 | ✅ |
| 12 | DU_PHONG | Chuỗi | n | ✅ |

---

## XML5 — Bảng 5 (Diễn biến lâm sàng)

**Kết quả: ✅ Khớp hoàn toàn (9/9 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML5 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | STT | Số | 10 | ✅ |
| 3 | DIEN_BIEN_LS | Chuỗi | n | ✅ |
| 4 | GIAI_DOAN_BENH | Chuỗi | n | ✅ |
| 5 | HOI_CHAN | Chuỗi | n | ✅ |
| 6 | PHAU_THUAT | Chuỗi | n | ✅ |
| 7 | THOI_DIEM_DBLS | Chuỗi | 12 | ✅ |
| 8 | NGUOI_THUC_HIEN | Chuỗi | 255 | ✅ |
| 9 | DU_PHONG | Chuỗi | n | ✅ |

---

## XML6 — Bảng 6 (Hồ sơ HIV/AIDS)

**Kết quả: ⚠️ XML6 có 14 trường dư không xuất hiện trong Bảng 6 của quyết định**

### Các trường có trong QĐ và trong XML6

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML6 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | MA_THE_BHYT | Chuỗi | n | ✅ |
| 3 | SO_CCCD | Số | 15 | ✅ |
| 4 | NGAYKD_HIV | Chuỗi | 8 | ✅ |
| 5 | BDDT_ARV | Chuỗi | 8 | ✅ |
| 6 | MA_PHAC_DO_DIEU_TRI_BD | Chuỗi | 200 | ✅ |
| 7 | MA_BAC_PHAC_DO_BD | Số | 1 | ✅ |
| 8 | MA_LYDO_DTRI | Số | 1 | ✅ |
| 9 | LOAI_DTRI_LAO | Số | 1 | ✅ |
| 10 | PHACDO_DTRI_LAO | Số | 2 | ✅ |
| 11 | NGAYBD_DTRI_LAO | Chuỗi | 8 | ✅ |
| 12 | NGAYKT_DTRI_LAO | Chuỗi | 8 | ✅ |
| 13 | MA_LYDO_XNTL_VR | Số | 1 | ✅ |
| 14 | NGAY_XN_TLVR | Chuỗi | 8 | ✅ |
| 15 | KQ_XNTL_VR | Số | 1 | ✅ |
| 16 | NGAY_KQ_XN_TLVR | Chuỗi | 8 | ✅ |
| 17 | MA_LOAI_BN | Số | 1 | ✅ |
| 18 | MA_TINH_TRANG_DK | Chuỗi | 18 | ✅ |
| 19 | LAN_XN_PCR | Số | 1 | ✅ |
| 20 | NGAY_XN_PCR | Chuỗi | 8 | ✅ |
| 21 | NGAY_KQ_XN_PCR | Chuỗi | 8 | ✅ |
| 22 | MA_KQ_XN_PCR | Số | 1 | ✅ |
| 23 | NGAY_NHAN_TT_MANG_THAI | Chuỗi | 8 | ✅ |
| 24 | NGAY_BAT_DAU_DT_CTX | Chuỗi | 8 | ✅ |
| 25 | MA_XU_TRI | Số | 1 | ✅ |
| 26 | NGAY_BAT_DAU_XU_TRI | Chuỗi | 8 | ✅ |
| 27 | NGAY_KET_THUC_XU_TRI | Chuỗi | 8 | ✅ |
| 28 | MA_PHAC_DO_DIEU_TRI | Chuỗi | 200 | ✅ |
| 29 | MA_BAC_PHAC_DO | Số | 1 | ✅ |
| 30 | SO_NGAY_CAP_THUOC_ARV | Số | 3 | ✅ |
| 31 | DU_PHONG | Chuỗi | n | ✅ |

### Các trường có trong XML6 nhưng **KHÔNG CÓ** trong Bảng 6 của QĐ

| Tên trường | Có trong XML6 | Có trong QĐ Bảng 6 | Nhận xét |
|---|:---:|:---:|---|
| NGAY_SINH | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| GIOI_TINH | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| DIA_CHI | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| MATINH_CU_TRU | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| MAHUYEN_CU_TRU | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| MAXA_CU_TRU | ✅ | ❌ | Trường nhân khẩu học, có ở các bảng khác |
| NOI_LAY_MAU_XN | ✅ | ❌ | Liên quan đến xét nghiệm HIV |
| NOI_XN_KD | ✅ | ❌ | Liên quan đến xét nghiệm HIV |
| NOI_BDDT_ARV | ✅ | ❌ | Liên quan đến điều trị ARV |
| GIAI_DOAN_LAM_SANG | ✅ | ❌ | Phân giai đoạn lâm sàng HIV |
| NHOM_DOI_TUONG | ✅ | ❌ | Nhóm đối tượng bệnh nhân |
| NGAY_CHUYEN_PHAC_DO | ✅ | ❌ | Thông tin chuyển phác đồ |
| LY_DO_CHUYEN_PHAC_DO | ✅ | ❌ | Lý do chuyển phác đồ |
| MA_CSKCB | ✅ | ❌ | Mã cơ sở KCB |

> **Lưu ý:** 14 trường dư này có thể xuất phát từ yêu cầu bổ sung của hệ thống HMED (Cổng quản lý điều trị HIV tại https://dieutri.arv.vn) mà Bảng 6 yêu cầu gửi song song. Cần xác nhận lại với đơn vị chủ quản hoặc tài liệu đặc tả kỹ thuật hệ thống HMED.

---

## XML7 — Bảng 7 (Giấy ra viện)

**Kết quả: ✅ Khớp hoàn toàn (25/25 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML7 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | SO_LUU_TRU | Chuỗi | 200 | ✅ |
| 3 | MA_YTE | Chuỗi | 200 | ✅ |
| 4 | MA_KHOA_RV | Chuỗi | 200 | ✅ |
| 5 | NGAY_VAO | Chuỗi | 12 | ✅ |
| 6 | NGAY_RA | Chuỗi | 12 | ✅ |
| 7 | MA_DINH_CHI_THAI | Số | 1 | ✅ |
| 8 | NGUYENNHAN_DINHCHI | Chuỗi | n | ✅ |
| 9 | THOIGIAN_DINHCHI | Chuỗi | 12 | ✅ |
| 10 | TUOI_THAI | Số | 2 | ✅ |
| 11 | CHAN_DOAN_RV | Chuỗi | 1500 | ✅ |
| 12 | PP_DIEUTRI | Chuỗi | 1500 | ✅ |
| 13 | GHI_CHU | Chuỗi | 1500 | ✅ |
| 14 | MA_TTDV | Chuỗi | 10 | ✅ |
| 15 | MA_BS | Chuỗi | 200 | ✅ |
| 16 | TEN_BS | Chuỗi | 255 | ✅ |
| 17 | NGAY_CT | Chuỗi | 8 | ✅ |
| 18 | MA_CHA | Chuỗi | 10 | ✅ |
| 19 | MA_ME | Chuỗi | 10 | ✅ |
| 20 | MA_THE_TAM | Chuỗi | 15 | ✅ |
| 21 | HO_TEN_CHA | Chuỗi | 255 | ✅ |
| 22 | HO_TEN_ME | Chuỗi | 255 | ✅ |
| 23 | SO_NGAY_NGHI | Số | 2 | ✅ |
| 24 | NGOAITRU_TUNGAY | Chuỗi | 8 | ✅ |
| 25 | NGOAITRU_DENNGAY | Chuỗi | 8 | ✅ |
| — | DU_PHONG | Chuỗi | n | ✅ |

> **Ghi chú:** Trường `DU_PHONG` trong XML7 là bổ sung hợp lệ, không ảnh hưởng đến tính đúng đắn.

---

## XML8 — Bảng 8 (Tóm tắt hồ sơ bệnh án)

**Kết quả: ✅ Khớp hoàn toàn (22/22 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML8 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | MA_LOAI_KCB | Số | 2 | ✅ |
| 3 | HO_TEN_CHA | Chuỗi | 255 | ✅ |
| 4 | HO_TEN_ME | Chuỗi | 255 | ✅ |
| 5 | NGUOI_GIAM_HO | Chuỗi | 255 | ✅ |
| 6 | DON_VI | Chuỗi | 1024 | ✅ |
| 7 | NGAY_VAO | Chuỗi | 12 | ✅ |
| 8 | NGAY_RA | Chuỗi | 12 | ✅ |
| 9 | CHAN_DOAN_VAO | Chuỗi | n | ✅ |
| 10 | CHAN_DOAN_RV | Chuỗi | n | ✅ |
| 11 | QT_BENHLY | Chuỗi | n | ✅ |
| 12 | TOMTAT_KQ | Chuỗi | n | ✅ |
| 13 | PP_DIEUTRI | Chuỗi | n | ✅ |
| 14 | NGAY_SINHCON | Chuỗi | 8 | ✅ |
| 15 | NGAY_CONCHET | Chuỗi | 8 | ✅ |
| 16 | SO_CONCHET | Số | 2 | ✅ |
| 17 | KET_QUA_DTRI | Số | 1 | ✅ |
| 18 | GHI_CHU | Chuỗi | n | ✅ |
| 19 | MA_TTDV | Số | 10 | ✅ |
| 20 | NGAY_CT | Chuỗi | 8 | ✅ |
| 21 | MA_THE_TAM | Chuỗi | 15 | ✅ |
| 22 | DU_PHONG | Chuỗi | n | ✅ |

---

## XML9 — Bảng 9 (Giấy chứng sinh)

**Kết quả: ✅ Khớp hoàn toàn (34/34 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML9 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | MA_BHXH_NND | Số | 10 | ✅ |
| 3 | MA_THE_NND | Chuỗi | 15 | ✅ |
| 4 | HO_TEN_NND | Chuỗi | 255 | ✅ |
| 5 | NGAYSINH_NND | Chuỗi | 8 | ✅ |
| 6 | MA_DANTOC_NND | Số | 2 | ✅ |
| 7 | SO_CCCD_NND | Số | 15 | ✅ |
| 8 | NGAYCAP_CCCD_NND | Chuỗi | 8 | ✅ |
| 9 | NOICAP_CCCD_NND | Chuỗi | 1024 | ✅ |
| 10 | NOI_CU_TRU_NND | Chuỗi | 1024 | ✅ |
| 11 | MA_QUOCTICH | Số | 3 | ✅ |
| 12 | MATINH_CU_TRU | Chuỗi | 3 | ✅ |
| 13 | MAHUYEN_CU_TRU | Chuỗi | 3 | ✅ |
| 14 | MAXA_CU_TRU | Chuỗi | 5 | ✅ |
| 15 | HO_TEN_CHA | Chuỗi | 255 | ✅ |
| 16 | MA_THE_TAM | Chuỗi | 15 | ✅ |
| 17 | HO_TEN_CON | Chuỗi | 255 | ✅ |
| 18 | GIOI_TINH_CON | Số | 1 | ✅ |
| 19 | SO_CON | Số | 2 | ✅ |
| 20 | LAN_SINH | Số | 2 | ✅ |
| 21 | SO_CON_SONG | Số | 2 | ✅ |
| 22 | CAN_NANG_CON | Số | 10 | ✅ |
| 23 | NGAY_SINH_CON | Chuỗi | 12 | ✅ |
| 24 | NOI_SINH_CON | Chuỗi | 1024 | ✅ |
| 25 | TINH_TRANG_CON | Chuỗi | n | ✅ |
| 26 | SINHCON_PHAUTHUAT | Số | 1 | ✅ |
| 27 | SINHCON_DUOI32TUAN | Số | 1 | ✅ |
| 28 | GHI_CHU | Chuỗi | n | ✅ |
| 29 | NGUOI_DO_DE | Chuỗi | 255 | ✅ |
| 30 | NGUOI_GHI_PHIEU | Chuỗi | 255 | ✅ |
| 31 | NGAY_CT | Chuỗi | 8 | ✅ |
| 32 | SO | Chuỗi | 200 | ✅ |
| 33 | QUYEN_SO | Chuỗi | 200 | ✅ |
| 34 | MA_TTDV | Số | 10 | ✅ |
| — | DU_PHONG | Chuỗi | n | ✅ |

> **Ghi chú:** Trường `DU_PHONG` trong XML9 là bổ sung hợp lệ theo thông lệ chung.

---

## XML10 — Bảng 10 (Giấy nghỉ dưỡng thai)

**Kết quả: ⚠️ XML10 có thêm trường `DU_PHONG` không xuất hiện trong Bảng 10 của quyết định**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML10 | Có trong QĐ |
|:---:|---|---|:---:|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ | ✅ |
| 2 | SO_SERI | Chuỗi | 200 | ✅ | ✅ |
| 3 | SO_CT | Chuỗi | 200 | ✅ | ✅ |
| 4 | SO_NGAY | Số | 3 | ✅ | ✅ |
| 5 | DON_VI | Chuỗi | 1024 | ✅ | ✅ |
| 6 | CHAN_DOAN_RV | Chuỗi | n | ✅ | ✅ |
| 7 | TU_NGAY | Chuỗi | 8 | ✅ | ✅ |
| 8 | DEN_NGAY | Chuỗi | 8 | ✅ | ✅ |
| 9 | MA_TTDV | Số | 10 | ✅ | ✅ |
| 10 | TEN_BS | Chuỗi | 255 | ✅ | ✅ |
| 11 | MA_BS | Chuỗi | 200 | ✅ | ✅ |
| 12 | NGAY_CT | Chuỗi | 8 | ✅ | ✅ |
| — | DU_PHONG | Chuỗi | n | ✅ | ❌ |

> **Ghi chú:** `DU_PHONG` không được liệt kê trong Bảng 10 nhưng là trường dự phòng tiêu chuẩn có mặt ở hầu hết các bảng khác. Đây là điểm lệch nhỏ, không ảnh hưởng thực tế.

---

## XML11 — Bảng 11 (Giấy nghỉ hưởng BHXH)

**Kết quả: ✅ Khớp hoàn toàn (22/22 trường)**

| STT | Tên trường | Kiểu DL | Kích thước | Có trong XML11 |
|:---:|---|---|:---:|:---:|
| 1 | MA_LK | Chuỗi | 100 | ✅ |
| 2 | SO_CT | Chuỗi | 200 | ✅ |
| 3 | SO_SERI | Chuỗi | 200 | ✅ |
| 4 | SO_KCB | Chuỗi | 200 | ✅ |
| 5 | DON_VI | Chuỗi | 1024 | ✅ |
| 6 | MA_BHXH | Số | 10 | ✅ |
| 7 | MA_THE_BHYT | Chuỗi | n | ✅ |
| 8 | CHAN_DOAN_RV | Chuỗi | n | ✅ |
| 9 | PP_DIEUTRI | Chuỗi | n | ✅ |
| 10 | MA_DINH_CHI_THAI | Số | 1 | ✅ |
| 11 | NGUYENNHAN_DINHCHI | Chuỗi | n | ✅ |
| 12 | TUOI_THAI | Số | 2 | ✅ |
| 13 | SO_NGAY_NGHI | Số | 3 | ✅ |
| 14 | TU_NGAY | Chuỗi | 8 | ✅ |
| 15 | DEN_NGAY | Chuỗi | 8 | ✅ |
| 16 | HO_TEN_CHA | Chuỗi | 255 | ✅ |
| 17 | HO_TEN_ME | Chuỗi | 255 | ✅ |
| 18 | MA_TTDV | Số | 10 | ✅ |
| 19 | MA_BS | Chuỗi | 200 | ✅ |
| 20 | NGAY_CT | Chuỗi | 8 | ✅ |
| 21 | MA_THE_TAM | Chuỗi | 15 | ✅ |
| 22 | MAU_SO | Chuỗi | 5 | ✅ |
| — | DU_PHONG | Chuỗi | n | ✅ |

> **Ghi chú:** Trường `DU_PHONG` trong XML11 là bổ sung hợp lệ theo thông lệ chung.

---

## XML13 — Giấy chuyển tuyến

**Kết quả: ❌ Không có bảng quy định tương ứng trong QĐ 130/QĐ-BYT (hợp nhất QĐ4750)**

Quyết định 130/QĐ-BYT và QĐ4750 không quy định Bảng 13. Các trường trong XML13 có thể tham chiếu từ biểu mẫu giấy chuyển tuyến theo **Thông tư 30/2020/TT-BYT** hoặc các quy định liên quan. Cần xác nhận thêm từ đặc tả kỹ thuật của BHXH Việt Nam.

### Danh sách trường trong XML13 (để tham chiếu)

| Tên trường | Ghi chú |
|---|---|
| MA_LK | Mã liên kết |
| SO_HOSO | Số hồ sơ |
| SO_CHUYENTUYEN | Số chuyển tuyến |
| GIAY_CHUYEN_TUYEN | Thông tin giấy chuyển tuyến |
| MA_CSKCB | Mã cơ sở KCB |
| MA_NOI_DI | Mã nơi đi |
| MA_NOI_DEN | Mã nơi đến |
| HO_TEN | Họ tên người bệnh |
| NGAY_SINH | Ngày sinh |
| GIOI_TINH | Giới tính |
| MA_QUOCTICH | Mã quốc tịch |
| MA_DANTOC | Mã dân tộc |
| MA_NGHE_NGHIEP | Mã nghề nghiệp |
| DIA_CHI | Địa chỉ |
| MA_THE_BHYT | Mã thẻ BHYT |
| GT_THE_DEN | Giá trị thẻ đến |
| NGAY_VAO | Ngày vào |
| NGAY_VAO_NOI_TRU | Ngày vào nội trú |
| NGAY_RA | Ngày ra |
| DAU_HIEU_LS | Dấu hiệu lâm sàng |
| CHAN_DOAN_RV | Chẩn đoán ra viện |
| QT_BENHLY | Quá trình bệnh lý |
| TOMTAT_KQ | Tóm tắt kết quả |
| PP_DIEUTRI | Phương pháp điều trị |
| MA_BENH_CHINH | Mã bệnh chính |
| MA_BENH_KT | Mã bệnh kèm theo |
| MA_BENH_YHCT | Mã bệnh YHCT |
| TEN_DICH_VU | Tên dịch vụ |
| TEN_THUOC | Tên thuốc |
| PP_DIEU_TRI | Phương pháp điều trị (chi tiết) |
| MA_LOAI_RV | Mã loại ra viện |
| MA_LYDO_CT | Mã lý do chuyển tuyến |
| HUONG_DIEU_TRI | Hướng điều trị |
| PHUONGTIEN_VC | Phương tiện vận chuyển |
| HOTEN_NGUOI_HT | Họ tên người hỗ trợ |
| CHUCDANH_NGUOI_HT | Chức danh người hỗ trợ |
| MA_BAC_SI | Mã bác sĩ |
| MA_TTDV | Mã thủ trưởng đơn vị |
| DU_PHONG | Dự phòng |

---

## XML14 — Giấy hẹn khám lại

**Kết quả: ❌ Không có bảng quy định tương ứng trong QĐ 130/QĐ-BYT (hợp nhất QĐ4750)**

### Danh sách trường trong XML14 (để tham chiếu)

| Tên trường | Ghi chú |
|---|---|
| MA_LK | Mã liên kết |
| SO_GIAYHEN_KL | Số giấy hẹn khám lại |
| MA_CSKCB | Mã cơ sở KCB |
| HO_TEN | Họ tên người bệnh |
| NGAY_SINH | Ngày sinh |
| GIOI_TINH | Giới tính |
| DIA_CHI | Địa chỉ |
| MA_THE_BHYT | Mã thẻ BHYT |
| GT_THE_DEN | Giá trị thẻ đến |
| NGAY_VAO | Ngày vào |
| NGAY_VAO_NOI_TRU | Ngày vào nội trú |
| NGAY_RA | Ngày ra |
| NGAY_HEN_KL | Ngày hẹn khám lại |
| CHAN_DOAN_RV | Chẩn đoán ra viện |
| MA_BENH_CHINH | Mã bệnh chính |
| MA_BENH_KT | Mã bệnh kèm theo |
| MA_BENH_YHCT | Mã bệnh YHCT |
| MA_DOITUONG_KCB | Mã đối tượng KCB |
| MA_BAC_SI | Mã bác sĩ |
| MA_TTDV | Mã thủ trưởng đơn vị |
| NGAY_CT | Ngày chứng từ |
| DU_PHONG | Dự phòng |

---

## XML15 — Chi tiết điều trị bệnh lao

**Kết quả: ❌ Không có bảng quy định tương ứng trong QĐ 130/QĐ-BYT (hợp nhất QĐ4750)**

### Danh sách trường trong XML15 (để tham chiếu)

| Tên trường | Ghi chú |
|---|---|
| MA_LK | Mã liên kết |
| STT | Số thứ tự |
| MA_BN | Mã bệnh nhân |
| HO_TEN | Họ tên |
| SO_CCCD | Số CCCD |
| PHANLOAI_LAO_VITRI | Phân loại lao theo vị trí |
| PHANLOAI_LAO_TS | Phân loại lao tiền sử |
| PHANLOAI_LAO_HIV | Phân loại lao/HIV |
| PHANLOAI_LAO_VK | Phân loại lao vi khuẩn |
| PHANLOAI_LAO_KT | Phân loại lao kháng thuốc |
| LOAI_DTRI_LAO | Loại điều trị lao |
| NGAYBD_DTRI_LAO | Ngày bắt đầu điều trị lao |
| PHACDO_DTRI_LAO | Phác đồ điều trị lao |
| NGAYKT_DTRI_LAO | Ngày kết thúc điều trị lao |
| KET_QUA_DTRI_LAO | Kết quả điều trị lao |
| MA_CSKCB | Mã cơ sở KCB |
| NGAYKD_HIV | Ngày khẳng định HIV |
| BDDT_ARV | Bắt đầu điều trị ARV |
| NGAY_BAT_DAU_DT_CTX | Ngày bắt đầu điều trị CTX |
| DU_PHONG | Dự phòng |

---

## Kết luận và khuyến nghị

### Tổng hợp vấn đề phát hiện

| Mức độ | Vấn đề | File liên quan |
|---|---|---|
| 🔴 Cần xác nhận | Có 14 trường trong XML6 không có cơ sở trong Bảng 6 của QĐ | XML6 |
| 🟡 Cần xác nhận nguồn | XML13, XML14, XML15 không tìm thấy bảng quy định trong QĐ 130+4750 | XML13, XML14, XML15 |
| 🟢 Không ảnh hưởng | `DU_PHONG` xuất hiện thêm trong XML10 (không có trong Bảng 10 QĐ) | XML10 |

### Khuyến nghị

1. **XML6 – Bảng 6 (HIV/AIDS):** Rà soát lại 14 trường dư với đặc tả kỹ thuật của hệ thống HMED (https://dieutri.arv.vn). Có thể các trường này được yêu cầu bởi cổng HMED theo Thông tư 28/2018/TT-BYT nhưng không được liệt kê trong Bảng 6 của QĐ 130.

2. **XML13, XML14, XML15:** Xác nhận cơ sở pháp lý. Có khả năng các bảng này được quy định tại Thông tư 48/2017/TT-BYT (về trích chuyển dữ liệu điện tử) hoặc tài liệu đặc tả kỹ thuật riêng của BHXH Việt Nam, không nằm trong phạm vi của QĐ 130/QĐ-BYT.

3. **XML10 – `DU_PHONG`:** Đây là trường dự phòng chuẩn, nên bổ sung vào ghi chú của Bảng 10 để đồng nhất với các bảng khác.

---

*Tài liệu tham chiếu: Quyết định số 130/QĐ-BYT ngày 18/01/2023 và Quyết định số 4750/QĐ-BYT ngày 29/12/2023 của Bộ trưởng Bộ Y tế.*
