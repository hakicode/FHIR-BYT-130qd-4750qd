##### **Bảng chỉ tiêu dữ liệu về trạng thái khám bệnh, chữa bệnh** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ<br>tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các<br>bảng còn lại ban hành kèm theo Quyết định này trong một<br>lần khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|STT|Số|10|Là số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|MA_BN|Chuỗi|100|Là mã người bệnh theo quy định của cơ sở KBCB|
|4|HO_TEN|Chuỗi|255|Là họ và tên của người bệnh.<br>**- Lưu ý:**Trường hợp trẻ sau khi sinh ra được hưởng quyền<br>lợi BHYT theo quy định của Luật BHYT nhưng chưa được<br>cơ quan BHXH cấp thẻ BHYT do chưa làm thủ tục cấp giấy<br>khai sinh thì cơ sở KBCB thực hiện ghi họ và tên của trẻ<br>theo quy định tại điểm b khoản 1 Điều 10 Thông tư số<br>30/2020/TT-BYT ngày 31 tháng 12 năm 2020 của Bộ<br>trưởng Bộ Y tế quy định chi tiết và hướng dẫn biện pháp thi<br>hành một số điều của Nghị định số 146/2018/NĐ-CP ngày<br>17/10/2018 của Chính phủ quy định chi tiết và hướng dẫn<br>biện pháp thi hành một số điều của Luật BHYT, cụ thể:<br>+ Nếu trẻ sơ sinh có mẹ hoặc cha (bố): ghi theo họ và tên<br>của mẹ hoặc của cha (bố);<br>+ Nếu trẻ sơ sinh không có mẹ hoặc cha (bố) nhưng có<br>người giám hộ: ghi theo họ và tên của người giám hộ;<br>+ Nếu trẻ sơ sinh không có người nhận hoặc bỏ rơi tại cơ sở<br>KBCB: ghi tên cơ sở KBCB nơi đang thực hiện việc điều trị<br>cho trẻ.|
|5|SO_CCCD|Số|15|Ghi số căn cước công dân hoặc số chứng minh thư nhân dân<br>hoặc số hộ chiếu của người bệnh.<br>Trường hợp không có số căn cước công dân hoặc số chứng<br>minh thư nhân dân hoặc số hộ chiếu thì sử dụng mã tài<br>khoản định danh điện tử.|

|6|NGAY_SINH|Chuỗi|12|Ghi ngày, tháng, năm sinh ghi trên thẻ BHYT của người<br>bệnh, gồm 12 ký tự, bao gồm: 04 ký tự năm + 02 ký tự tháng<br>+ 02 ký tự ngày + 02 ký tự giờ + 02 ký tự phút.<br>Lưu ý:<br>- Trường hợp không có thông tin giờ, phút sinh thì ký tự giờ<br>và phút được mặc định là 0000;<br>- Trường hợp không có thông tin ngày sinh, tháng sinh thì ký<br>tự ngày sinh, tháng sinh được mặc định là 0000;<br>- Trường hợp trẻ mới sinh (từ đủ 28 ngày tuổi trở xuống) thì<br>phải ghi đầy đủ thông tin ngày, tháng, năm, giờ, phút sinh<br>của trẻ (nếu có);<br>- Trường hợp trẻ bị bỏ rơi mà không xác định được thông tin<br>chính xác ngày, tháng, năm, giờ, phút sinh của trẻ thì ghi<br>theo thời điểm mà cơ sở KBCB tiếp nhận trẻ.|
|---|---|---|---|---|
|7|GIOI_TINH|Số|1|Là mã giới tính của người bệnh (1: Nam; 2: Nữ; 3: Chưa xác<br>định)|
|8|MA_THE_BHYT|Chuỗi|15|Ghi mã thẻ BHYT của người bệnh do cơ quan BHXH cấp.<br>**Lưu ý**:<br>- Khi tiếp đón người bệnh, cơ sở KBCB có trách nhiệm tra<br>cứu trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám<br>định BHYT của BHXH Việt Nam để kiểm tra thông tin thẻ<br>BHYT. Trường hợp cấp cứu mà người bệnh hoặc thân nhân<br>người bệnh không xuất trình được thẻ BHYT ngay thì cơ sở<br>KBCB tra cứu thông tin thẻ BHYT trước khi người bệnh ra<br>viện.<br>- Đối với thẻ BHYT của các đối tượng có các mã QN, HC,<br>LS, XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ<br>Công an cấp: Tra cứu để kiểm tra thời hạn sử dụng của thẻ<br>BHYT trong trường hợp các đối tượng này không còn phục<br>vụ trong lực lượng Quân đội, Công an, Cơ yếu.<br>- Trường hợp người bệnh chưa có thẻ BHYT, cơ sở KBCB<br>sử dụng chức năng “Thông tuyến khám chữa bệnh\Tra cứu<br>thẻ tạm của trẻ em hoặc của người hiến tạng” trên Cổng tiếp<br>nhận dữ liệu Hệ thống thông tin giám định BHYT của<br>BHXH Việt Nam để tra cứu mã thẻ BHYT tạm thời.<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|

|9|MA_DKBD|Chuỗi|5|Ghi mã cơ sở KBCB nơi người bệnh đăng ký ban đầu ghi<br>trên thẻ BHYT, gồm có 05 ký tự.<br>Lưu ý đối với một số trường hợp sau:<br>- Trường hợp người bệnh chưa có thẻ BHYT nhưng được cơ<br>quan BHXH cấp mã thẻ tạm thời: Ghi theo 02 ký tự cuối của<br>mã đơn vị hành chính của tỉnh, thành phố trực thuộc Trung<br>ương nơi người bệnh cư trú (Quy định tại Phụ lục 1 Thông<br>tư số 07/2016/TT-BCA ngày 01 tháng 2 năm 2016 của Bộ<br>trưởng Bộ Công an) + 000. Ví dụ: Hà Nội thì ghi là 01000.<br>- Riêng đối với trẻ em hoặc người đã hiến bộ phận cơ thể<br>người thì thực hiện theo quy định tại Điều 10 Thông tư số<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|---|---|---|---|---|
|10|GT_THE_TU|Chuỗi|8|Ghi thời điểm thẻ BHYT bắt đầu có giá trị sử dụng, gồm 08<br>ký tự, bao gồm: 04 ký tự năm + 02 ký tự tháng + 02 ký tự<br>ngày.<br>**Lưu ý đối với một số trường hợp sau:**<br>- Trường hợp người bệnh KBCB BHYT nhưng chưa có thẻ<br>BHYT: Thay thời điểm thẻ BHYT có giá trị bằng thời gian<br>người bệnh vào cơ sở KBCB (gồm 08 ký tự, bao gồm: 04 ký<br>tự năm + 02 ký tự tháng + 02 ký tự ngày);<br>- Trường hợp thẻ BHYT các đối tượng có mã QN, HC, LS,<br>XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công<br>an cấp mà không tra cứu được thì ghi thời điểm thẻ có giá trị<br>sử dụng ghi trên thẻ giấy;<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|11|GT_THE_DEN|Chuỗi|8|Ghi thời điểm thẻ BHYT hết giá trị sử dụng, gồm 08 ký tự,<br>bao gồm: 04 ký tự năm + 02 ký tự tháng + 02 ký tự ngày.<br>**Lưu ý đối với một số trường hợp sau:**<br>- Trường hợp người bệnh KBCB BHYT nhưng chưa có thẻ<br>BHYT: Thay thời điểm thẻ hết giá trị bằng thời gian người<br>bệnh ra viện (gồm 08 ký tự, bao gồm 04 ký tự năm + 02 ký<br>tự tháng + 02 ký tự ngày).<br>- Trường hợp thẻ BHYT của các đối tượng có mã QN, HC,<br>LS, XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ<br>Công an cấp mà không tra cứu được trên Cổng tiếp nhận dữ<br>liệu Hệ thống thông tin giám định BHYT của BHXH Việt<br>Nam thì để trống;<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|12|MA_DOITUONG_KCB|Số|1|Ghi mã đối tượng đến KBCB theo Bộ mã DMDC do Bộ<br>trưởng Bộ Y tế ban hành.|

|13|NGAY_VAO|Chuỗi|12|Ghi thời điểm người bệnh đến KBCB, gồm 12 ký tự, trong<br>đó: 04 ký tự năm + 02 ký tự tháng + 02 ký tự ngày + 02 ký<br>tự giờ (định dạng theo 24 giờ) + 02 ký tự phút.<br>Ví dụ: người bệnh đến KBCB lúc 15 giờ 20 phút ngày<br>31/03/2017 được hiển thị là: 201703311520|
|---|---|---|---|---|
|14|MA_LOAI_KCB|Số|2|Ghi mã hình thức KBCB theo Bộ mã DMDC do Bộ trưởng<br>Bộ Y tế ban hành.|
|15|MA_CSKCB|Chuỗi|5|Ghi mã cơ sở KBCB nơi người bệnh đến khám bệnh, điều trị<br>do cơ quan có thẩm quyền cấp.|
|16|MA_DICH_VU|Chuỗi|50|Ghi mã dịch vụ kỹ thuật hoặc mã dịch vụ khám bệnh thực<br>hiện đối với người bệnh, theo quy định tại Bộ mã danh mục<br>dùng chung (DMDC) do Bộ trưởng Bộ Y tế ban hành.|
|17|TEN_DICH_VU|Chuỗi|1024|Ghi tên dịch vụ kỹ thuật hoặc tên dịch vụ khám bệnh.|
|18|NGAY_YL|Chuỗi|12|Ghi thời điểm ra y lệnh (gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHmm, bao gồm: 04 ký tự năm + 02 ký tự tháng<br>+ 02 ký tự ngày + 02 ký tự giờ (24 giờ) + 02 ký tự phút).<br>Ví dụ: Thời điểm ra y lệnh lúc 15 giờ 20 phút ngày 31 tháng<br>03 năm 2017 được hiển thị là: 201703311520|

##### **Bảng 1. Chỉ tiêu tổng hợp khám bệnh, chữa bệnh** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởn 18 01 g Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ<br>tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các<br>bảng còn lại ban hành kèm theo Quyết định này trong một lần<br>khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|STT|Số|10|Là số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|MA_BN|Chuỗi|100|Là mã người bệnh theo quy định của cơ sở KBCB|
|4|HO_TEN|Chuỗi|255|Là họ và tên của người bệnh.<br>- **Lưu ý:** Trường hợp trẻ sau khi sinh ra được hưởng quyền lợi<br>BHYT theo quy định của Luật BHYT nhưng chưa được cơ<br>quan BHXH cấp thẻ BHYT do chưa làm thủ tục cấp giấy khai<br>sinh thì cơ sở KBCB thực hiện ghi họ và tên của trẻ theo quy<br>định tại điểm b khoản 1 Điều 10 Thông tư số 30/2020/TT-BYT<br>ngày 31 tháng 12 năm 2020 của Bộ trưởng Bộ Y tế quy định<br>chi tiết và hướng dẫn biện pháp thi hành một số điều của Nghị<br>định số 146/2018/NĐ-CP ngày 17/10/2018 của Chính phủ quy<br>định chi tiết và hướng dẫn biện pháp thi hành một số điều của<br>Luật BHYT, cụ thể:<br>+ Nếu trẻ sơ sinh có mẹ hoặc cha (bố): ghi theo họ và tên của<br>mẹ hoặc của cha (bố);<br>+ Nếu trẻ sơ sinh không có mẹ hoặc cha (bố) nhưng có người<br>giám hộ: ghi theo họ và tên của người giám hộ;<br>+ Nếu trẻ sơ sinh không có người nhận hoặc bỏ rơi tại cơ sở<br>KBCB: ghi tên cơ sở KBCB nơi đang thực hiện việc điều trị<br>cho trẻ.|
|5|SO_CCCD|Số|15|Ghi số căn cước công dân hoặc số chứng minh thư nhân dân<br>hoặc số hộ chiếu của người bệnh.<br>Trường hợp không có số căn cước công dân hoặc số chứng<br>minh thư nhân dân hoặc số hộ chiếu thì sử dụng mã tài khoản<br>định danh điện tử.|

|6|NGAY_SINH|Chuỗi|12|Ghi ngày, tháng, năm sinh ghi trên thẻ BHYT của người bệnh,<br>gồm 12 ký tự theo định dạng yyyymmddHHMM.<br>Lưu ý:<br>- Trường hợp không có thông tin giờ, phút sinh thì ký tự giờ và<br>phút được mặc định là 0000;<br>- Trường hợp không có thông tin ngày sinh, tháng sinh thì ký<br>tự ngày sinh, tháng sinh được mặc định là 0000;<br>- Trường hợp trẻ mới sinh (từ đủ 28 ngày tuổi trở xuống) thì<br>phải ghi đầy đủ thông tin ngày, tháng, năm, giờ, phút sinh của<br>trẻ (nếu có);<br>- Trường hợp trẻ bị bỏ rơi mà không xác định được thông tin<br>chính xác ngày, tháng, năm, giờ, phút sinh của trẻ thì ghi theo<br>thời điểm mà cơ sở KBCB tiếp nhận trẻ.|
|---|---|---|---|---|
|7|GIOI_TINH|Số|1|Là mã giới tính của người bệnh (1: Nam; 2: Nữ; 3: Chưa xác<br>định)|
|8|MA_QUOCTICH|Số|3|Ghi mã quốc tịch của người bệnh theo quy định tại Phụ lục 2<br>Thông tư số 07/2016/TT-BCA ngày 01 tháng 2 năm 2016 của<br>Bộ trưởng Bộ Công an.|
|9|MA_DANTOC|Số|2|Ghi mã dân tộc của người bệnh (thực hiện theo Danh mục các<br>dân tộc Việt Nam ban hành kèm theo Quyết định số 121-<br>TCTK/PPCĐ ngày 02/3/1979 của Tổng cục trưởng Tổng cục<br>Thống kê để điền chi tiết). Tra cứu mã dân tộc tại đường link:<br>_http://tongdieutradanso.vn/danh-muc-cac-dan-toc-viet-_|
|10|MA_NGHE_NGHIEP|Số|5|Ghi mã nghề nghiệp của người bệnh. Thực hiện ghi mã nghề<br>nghiệp theo quy định tại Quyết định số 34/2020/QĐ-TTg ngày<br>26 tháng 11 năm 2020 của Thủ tướng Chính phủ. Tra cứu mã<br>nghề nghiệp tại đường link:_https://luatvietnam.vn/lao-_<br>_dong/quyet-dinh-34-2020-qd-ttg-danh-muc-nghe-nghiep-viet-_<br>**- Lưu ý:**<br>+ Trường hợp người bệnh không có hoặc chưa có nghề nghiệp<br>thì ghi mã 00000;<br>+ Trường hợp người bệnh có nhiều nghề thì ghi mã nghề<br>nghiệp chính hoặc nghề nghiệp hiện tại;|

|11|DIA_CHI|Chuỗi|1024|Ghi địa chỉ nơi cư trú hiện tại của người bệnh.<br>- Lưu ý:<br>+ Trường hợp người bệnh là người Việt Nam: Ghi địa chỉ theo<br>địa chỉ nơi cư trú hiện tại của người bệnh đã được cập nhật<br>thông tin trong Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu<br>dân cư về cư trú, gồm: số nhà (nếu có); thôn, xóm hoặc đường,<br>phố (nếu có); xã, phường, thị trấn; quận, huyện, thị xã, thành<br>phố trực thuộc tỉnh; tỉnh, thành phố trực thuộc TW.<br>Trường hợp trẻ sau khi sinh ra được hưởng quyền lợi BHYT<br>theo quy định của Luật BHYT nhưng chưa được cơ quan<br>BHXH cấp thẻ BHYT do chưa làm thủ tục cấp giấy khai sinh<br>thì cơ sở KBCB thực hiện ghi theo địa chỉ nơi người mẹ hoặc<br>người giám hộ hợp pháp cư trú hoặc nơi cơ sở KBCB đặt trụ sở<br>đối với trường hợp trẻ sơ sinh không có người nhận hoặc bị bỏ<br>rơi.<br>+ Trường hợp người bệnh là người nước ngoài thì ghi theo địa<br>chỉ do người bệnh tự khai báo.|
|---|---|---|---|---|
|12|MATINH_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp tỉnh nơi cư trú hiện tại của người<br>bệnh. Ghi theo 02 ký tự cuối của mã đơn vị hành chính của<br>tỉnh, thành phố trực thuộc Trung ương nơi người bệnh cư trú<br>(Quy định tại Phụ lục 1 Thông tư số 07/2016/TT-BCA ngày 01<br>tháng 2 năm 2016 của Bộ trưởng Bộ Công an).|
|13|MAHUYEN_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp huyện nơi cư trú hiện tại của người<br>bệnh. Ghi mã đơn vị hành chính cấp huyện theo Quyết định số<br>124/2004/QĐ-TTg ngày 08/7/2004 của Thủ tướng Chính phủ<br>ban hành danh mục mã đơn vị hành chính.|
|14|MAXA_CU_TRU|Chuỗi|5|Mã đơn vị hành chính cấp xã nơi cư trú hiện tại của người<br>bệnh. Ghi mã đơn vị hành chính cấp xã theo Quyết định số<br>124/2004/QĐ-TTg ngày 08/7/2004 của Thủ tướng Chính phủ<br>ban hành danh mục mã đơn vị hành chính.|
|15|DIEN_THOAI|Số|15|Ghi số điện thoại liên lạc của người bệnh hoặc của thân nhân<br>người bệnh. Trường thông tin này chỉ ghi khi người bệnh cung<br>cấp. Trường hợp không có thì để trống trường thông tin này.|

|16|<!-- FIELD_NAME_MISSING -->|Chuỗi||Ghi mã thẻ BHYT của người bệnh do cơ quan BHXH cấp.<br>Lưu ý:<br>- Khi tiếp đón người bệnh, cơ sở KBCB có trách nhiệm tra cứu<br>trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định<br>BHYT của BHXH Việt Nam để kiểm tra thông tin thẻ BHYT.<br>Trường hợp cấp cứu mà người bệnh hoặc thân nhân người<br>bệnh không xuất trình được thẻ BHYT ngay thì cơ sở KBCB<br>tra cứu thông tin thẻ BHYT trước khi người bệnh ra viện.<br>- Đối với thẻ BHYT của các đối tượng có các mã QN, HC, LS,<br>XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công an<br>cấp: Tra cứu để kiểm tra thời hạn sử dụng của thẻ BHYT trong<br>trường hợp các đối tượng này không còn phục vụ trong lực<br>lượng Quân đội, Công an, Cơ yếu.<br>- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ<br>BHYT mới có thay đổi thông tin liên quan đến mã thẻ thì ghi<br>tiếp mã thẻ mới (mỗi mã thẻ gồm có 15 ký tự), giữa các mã thẻ<br>cách nhau bằng dấu chấm phẩy “;”;<br>- Trường hợp người bệnh chưa có thẻ BHYT, cơ sở KBCB sử<br>dụng chức năng “Thông tuyến khám chữa bệnh\Tra cứu thẻ<br>tạm của trẻ em hoặc của người hiến tạng” trên Cổng tiếp nhận<br>dữ liệu Hệ thống thông tin giám định BHYT của BHXH Việt<br>Nam để tra cứu mã thẻ BHYT tạm thời.<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|---|---|---|---|---|
|17|MA_DKBD|Chuỗi||Ghi mã cơ sở KBCB nơi người bệnh đăng ký ban đầu ghi trên<br>thẻ BHYT, gồm có 05 ký tự.<br>**Lưu ý:**<br>- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ<br>BHYT mới có thay đổi thông tin liên quan đến mã cơ sở<br>KBCB BHYT ban đầu thì ghi tiếp mã cơ sở KBCB BHYT ban<br>đầu trên thẻ mới sau mã cơ sở KBCB BHYT ban đầu ghi trên<br>thẻ BHYT trước đó, cách nhau bằng dấu chấm phẩy “;”;<br>- Trường hợp người bệnh chưa có thẻ BHYT nhưng được cơ<br>quan BHXH cấp mã thẻ tạm thời: Ghi theo 02 ký tự cuối của<br>mã đơn vị hành chính của tỉnh, thành phố trực thuộc Trung<br>ương nơi người bệnh cư trú (Quy định tại Phụ lục 1 Thông tư<br>số 07/2016/TT-BCA ngày 01 tháng 2 năm 2016 của Bộ trưởng<br>Bộ Công an) + 000. Ví dụ: Hà Nội thì ghi là 01000.<br>- Riêng đối với trẻ em hoặc người đã hiến bộ phận cơ thể người<br>thì thực hiện theo quy định tại Điều 10 Thông tư số<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|

|18|GT_THE_TU|Chuỗi||Ghi thời điểm thẻ BHYT bắt đầu có giá trị sử dụng, gồm 08 ký<br>tự theo định dạng yyyymmdd.<br>Lưu ý:<br>- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ<br>BHYT mới có thay đổi thông tin liên quan đến thời điểm thẻ<br>bắt đầu có giá trị sử dụng thì ghi tiếp thời điểm sử dụng của thẻ<br>mới (gồm 08 ký tự theo định dạng yyyymmdd), cách nhau<br>bằng dấu chấm phẩy “;”;<br>- Trường hợp người bệnh KBCB BHYT nhưng chưa có thẻ<br>BHYT: Thay thời điểm thẻ BHYT có giá trị bằng thời gian<br>người bệnh vào cơ sở KBCB (gồm 08 ký tự theo định dạng<br>- Trường hợp thẻ BHYT các đối tượng có mã QN, HC, LS,<br>XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công an<br>cấp mà không tra cứu được thì ghi thời điểm thẻ có giá trị sử<br>dụng ghi trên thẻ giấy;<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|---|---|---|---|---|
|19|GT_THE_DEN|Chuỗi||Ghi thời điểm thẻ BHYT hết giá trị sử dụng, gồm 08 ký tự theo<br>định dạng yyyymmdd.<br>**Lưu ý:**<br>- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ<br>BHYT mới có thay đổi thông tin liên quan đến thời điểm hết<br>giá trị sử dụng của thẻ BHYT thì ghi tiếp thời điểm thẻ BHYT<br>hết giá trị sử dụng ghi trên thẻ mới (gồm 08 ký tự theo định<br>dạng yyyymmdd), cách nhau bằng dấu chấm phẩy “;”;<br>- Trường hợp người bệnh KBCB BHYT nhưng chưa có thẻ<br>BHYT: Thay thời điểm thẻ hết giá trị bằng thời gian người<br>bệnh ra viện (gồm 08 ký tự, theo định dạng yyyymmdd).<br>- Trường hợp thẻ BHYT của các đối tượng có mã QN, HC, LS,<br>XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công an<br>cấp mà không tra cứu được trên Cổng tiếp nhận dữ liệu Hệ<br>thống thông tin giám định BHYT của BHXH Việt Nam thì để<br>trống trường thông tin này;<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|

|20|NGAY_MIEN_CCT 1 8 /|Chuỗi|12|Ghi thời điểm người bệnh tham gia BHYT được hưởng chế độ<br>miễn cùng chi trả;<br>- Lưu ý:<br>+ Trường hợp đã được cấp giấy miễn cùng chi trả: ghi ngày bắt<br>đầu đủ điều kiện được hưởng chế độ miễn cùng chi trả theo<br>thông tin ghi trên giấy miễn cùng chi trả, gồm 08 ký tự theo<br>định dạng năm, tháng, ngày, viết tắt là yyyymmdd;<br>Ví dụ: ngày 05 tháng 04 năm 2017 được hiển thị là: 20170405;<br>+ Trường hợp chưa được cấp giấy miễn cùng chi trả: ghi thời<br>điểm đủ điều kiện miễn cùng chi trả theo hướng dẫn cách ghi<br>bảng kê chi phí KBCB ban hành kèm theo Quyết định số<br>6556/QĐ-BYT ngày 30 tháng 10 năm 2018 của Bộ trưởng Bộ<br>Y tế, gồm 12 kí tự theo định dạng yyyymmddHHMM;<br>+ Trường hợp người bệnh không có giấy miễn cùng chi trả<br>hoặc không đủ cơ sở để xác định thời điểm miễn cùng chi trả<br>thì để trống trường thông tin này.|
|---|---|---|---|---|
|21|LY_DO_VV|Chuỗi||Ghi lý do đến KBCB của người bệnh;<br>- **Lưu ý**:<br>+ Trường hợp đặc biệt do thiên tai, dịch bệnh mà cơ sở KBCB<br>phải chuyển thuốc, VTYT đến cơ sở KBCB khác thì cơ sở<br>KBCB nơi nhận thuốc, VTYT để điều trị cho người bệnh ghi<br>nhận tại trường LY_DO_VV như sau: "Khám bệnh, chữa bệnh<br>cấp thuốc, VTYT theo Giấy hẹn khám lại và hướng dẫn điều trị<br>của + Tên cơ sở KBCB (Nơi cấp Giấy hẹn khám lại) theo<br>hướng dẫn của Bộ Y tế.<br>_Ví dụ:_ Người bệnh được BV Bạch Mai cấp giấy hẹn khám lại<br>nhưng vì dịch bệnh COVID-19 nên không đến khám tại BV<br>Bạch Mai được mà phải đến BV đa khoa tỉnh Phú Thọ để<br>khám, nhận thuốc. BV Bạch Mai phải chuyển thuốc về BV đa<br>khoa tỉnh Phú Thọ thì BV đa khoa tỉnh Phú Thọ ghi nhận tại<br>trường LY_DO_VV như sau: "**_Khám bệnh, chữa bệnh cấp_**<br>**_thuốc theo Giấy hẹn khám lại và hướng dẫn điều trị của_**<br>**_Bệnh viện Bạch Mai_".**<br>+ Đối với các trường hợp khác phải chuyển thuốc thì thực hiện<br>theo hướng dẫn của Bộ Y tế.|
|22|LY_DO_VNT|Chuỗi||Ghi lý do vào nội trú, áp dụng đối với trường hợp điều trị nội<br>trú hoặc nội trú ban ngày (bao gồm cả triệu chứng lâm sàng<br>hoặc các lý do khác khiến cho người bệnh đến cơ sở KBCB).|
|23|MA_LY_DO_VNT|Chuỗi|5|Ghi mã lý do người bệnh vào điều trị nội trú theo quy định của<br>Bộ Y tế.<br>**Lưu ý:** Trường thông tin này áp dụng bắt buộc thực hiện khi<br>Bộ Y tế ban hành danh mục mã lý do vào điều trị nội trú và có<br>văn bản hướng dẫn.|

|24|CHAN_DOAN_VAO|Chuỗi||Ghi chẩn đoán của cơ sở KBCB ở thời điểm tiếp nhận người<br>bệnh (Chẩn đoán sơ bộ).|
|---|---|---|---|---|
|25|CHAN_DOAN_RV|Chuỗi||Ghi đầy đủ chẩn đoán xác định bệnh chính, bệnh kèm theo<br>và/hoặc các triệu chứng hoặc hội chứng, được bác sỹ ghi trong<br>hồ sơ KBCB tại thời điểm kết thúc KBCB đối với người bệnh.<br>**Lưu ý:**Đối với việc ghi chẩn đoán ra viện để phục vụ việc tạo<br>lập giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội thì thực<br>hiện theo hướng dẫn tại Thông tư số 18/2022/TT-BYT của Bộ<br>Y tế, trong đó:<br>- Nội dung chẩn đoán phải mô tả cụ thể về tình trạng sức khỏe<br>hoặc ghi tên bệnh hoặc mã bệnh.<br>- Trường hợp mắc bệnh cần chữa trị dài ngày thì ghi mã bệnh;<br>trường hợp chưa có mã bệnh thì ghi đầy đủ tên bệnh. Việc ghi<br>mã bệnh và tên bệnh thực hiện theo quy định tại Thông tư số<br>46/2016/TT-BYT ngày 30 tháng 12 năm 2016 của Bộ trưởng<br>Bộ Y tế ban hành danh mục bệnh dài ngày;<br>- Trường hợp điều trị dưỡng thai: Ghi rõ cụm từ “dưỡng thai”.|
|26|MA_BENH_CHINH|Chuỗi|7|Ghi mã bệnh chính theo mã ICD-10 do Bộ trưởng Bộ Y tế ban<br>hành (Quyết định số 4469/QĐ-BYT ngày 28 tháng 10 năm<br>2020 và các văn bản cập nhật, bổ sung).<br>**Lưu ý**: Cơ sở KBCB xác định và chỉ ghi 01 mã bệnh chính<br>theo quy định của Bộ Y tế.|
|27|MA_BENH_KT|Chuỗi|100|Ghi mã các bệnh kèm theo (theo mã ICD-10 do Bộ trưởng Bộ<br>Y tế ban hành kèm theo Quyết định số 4469/QĐ-BYT ngày 28<br>tháng 10 năm 2020 và các văn bản cập nhật, bổ sung) hoặc mã<br>của triệu chứng, hội chứng.<br>**Lưu ý**:<br>- Cơ sở KBCB xác định triệu chứng hoặc bệnh kèm theo theo<br>quy định của Bộ Y tế.<br>- Trường hợp có nhiều mã thì được phân cách bằng dấu chấm<br>phẩy “;”;<br>- Cơ sở KBCB chỉ được ghi tối đa 12 mã bệnh kèm theo.|
|28|MA_BENH_YHCT|Chuỗi|255|Ghi mã bệnh áp dụng trong KBCB bằng YHCT (nếu có);<br>- **Lưu ý**:<br>+ Trường hợp người bệnh KBCB bằng YHCT thì tại các<br>trường thông tin có số thứ tự 22 và 23 của Bảng này, cơ sở<br>KBCB ghi đầy đủ các mã bệnh YHCT, bao gồm mã bệnh<br>chính và các mã bệnh kèm theo tương ứng với mã bệnh theo<br>+ Trường hợp bệnh kèm theo có nhiều mã bệnh YHCT thì các<br>mã bệnh được phân cách bằng dấu chấm phẩy “;”.|

|29|MA_PTTT_QT|Chuỗi|125|Ghi mã phẫu thuật, thủ thuật quốc tế ICD-9 CM (theo mã phẫu<br>thuật, thủ thuật ICD-9 CM do Bộ trưởng Bộ Y tế ban hành kèm<br>theo Quyết định số 4440/QĐ-BYT ngày 27 tháng 10 năm<br>- Lưu ý:<br>+ Trường hợp có nhiều phẫu thuật, thủ thuật thì mỗi mã phẫu<br>thuật, thủ thuật được phân cách bằng dấu chấm phẩy “;”;<br>+ Chỉ ghi trong trường hợp người bệnh có thực hiện phẫu<br>thuật, thủ thuật.|
|---|---|---|---|---|
|30|MA_DOITUONG_KCB|Chuỗi|3|Ghi mã đối tượng đến KBCB theo Bộ mã DMDC do Bộ trưởng<br>Bộ Y tế ban hành.|
|31|MA_NOI_DI|Chuỗi|5|Ghi mã cơ sở KBCB nơi chuyển người bệnh do cơ quan có<br>thẩm quyền cấp. Ghi thông tin trường này trong trường hợp<br>chuyển tuyến khám chữa bệnh hoặc người bệnh đến khám lại<br>theo giấy hẹn quy định tại khoản 6 Điều 6 Thông tư<br>30/2020/TT-BYT hoặc lĩnh thuốc tại TYT xã theo quy định tại<br>điểm h khoản 1 Điều 14 Nghị định số 146/2018/NĐ-CP.<br>- Ví dụ 1: Người bệnh chuyển tuyến từ BV A đến BV B, tại<br>+ MA_CSKCB: 05 ký tự mã CSKCB của BV A<br>+ MA_NOI_DI: để trống<br>+ MA_NOI_DEN: 05 ký tự mã CSKCB BV B<br>- Ví dụ 2: BN chuyển tuyến từ BV A đến BV B, tại BV B ghi:<br>+ MA_NOI_DI: 05 ký tự mã CSKCB BV A<br>+ MA_CSKCB: 05 ký tự mã CSKCB của BV B<br>+ MA_NOI_DEN: để trống<br>- **Lưu ý**:<br>+ Trường hợp người bệnh không chuyển tuyến thì để trống<br>trường thông tin này<br>+ Trường hợp đặc biệt do thiên tai, dịch bệnh cơ sở KBCB<br>phải chuyển thuốc, VTYT đến cơ sở KBCB khác thì cơ sở<br>KBCB nơi nhận thuốc, VTYT để điều trị cho người bệnh thực<br>hiện chuyển dữ liệu chi phí thuốc, VTYT này lên Cổng tiếp<br>nhận dữ liệu Hệ thống thông tin giám định BHYT và tại trường<br>MA_NOI_DI ghi mã cơ sở KBCB nơi chuyển thuốc, VTYT.|

|32|MA_NOI_DEN|Chuỗi|5|Ghi mã cơ sở KBCB nơi chuyển người bệnh đến do cơ quan có<br>thẩm quyền cấp.<br>Lưu ý:<br>- Người bệnh chuyển tuyến từ BV A đến BV B và tiếp tục<br>chuyển đến BV C, tại BV B ghi:<br>+ MA_CSKCB: 05 ký tự mã CSKCB của BV B<br>+ MA_NOI_DI: 05 ký tự mã CSKCB của BV A<br>+ MA_NOI_DEN: 05 ký tự mã CSKCB BV C<br>- Trường hợp người bệnh không chuyển tuyến thì để trống<br>trường thông tin này.|
|---|---|---|---|---|
|33|MA_TAI_NAN|Số|1|Ghi mã tai nạn thương tích.<br>Cơ sở KBCB tham chiếu danh mục mã tai nạn thương tích tại<br>Phụ lục số 4 ban hành kèm theo Quyết định số 5937/QĐ-BYT<br>ngày 30 tháng 12 năm 2021 của Bộ trưởng Bộ Y tế.|
|34|NGAY_VAO|Chuỗi|12|Ghi thời điểm người bệnh đến KBCB, gồm 12 ký tự, theo định<br>dạng yyyymmddHHMM.<br>_Ví dụ_: người bệnh đến KBCB lúc 15 giờ 20 phút ngày<br>31/03/2017 được hiển thị là: 201703311520.|
|35|NGAY_VAO_NOI_TR|Chuỗi|12|Ghi thời điểm người bệnh được bác sỹ chỉ định vào điều trị nội<br>trú hoặc điều trị nội trú ban ngày, gồm 12 ký tự, theo định dạng<br>_Ví dụ_: Thời điểm người bệnh được chỉ định vào điều trị nội trú<br>hoặc điều trị nội trú ban ngày lúc 15 giờ 20 phút ngày<br>31/03/2017, khi đó được hiển thị là: 201703311520|

|36|<!-- FIELD_NAME_MISSING -->|Chuỗi|12|Ghi thời điểm người bệnh kết thúc điều trị nội trú, kết thúc điều trị<br>nội trú ban ngày, kết thúc điều trị ngoại trú hoặc kết thúc khám bệnh,<br>gồm 12 ký tự theo định dạng yyyymmddHHMM.<br>Ví dụ: Thời điểm người bệnh kết thúc điều trị lúc 09 giờ 20 phút<br>ngày 05/04/2022, khi đó được hiển thị là: 202204050920.<br>Lưu ý:<br>- Trường hợp khám bệnh (MA_LOAI_KCB = 01) thì ghi thời điểm<br>kết thúc lần khám bệnh;<br>- Trường hợp điều trị ngoại trú (MA_LOAI_KCB = 02); điều trị<br>ngoại trú các bệnh mạn tính dài ngày liên tục trong năm, áp dụng<br>cho các bệnh theo danh mục ban hành kèm theo Thông tư số<br>46/2016/TT-BYT, có khám bệnh và lĩnh thuốc (MA_LOAI_KCB =<br>05); nhận thuốc theo hẹn (không khám bệnh) (MA_LOAI_KCB =<br>07): Ghi ngày kết thúc của đợt KBCB (là ngày cuối cùng sử dụng<br>thuốc hoặc dịch vụ theo chỉ định của bác sỹ), gồm 02 ký tự giờ + 02<br>ký tự phút và mặc định là 2359 (Thời điểm cuối cùng của ngày kết<br>thúc đợt KBCB);<br>- Trường hợp điều trị ngoại trú các bệnh mạn tính dài ngày liên tục<br>trong năm, áp dụng cho các bệnh theo danh mục ban hành kèm theo<br>Thông tư số 46/2016/TT-BYT, có khám bệnh, có thực hiện các dịch<br>vụ kỹ thuật và/hoặc được sử dụng thuốc (MA_LOAI_KCB = 08):<br>Ghi thời điểm kết thúc của đợt KBCB (Ví dụ: Trường hợp chạy thận<br>nhân tạo thì ghi ngày cuối cùng của đợt chạy thận nhân tạo);<br>- Trường hợp người bệnh được chuyển tuyến đến cơ sở KBCB khác<br>thì thời điểm người bệnh ra viện bằng thời điểm người bệnh được<br>chuyển tuyến.|
|---|---|---|---|---|
|37|GIAY_CHUYEN_TUY|Chuỗi|50|Ghi số giấy chuyển tuyến của cơ sở KBCB nơi chuyển người<br>bệnh chuyển đi (trong trường hợp người bệnh có giấy chuyển<br>tuyến) hoặc số giấy hẹn khám lại (nếu có).|
|38|SO_NGAY_DTRI|Số|3|Là số ngày điều trị thực tế để phục vụ mục đích thống kê, cụ<br>thể như sau:<br>- Đối với Trường thông tin MA_LOAI_KCB có các mã "1",<br>"7", "9" thì trường thông tin SO_NGAY_DTRI = 0;<br>- Đối với Trường thông tin MA_LOAI_KCB có các mã "2",<br>"3", "4", "6" thì trường thông tin SO_NGAY_DTRI = Ngày<br>RA trừ (-) ngày VÀO cộng (+) 1;<br>- Đối với Trường thông tin MA_LOAI_KCB có mã "5" thì<br>trường thông tin SO_NGAY_DTRI = Số ngày dùng thuốc;<br>- Đối với Trường thông tin MA_LOAI_KCB có mã "8":<br>trường thông tin SO_NGAY_DTRI = Số ngày thực tế có sử<br>dụng DVKT.|
|39|PP_DIEU_TRI|Chuỗi||Ghi phương pháp điều trị theo đúng hướng dẫn tại Thông tư số<br>18/2022/TT-BYT của Bộ trưởng Bộ Y tế|

|40|KET_QUA_DTRI|Số|1|Ghi mã kết quả điều trị, trong đó:<br>- Mã "1": Khỏi;<br>- Mã "2": Đỡ;<br>- Mã "3": Không thay đổi;<br>- Mã "4": Nặng hơn;<br>- Mã "5": Tử vong;<br>- Mã "6": Tiên lượng nặng xin về;<br>- Mã "7": Chưa xác định (không thuộc một trong các mã kết<br>quả điều trị nêu trên).|
|---|---|---|---|---|
|41|MA_LOAI_RV|Số|1|Ghi mã loại ra viện, trong đó:<br>- Mã "1": Ra viện;<br>- Mã "2": Chuyển tuyến theo yêu cầu chuyên môn;<br>- Mã "3": Trốn viện;<br>- Mã "4": Xin ra viện;<br>- Mã "5": Chuyển tuyến theo yêu cầu người bệnh.|
|42|GHI_CHU|Chuỗi||Ghi lời dặn của bác sĩ hoặc nhân viên y tế đối với người bệnh<br>sau khi kết thúc lần KBCB.|
|43|NGAY_TTOAN|Chuỗi|12|Ghi thời điểm người bệnh thanh toán chi phí KBCB, gồm 12<br>ký tự theo định dạng yyyymmddHHMM.<br>_Ví dụ_: thời điểm người bệnh thanh toán chi phí KBCB lúc 09<br>giờ 20 phút, ngày 05/04/2017, khi đó thông tin được hiển thị<br>là: 201704050920;<br>**Lưu ý**: Trường hợp người bệnh ra viện nhưng chưa thực hiện<br>thanh toán thì để trống trường thông tin này khi chuyển dữ liệu<br>lên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định<br>BHYT của BHXH Việt Nam (Cổng tiếp nhận). Khi người bệnh<br>hoàn tất thủ tục thanh toán hoặc cơ sở KBCB hoàn tất thủ tục<br>thanh toán (do người bệnh không thực hiện hoặc không thể<br>thực hiện nghĩa vụ thanh toán) thì cơ sở KBCB có trách nhiệm<br>bổ sung thông tin ngày thanh toán và gửi lại dữ liệu lên Cổng<br>tiếp nhận hoặc bổ sung thông tin ngày thanh toán trực tiếp trên<br>Cổng tiếp nhận.|
|44|T_THUOC|Số|15|Ghi tổng thành tiền (THANH_TIEN_BV) các khoản chi của<br>thuốc (kể cả oxy), dịch truyền, máu và chế phẩm máu (đã bao<br>gồm chi phí xét nghiệm NAT và kháng thể bất thường, KIT<br>gạn tách tiểu cầu), chi phí vận chuyển máu và chi phí bao bì<br>(đối với thuốc thang) tại bảng XML 2 ban hành kèm theo<br>Quyết định này.|
|45|T_VTYT|Số|15|Ghi tổng thành tiền của vật tư y tế trong trường thông tin<br>THANH_TIEN_BV tại bảng XML 3 ban hành kèm theo Quyết<br>định này.|
|46|T_TONGCHI_BV|Số|15|Ghi tổng chi phí trong lần khám bệnh hoặc trong đợt điều trị, là<br>tổng số tiền THANH_TIEN_BV tại bảng XML2 và XML3 ban<br>hành kèm theo Quyết định này.|

|47|T_TONGCHI_BH|Số|15|Ghi tổng chi phí trong phạm vi quỹ BHYT thanh toán của lần<br>khám bệnh hoặc đợt điều trị, là tổng số tiền<br>THANH_TIEN_BH tại bảng XML2 và XML3 ban hành kèm<br>theo Quyết định này.|
|---|---|---|---|---|
|48|T_BNTT|Số|15|Ghi tổng số tiền người bệnh tự trả ngoài phạm vi chi trả của<br>Quỹ BHYT, là tổng số tiền T_BNTT tại bảng XML2 và XML3<br>ban hành kèm theo Quyết định này.|
|49|T_BNCCT|Số|15|Ghi tổng số tiền người bệnh cùng chi trả trong phạm vi quyền<br>lợi được hưởng BHYT, là tổng số tiền T_BNCCT tại bảng<br>XML2 và XML3 ban hành kèm theo Quyết định này.|
|50|T_BHTT|Số|15|Ghi tổng số tiền đề nghị cơ quan bảo hiểm xã hội thanh toán,<br>theo công thức sau: T_BHTT = T_TONGCHI_BH -|
|51|T_NGUONKHAC|Số|15|Ghi tổng số tiền các nguồn khác chi trả ngoài phạm vi chi trả<br>của quỹ BHYT, là tổng số tiền T_NGUONKHAC tại bảng<br>XML2 và XML3 ban hành kèm theo Quyết định này.|
|52|T_BHTT_GDV|Số|15|Ghi số tiền quỹ BHYT thanh toán đối với các khoản chi ngoài<br>định suất hoặc ngoài DRG theo quy định của Bộ Y tế (Là số<br>tiền T_BHTT tại bảng XML2 và XML3 đối với các chi phí có<br>MA_PTTT là "1" (Phí dịch vụ)).|
|53|NAM_QT|Số|4|Ghi năm mà cơ sở KBCB đề nghị cơ quan BHXH thanh toán.|
|54|THANG_QT|Số|2|Ghi tháng mà cơ sở KBCB đề nghị cơ quan BHXH thanh toán|
|55|MA_LOAI_KCB|Số|2|Ghi mã hình thức KBCB theo Bộ mã DMDC do Bộ trưởng Bộ<br>Y tế ban hành.|
|56|MA_KHOA|Chuỗi|50|Ghi mã khoa nơi người bệnh điều trị.<br>**Lưu ý:**<br>**+ **Mã khoa ghi theo Phụ lục số 5 ban hành kèm theo Quyết<br>định số 5937/QĐ-BYT ngày 30 tháng 12 năm 2021 của Bộ<br>trưởng Bộ Y tế.<br>+ Trường hợp người bệnh điều trị ở nhiều khoa thì thì ghi lần<br>lượt mã khoa nơi người bệnh đã điều trị, các mã khoa được<br>phân cách bằng dấu chấm phẩy “;”|
|57|MA_CSKCB|Chuỗi|5|Ghi mã cơ sở KBCB nơi người bệnh đến khám bệnh, điều trị<br>do cơ quan có thẩm quyền cấp.|
|58|MA_KHUVUC|Chuỗi|2|Ghi mã nơi sinh sống của người bệnh ghi trên thẻ BHYT (K1<br>hoặc K2 hoặc K3)|
|59|CAN_NANG|Chuỗi|6|Ghi số kilogram (kg) cân nặng của người bệnh, biểu thị đầy đủ<br>cả số thập phân, dấu thập phân là dấu chấm “.”, ghi đến 2 chữ<br>số sau dấu thập phân.|
|60|CAN_NANG_CON|Chuỗi|100|Ghi số gram (ký hiệu là: g) cân nặng của con mới sinh. Chỉ ghi<br>trong trường hợp sinh con.<br>Trường hợp sinh từ 02 con trở lên thì ghi lần lượt cân nặng của<br>từng con, cách nhau bởi dấu chấm phẩy “;”.|

|61|NAM_NAM_LIEN_TU|Chuỗi|8|Ghi thời điểm người bệnh tham gia BHYT đủ 05 năm liên tục,<br>gồm 08 ký tự theo định dạng yyyymmdd.|
|---|---|---|---|---|
|62|NGAY_TAI_KHAM|Chuỗi|50|Ghi ngày cơ sở KBCB hẹn người bệnh tái khám tiếp theo (nếu<br>có), gồm 08 ký tự theo định dạng yyyymmdd.<br>Trường hợp người bệnh được cơ sở KBCB hẹn nhiều ngày tái<br>khám khác nhau (người bệnh được chỉ định khám nhiều hơn 01<br>chuyên khoa trong một đợt KBCB) thì giữa các ngày tái khám<br>cách nhau bằng dấu chấm phẩy “;”.|
|63|MA_HSBA|Chuỗi|100|Ghi mã số hồ sơ bệnh án hoặc số phiếu khám ngoại trú của<br>người bệnh do cơ sở KBCB quy định.|
|64|MA_TTDV|Chuỗi|10|Ghi mã số định danh y tế (mã số BHXH) của người đứng đầu<br>cơ sở KBCB hoặc người được người đứng đầu cơ sở KBCB ủy<br>quyền được ký và đóng dấu của cơ sở KBCB đó.|
|65|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần thiết.|

##### **Bảng 2. Chỉ tiêu chi tiết thuốc** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu<br>tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn<br>lại ban hành kèm theo Quyết định này trong một lần khám bệnh,<br>chữa bệnh (PRIMARY KEY)).|
|2|STT|Số|10|Số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|MA_THUOC|Chuỗi|255|Ghi mã hoạt chất theo quy định tại Bộ mã danh mục dùng chung do<br>Bộ Y tế ban hành.<br>**Lưu ý**:<br>- Đối với thuốc do cơ sở KBCB tự bào chế, pha chế: ghi mã thuốc<br>gồm mã các hoạt chất/thành phần, cách nhau bằng dấu cộng "+";<br>- Khí oxy: ghi mã "40.17"; khí NO: ghi mã "40.573";<br>- Máu và chế phẩm của máu: Ghi theo mã danh mục dùng chung do<br>Bộ trưởng Bộ Y tế ban hành;<br>- Đối với máu và chế phẩm của máu có cộng thêm chi phí xét nghiệm<br>kháng thể bất thường: Sau mã máu và chế phẩm của máu ghi thêm 02<br>ký tự "KT", phân cách bằng dấu chấm “.”;<br>- Trường hợp máu và chế phẩm của máu có cộng thêm chi phí xét<br>nghiệm acid nucleic (viết tắt là NAT): Sau mã máu và chế phẩm của<br>máu ghi thêm 03 ký tự "NAT", phân cách bằng dấu chấm “.”;<br>- Trường hợp máu và chế phẩm của máu có cộng thêm chi phí xét<br>nghiệm kháng thể bất thường và xét nghiệm NAT: Sau mã máu và<br>chế phẩm của máu ghi thêm 05 ký tự "KTNAT", phân cách bằng dấu<br>chấm “.”;<br>- Trường hợp chế phẩm máu có sử dụng bộ dụng cụ gạn tách (kít tách<br>tiểu cầu, bạch cầu...) thì ghi mã bộ dụng cụ gạn tách theo quy định tại<br>Bộ mã danh mục dùng chung do Bộ Y tế ban hành vào trường<br>MA_VAT_TU tại Bảng 3;<br>- Trường hợp máu, chế phẩm máu phải thực hiện các xét nghiệm bắt<br>buộc có điều kiện quy định tại tiết d khoản 10 Điều 3 Thông tư số<br>17/2020/TT-BYT ngày 12/11/2020 của Bộ Y tế thì ghi thêm mã dịch<br>vụ kỹ thuật của xét nghiệm đó theo quy định tại Bộ mã DMDC do Bộ<br>trưởng Bộ Y tế ban hành tại trường MA_DVKT của Bảng này;|
|4|MA_PP_CHEBIEN|Chuỗi|255|Ghi mã phương pháp chế biến vị thuốc cổ truyền theo Bộ mã<br>DMDC do Bộ trưởng Bộ Y tế ban hành (Phương pháp chế biến<br>vị thuốc cổ truyền theo quy định tại Thông tư số 30/2017/TT-<br>BYT của Bộ trưởng Bộ Y tế).<br>**Ghi chú:** Trường hợp vị thuốc cổ truyền có nhiều phương pháp<br>chế biến thì ghi đầy đủ các mã phương pháp chế biến, giữa các<br>mã cách nhau bằng dấu chấm phẩy ";".|

|5|MA_CSKCB_THUOC|Chuỗi|5|- Trường hợp do thiên tai, dịch bệnh phải chuyển thuốc đến cơ<br>sở KBCB khác để điều trị cho người bệnh thì ghi C.XXXXX<br>(XXXXX là mã cơ sở KBCB nơi chuyển thuốc đi).<br>- Trường hợp thuốc thanh toán ngoài giá dịch vụ cận lâm sàng<br>chuyển thực hiện tại cơ sở KBCB khác thì ghi K.XXXXX<br>(XXXXX là mã cơ sở KBCB nơi thực hiện dịch vụ cận lâm<br>sàng).<br>- Trường hợp chế phẩm máu có sử dụng bộ dụng cụ gạn tách<br>(kít tách tiểu cầu, bạch cầu...) hoặc xét nghiệm được thanh toán<br>ngoài giá đơn vị máu, chế phẩm máu quy định tại tiết d khoản<br>10 Điều 3 Thông tư số 17/2020/TT-BYT ngày 12/11/2020 của<br>Bộ Y tế thì ghi M.XXXXX (trong đó XXXXX là mã cơ sở<br>KBCB của đơn vị cung cấp máu).|
|---|---|---|---|---|
|6|MA_NHOM|Số|2|Là mã nhóm theo chi phí, dùng để phân loại, sắp xếp các chi phí<br>vào các nhóm. Ghi theo Phụ lục số 3 ban hành kèm theo Quyết<br>định số 5937/QĐ-BYT ngày 30 tháng 12 năm 2021 của Bộ<br>trưởng Bộ Y tế.|
|7|TEN_THUOC|Chuỗi|1024|Ghi tên thuốc theo đúng tên thuốc được Cục Quản lý Dược hoặc<br>Cục Quản lý Y, dược cổ truyền cấp số đăng ký. Trường hợp<br>thuốc do cơ sở KBCB tự bào chế, chế biến thì ghi tên thuốc theo<br>đúng hồ sơ được người đứng đầu cơ sở KBCB phê duyệt.|
|8|DON_VI_TINH|Chuỗi|50|Ghi đơn vị tính nhỏ nhất, đơn vị tính của thuốc thực tế sử dụng<br>cho người bệnh.<br>**Lưu ý**: Trường hợp đơn vị tính là chai, lọ, túi, ống nhưng chia<br>nhỏ theo đơn vị quốc tế (viết tắt là UI) hoặc mililít (viết tắt là<br>ml) thì khai báo đơn vị tính theo UI hoặc ml.|
|9|HAM_LUONG|Chuỗi|1024|Ghi hàm lượng của thuốc theo kết quả trúng thầu (Ghi đúng<br>hàm lượng của thuốc được Cục Quản lý Dược hoặc Cục Quản lý<br>Y, dược cổ truyền cấp giấy đăng ký lưu hành hoặc hàm lượng<br>điều chỉnh theo văn bản của Cục Quản lý Dược hoặc Cục Quản<br>lý Y, dược cổ truyền hoặc do cơ sở KBCB tự bào chế).<br>**Lưu ý**:<br>- Trường hợp nếu thuốc có nhiều hoạt chất hoặc thành phần thì<br>ghi hàm lượng của các hoạt chất hoặc thành phần, giữa các hàm<br>lượng cách nhau bằng dấu cộng "+";<br>- Đối với vị thuốc, bài thuốc y học cổ truyền thì ghi đầy đủ khối<br>lượng của từng dược liệu, vị thuốc; giữa các khối lượng cách<br>nhau bằng dấu cộng "+".|

|10|DUONG_DUNG|Chuỗi|4|Ghi mã đường dùng tương ứng với đường dùng của thuốc theo<br>thông tin được Cục Quản lý Dược hoặc Cục Quản lý Y, dược cổ<br>truyền cấp giấy đăng ký lưu hành.<br>Trường hợp thuốc do cơ sở KBCB tự bào chế, chế biến thì ghi<br>mã đường dùng tương ứng với đường dùng của thuốc theo đúng<br>hồ sơ được người đứng đầu cơ sở KBCB phê duyệt.|
|---|---|---|---|---|
|11|DANG_BAO_CHE|Chuỗi|1024|Ghi dạng bào chế của thuốc (đối với thuốc hoá dược) hoặc dạng<br>bào chế, chế biến của thuốc (đối với thuốc cổ truyền, thuốc dược<br>liệu) theo thông tin được Cục Quản lý Dược hoặc Cục Quản lý<br>Y, dược cổ truyền cấp giấy đăng ký lưu hành. Trường hợp thuốc<br>do cơ sở KBCB tự bào chế, chế biến thì ghi dạng bào chế, chế<br>biến của thuốc theo đúng hồ sơ được người đứng đầu cơ sở<br>KBCB phê duyệt.|
|12|LIEU_DUNG|Chuỗi|1024|Ghi liều dùng thuốc cho người bệnh, cụ thể:<br>- Đối với ngoại trú, được thể hiện bằng: số lượng thuốc dùng<br>trong một lần sử dụng * số lần trong ngày * số ngày sử dụng<br>[tổng số thuốc/ngày].<br>_Ví dụ_: liều dùng của thuốc A: 2 viên/lần, 2 lần/ngày, sử dụng<br>trong 5 ngày thì được ghi như sau: 2 viên/lần * 2 lần/ngày * 5<br>ngày [4 viên/ngày].<br>- Đối với nội trú, được thể hiện bằng: số lượng thuốc dùng trong<br>một lần sử dụng * số lần trong ngày * 01 ngày [tổng số<br>thuốc/ngày].<br>**Lưu ý:**<br>**- **Trường hợp liều thuốc thay đổi trong ngày theo từng lần sử<br>dụng thì ghi chi tiết.<br>_Ví dụ:_liều dùng của thuốc A, sáng: 3 viên, chiều: 2 viên, tối: 1<br>viên. Như vậy, sẽ ghi như sau: Sáng: 3 viên, Chiều: 2 viên, Tối:<br>1 viên [6 viên/ngày].|
|13|CACH_DUNG|Chuỗi|1024|Ghi lời dặn của thầy thuốc trên đơn thuốc hoặc y lệnh.|

|14|SO_DANG_KY H o|Chuỗi|5|Ghi số đăng ký lưu hành của thuốc do Cục Quản lý Dược hoặc Cục<br>Quản lý Y, dược cổ truyền cấp phép (giữa các ký tự không có khoảng<br>trống (space)).<br>Lưu ý:<br>- Đối với dược liệu nhập khẩu thì ghi số giấy chứng nhận nguồn gốc,<br>xuất xứ của dược liệu (Giấy chứng nhận C/O) do cơ quan có thẩm<br>quyền của nước xuất khẩu cấp;<br>- Đối với dược liệu được cơ sở trong nước nuôi trồng, thu hái hoặc<br>khai thác tự nhiên đạt thực hành tốt nuôi trồng, thu hái dược liệu, khai<br>thác dược liệu tự nhiên thì ghi số Giấy chứng nhận dược liệu đạt<br>- Đối với vị thuốc cổ truyền thì ghi số đăng ký lưu hành của vị thuốc<br>cổ truyền;<br>- Đối với thuốc cổ truyền thì ghi số đăng ký lưu hành của thuốc cổ<br>truyền.<br>- Trường thông tin này không bắt buộc đối với khí Oxy (mã "40.17");<br>khí Nitric oxid (NO) (mã "40.573"); máu và chế phẩm của máu; thuốc<br>thang; thuốc phóng xạ (trừ trường hợp thuốc phóng xạ được Cục<br>Quản lý Dược cấp giấy đăng ký lưu hành);<br>- Đối với thuốc tự bào chế, pha chế, chế biến: mã hóa theo chữ cái<br>“HD” (hoá dược) hoặc "CP" (chế phẩm) hoặc "VT" (vị thuốc), mã cơ<br>sở KBCB, hai ký tự cuối của năm ban hành và số thứ tự của thuốc<br>trong danh mục thuốc tự bào chế do thủ trưởng cơ sở KBCB ban<br>hành, cách nhau bằng dấu chấm ".".<br>Ví dụ: Chế phẩm y học cổ truyền C được bào chế tại cơ sở khám chữa<br>bệnh B có mã cơ sở khám chữa bệnh là 19010. Thuốc C có số thứ tự<br>trong danh Mục thuốc tự bào chế do thủ trưởng cơ sở khám chữa|
|---|---|---|---|---|
|||||Ghi thông tin thầu của thuốc theo thứ tự, gồm: Số quyết định phê|

|15|TT_THAU a|Chuỗi|5|duyệt kết quả lựa chọn nhà thầu; mã gói thầu; mã nhóm thầu (theo<br>quy định tại Phụ lục số 6 ban hành kèm theo Quyết định số 5937/QĐ-<br>BYT ngày 30 tháng 12 năm 2021 của Bộ trưởng Bộ Y tế); năm ban<br>hành quyết định phê duyệt kết quả lựa chọn nhà thầu. Các thông tin<br>này cách nhau bằng dấu chấm phẩy “;”.<br>Lưu ý:<br>- Trường hợp có hai nhà thầu cùng trúng thầu một thuốc thì bổ sung<br>mã gói thầu và số thứ tự nhà thầu trúng thầu của đơn vị đấu thầu, với<br>định dạng Gi.YY, trong đó: "i" là số gói thầu, YY là số thứ tự của nhà<br>thầu trúng thầu trong quyết định của cơ quan có thẩm quyền phê<br>duyệt kết quả trúng thầu, cách nhau bằng dấu chấm phẩy “;”.<br>Ví dụ: Tại gói thầu số 2 (Quyết định trúng thầu số 57/QĐ-TTMS, năm<br>2022), thuốc Ulceron (số đăng ký: VN-20256-17, hoạt chất:<br>Pantoprazol, hàm lượng: 40mg, dạng bào chế: bột đông khô pha tiêm,<br>đường dùng: Tiêm hoặc truyền, nhóm 1; nhà sản xuất: Anfarm hellas<br>S.A; nước sản suất: Greece (Hy Lạp); quy cách đóng gói: hộp 1 lọ) có<br>02 nhà thầu trúng thầu, nhà thầu trúng thầu thứ nhất là Công ty CP<br>Dược vật tư y tế Quảng Trị, nhà thầu trúng thầu thứ 2 là Công ty Cổ<br>phần dược phẩm Vipharco cùng trúng thầu, thì mã hóa bổ sung thêm<br>trong thông tin thầu sau năm ban hành, nhà thầu thứ nhất là: 57/QĐ-<br>TTMS;G1;N1;2022;G2.01 và nhà thầu thứ 2 là 57/QĐ-<br>TTMS;G1;N1;2022;G2.02<br>- Trường hợp áp thầu thì bổ sung mã đơn vị ban hành quyết định.<br>Trong đó: Trung tâm mua sắm tập trung (TTMSTT) quốc gia là mã<br>"00"; trường hợp các tỉnh, thành phố đấu thầu tập trung thì lấy mã<br>tỉnh, thành phố; trường hợp cơ sở KCB đấu thầu thì lấy mã cơ sở<br>KCB), cách nhau bằng dấu chấm phẩy “;”.|
|---|---|---|---|---|
|16|PHAM_VI|Số|1|Ghi mã để xác định phạm vi của thuốc, trong đó:<br>- Mã "1": là thuốc trong phạm vi hưởng BHYT (trong danh mục<br>thuốc do quỹ BHYT chi trả);<br>- Mã "2": là thuốc ngoài phạm vi hưởng BHYT (ngoài danh<br>mục thuốc do quỹ BHYT chi trả);<br>- Mã "3": là thuốc ngoài danh mục thuốc do quỹ BHYT chi trả ,<br>trừ các đối tượng thuộc quân đội, công an, cơ yếu theo quy định<br>của Nghị định 70/2015/NĐ-CP của Chính phủ.<br>~~ố~~<br>~~ầ~~<br>~~ế~~<br>~~ầ~~|
|17|TYLE_TT_BH|Số|3|Ghi tỷ lệ thanh toán BHYT đối với thuốc có quy định tỷ lệ phần<br>trăm (ký hiệu: %); Biểu thị bằng số nguyên dương.<br>_Ví dụ_: Tỷ lệ thanh toán của thuốc là 50% thì ghi là 50.<br>- Trường hợp thuốc không quy định tỷ lệ thanh toán thì ghi<br>"100", trường hợp thuốc không thuộc phạm vi thanh toán của<br>quỹ BHYT thì ghi là "0".|
|18|SO_LUONG|Số|10|Ghi số lượng thuốc thực tế sử dụng cho người bệnh, làm tròn số<br>đến 3 chữ số thập phân. Sử dụng dấu chấm “.” để phân cách<br>giữa số Nguyên (hàng đơn vị) với số thập phân đầu tiên.|

|19|DON_GIA|Số|5|Ghi đơn giá của thuốc, là giá theo hóa đơn mua vào của cơ sở<br>KBCB; làm tròn đến 3 (ba) chữ số thập phân. Sử dụng dấu chấm<br>“.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập phân<br>đầu tiên, trong đó:<br>- Đối với thuốc do cơ sở KBCB tự bào chế, chế biến: Đơn giá<br>của thuốc do người đứng đầu cơ sở KBCB xây dựng, phê duyệt<br>và thống nhất với cơ quan BHXH để làm căn cứ thanh toán.<br>- Trường hợp thuốc cổ truyền (bao gồm cả vị thuốc cổ truyền),<br>thuốc hoá dược, thuốc phóng xạ (theo Thông tư 43/2017/TT-<br>BYT, Thông tư 27/2020/TT-BYT, Thông tư 20/2022/TT-BYT)<br>thì đơn giá được cộng thêm các chi phí khác (nếu có) theo quy<br>định của Bộ Y tế.<br>- Trường hợp thuốc sử dụng thực tế theo đơn vị tính được chia<br>nhỏ hơn đơn vị tính tại quyết định phê duyệt kết quả lựa chọn<br>nhà thầu (ví dụ: đơn vị tính theo đơn vị quốc tế (UI) hoặc mililít<br>(ml)) thì đơn giá phải chia nhỏ theo đơn vị tính tương ứng.|
|---|---|---|---|---|
|20|THANH_TIEN_BV|Số|15|Được tính theo công thức: THANH_TIEN_BV = SO_LUONG<br>* DON_GIA, làm tròn số đến 2 chữ số thập phân. Sử dụng dấu<br>chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.|
|21|THANH_TIEN_BH|Số|15|Được tính theo công thức: THANH_TIEN_BH = SO_LUONG<br>* DON_GIA * TYLE_TT_BH/100, làm tròn số đến 2 chữ số<br>thập phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên<br>(hàng đơn vị) với số thập phân đầu tiên.|
|22|T_NGUONKHAC_NS|Số|15|Ghi số tiền thuốc được ngân sách nhà nước (Trung ương<br>và/hoặc địa phương) hỗ trợ, làm tròn số đến 2 chữ số thập phân.<br>Sử dụng dấu chấm “.” để phân cách giữa số Nguyên (hàng đơn<br>vị) với số thập phân đầu tiên.|
|23|T_NGUONKHAC_VT|Số|15|Ghi số tiền thuốc được các tổ chức, đơn vị có trụ sở ngoài lãnh<br>thổ Việt Nam hoặc các cá nhân đang sinh sống, học tập, lao<br>động ngoài lãnh thổ Việt Nam hỗ trợ; làm tròn số đến 2 chữ số<br>thập phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên<br>(hàng đơn vị) với số thập phân đầu tiên.|
|24|T_NGUONKHAC_VT|Số|15|Ghi số tiền thuốc được các tổ chức, cơ quan, đơn vị có trụ sở<br>trong lãnh thổ Việt Nam hoặc các cá nhân đang sinh sống, học<br>tập, lao động trong lãnh thổ Việt Nam hỗ trợ; làm tròn số đến 2<br>chữ số thập phân. Sử dụng dấu chấm “.” để phân cách giữa số<br>Nguyên (hàng đơn vị) với số thập phân đầu tiên.|

|25|T_NGUONKHAC_CL|Số|15|Ghi số tiền thuốc được các nguồn khác còn lại (Không thuộc<br>một trong ba nguồn quy định tại các trường thông tin:<br>T_NGUONKHAC_NSNN, T_NGUONKHAC_VTNN,<br>T_NGUONKHAC_VTTN) hỗ trợ; làm tròn số đến 2 chữ số<br>thập phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên<br>(hàng đơn vị) với số thập phân đầu tiên.|
|---|---|---|---|---|
|26|T_NGUONKHAC|Số|15|Công thức tính T_NGUONKHAC = T_NGUONKHAC_NSNN<br>+ T_NGUONKHAC_VTNN + T_NGUONKHAC_VTTN +<br>Trường hợp chi phí KBCB được nguồn tài chính khác hỗ trợ<br>thông qua cơ sở KBCB (Với điều kiện: 0 < T_NGUONKHAC <<br>THANH_TIEN_BV), khi đó:<br>a) Trường hợp nguồn tài chính này chỉ hỗ trợ cho riêng cá nhân<br>người bệnh thì số tiền hỗ trợ này sẽ được khấu trừ vào các chi<br>phí theo thứ tự ưu tiên lần lượt như sau: T_BNTT, T_BNCCT,<br>b) Trường hợp nguồn tài chính này hỗ trợ chung cho cơ sở KCB<br>để hỗ trợ chi phí KCB cho người bệnh thì nguồn tài chính này<br>được khấu trừ vào tổng chi phí KBCB, phần chi phí còn lại<br>được phân bổ như bình thường (theo thứ tự: Quỹ BHYT chi trả,<br>người bệnh cùng chi trả, người bệnh tự trả).<br>c) Trường hợp đặc biệt, không thuộc hướng dẫn tại điểm a, điểm<br>b nêu trên thì Bộ Y tế sẽ có hướng dẫn cách tính cụ thể (Ví dụ:<br>đối với thuốc ARV thì T_NGUONKHAC = T_BNCCT (tạm<br>tính), T_BNCCT = 0).|

27 MUC_HUONG Số 3

Ghi mức hưởng tương ứng với từng loại chi phí, trong đó:

- Trường hợp người bệnh KBCB BHYT đúng tuyến ghi mức
hưởng là 80 hoặc 95 hoặc 100; trường hợp trái tuyến ghi mức
hưởng sau khi đã nhân với tỷ lệ hưởng trái tuyến tương ứng với
tuyến chuyên môn kỹ thuật của cơ sở KCB.
Ví dụ: Người bệnh có mức hưởng BHYT 80%, điều trị trái
tuyến nội trú tại cơ sở KBCB tuyến trung ương (có tỷ lệ hưởng
trái tuyến là 40%) ghi mức hưởng là 32;

- Trường hợp người bệnh KBCB BHYT đúng tuyến, có tổng chi
phí trong phạm vi được hưởng dưới 15% mức lương cơ sở hoặc
KBCB tại Trạm y tế tuyến xã hoặc người bệnh đủ điều kiện
được hưởng miễn cùng chi trả trong năm: ghi mức hưởng 100;

- Trường hợp người bệnh KBCB BHYT trái tuyến, có tổng chi
phí dưới 15% mức lương cơ sở ghi mức trái tuyến tương ứng
với tuyến chuyên môn kỹ thuật của cơ sở KCB.

- Trường hợp người bệnh có bệnh mạn tính, đã được khám và
chỉ định thuốc ở tuyến trên, nhưng được cấp phát thuốc tại Trạm
y tế tuyến xã theo quy định của Thông tư số 30/2018/TT-BYT
và điểm h khoản 1 Điều 14 Nghị định số 146/2018/NĐ-CP thì
ghi mức hưởng theo mức hưởng của thẻ BHYT (trừ trường hợp
có tổng chi phí KBCB trong một lần khám bệnh dưới 15% mức
lương cơ sở thì ghi mức hưởng là 100).

28 T_BNTT Số 15

Ghi số tiền người bệnh tự trả ngoài phạm vi chi trả của quỹ
BHYT, làm tròn số đến 2 chữ số thập phân. Sử dụng dấu chấm
“.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập phân
đầu tiên.
a) Cách tính áp dụng đối với trường hợp quy định tại điểm a
trường T_NGUONKHAC bảng này:

- Bước 1: T_BNTT (tạm tính) = THANH_TIEN_BV THANH_TIEN_BH

- Bước 2: So sánh các giá trị
+ Nếu T_NGUONKHAC = 0 thì T_BNTT giữ nguyên
+ T_NGUONKHAC > 0 THÌ CÓ 2 trường hợp:
(i) T_NGUONKHAC < T_BNTT (tạm tính):
T_BNTT = T_BNTT (tạm tính) - T_NGUONKHAC.
(ii) T_NGUONKHAC >= T_BNTT (tạm tính) thì T_BNTT = 0.
b) Cách tính áp dụng đối với trường hợp quy định tại điểm b
Trường số 24 (T_NGUONKHAC):
_Ví dụ:_ Tổng chi phí tiền thuốc A (có tỷ lệ thanh toán 50%) hết
10.000.000đ; nhà tài trợ hỗ trợ 3.000.000đ. Như vậy Tổng chi
phí tiền thuốc còn lại là 7.000.000đ, người bệnh có mức hưởng
80%, được phân bổ như sau:
+ THANH_TIEN_BH = 7.000.000 * 50% = 3.500.000đ
+ T_BHTT = 3.500.000 * 80% = 2.800.000đ
+ T_BNCCT = 3.500.000 - 2.800.000 = 700.000đ
+ T_BNTT = 7.000.000 - 3.500.000 = 3.500.000đ

29 T_BNCCT Số 15

Ghi số tiền người bệnh cùng chi trả trong phạm vi quyền lợi
mức hưởng BHYT, làm tròn số đến 2 chữ số thập phân. Sử dụng
dấu chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số
thập phân đầu tiên.
a) Cách tính áp dụng đối với trường hợp quy định tại điểm a
trường T_NGUONKHAC:

- Bước 1:

+) T_BNTT (tạm tính) = THANH_TIEN_BV THANH_TIEN_BH
+) T_BHTT (tạm tính) = THANH_TIEN_BH *
MUC_HUONG/100
+) T_BNCCT (tạm tính) = THANH_TIEN_BH - T_BHTT (tạm
tính)

- Bước 2:
+) Nếu T_NGUONKHAC < = T_BNTT (tạm tính) thì
T_BNCCT = T_BNCCT (tạm tính)
+) Nếu T_NGUONKHAC > T_BNTT (tạm tính) thì có 2 trường
hợp:
(i) Nếu T_BNCCT (tạm tính) > T_NGUONKHAC - T_BNTT
(tạm tính) thì T_BNCCT = T_BNCCT (tạm tính) (T_NGUONKHAC - T_BNTT (tạm tính))
(ii) Nếu T_BNCCT (tạm tính) <= T_NGUONKHAC - T_BNTT
(tạm tính) thì T_BNCCT = 0
b) Cách tính áp dụng đối với trường hợp quy định tại điểm b
trường T_NGUONKHAC: Xem ví dụ tại trường T_BNTT bảng
này.

|30|T_BHTT g|Số|5|Ghi số tiền cơ sở KBCB đề nghị cơ quan BHXH thanh toán theo<br>phạm vi quyền lợi mức hưởng BHYT của người bệnh, làm tròn<br>số đến 2 chữ số thập phân. Sử dụng dấu chấm “.” để phân cách<br>giữa số Nguyên (hàng đơn vị) với số thập phân đầu tiên.<br>a) Cách tính áp dụng đối với trường hợp quy định tại điểm a<br>trường T_NGUONKHAC:<br>- Bước 1:<br>(i) T_BHTT (tạm tính) = THANH_TIEN_BH *<br>(ii) T_BNCCT (Tạm tính) = THANH_TIEN_BH - T_BHTT<br>(Tạm tính)<br>(iii) T_BNTT (tạm tính) = THANH_TIEN_BV -<br>- Bước 2:<br>(i) Nếu T_NGUONKHAC < T_BNCCT (tạm tính) + T_BNTT<br>(tạm tính) thì T_BHTT = T_BHTT (tạm tính)<br>(ii) Nếu T_NGUONKHAC > T_BNCCT (tạm tính) + T_BNTT<br>(tạm tính) thì T_BHTT = T_BHTT (tạm tính) -<br>(T_NGUONKHAC - T_BNCCT (tạm tính) - T_BNTT (tạm<br>tính)).<br>b) Cách tính áp dụng đối với trường hợp quy định tại điểm b<br>trường T_NGUONKHAC: Xem ví dụ tại trường T_BNTT|
|---|---|---|---|---|
|31|MA_KHOA|Chuỗi|15|Ghi mã khoa nơi người bệnh được chỉ định sử dụng thuốc, theo<br>Phụ lục số 5 ban hành kèm theo Quyết định số 5937/QĐ-BYT<br>ngày 30 tháng 12 năm 2021 của Bộ trưởng Bộ Y tế.|
|32|MA_BAC_SI|Chuỗi|255|Ghi mã bác sỹ khám, chỉ định thuốc (là mã định danh y tế của<br>nhân viên y tế).<br>**Lưu ý:** Trường hợp thuốc được chỉ định bởi bác sỹ tuyến trên<br>thì ghi mã định danh y tế của bác sỹ tuyến trên và mã định danh<br>y tế của nhân viên y tế cấp thuốc, cách nhau bằng dấu chấm<br>phẩy ";".|

|33|MA_DICH_VU H o|Chuỗi|5|Ghi mã dịch vụ kỹ thuật hoặc mã dịch vụ khám bệnh thực hiện đối<br>với người bệnh, theo quy định tại Bộ mã danh mục dùng chung<br>(DMDC) do Bộ trưởng Bộ Y tế ban hành.<br>Lưu ý: Bắt buộc ghi mã dịch vụ kỹ thuật trong trường hợp:<br>- Có sử dụng thuốc để thực hiện dịch vụ kỹ thuật và thuốc được thanh<br>toán riêng do chưa được kết cấu trong giá dịch vụ kỹ thuật (như hợp<br>chất đánh dấu phóng xạ, thuốc cản quang, botulium toxine,...);<br>- Trường hợp xét nghiệm được thanh toán ngoài giá đơn vị máu, chế<br>phẩm máu quy định tại tiết d khoản 10 Điều 3 Thông tư số<br>17/2020/TT-BYT ngày 12/11/2020 của Bộ Y tế thì ghi mã dịch vụ kỹ<br>thuật của xét nghiệm đó theo quy định tại Bộ mã DMDC do Bộ<br>trưởng Bộ Y tế ban hành;<br>- Thuốc thanh toán ngoài giá dịch vụ cận lâm sàng chuyển thực hiện<br>tại cơ sở KBCB khác thì mã hóa mã dịch vụ kỹ thuật như sau: mã hoá<br>theo nguyên tắc: XX.YYYY.ZZZZ.K.WWWWW, trong đó<br>XX.YYYY.ZZZZ là mã dịch vụ cận lâm sàng tại Bộ mã DMDC do<br>Bộ Y tế ban hành, WWWWW là mã cơ sở KBCB nơi thực hiện dịch<br>vụ cận lâm sàng.<br>- Thuốc sử dụng trong DVKT thực hiện bằng phương pháp vô cảm<br>gây tê, bổ sung cụm từ "_GT" sau mã DVKT tương đương<br>- Thuốc sử dụng trong DVKT đã chỉ định thực hiện nhưng vì nguyên<br>nhân diễn biến bệnh hoặc thể trạng người bệnh nên không thể tiếp tục<br>thực hiện được kỹ thuật đã chỉ định theo quy định tại khoản 3 Điều 7<br>Thông tư số 39/2018/TT-BYT thì bổ sung các ký tự "_TB" sau mã<br>DVKT tương đương (mã có cấu trúc: XX.YYYY.ZZZZ_TB).<br>- Thuốc sử dụng trong DVKT đã được cấp có thẩm quyền phê duyệt|
|---|---|---|---|---|
|34|NGAY_YL|Chuỗi|12|Ghi thời điểm ra y lệnh thuốc, gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHmm, trong đó: 04 ký tự năm + 02 ký tự tháng +<br>02 ký tự ngày + 02 ký tự giờ (tính theo 24 giờ) + 02 ký tự phút).<br>_Ví dụ_: Thời điểm ra y lệnh thuốc lúc 15 giờ 20 phút, ngày<br>31/03/2022, khi đó được hiển thị là: 202203311520.<br>**Lưu ý**: Trường hợp ngày ra y lệnh thuốc là ngày nghỉ (Thứ Bảy<br>và/hoặc Chủ Nhật), ngày nghỉ lễ, nghỉ tết theo quy định của Bộ<br>Luật Lao động thì ngày ra y lệnh của những ngày nghỉ mặc định<br>là ngày ra y lệnh của ngày liền kề trước ngày nghỉ (Trừ trường<br>hợp cấp cứu hoặc các trường hợp bất thường khác).|
|35|MA_PTTT|Số|1|Ghi mã phương thức thanh toán đối với thuốc, trong đó:<br>- Mã "1": thanh toán theo Phí dịch vụ;<br>- Mã "2": thanh toán theo Định suất;<br>- Mã "3": thanh toán theo Trường hợp bệnh (DRG).|
|36|NGUON_CTRA|Số|1|Ghi mã để xác định nguồn thuốc chi trả cho người bệnh, như<br>thuốc ARV, thuốc điều trị viêm gan C…, trong đó:<br>- Mã "1": do quỹ BHYT chi trả;<br>- Mã "2": thuốc của dự án hoặc viện trợ;<br>- Mã "3": thuốc thuộc chương trình mục tiêu Quốc gia;<br>- Mã "4": các nguồn khác chi trả.|

|37|VET_THUONG_TP|Số|1|Ghi mã của vết thương tái phát. Chỉ ghi số "1" nếu sử dụng<br>thuốc có quy định tỷ lệ thanh toán BHYT để điều trị vết thương<br>tái phát, bệnh tật tái phát cho đối tượng thương binh, người<br>hưởng chính sách như thương binh, thương binh loại B, bệnh|
|---|---|---|---|---|
|38|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng sử dụng khi cần thiết.|

**Ghi chú: Ký hiệu trong bảng này được hiểu như sau:**

 - Ký hiệu (*): phép tính nhân;

 - Ký hiệu (>): lớn hơn;

 - Ký hiệu (<): nhỏ hơn.

##### **Bảng 3. Chỉ tiêu chi tiết dịch vụ kỹ thuật và vật tư y tế** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu tổng<br>hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn lại ban<br>hành kèm theo Quyết định này trong một lần khám bệnh, chữa bệnh|
|2|STT|Số|10|Số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|MA_DICH_VU|Chuỗi|50|Ghi mã dịch vụ kỹ thuật hoặc mã tiền khám hoặc mã tiền giường bệnh theo<br>hạng bệnh viện theo quy định tại Bộ mã DMDC do Bộ Y tế ban hành.<br>**Lưu ý:**<br>- Vận chuyển người bệnh: Ghi VC.XXXXX, trong đó XXXXX là mã cơ sở<br>KBCB nơi người bệnh được chuyển đến;<br>- Mã tiền giường theo hạng bệnh viện quy định tại Bộ mã DMDC do Bộ<br>trưởng Bộ Y tế ban hành;<br>- Trường hợp phải chuyển mẫu bệnh phẩm hoặc chuyển người bệnh đến cơ<br>sở KBCB khác để thực hiện dịch vụ cận lâm sàng theo quy định của Thông<br>tư 09/2019/TT-BYT thì mã hoá theo nguyên tắc:<br>XX.YYYY.ZZZZ.K.WWWWW, trong đó XX.YYYY.ZZZZ là mã dịch vụ<br>cận lâm sàng tại Bộ mã DMDC do Bộ trưởng Bộ Y tế ban hành,<br>WWWWW là mã cơ sở KBCB nơi thực hiện dịch vụ cận lâm sàng.<br>- Đối với DVKT sử dụng phương pháp vô cảm gây tê, bổ sung ký hiệu<br>"_GT" sau mã DVKT tương đương. Cụ thể: (XX.YYYY.ZZZZ_GT).<br>- Đối với DVKT đã được cấp có thẩm quyền phê duyệt thực hiện nhưng<br>chưa được quy định mức giá theo quy định tại khoản 3 Điều 7 Thông tư số<br>39/2018/TT-BYT thì mã hoá DVKT theo nguyên tắc mã DVKT tương<br>đương, 04 ký tự cuối ghi "0000" (khi đó, mã có cấu trúc: XX.YYYY.0000);<br>- Đối với DVKT đã chỉ định thực hiện nhưng vì nguyên nhân diễn biến<br>bệnh hoặc thể trạng người bệnh nên không thể tiếp tục thực hiện được kỹ<br>thuật đã chỉ định theo quy định tại khoản 3 Điều 7 Thông tư số 39/2018/TT-<br>BYT thì bổ sung các ký tự "_TB" sau mã DVKT tương đương (khi đó, mã<br>có cấu trúc: XX.YYYY.ZZZZ_TB); DON_GIA_BH = 0; DON_GIA_BV<br>= 0; các thuốc, VTYT (thuộc phạm vi chi trả của quỹ BHYT) đã được sử<br>dụng cho người bệnh thì cơ sở KBCB thống kê vào các trường dữ liệu|

4 MA_PTTT_QT Chuỗi 255

Ghi mã dịch vụ kỹ thuật hoặc mã tiền khám hoặc mã tiền giường bệnh theo
hạng bệnh viện theo quy định tại Bộ mã DMDC do Bộ Y tế ban hành.
**Lưu ý:**

- Vận chuyển người bệnh: Ghi VC.XXXXX, trong đó XXXXX là mã cơ sở
KBCB nơi người bệnh được chuyển đến;

- Mã tiền giường theo hạng bệnh viện quy định tại Bộ mã DMDC do Bộ
trưởng Bộ Y tế ban hành;

- Trường hợp phải chuyển mẫu bệnh phẩm hoặc chuyển người bệnh đến cơ
sở KBCB khác để thực hiện dịch vụ cận lâm sàng theo quy định của Thông
tư 09/2019/TT-BYT thì mã hoá theo nguyên tắc:
XX.YYYY.ZZZZ.K.WWWWW, trong đó XX.YYYY.ZZZZ là mã dịch vụ
cận lâm sàng tại Bộ mã DMDC do Bộ trưởng Bộ Y tế ban hành,
WWWWW là mã cơ sở KBCB nơi thực hiện dịch vụ cận lâm sàng.

- Đối với DVKT sử dụng phương pháp vô cảm gây tê, bổ sung ký hiệu
"_GT" sau mã DVKT tương đương. Cụ thể: (XX.YYYY.ZZZZ_GT).

- Đối với DVKT đã được cấp có thẩm quyền phê duyệt thực hiện nhưng
chưa được quy định mức giá theo quy định tại khoản 3 Điều 7 Thông tư số
39/2018/TT-BYT thì mã hoá DVKT theo nguyên tắc mã DVKT tương
đương, 04 ký tự cuối ghi "0000" (khi đó, mã có cấu trúc: XX.YYYY.0000);

DON_GIA_BH = 0;

- Đối với DVKT đã chỉ định thực hiện nhưng vì nguyên nhân diễn biến
bệnh hoặc thể trạng người bệnh nên không thể tiếp tục thực hiện được kỹ
thuật đã chỉ định theo quy định tại khoản 3 Điều 7 Thông tư số 39/2018/TTBYT thì bổ sung các ký tự "_TB" sau mã DVKT tương đương (khi đó, mã
có cấu trúc: XX.YYYY.ZZZZ_TB); DON_GIA_BH = 0; DON_GIA_BV
= 0; các thuốc, VTYT (thuộc phạm vi chi trả của quỹ BHYT) đã được sử
dụng cho người bệnh thì cơ sở KBCB thống kê vào các trường dữ liệu

|5|MA_VAT_TU a n|Chuỗi|5|Ghi mã VTYT chi tiết đến từng kích thước cụ thể đã được sử dụng<br>cho người bệnh.<br>Lưu ý:<br>- Mã VTYT được cấp tự động trên Cổng tiếp nhận dữ liệu Hệ thống<br>thông tin giám định BHYT của BHXH Việt Nam theo nguyên tắc mã<br>hóa quy định tại Quyết định số 5086/QĐ-BYT ngày 04/11/2021 của<br>Bộ trưởng Bộ Y tế;<br>- Chỉ ghi các VTYT chưa có trong cơ cấu giá dịch vụ kỹ thuật;<br>VTYT sử dụng trong DVKT đã chỉ định thực hiện nhưng vì nguyên<br>nhân diễn biến bệnh hoặc thể trạng người bệnh nên không thể tiếp tục<br>thực hiện được kỹ thuật đã chỉ định theo quy định tại khoản 3 Điều 7<br>Thông tư số 39/2018/TT-BYT; VTYT sử dụng trong DVKT đã được<br>cấp có thẩm quyền phê duyệt thực hiện nhưng chưa được quy định<br>mức giá theo quy định tại khoản 3 Điều 7 Thông tư số 39/2018/TT-<br>- Các VTYT sử dụng trong phẫu thuật, thủ thuật được thanh toán<br>riêng: ghi mã phẫu thuật, thủ thuật vào trường thông tin:<br>- Các VTYT không sử dụng trong phẫu thuật, thủ thuật: trường thông<br>tin mã dịch vụ <MA_DICH_VU> để trống;<br>- Đối với sinh phẩm xét nghiệm COVID-19: Ghi mã sinh phẩm xét<br>nghiệm COVID-19 theo hướng dẫn tại Phụ lục 9 ban hành kèm theo<br>Quyết định số 5937/QĐ-BYT ngày 30/12/2021 của Bộ trưởng Bộ Y<br>tế.|
|---|---|---|---|---|
|6|MA_NHOM|Số|2|Ghi mã nhóm theo chi phí, dùng để phân loại, sắp xếp các chi phí vào<br>các nhóm, ghi theo Phụ lục số 3 ban hành kèm theo Quyết định số<br>5937/QĐ-BYT ngày 30 tháng 12 năm 2021 của Bộ trưởng Bộ Y tế.|
|7|GOI_VTYT|Chuỗi|3|Ghi mã gói VTYT trong một lần sử dụng dịch vụ kỹ thuật (lần thứ<br>nhất ghi G1, lần thứ hai ghi G2,…).|
|8|TEN_VAT_TU|Chuỗi|1024|Ghi tên thương mại của VTYT.<br>**Lưu ý:**Đối với sinh phẩm xét nghiệm COVID-19: Ghi tên sinh phẩm<br>thương mại vào trường thông tin "TEN_VAT_TU" theo hướng dẫn<br>tại Phụ lục 9 ban hành kèm theo Quyết định số 5937/QĐ-BYT ngày<br>30/12/2021 của Bộ trưởng Bộ Y tế.|
|9|TEN_DICH_VU|Chuỗi|1024|Ghi tên dịch vụ kỹ thuật hoặc tên dịch vụ khám bệnh hoặc tên giường<br>bệnh đề nghị quỹ BHYT thanh toán.<br>**Lưu ý:**<br>- Đối với dịch vụ kỹ thuật, trường hợp cần ghi rõ vị trí, phương pháp<br>thực hiện hoặc phân biệt các mức giá khác nhau thì sau tên dịch vụ<br>kỹ thuật ghi phần mô tả chi tiết trong ngoặc vuông [ ];<br>- Đối với DVKT sử dụng phương pháp vô cảm gây tê, bổ sung cụm<br>từ "[gây tê]" sau tên dịch vụ;<br>- Đối với trường hợp xét nghiệm COVID-19 thì ghi tên dịch vụ theo<br>quy định tại Phụ lục 9 ban hành kèm theo Quyết định số 5937/QĐ-<br>BYT ngày 30/12/2021 của Bộ trưởng Bộ Y tế.|

|10|MA_XANG_DAU|Chuỗi|20|Ghi mã loại xăng, dầu để tính chi phí vận chuyển người bệnh, ghi<br>theo Bộ mã DMDC do Bộ trưởng Bộ Y tế ban hành.|
|---|---|---|---|---|
|11|DON_VI_TINH|Chuỗi|50|Ghi đơn vị tính của VTYT hoặc DVKT đề nghị thanh toán.|
|12|PHAM_VI|Số|1|Ghi mã để xác định phạm vi của VTYT, dịch vụ kỹ thuật, trong đó:<br>- Mã "1": Trong phạm vi hưởng BHYT (trong danh mục do quỹ<br>BHYT chi trả);<br>- Mã "2": Ngoài phạm vi hưởng BHYT (ngoài danh mục do quỹ<br>BHYT chi trả);<br>- Mã "3": Ngoài danh mục do quỹ BHYT chi trả nhưng được quỹ<br>BHYT chi trả cho các đối tượng thuộc quân đội, công an, cơ yếu theo<br>quy định của Nghị định 70/2015/NĐ-CP của Chính phủ.|
|13|SO_LUONG|Số|10|Ghi số lượng dịch vụ kỹ thuật hoặc VTYT thực tế sử dụng cho người<br>bệnh, làm tròn số đến 3 chữ số thập phân. Sử dụng dấu chấm “.” để<br>phân cách giữa số Nguyên (hàng đơn vị) với số thập phân đầu tiên.|
|14|DON_GIA_BV|Số|15|Ghi đơn giá dịch vụ kỹ thuật, tiền giường bệnh, tiền công khám bệnh<br>(theo giá do cấp có thẩm quyền quy định hoặc giá do cơ sở KBCB<br>xây dựng) hoặc đơn giá của VTYT (Giá theo hóa đơn mua vào của<br>cơ sở KBCB); làm tròn đến 3 (ba) chữ số thập phân. Sử dụng dấu<br>chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.<br>**Lưu ý:**Trường hợp VTYT tái sử dụng được tính theo công thức:<br>DON_GIA_BV = DON_GIA_BH|
|15|DON_GIA_BH|Số|15|Ghi đơn giá dịch vụ kỹ thuật, VTYT, tiền giường bệnh, tiền công<br>khám bệnh do quỹ BHYT thanh toán; làm tròn đến 3 (ba) chữ số thập<br>phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên (hàng đơn<br>vị) với số thập phân đầu tiên.<br>**Lưu ý:**<br>**- **Trường hợp VTYT tái sử dụng: DON_GIA_BH bao gồm chi phí để<br>tái sử dụng theo quy định của Bộ trưởng Bộ Y tế, thống nhất với cơ<br>quan BHXH để làm căn cứ thanh toán.<br>_Ví dụ:_ đơn giá mua VTYT là 100.000 đồng, định mức sử dụng 2 lần,<br>chi phí tái sử dụng là 10.000 đồng, đơn giá ghi 55.000 đồng.<br>- Đối với VTYT do cơ sở KBCB tự sản xuất: đơn giá của VTYT do<br>người đứng đầu cơ sở KBCB xây dựng, phê duyệt và thống nhất với<br>cơ quan BHXH để làm căn cứ thanh toán theo quy định tại khoản 4<br>Điều 3 Thông tư số 04/2017/TT-BYT.|
|||||Ghi thông tin thầu của VTYT theo thứ tự, gồm: Số quyết định phê duyệt<br>kết quả lựa chọn nhà thầu; số gói thầu; mã nhóm thầu (theo quy định tại<br>Phụ lục số 7 ban hành kèm theo Quyết định số 5937/QĐ-BYT ngày 30<br>tháng 12 năm 2021 của Bộ trưởng Bộ Y tế); năm ban hành quyết định phê<br>duyệt kết quả lựa chọn nhà thầu. Các thông tin này cách nhau bằng dấu<br>chấm phẩy “;”.<br>**Lưu ý:**<br>- Trường hợp VTYT áp thầu thì Trường thông tin TT_THAU của VTYT<br>ghi như sau: Sốquyết định Mã đơn vịban hành quyết định;G;N;XXXX|

16 TT_THAU Chuỗi 25

ghi như sau: Số quyết định.Mã đơn vị ban hành quyết định;G i ;N i ;XXXX.
Mã đơn vị ban hành quyết định trúng thầu của VTYT thực hiện như sau:
TTMSTT quốc gia là mã "00"; trường hợp các tỉnh, thành phố đấu thầu tập
trung thì sử dụng mã tỉnh, thành phố; trường hợp cơ sở KBCB đấu thầu thì
sử dụng mã cơ sở KBCB; G i là số gói thầu; N i là số nhóm thầu; XXXX là
năm ban hành quyết định).
_Ví dụ 1_ : VTYT áp thầu theo Quyết định trúng thầu của TTMSTT quốc gia
có thông tin thầu là 20/QĐ-TTMS; số gói thầu "1"; mã nhóm thầu "1"; năm
ban hành quyết định là năm 2021 thì ghi thông tin thầu của VTYT là:

20.00;G1;N1;2021
_Ví dụ 2_ : VTYT áp thầu theo Quyết định trúng thầu của Sở Y tế thành phố
Hà Nội có thông tin thầu 1516/QĐ-SYT; số gói thầu "1"; mã nhóm thầu
"1"; năm ban hành quyết định là năm 2021 thì ghi thông tin thầu của VTYT

là: 1516.01;G1;N1;2021
_Ví dụ 3_ : VTYT áp thầu theo Quyết định trúng thầu của Bệnh viện Hữu nghị
Việt Đức có thông tin thầu là Quyết định số 132/QĐ-VĐ; số gói thầu "1";
mã nhóm thầu "2"; năm ban hành quyết định là năm 2021, thì ghi thông tin
thầu của VTYT là: 132.01901;G1;N2;2021

- Trường hợp VTYT tự sản xuất: Số quyết định trúng thầu thì ghi theo số
văn bản gửi cơ quan BHXH, năm ban hành quyết định thì ghi năm ban

hành văn bản;
Ví dụ (4): Chế phẩm Cao thấp khớp do BV YHCT Trung ương tự bào chế
năm 2023, BV YHCT TW có văn bản số 456/BVYHCTTW-BH gửi
BHXH TP Hà Nội thì mã hoá thông tin thầu của chế phẩm như sau:

456/BVYHCTTW-BH;2023

- Trường hợp VTYT được phê duyệt kế hoạch lựa chọn nhà thầu trước
ngày Thông tư số 14/2020/TT-BYT có hiệu lực thì trường TT_THAU ghi
như sau: Số quyết định.Mã đơn vị ban hành quyết định;Gi;XXXX

|17|TYLE_TT_DV n|Số|5|Ghi tỷ lệ thanh toán VTYT theo dịch vụ kỹ thuật đối với một số dịch vụ kỹ<br>thuật đặc biệt. Tỷ lệ này là số nguyên dương. Cụ thể:<br>- Đối với ngày giường bệnh điều trị nội trú, trường hợp người bệnh chuyển<br>từ 02 khoa trở lên trong cùng một ngày:<br>+ Khoa có giá tiền giường cao nhất và thấp nhất: mã tiền giường và đơn giá<br>không thay đổi; số lượng ghi 0,5; trường thông tin "TYLE_TT_DV" ghi<br>+ Các khoa khác (nếu có), mã tiền giường và đơn giá không thay đổi: số<br>lượng ghi "0";<br>- Trường hợp người bệnh chuyển từ 02 khoa trở lên trong cùng một ngày<br>đồng thời có nằm ghép:<br>+ Nếu nằm ghép 02 người, mã tiền giường và đơn giá không thay đổi: số<br>lượng ghi 0,5; trường thông tin TYLE_TT_DV ghi 50;<br>+ Nếu nằm ghép từ 03 người trở lên: mã tiền giường và đơn giá không thay<br>đổi; số lượng ghi 0,33; trường thông tin "TYLE_TT_DV" ghi 33;<br>+ Nếu nằm 01 người/giường bệnh thì trường thông tin "TYLE_TT_DV"<br>- Đối với tiền khám bệnh, trường thông tin "TYLE_TT_DV" ghi 100 tương<br>ứng với lần khám bệnh thứ nhất, ghi 30 tương ứng với lần khám thứ hai<br>đến lần khám thứ tư, ghi 10 tương ứng với lần khám thứ năm, ghi 0 từ lần<br>khám thứ sáu trở đi.<br>- Đối với trường hợp thực hiện nhiều can thiệp trong cùng một lần phẫu<br>thuật, từ dịch vụ kỹ thuật thứ 2 trở đi, trường thông tin "TYLE_TT_DV"<br>ghi 50 đối với trường hợp phẫu thuật do một kíp phẫu thuật thực hiện; ghi<br>80 đối với trường hợp phẫu thuật do kíp phẫu thuật khác thực hiện; ghi 80|
|---|---|---|---|---|
|18|TYLE_TT_BH|Số|3|~~ếdịh~~<br>~~hát i h là thủth ật~~<br>Ghi tỷ lệ thanh toán BHYT đối với dịch vụ kỹ thuật hoặc VTYT có<br>quy định tỷ lệ (%). Tỷ lệ này là số nguyên dương.<br>_Ví dụ_: Tỷ lệ thanh toán của dịch vụ kỹ thuật hoặc VTYT là 50% thì<br>trường thông tin này ghi là 50.<br>- Trường hợp dịch vụ kỹ thuật hoặc VTYT không quy định tỷ lệ<br>thanh toán thì ghi 100;<br>- Trường hợp dịch vụ kỹ thuật hoặc VTYT không thuộc phạm vi<br>thanh toán của quỹ BHYT thì ghi là 0.|
|19|THANH_TIEN_BV|Số|15|Ghi số tiền thanh toán theo giá của bệnh viện. Trường thông tin này<br>được xác định như sau: THANH_TIEN_BV = SO_LUONG *<br>DON_GIA_BV, làm tròn số đến 2 chữ số thập phân. Sử dụng dấu<br>chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.|

|20|THANH_TIEN_BH|Số|5|Ghi mức giá do quỹ BHYT thanh toán theo quy định của cơ quan có<br>thẩm quyền. Trường thông tin này được xác định như sau:<br>THANH_TIEN_BH = SO_LUONG * DON_GIA_BH *<br>TYLE_TT_BH/100, làm tròn số đến 2 chữ số thập phân. Sử dụng<br>dấu chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.<br>Lưu ý: Đối với trường hợp có tỷ lệ thanh toán đặc biệt (người bệnh<br>nằm ghép, hoặc khám bệnh lần 2, lần 3,...) được tính theo công thức:<br>THANH_TIEN_BH = SO_LUONG * DON_GlA_BH *<br>TYLE_TT_DV/100 * TYLE_TT_BH/100, làm tròn số đến 2 chữ số<br>thập phân. Sử dụng dấu chấm “.” để phân cách giữa số nguyên (hàng<br>đơn vị) với số thập phân đầu tiên.|
|---|---|---|---|---|
|21|T_TRANTT|Số|15|Ghi mức thanh toán đối đa (45 tháng lương cơ sở) của gói VTYT<br>trong một lần thực hiện DVKT theo quy định tại Thông tư<br>04/2017/TT-BYT của Bộ Y tế. Trường hợp không có trần thanh toán<br>thì để trống trường thông tin này.|
|22|MUC_HUONG|Số|3|Ghi mức hưởng tương ứng với từng loại chi phí, trong đó:<br>- Trường hợp người bệnh KBCB BHYT đúng tuyến ghi mức hưởng<br>là 80 hoặc 95 hoặc 100;<br>- Trường hợp trái tuyến ghi mức hưởng sau khi đã nhân với tỷ lệ<br>hưởng trái tuyến tương ứng với tuyến chuyên môn kỹ thuật của cơ sở<br>_Ví dụ_: Người bệnh có mức hưởng BHYT 80%, điều trị trái tuyến nội<br>trú tại cơ sở KBCB tuyến trung ương (có tỷ lệ hưởng trái tuyến là<br>40%): ghi mức hưởng là 32;<br>- Trường hợp người bệnh KBCB BHYT đúng tuyến, có tổng chi phí<br>trong phạm vi được hưởng dưới 15% mức lương cơ sở hoặc KBCB<br>tại Trạm y tế tuyến xã hoặc người bệnh đủ điều kiện được hưởng<br>miễn cùng chi trả trong năm: ghi mức hưởng 100;<br>- Trường hợp người bệnh KBCB BHYT trái tuyến, có tổng chi phí<br>dưới 15% mức lương cơ sở ghi mức trái tuyến tương ứng với tuyến<br>chuyên môn kỹ thuật của cơ sở KBCB.|
|23|T_NGUONKHAC_|Số|15|Ghi số tiền dịch vụ kỹ thuật hoặc VTYT được ngân sách nhà nước<br>(Trung ương và/hoặc địa phương) hỗ trợ, làm tròn số đến 2 chữ số<br>thập phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên (hàng<br>đơn vị) với số thập phân đầu tiên.|
|24|T_NGUONKHAC_|Số|15|Ghi số tiền dịch vụ kỹ thuật hoặc VTYT được các tổ chức, đơn vị có<br>trụ sở ngoài lãnh thổ Việt Nam hoặc các cá nhân đang sinh sống, học<br>tập, lao động ngoài lãnh thổ Việt Nam hỗ trợ, làm tròn số đến 2 chữ<br>số thập phân. Sử dụng dấu chấm “.” để phân cách giữa số Nguyên<br>(hàng đơn vị) với số thập phân đầu tiên.|
|25|T_NGUONKHAC_|Số|15|Ghi số tiền dịch vụ kỹ thuật hoặc VTYT được các tổ chức, cơ quan,<br>đơn vị có trụ sở trong lãnh thổ Việt Nam hoặc các cá nhân đang sinh<br>sống, học tập, lao động trong lãnh thổ Việt Nam hỗ trợ, làm tròn số<br>đến 2 chữ số thập phân. Sử dụng dấu chấm “.” để phân cách giữa số<br>Nguyên (hàng đơn vị) với số thập phân đầu tiên.|

|26|T_NGUONKHAC_|Số|15|Ghi số tiền dịch vụ kỹ thuật hoặc VTYT được các nguồn khác còn lại<br>(Không thuộc một trong ba nguồn của các trường thông tin trong<br>bảng này: "T_NGUONKHAC_NSNN",<br>"T_NGUONKHAC_VTNN", "T_NGUONKHAC_VTTN") hỗ trợ,<br>làm tròn số đến 2 chữ số thập phân. Sử dụng dấu chấm “.” để phân<br>cách giữa số Nguyên (hàng đơn vị) với số thập phân đầu tiên.|
|---|---|---|---|---|
|27|T_NGUONKHAC|Số|15|Là số tiền do nguồn khác chi trả; được tính theo công thức như sau:<br>T_NGUONKHAC = T_NGUONKHAC_NSNN +<br>T_NGUONKHAC_VTNN + T_NGUONKHAC_VTTN +<br>- Trường hợp chi phí KBCB được nguồn tài chính khác hỗ trợ thông<br>qua cơ sở KBCB (Với điều kiện: 0 < T_NGUONKHAC <<br>THANH_TIEN_BV), khi đó:<br>a) Trường hợp nguồn tài chính này chỉ hỗ trợ cho riêng cá nhân<br>người bệnh thì số tiền hỗ trợ này sẽ được khấu trừ vào các chi phí<br>theo thứ tự ưu tiên, lần lượt như sau: T_BNTT, T_BNCCT,<br>b) Trường hợp nguồn tài chính này hỗ trợ chung cho cơ sở KBCB để<br>hỗ trợ chi phí KBCB cho người bệnh thì nguồn tài chính này được<br>khấu trừ vào tổng chi phí KBCB, phần chi phí còn lại được phân bổ<br>như bình thường (theo thứ tự: Quỹ BHYT chi trả, người bệnh cùng<br>chi trả, người bệnh tự trả).<br>c) Trường hợp đặc biệt, không thuộc hướng dẫn tại điểm a, điểm b<br>của trường thông tin này thì Bộ Y tế có văn bản hướng dẫn cách tính<br>cụ thể.|
|28|T_BNTT|Số|15|Ghi số tiền người bệnh tự trả ngoài phạm vi chi trả của Quỹ BHYT,<br>làm tròn số đến 2 chữ số thập phân. Sử dụng dấu chấm “.” để phân<br>cách giữa số Nguyên (hàng đơn vị) với số thập phân đầu tiên.<br>Cách tính:<br>- Bước 1: T_BNTT (tạm tính) = THANH_TIEN_BV -<br>- Bước 2: So sánh các giá trị<br>+ Nếu T_NGUONKHAC = 0 thì T_BNTT giữ nguyên;<br>+ T_NGUONKHAC > 0 thì có 02 trường hợp:<br>(i) T_NGUONKHAC < T_BNTT (tạm tính): T_BNTT = T_BNTT<br>(tạm tính) - T_NGUONKHAC.<br>(ii) T_NGUONKHAC => T_BNTT (tạm tính) thì T_BNTT = 0.|

|29|T_BNCCT T|Số|5|Ghi số tiền người bệnh cùng chi trả trong phạm vi quyền lợi được<br>hưởng BHYT, làm tròn số đến 2 chữ số thập phân. Sử dụng dấu<br>chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.<br>Cách tính:<br>- Bước 1:<br>+) T_BNTT (tạm tính) = THANH_TIEN_BV - THANH_TIEN_BH<br>+) T_BHTT (tạm tính) = THANH_TIEN_BH * MUC_HUONG/100<br>+) T_BNCCT (tạm tính) = THANH_TIEN_BH - T_BHTT (tạm<br>tính);<br>- Bước 2:<br>+) Nếu T_NGUONKHAC <= T_BNTT (tạm tính) thì T_BNCCT =<br>T_BNCCT (tạm tính);<br>+) Nếu T_NGUONKHAC > T_BNTT (tạm tính) thì có 02 trường<br>hợp:<br>(i) Nếu T_BNCCT (tạm tính) > T_NGUONKHAC - T_BNTT (tạm<br>tính) thì T_BNCCT = T_BNCCT (tạm tính) - (T_NGUONKHAC -<br>T_BNTT (tạm tính)) ;<br>(ii) Nếu T_BNCCT (tạm tính) <= T_NGUONKHAC - T_BNTT (tạm<br>tính) thì T_BNCCT = 0;|
|---|---|---|---|---|
|30|T_BHTT|Số|15|Ghi số tiền đề nghị cơ quan BHXH thanh toán theo phạm vi quyền<br>lợi hưởng BHYT, làm tròn số đến 2 chữ số thập phân. Sử dụng dấu<br>chấm “.” để phân cách giữa số Nguyên (hàng đơn vị) với số thập<br>phân đầu tiên.<br>Cách tính:<br>- Bước 1:<br>+) T_BHTT (tạm tính) = THANH_TIEN_BH * MUC_HUONG/100<br>+) T_BNCCT (tạm tính) = THANH_TIEN_BH - T_BHTT (tạm tính)<br>+) T_BNTT (tạm tính) = THANH_TIEN_BV - THANH_TIEN_BH<br>- Bước 2:<br>+) Nếu T_NGUONKHAC < T_BNCCT (tạm tính) + T_BNTT (tạm<br>tính) thì T_BHTT = T_BHTT (tạm tính)<br>+) Nếu T_NGUONKHAC > T_BNCCT (tạm tính) + T_BNTT (tạm<br>tính) thì T_BHTT = T_BHTT (tạm tính) - (T_NGUONKHAC -<br>T_BNCCT (tạm tính) - T_BNTT (tạm tính)).|
|31|MA_KHOA|Chuỗi|20|Ghi mã khoa nơi người bệnh được cung cấp DVKT, VTYT, giường<br>bệnh. Mã khoa ghi theo Phụ lục số 5 ban hành kèm theo Quyết định<br>số 5937/QĐ-BYT ngày 30 tháng 12 năm 2021 của Bộ trưởng Bộ Y<br>tế.|

|32|MA_GIUONG|Chuỗi|5|Ghi mã giường tại khoa điều trị. Mã giường gồm 04 ký tự và được<br>mã hóa theo nguyên tắc:<br>- Đối với giường kế hoạch: H + số giường tại khoa điều trị (đánh số<br>từ 001 đến hết);<br>- Đối với giường kê thêm: T + số giường tại khoa điều trị (đánh số từ<br>001 đến hết);<br>- Đối với giường tự chọn: C + số giường tại khoa điều trị (đánh số từ<br>001 đến hết);<br>- Đối với các loại giường khác (băng ca, giường gấp...): K + số<br>giường tại từng khoa điều trị (đánh số từ 001 đến hết);<br>Lưu ý: Nếu người bệnh chuyển nhiều giường thì giữa các mã giường<br>cách nhau bằng dấu chấm phẩy “;”<br>Ví dụ: Bệnh viện có 2 khoa, có mã là K02 và K03 và có 10 giường kế<br>hoạch được đặt 3 giường tại khoa K02 và 7 giường tại khoa K03 thì<br>mã giường được mã như sau: Tại khoa K02 có mã giường từ H001<br>đến H003; tại khoa K03 có mã giường từ H001 đến H007|
|---|---|---|---|---|
|33|MA_BAC_SI|Chuỗi|255|Ghi mã nhân viên y tế khám, chỉ định (là mã định danh y tế của nhân<br>viên y tế).<br>**Lưu ý:**<br>- Trường hợp có nhiều nhân viên y tế cùng khám và chỉ định thì ghi<br>mã định danh y tế của các nhân viên y tế, cách nhau bằng dấu chấm<br>phẩy “;”;<br>- Trường hợp nhân viên y tế (Bác sỹ) được huy động, điều động cho<br>phòng, chống dịch hoặc thiên tai, thảm họa tại cơ sở KBCB khác, mã<br>hoá theo nguyên tắc: MA_BAC_SI.C.XXXXX|
|34|NGUOI_THUC_HI|Chuỗi|255|Ghi mã nhân viên y tế thực hiện dịch vụ kỹ thuật (là mã định danh y<br>tế của nhân viên y tế). Trường hợp có nhiều nhân viên y tế cùng thực<br>hiện thì ghi mã định danh y tế của các nhân viên y tế, cách nhau bằng<br>dấu chấm phẩy “;”.<br>- Trường hợp nhân viên y tế được huy động, điều động cho phòng,<br>chống dịch hoặc thiên tai, thảm họa tại cơ sở KBCB khác, mã hoá<br>theo nguyên tắc: MA_BAC_SI.C.XXXXX|
||MA_BENH|Chuỗi|100|Ghi mã ICD10 của bệnh cần chỉ định DVKT bổ sung so với mã bệnh<br>chính (nếu có). Trường hợp không có thông tin ở trường này thì được<br>hiểu là DVKT được chỉ định để điều trị bệnh chính|
||MA_BENH_YHCT|Chuỗi|255|Trường hợp người bệnh được KBCB bằng YHCT, ghi mã bệnh<br>YHCT của bệnh cần chỉ định DVKT bổ sung so với mã bệnh chính,<br>tương ứng với mã ICD10 (nếu có). Trường hợp không có thông tin ở<br>trường này thì được hiểu là DVKT được chỉ định để điều trị bệnh<br>chính (MA_BENH_CHINH).|

|35|NGAY_YL|Chuỗi|12|Ghi thời điểm ra y lệnh, gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHMM, trong đó: 04 ký tự năm (yyyy) + 02 ký tự tháng<br>(mm) + 02 ký tự ngày (dd) + 02 ký tự giờ, tính theo 24 giờ (HH) + 02<br>ký tự phút (MM).<br>Ví dụ: Dịch vụ kỹ thuật A được chỉ định lúc 10 giờ 30 phút ngày<br>31/03/2017, khi đó được hiển thị là: 201703311030|
|---|---|---|---|---|
|36|NGAY_TH_YL|Chuỗi|12|Ghi thời điểm thực hiện y lệnh, gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHMM, trong đó: 04 ký tự năm (yyyy) + 02 ký tự tháng<br>(mm) + 02 ký tự ngày (dd) + 02 ký tự giờ, tính theo 24 giờ (HH) + 02<br>ký tự phút (MM).<br>_Ví dụ:_ Dịch vụ kỹ thuật A được thực hiện lúc 15 giờ 20 phút ngày<br>31/03/2017, khi đó được hiển thị là: 201703311520|
|37|NGAY_KQ|Chuỗi|12|Ghi thời điểm có kết quả, gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHMM, trong đó: 04 ký tự năm (yyyy) + 02 ký tự tháng<br>(mm) + 02 ký tự ngày (dd) + 02 ký tự giờ, tính theo 24 giờ (HH) + 02<br>ký tự phút (MM).<br>_Ví dụ:_ Dịch vụ kỹ thuật A có kết quả lúc 16 giờ 45 phút ngày<br>31/03/2017, khi đó được hiển thị là: 201703311645.<br>**Lưu ý**:<br>- Đối với phẫu thuật, thủ thuật, can thiệp: ghi thời điểm kết thúc phẫu<br>thuật, thủ thuật, can thiệp;<br>- Đối với ngày giường bệnh: ghi thời điểm kết thúc sử dụng từng loại<br>giường bệnh;<br>_Ví dụ_: ngày 31/03/2017 15:20 được hiển thị là: 201703311520<br>- Trường hợp người bệnh ra viện nhưng chưa có kết quả xét nghiệm<br>thì để trống trường thông tin này khi gửi dữ liệu XML thông tuyến và<br>bổ sung đầy đủ thông tin thời điểm có kết quả xét nghiệm trước khi<br>gửi đề nghị giám định theo qui định tại khoản 1 Điều 7 Thông tư số<br>- Trường hợp sau 07 ngày mới có kết quả thì cơ sở KBCB nhập<br>thông tin ngày kết quả cận lâm sàng trực tiếp trên Cổng tiếp nhận dữ<br>liệu Hệ thống thông tin giám định BHYT của BHXH Việt Nam,<br>nhưng không quá 30 ngày kể từ ngày kết thúc đợt KBCB.|
|38|MA_PTTT|Số|1|Ghi mã phương thức thanh toán, trong đó:<br>- Mã "1": thanh toán theo phí dịch vụ;<br>- Mã "2": thanh toán theo định suất;<br>- Mã "3": thanh toán theo trường hợp bệnh (DRG).|

~~i~~ ~~à~~

|39|VET_THUONG_TP|Số|5|Ghi mã của vết thương tái phát. Chỉ ghi số "1" nếu sử dụng DVKT,<br>VTYT có quy định tỷ lệ thanh toán BHYT để điều trị vết thương tái<br>phát, bệnh tật tái phát cho các đối tượng là thương binh, bao gồm cả<br>thương binh loại B được công nhận trước ngày 31 tháng 12 năm<br>1993, người hưởng chính sách như thương binh, bệnh binh khi điều<br>trị vết thương, bệnh tật tái phát (Quy định tại gạch đầu dòng thứ 7,<br>điểm d khoản 1 Điều 183 Nghị định số 131/2021/NĐ-CP ngày<br>30/12/2021 của Chính phủ quy định chi tiết và biện pháp thi hành<br>Pháp lệnh Ưu đãi người có công với cách mạng).|
|---|---|---|---|---|
|40|PP_VO_CAM|Số|1|Ghi mã phương pháp vô cảm được sử dụng trong phẫu thuật, thủ<br>thuật, trong đó:<br>- Mã "1": Gây mê;<br>- Mã "2": Gây tê;<br>- Mã "3": Châm tê;<br>- Mã "4": các phương pháp vô cảm khác.<br>Trường thông tin này chỉ bắt buộc khi thực hiện phẫu thuật, thủ thuật<br>có sử dụng phương pháp vô cảm.|
|41|VI_TRI_TH_DVKT|Số|3|Ghi mã vị trí thực hiện phẫu thuật hoặc thủ thuật theo danh mục mã<br>vị trí cơ thể.<br>Cơ sở KBCB áp dụng thực hiện trường thông tin này khi Bộ trưởng<br>Bộ Y tế ban hành danh mục mã vị trí cơ thể.|
|42|MA_MAY|Chuỗi|1024|Ghi mã các máy thực hiện dịch vụ cận lâm sàng, phẫu thuật, thủ thuật (máy<br>xét nghiệm, máy XQuang, máy siêu âm…), tạm thời được ghi theo nguyên<br>tắc: XX.n.YYYYY.Z, trong đó:<br>- XX hoặc XXX: Mã nhóm máy thực hiện, trong đó: Huyết học ghi mã<br>"HH"; vi sinh ghi mã "VS"; sinh hóa ghi mã "SH"; siêu âm ghi mã "SA";<br>Xquang ghi mã "XQ"; chụp cắt lớp vi tính ghi mã "CL"; chụp MRI ghi mã<br>"MRI"; máy thực hiện phẫu thuật ghi mã "PT"; máy thực hiện thủ thuật ghi<br>mã "TT"; máy xét nghiệm đa chức năng thì ghi mã "DC"; máy xạ trị ghi mã<br>"XT"; máy chụp SPECT ghi mã "SP"; máy chụp PET/CT ghi mã "PET";<br>máy xạ hình xương ghi mã "XH"; máy nội soi ghi mã "NS"; máy chụp<br>mạch xoá nền DSA ghi mã "DSA"; máy điện tim ghi mã "ĐT",...._(Đối với_<br>_các máy chưa quy định mã nhóm máy (XX hoặc XXX) thì ghi các chữ cái_<br>_đầu tiên theo phiên âm tiếng Việt của máy, tối đa không quá 03 ký tự đầu_<br>_tiên)._<br>- n: Ký hiệu của nguồn kinh phí mua máy, trong đó:<br>+ Mã "1": ngân sách nhà nước;<br>+ Mã "2": xã hội hóa;<br>+ Mã "3": các nguồn khác;<br>- YYYYY: Mã cơ sở KBCB;<br>- Z: Số serial của máy (Ghi cả phần chữ và phần số). Trường hợp không có<br>số serial của máy thì sử dụng mã quản lý của máy do cơ sở KBCB lập. Đối<br>với hệ thống máy gồm nhiều máy thì ghi tất cả các serial của các máy, cách<br>nhau bằng dấu chấm phẩy ";"<br>- Trường hợp chuyển mẫu bệnh phẩm thì không bắt buộc ghi trường thông|

|43|MA_HIEU_SP|Chuỗi|255|Ghi mã hiệu sản phẩm của VTYT, là mã hiệu do Công ty sản xuất tự<br>đặt cho sản phẩm của mình. Mã hiệu có thể là số Model sản phẩm<br>hoặc số Serial hoặc số EMEI được in trên sản phẩm hoặc bao bì sản<br>phẩm.<br>Mã hiệu sản phẩm chỉ bắt buộc đối với VTYT có thông tin mã hiệu<br>sản phẩm.|
|---|---|---|---|---|
|44|TAI_SU_DUNG|Số|1|Là mã đánh dấu đối với VTYT tái sử dụng, trong đó:<br>- Ghi mã “1” nếu là VTYT tái sử dụng;<br>- Nếu VTYT không tái sử dụng thì để trống trường thông tin này.|
|45|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần|

**Ghi chú:**

 - Trường hợp dịch vụ kỹ thuật có sử dụng vật tư y tế kèm theo: ghi mã dịch vụ kỹ thuật tại chỉ tiêu thứ 3
(MA_DICH_VU), ghi mã vật tư y tế tại chỉ tiêu thứ 5 (MA_VAT_TU)

 - Chỉ tiêu số thứ tự 35 (NGAY_YL):
+ Riêng ngày giường bệnh, yêu cầu tất cả các cơ sở khám bệnh, chữa bệnh phải thực hiện ngay việc ghi ngày y
lệnh theo ngày bắt đầu sử dụng hoặc ngày thay đổi loại giường, giá giường, nằm ghép, chuyển giữa các khoa.
+ Đối với vật tư y tế: Ghi ngày thực hiện phẫu thuật, thủ thuật, can thiệp có sử dụng vật tư y tế để xác định mức
trần thanh toán vật tư y tế cho một lần sử dụng dịch vụ kỹ thuật (vật tư y tế chưa có trong cơ cấu giá dịch vụ kỹ
thuật).

 - Ký hiệu (*): phép tính nhân;

 - Ký hiệu (>): lớn hơn;

 - Ký hiệu (<): nhỏ hơn.

##### **Bảng 4. Chỉ tiêu chi tiết dịch vụ cận lâm sàng** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu<br>tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn<br>lại ban hành kèm theo Quyết định này trong một lần khám bệnh,<br>chữa bệnh (PRIMARY KEY)).|
|2|STT|Số|10|Số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|MA_DICH_VU|Chuỗi|15|Ghi mã dịch vụ kỹ thuật cận lâm sàng, thực hiện theo Phụ lục số 1<br>ban hành kèm theo Quyết định số 7603/QĐ-BYT ngày 25 tháng<br>12 năm 2018 của Bộ trưởng Bộ Y tế.|
|4|MA_CHI_SO|Chuỗi|50|Ghi mã chỉ số xét nghiệm, chẩn đoán hình ảnh, thăm dò chức năng<br>theo Phụ lục số 11 ban hành kèm theo Quyết định số 7603/QĐ-<br>BYT ngày 25 tháng 12 năm 2018 của Bộ trưởng Bộ Y tế.|
|5|TEN_CHI_SO|Chuỗi|255|Ghi tên chỉ số xét nghiệm, chẩn đoán hình ảnh, thăm dò chức<br>năng, theo Phụ lục số 11 ban hành kèm theo Quyết định số<br>7603/QĐ-BYT ngày 25 tháng 12 năm 2018 của Bộ trưởng Bộ Y<br>tế.|
|6|GIA_TRI|Chuỗi|50|Ghi giá trị chỉ số (kết quả xét nghiệm, chẩn đoán hình ảnh, thăm<br>dò chức năng).<br>Trường hợp người bệnh ra viện nhưng chưa có kết quả xét nghiệm<br>thì để trống trường thông tin này khi gửi dữ liệu XML thông tuyến<br>và bổ sung đầy đủ thông tin kết quả xét nghiệm trước khi gửi đề<br>nghị giám định theo khoản 1 Điều 7 Thông tư 48/2017/TT-BYT.<br>Trường hợp sau 7 ngày mới có kết quả thì cơ sở KBCB nhập<br>thông tin kết quả xét nghiệm trực tiếp trên Cổng tiếp nhận dữ liệu<br>Hệ thống thông tin giám định BHYT của BHXH Việt Nam nhưng<br>không quá 30 ngày kể từ ngày kết thúc đợt KBCB.|
|7|DON_VI_DO|Chuỗi|50|Ghi đơn vị đo của chỉ số xét nghiệm, chẩn đoán hình ảnh, thăm dò<br>chức năng theo Phụ lục 11 ban hành kèm theo Quyết định số<br>7603/QĐ-BYT ngày 25 tháng 12 năm 2018 của Bộ trưởng Bộ Y<br>tế. Đối với các chỉ số không có đơn vị đo thì để trống trường<br>thông tin này.|
|8|MO_TA|Chuỗi||Ghi các mô tả do người đọc kết quả ghi.<br>Trường hợp không có kết quả thì để trống trường thông tin này.|
|9|KET_LUAN|Chuỗi||Ghi các kết luận của người đọc kết quả.<br>Trường hợp không có kết quả thì để trống trường thông tin này.|

|10|NGAY_KQ|Chuỗi|5|Ghi thời điểm có kết quả cận lâm sàng; gồm 12 ký tự, theo cấu<br>trúc: yyyymmddHHMM, trong đó: 04 ký tự năm (yyyy) + 02 ký<br>tự tháng (mm) + 02 ký tự ngày (dd) + 02 ký tự giờ, tính theo 24<br>giờ (HH) + 02 ký tự phút (MM).<br>Ví dụ: ngày 31/03/2017 15:20 được hiển thị là: 201703311520<br>Trường hợp người bệnh ra viện nhưng chưa có kết quả xét nghiệm<br>thì để trống trường thông tin này khi gửi dữ liệu XML thông tuyến<br>và bổ sung đầy đủ thông tin thời điểm có kết quả xét nghiệm trước<br>khi gửi đề nghị giám định theo khoản 1 Điều 7 Thông tư<br>48/2017/TT-BYT. Trường hợp sau 7 ngày mới có kết quả thì cơ<br>sở KBCB nhập thông tin ngày kết quả cận lâm sàng trực tiếp trên<br>Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT của<br>BHXH Việt Nam nhưng không quá 30 ngày kể từ ngày kết thúc<br>đợt KBCB.|
|---|---|---|---|---|
|11|MA_BS_DOC_KQ|Chuỗi|255|Ghi mã của người có thẩm quyền đọc hoặc duyệt kết quả đọc, ghi<br>mã của người này theo mã định danh y tế.|
|12|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần thiết.|

**Ghi chú:** Cơ sở KBCB chỉ gửi dữ liệu Bảng này trong trường hợp người bệnh có thực hiện các dịch vụ cận lâm
sàng.

##### **Bảng 5. Chỉ tiêu chi tiết diễn biến lâm sàng** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế) 130 18 [01]

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu<br>tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn<br>lại ban hành kèm theo Quyết định này trong một lần khám<br>bệnh, chữa bệnh (PRIMARY KEY)).|
|2|STT|Số|10|Số thứ tự tăng từ 1 đến hết trong một lần gửi dữ liệu.|
|3|DIEN_BIEN_LS|Chuỗi||Ghi diễn biến lâm sàng của người bệnh trong lần khám và/hoặc<br>ghi nội dung chăm sóc của nhân viên y tế.|
|4|GIAI_DOAN_BENH|Chuỗi||Ghi giai đoạn bệnh trong trường hợp người bệnh đã được cơ sở<br>KBCB xác định giai đoạn bệnh.|
|5|HOI_CHAN|Chuỗi||Ghi kết quả hội chẩn (nếu có).|
|6|PHAU_THUAT|Chuỗi||Ghi mô tả cách thức phẫu thuật, thủ thuật (nếu có).|
|7|THOI_DIEM_DBLS|Chuỗi|12|Ghi thời điểm diễn biến lâm sàng, gồm 12 ký tự, theo cấu trúc:<br>yyyymmddHHMM, trong đó: 04 ký tự năm (yyyy) + 02 ký tự<br>tháng (mm) + 02 ký tự ngày (dd) + 02 ký tự giờ, tính theo 24<br>giờ (HH) + 02 ký tự phút (MM).<br>_Ví dụ_: ngày 31/03/2015 15:20 được hiển thị là: 201503311520|
|8|NGUOI_THUC_HIEN|Chuỗi|255|Ghi mã định danh y tế của nhân viên y tế thực hiện ghi chép<br>diễn biến lâm sàng.<br>**Lưu ý:** Trường hợp có nhiều người thực hiện ghi chép diễn<br>biến lâm sàng thì ghi người thực hiện chính đầu tiên, giữa các<br>người thực hiện ghi chép diễn biến lâm sàng cách nhau bằng<br>dấu chấm phẩy “;”.|
|9|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần thiết.|

**Ghi chú:** Cơ sở KCB chỉ gửi dữ liệu Bảng này trong trường hợp người bệnh điều trị ngoại trú
(MA_LOAI_KCB = 02, 05, 08) hoặc điều trị nội trú hoặc điều trị nội trú ban ngày hoặc điều trị lưu tại TYT
tuyến xã, PKĐKKV hoặc điều trị nội trú dưới 4 giờ.

|Chỉ tiêu|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu<br>tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn<br>lại ban hành kèm theo Quyết định này trong một lần khám bệnh,<br>chữa bệnh (PRIMARY KEY)).|
|2|MA_THE_BHYT|Chuỗi||Ghi mã thẻ BHYT của người bệnh do cơ quan BHXH cấp.<br>**Lưu ý**:<br>- Khi tiếp đón người bệnh, cơ sở KBCB có trách nhiệm tra cứu<br>trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT<br>của BHXH Việt Nam để kiểm tra thông tin thẻ BHYT. Trường<br>hợp cấp cứu mà người bệnh hoặc thân nhân người bệnh không<br>xuất trình được thẻ BHYT ngay thì cơ sở KBCB tra cứu thông tin<br>thẻ BHYT trước khi người bệnh ra viện.<br>- Đối với thẻ BHYT của các đối tượng có các mã QN, HC, LS,<br>XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công an cấp:<br>Tra cứu để kiểm tra thời hạn sử dụng của thẻ BHYT trong trường<br>hợp các đối tượng này không còn phục vụ trong lực lượng Quân<br>đội, Công an, Cơ yếu.<br>- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ<br>BHYT mới có thay đổi thông tin liên quan đến mã thẻ thì ghi tiếp<br>mã thẻ mới (mỗi mã thẻ gồm có 15 ký tự), giữa các mã thẻ cách<br>nhau bằng dấu chấm phẩy “;”.<br>- Trường hợp người bệnh chưa có thẻ BHYT, cơ sở KBCB sử<br>dụng chức năng “Thông tuyến khám chữa bệnh\Tra cứu thẻ tạm<br>của trẻ em hoặc của người hiến tạng” trên Cổng tiếp nhận dữ liệu<br>của BHXH Việt Nam để tra cứu mã thẻ BHYT tạm thời.<br>- Trường hợp người bệnh không KBCB BHYT thì để trống<br>trường thông tin này.|
|3|SO_CCCD|Số|15|Ghi số căn cước công dân hoặc số chứng minh thư nhân dân hoặc<br>số hộ chiếu của người bệnh.<br>Trường hợp không có số căn cước công dân hoặc số chứng minh<br>thư nhân dân hoặc số hộ chiếu thì sử dụng mã tài khoản định<br>danh điện tử.|
|4|NGAYKD_HIV|Chuỗi|8|Ghi thời điểm khẳng định HIV của người nhiễm HIV, định dạng<br>Trường hợp điều trị phơi nhiễm thì để trống trường thông tin này.|
|5|BDDT_ARV|Chuỗi|8|Ghi thời điểm đầu tiên người bệnh nhận thuốc ARV trong<br>chương trình chăm sóc và điều trị được ghi trong hồ sơ bệnh án<br>của người bệnh; định dạng yyyymmdd.|

|6|MA_PHAC_DO_DIEU_T|Chuỗi|200|Ghi mã phác đồ điều trị HIV/AIDS khi bắt đầu điều trị ARV theo<br>danh mục mã phác đồ điều trị HIV/AIDS tại Phụ lục 10 ban hành<br>kèm theo Quyết định số 5937/QĐ-BYT ngày 30/12/2021 của Bộ<br>trưởng Bộ Y tế.|
|---|---|---|---|---|
|7|MA_BAC_PHAC_DO_B|Số|1|Ghi mã bậc của phác đồ khi bắt đầu điều trị ARV sử dụng phác<br>đồ điều trị là "Khác", trong đó:<br>- Mã "1": Phác đồ bậc 1;<br>- Mã "2": Phác đồ bậc 2;<br>- Mã "3": Phác đồ bậc 3.|
|8|MA_LYDO_DTRI|Số|1|Ghi mã lý do bệnh nhân đăng ký giai đoạn điều trị tại cơ sở<br>KBCB, trong đó:<br>- Mã "1": Bệnh nhân HIV mới đăng ký lần đầu;<br>- Mã "2": Bệnh nhân HIV chưa điều trị ARV chuyển tới;<br>- Mã "3": Bệnh nhân HIV đã điều trị ARV chuyển tới;<br>- Mã "4": Bệnh nhân HIV đã điều trị ARV nay điều trị lại;<br>- Mã "5": Bệnh nhân HIV chưa điều trị ARV đăng ký lại.|
|9|LOAI_DTRI_LAO|Số|1|Ghi mã loại điều trị lao, trong đó:<br>- Mã "0": Không điều trị lao;<br>- Mã "1": Điều trị lao tiềm ẩn;<br>- Mã "2": Điều trị lao;<br>- Mã "3": Điều trị lao kháng thuốc.|
|10|PHACDO_DTRI_LAO|Số|2|- Ghi mã phác đồ điều trị bệnh lao ở người nhiễm HIV, trong đó:<br>+ Mã "1": Phác đồ 2RHZE/4RHE;<br>+ Mã "2": Phác đồ 2RHZE/4RH;<br>+ Mã "3": Phác đồ 2RHZE/10RHE;<br>+ Mã "4": Phác đồ 2RHZE/10RH;<br>+ Mã "5": Phác đồ khác.<br>- Ghi mã phác đồ điều trị đối với bệnh nhân lao tiềm ẩn, trong đó:<br>+ Mã "6": Phác đồ INH;<br>+ Mã "7": Phác đồ 3HP;<br>+ Mã "8: Phác đồ 1HP;<br>+ Mã "9": Phác đồ 3HR;<br>+ Mã "10": Phác đồ 4R;<br>+ Mã "11": Phác đồ 6L;<br>+ Mã "12": Phác đồ khác.|
|11|NGAYBD_DTRI_LAO|Chuỗi|8|Ghi thời điểm bắt đầu điều trị bệnh lao hoặc lao tiềm ẩn tại cơ sở<br>KBCB, định dạng yyyymmdd.|
|12|NGAYKT_DTRI_LAO|Chuỗi|8|Ghi thời điểm kết thúc điều trị bệnh lao hoặc lao tiềm ẩn tại cơ sở<br>KBCB, định dạng yyyymmdd.<br>Trường hợp chưa kết thúc điều trị thì để trống trường thông tin<br>này.|

|13|MA_LYDO_XNTL_VR|Số|1|Ghi mã lý do chỉ định xét nghiệm đo tải lượng vi rút ở người<br>bệnh đang điều trị ARV, trong đó:<br>- Mã "1": Thường quy;<br>- Mã "2": Nghi ngờ thất bại điều trị;<br>- Mã "3": Khác.|
|---|---|---|---|---|
|14|NGAY_XN_TLVR|Chuỗi|8|Ghi thời điểm lấy mẫu làm xét nghiệm tải lượng virus, gồm 08 ký<br>tự theo định dạng yyyymmdd.<br>_Ví dụ_: Thời điểm lấy mẫu làm xét nghiệm tải lượng virus là ngày<br>31/03/2017, khi đó trường thông tin này được hiển thị là:|
|15|KQ_XNTL_VR|Số|1|Ghi mã kết quả xét nghiệm tải lượng vi rút HIV, là số lượng bản<br>sao vi rút HIV trên 1 ml máu, trong đó:<br>- Mã "1": Không phát hiện;<br>- Mã "2": Dưới 50 bản sao/ml;<br>- Mã "3": Từ 50 đến dưới 200 bản sao/ml;<br>- Mã "4": Từ 200 đến 1000 bản sao/ml;<br>- Mã "5: Trên 1000 bản sao/ml.|
|16|NGAY_KQ_XN_TLVR|Chuỗi|8|Ghi thời điểm có kết quả xét nghiệm tải lượng virus, gồm 08 ký<br>tự theo định dạng yyyymmdd.<br>_Ví dụ_: Ngày có kết quả xét nghiệm tải lượng virus là ngày<br>31/03/2017, khi đó trường thông tin này được được hiển thị là:|
|17|MA_LOAI_BN|Số|1|Ghi mã đối tượng đến khám, trong đó:<br>- Mã "1": Người nhiễm HIV;<br>- Mã "2": Trẻ phơi nhiễm với HIV;<br>- Mã "3": Điều trị dự phòng trước phơi nhiễm;<br>- Mã "4": Điều trị dự phòng sau phơi nhiễm;<br>- Mã "5": Khác.|
|18|MA_TINH_TRANG_DK|Chuỗi|18|Ghi mã tình trạng của đối tượng đến khám, trong đó:<br>- Mã "1": Trẻ dưới 18 tháng sinh ra từ mẹ nhiễm HIV;<br>- Mã "2": Phơi nhiễm;<br>- Mã "3": Đang điều trị lao;<br>- Mã "4": Có bầu;<br>- Mã "5": Chuyển dạ;<br>- Mã "6": Sau sinh;<br>- Mã "7": Viêm gan;<br>- Mã "8": Nghiện chích ma túy;<br>- Mã "9": Khác.<br>Trường hợp đối tượng khám có 2 tình trạng trở lên thì các Mã<br>cách nhau bởi dấu chấm phẩy “;”. Ví dụ: 1;2;3|

|19|LAN_XN_PCR|Số|1|Ghi mã lần thực hiện xét nghiệm PCR, trong đó:<br>- Mã "1": lần 1;<br>- Mã "2": lần 2;<br>- Mã "3": lần 3 (chỉ áp dụng trong lần 1 âm tính và lần 2 dương<br>tính).<br>Trường thông tin này chỉ áp dụng cho trẻ dưới 18 tháng tuổi bị<br>phơi nhiễm với HIV.|
|---|---|---|---|---|
|20|NGAY_XN_PCR|Chuỗi|8|Ghi ngày mà người bệnh thực hiện xét nghiệm PCR, gồm 08 ký<br>tự theo định dạng yyyymmdd.<br>_Ví dụ_: Ngày mà người bệnh thực hiện xét nghiệm PCR là ngày<br>31/03/2017, khi đó, trường thông tin này được hiển thị là:<br>Trường thông tin này chỉ áp dụng cho trẻ dưới 18 tháng tuổi bị<br>phơi nhiễm với HIV.|
|21|NGAY_KQ_XN_PCR|Chuỗi|8|Ghi ngày mà người bệnh có kết quả xét nghiệm PCR1, gồm 08<br>ký tự theo định dạng yyyymmdd.<br>_Ví dụ_: Ngày mà người bệnh có kết quả xét nghiệm PCR1 là ngày<br>31/03/2017, khi đó, trường thông tin này được hiển thị là:<br>Trường thông tin này chỉ áp dụng cho trẻ dưới 18 tháng tuổi bị<br>phơi nhiễm với HIV|
|22|MA_KQ_XN_PCR|Số|1|Ghi mã kết quả xét nghiệm PCR1, trong đó:<br>- Mã "0": Âm tính;<br>- Mã "1": Dương tính.<br>Trường thông tin này chỉ áp dụng cho trẻ dưới 18 tháng tuổi bị<br>phơi nhiễm với HIV.|
|23|NGAY_NHAN_TT_MAN|Chuỗi|8|Ghi thời điểm nhận thông tin mang thai, gồm 08 ký tự theo định<br>dạng yyyymmdd.<br>_Ví dụ_: Ngày nhận thông tin mang thai là ngày 31/03/2017, khi đó,<br>trường thông tin này được hiển thị là: 20170331|
|24|NGAY_BAT_DAU_DT_|Chuỗi|8|Ghi thời điểm bắt đầu điều trị Cotrimoxazol (CTX), gồm 08 ký tự<br>theo định dạng yyyymmdd.<br>_Ví dụ_: Ngày bắt đầu điều trị Cotrimoxazol (CTX) là ngày<br>31/03/2017, khi đó, trường thông tin này được hiển thị là:|
|25|MA_XU_TRI|Số|1|Ghi mã xử trí của cơ sở y tế, trong đó:<br>- Mã "1": Điều trị ARV;<br>- Mã "2": Điều trị lao;<br>- Mã "3": Dự phòng lao;<br>- Mã "4": Cotrimoxazol;<br>- Mã "5": PLTMC;<br>- Mã "6": Điều trị viêm gan;<br>- Mã "7": Khác.<br>Trường hợp có nhiều xử trí thì ghi các mã xử trí, giữa các mã xử<br>trí phân cách bằng dấu chấm phẩy “;”.|

|26|NGAY_BAT_DAU_XU_|Chuỗi|8|Ghi ngày bắt đầu xử trí của đợt điều trị ARV (áp dụng đối với<br>trường hợp có mã xử trí (MA_XU_TRI) là "1"), gồm 08 ký tự<br>theo định dạng yyyymmdd.<br>Ví dụ: Ngày bắt đầu xử trí của đợt điều trị ARV là ngày<br>31/03/2017, khi đó, trường thông tin này được hiển thị là:|
|---|---|---|---|---|
|27|NGAY_KET_THUC_XU|Chuỗi|8|Ghi ngày kết thúc xử trí của đợt điều trị ARV (áp dụng đối với<br>trường hợp có mã xử trí (MA_XU_TRI) là "1"), gồm 08 ký tự<br>theo định dạng yyyymmdd.<br>_Ví dụ_: Ngày kết thúc xử trí của đợt điều trị ARV là ngày<br>31/03/2017, khi đó, trường thông tin này được hiển thị là:|
|28|MA_PHAC_DO_DIEU_T|Chuỗi|200|Ghi mã phác đồ điều trị HIV/AIDS của đợt điều trị (Tham chiếu<br>danh mục mã phác đồ điều trị HIV/AIDS tại Phụ lục 10 ban hành<br>kèm theo Quyết định số 5937/QĐ-BYT ngày 30/12/2021 của Bộ<br>trưởng Bộ Y tế).|
|29|MA_BAC_PHAC_DO|Số|1|Ghi mã bậc phác đồ của đợt điều trị khi phác đồ điều trị là<br>"Khác", trong đó:<br>- Mã "1": Phác đồ bậc 1;<br>- Mã "2": Phác đồ bậc 2;<br>- Mã "3": Phác đồ bậc 3.|
|30|SO_NGAY_CAP_THUO|Số|3|Ghi số ngày thuốc ARV được cấp (nhỏ hơn hoặc bằng với ngày<br>trong trường thông tin NGAY_KET_THUC_XU_TRI trừ đi (-)<br>ngày trong trường thông tin NGAY_BAT_DAU_XU_TRI)|
|31|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần|

**Ghi chú:** Các trường dữ liệu này gắn với HSBA điều trị HIV/AIDS ban hành kèm theo TT28/2018/TT-BYT. Cơ sở
KCB gửi dữ liệu XML về Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT của BHXH Việt Nam theo
quy định của Thông tư 48/2017/TT-BYT, đồng thời gửi về Cổng quản lý điều trị và dự phòng HIV (HMED) tại địa
chỉ: https://dieutri.arv.vn theo hướng dẫn của Cục Phòng, chống HIV/AIDS.

##### **Bảng 7. Chỉ tiêu dữ liệu giấy ra viện** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng<br>chỉ tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1)<br>và các bảng còn lại ban hành kèm theo Quyết định này<br>trong một lần khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|SO_LUU_TRU|Chuỗi|200|Ghi số lưu trữ, là số hồ sơ bệnh án của người bệnh trong<br>đợt điều trị|
|3|MA_YTE|Chuỗi|200|Ghi mã y tế, lấy theo mã số người bệnh quy định tại<br>trường MA_BN tại Bảng XML 1 ban hành kèm theo<br>quyết định này.|
|4|MA_KHOA_RV|Chuỗi|200|Ghi mã khoa nơi tổng kết hồ sơ bệnh án của người bệnh.|
|5|NGAY_VAO|Chuỗi|12|Ghi thời điểm người bệnh đến KBCB, gồm 12 ký tự, theo<br>định dạng yyyymmddHHMM.<br>_Ví dụ_: người bệnh đến KBCB lúc 15 giờ 20 phút ngày<br>31/03/2017 được hiển thị là: 201703311520.|
|6|NGAY_RA|Chuỗi|12|~~Ghi thời điểm người bệnh kết thúc điều trị nội trú, kết thúc~~<br>điều trị nội trú ban ngày, kết thúc điều trị ngoại trú hoặc kết<br>thúc khám bệnh, gồm 12 ký tự theo định dạng<br>_Ví dụ_: Thời điểm người bệnh kết thúc điều trị lúc 09 giờ 20<br>phút ngày 05/04/2022, khi đó được hiển thị là: 202204050920.<br>**Lưu ý:**<br>- Trường hợp khám bệnh (MA_LOAI_KCB = 01) thì ghi thời<br>điểm kết thúc lần khám bệnh;<br>- Trường hợp điều trị ngoại trú (MA_LOAI_KCB = 02), điều<br>trị ngoại trú các bệnh mạn tính dài ngày liên tục trong năm<br>(MA_LOAI_KCB = 05), nhận thuốc theo hẹn (không khám<br>bệnh) (MA_LOAI_KCB = 07): Ghi ngày kết thúc của đợt<br>KBCB (là ngày cuối cùng sử dụng thuốc hoặc dịch vụ theo chỉ<br>định của bác sỹ), gồm 02 ký tự giờ + 02 ký tự phút và mặc<br>định là 2359 (Thời điểm cuối cùng của ngày kết thúc đợt<br>- Trường hợp điều trị ngoại trú các bệnh mạn tính dài ngày<br>liên tục trong năm (MA_LOAI_KCB = 08): Ghi thời điểm kết<br>thúc của đợt KBCB (_Ví dụ_: Trường hợp chạy thận nhân tạo thì<br>ghi ngày cuối cùng của đợt chạy thận nhân tạo);<br>- Trường hợp người bệnh được chuyển tuyến đến cơ sở KBCB<br>khác thì thời điểm người bệnh ra viện bằng thời điểm người<br>bệnh được chuyển tuyến.|

|7|MA_DINH_CHI_THAI|Số|1|Ghi mã "1" là đình chỉ thai nghén, mã "0" là không đình<br>chỉ thai nghén.<br>Trường hợp đình chỉ thai nghén bắt buộc nhập thông tin<br>vào trường thông tin tuổi thai (TUOI_THAI) và trường<br>thông tin nguyên nhân đình chỉ thai nghén|
|---|---|---|---|---|
|8|NGUYENNHAN_DINHC|Chuỗi||Ghi nguyên nhân đình chỉ thai nghén.<br>**Lưu ý:**Bắt buộc ghi trường thông tin này khi<br>MA_DINH_CHI_THAI là mã "1".|
|9|THOIGIAN_DINHCHI|Chuỗi|12|Ghi thời điểm đình chỉ thai nghén, gồm 12 ký tự, theo<br>định dạng yyyymmddHHMM<br>_Ví dụ:_ ngày 31/10/2022 15:20 được hiển thị là:<br>**Lưu ý:**Bắt buộc ghi trường thông tin này khi|
|10|TUOI_THAI|Số|2|Ghi rõ tuần tuổi thai thực tế (kể cả trường hợp đình chỉ<br>thai ngoài tử cung, thai trứng cần xác định rõ tuần tuổi<br>thai), trong đó tuổi thai luôn luôn lớn hơn hoặc bằng 1 và<br>nhỏ hơn hoặc bằng tuổi 42 tuần tuổi.<br>**Lưu ý:**Bắt buộc ghi trường thông tin này khi<br>MA_DINH_CHI_THAI = 1.|
|11|CHAN_DOAN_RV|Chuỗi|1500|Ghi đầy đủ chẩn đoán xác định bệnh chính, bệnh kèm<br>theo và/hoặc các triệu chứng hoặc hội chứng, được bác<br>sỹ ghi trong hồ sơ KBCB tại thời điểm kết thúc KBCB<br>đối với người bệnh.<br>**Lưu ý:**Đối với việc ghi chẩn đoán ra viện để phục vụ<br>việc tạo lập giấy chứng nhận nghỉ việc hưởng bảo hiểm<br>xã hội thì thực hiện theo hướng dẫn tại Thông tư số<br>18/2022/TT-BYT của Bộ trưởng Bộ Y tế, trong đó:<br>- Nội dung chẩn đoán phải mô tả cụ thể về tình trạng sức<br>khỏe hoặc ghi tên bệnh hoặc mã bệnh.<br>- Trường hợp mắc bệnh cần chữa trị dài ngày thì ghi mã<br>bệnh; trường hợp chưa có mã bệnh thì ghi đầy đủ tên<br>bệnh. Việc ghi mã bệnh và tên bệnh thực hiện theo quy<br>định tại Thông tư số 46/2016/TT-BYT ngày 30 tháng 12<br>năm 2016 của Bộ trưởng Bộ Y tế ban hành danh mục<br>bệnh dài ngày;<br>- Trường hợp điều trị dưỡng thai: Ghi rõ cụm từ “dưỡng|
|12|PP_DIEUTRI|Chuỗi|1500|Ghi phương pháp điều trị theo đúng hướng dẫn tại Thông<br>tư số 18/2022/TT-BYT của Bộ trưởng Bộ Y tế.|

|13|GHI_CHU|Chuỗi|1500|Trường thông tin này áp dụng đối với trường hợp cấp<br>giấy ra viện để giải quyết chế độ BHXH.<br>Ghi theo hướng dẫn tại mẫu Phụ lục 3 ban hành kèm theo<br>Thông tư số 18/2022/TT-BYT của Bộ trưởng Bộ Y tế.|
|---|---|---|---|---|
|14|MA_TTDV|Chuỗi|10|Ghi mã số định danh y tế (mã số BHXH) của người đứng<br>đầu cơ sở KBCB hoặc người được người đứng đầu cơ sở<br>KBCB ủy quyền được ký và đóng dấu của cơ sở KBCB<br>đó.|
|15|MA_BS|Chuỗi|200|Ghi mã số định danh y tế (mã số BHXH) của Trưởng<br>khoa hoặc Phó trưởng khoa được uỷ quyền ký tên theo<br>quy định của Thủ trưởng cơ sở KBCB.|
|16|TEN_BS|Chuỗi|255|Ghi họ và tên của Trưởng khoa hoặc Phó trưởng khoa<br>được uỷ quyền ký tên theo quy định của Thủ trưởng cơ<br>sở KBCB.|
|17|NGAY_CT|Chuỗi|8|Ghi ngày chứng từ (Giấy ra viện), theo định dạng<br>yyyymmdd, là ngày Trưởng khoa hoặc Trưởng phòng<br>hoặc Phó trưởng khoa hoặc Phó trưởng phòng cấp giấy ra<br>viện.<br>**Lưu ý**: Việc ghi ngày, tháng, năm tại phần chữ ký của<br>Trưởng khoa hoặc Trưởng phòng hoặc Phó trưởng khoa<br>hoặc Phó trưởng phòng điều trị phải trùng với ngày ra<br>viện.|
|18|MA_CHA|Chuỗi|10|Ghi mã số định danh y tế (mã số BHXH) của người cha<br>đối với trường hợp người bệnh là trẻ em dưới 16 tuổi<br>(Nếu có cha (bố)).<br>Trường hợp không có cha thì để trống trường thông tin<br>này.|
|19|MA_ME|Chuỗi|10|Ghi mã số định danh y tế (mã số BHXH) của người mẹ<br>đối với trường hợp người bệnh là trẻ em dưới 16 tuổi<br>(Nếu có mẹ).<br>Trường hợp không có mẹ thì để trống trường thông tin<br>này.|
|20|MA_THE_TAM|Chuỗi|15|Ghi mã thẻ BHYT tạm thời của trẻ em sinh ra hoặc của<br>người hiến tạng nhưng chưa được cơ quan BHXH cấp<br>thẻ BHYT. Cơ sở KBCB sử dụng chức năng “Thông<br>tuyến khám chữa bệnh\Tra cứu thẻ tạm của trẻ em hoặc<br>của người hiến tạng” trên Cổng tiếp nhận dữ liệu Hệ<br>thống thông tin giám định BHYT của BHXH Việt Nam<br>để tra cứu mã thẻ BHYT tạm thời.|
|21|HO_TEN_CHA|Chuỗi|255|Ghi họ và tên cha đối với trường hợp người bệnh là trẻ<br>em dưới 16 tuổi (Nếu có cha (bố)) theo quy định tại Phụ<br>lục 3 Thông tư số 56/2017/TT-BYT của Bộ Y tế.<br>Trường hợp không có cha (bố) thì để trống trường thông<br>tin này.|

|22|HO_TEN_ME|Chuỗi|255|Ghi họ và tên mẹ đối với trường hợp người bệnh là trẻ<br>em dưới 16 tuổi (Nếu có mẹ) theo quy định tại Phụ lục 3<br>Thông tư số 56/2017/TT-BYT của Bộ Y tế.<br>Trường hợp không có mẹ thì để trống trường thông tin<br>này.|
|---|---|---|---|---|
|23|SO_NGAY_NGHI|Số|2|Ghi rõ số ngày mà người bệnh cần nghỉ để điều trị ngoại<br>trú sau khi ra viện.|
|24|NGOAITRU_TUNGAY|Chuỗi|8|Ghi ngày bắt đầu nghỉ ngoại trú sau khi điều trị của<br>người được cấp giấy ra viện theo định dạng yyyymmdd.|
|25|NGOAITRU_DENNGAY|Chuỗi|8|Ghi ngày kết thúc nghỉ ngoại trú sau khi điều trị của<br>người được cấp giấy ra viện theo định dạng yyyymmdd.|

**Ghi chú:** Trường hợp đẻ sinh đôi hoặc sinh nhiều hơn thì cơ sở y tế tạo lập, gửi dữ liệu XML giấy ra viện cho
từng trẻ.

##### **Bảng 8. Chỉ tiêu dữ liệu tóm tắt hồ sơ bệnh án** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ<br>tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các<br>bảng còn lại ban hành kèm theo Quyết định này trong một lần<br>khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|MA_LOAI_KCB|Số|2|Ghi mã hình thức KBCB, trong đó:<br>- Mã "02": Điều trị ngoại trú;<br>- Mã "03": Điều trị nội trú;<br>- Mã "04": Điều trị nội trú ban ngày;|
|3|HO_TEN_CHA|Chuỗi|255|Ghi họ và tên cha (bố) theo hồ sơ bệnh án của người bệnh (nếu<br>có).|
|4|HO_TEN_ME|Chuỗi|255|Ghi họ và tên mẹ theo hồ sơ bệnh án của người bệnh (nếu có).|
|5|NGUOI_GIAM_HO|Chuỗi|255|Ghi họ và tên người giám hộ theo hồ sơ bệnh án của người<br>bệnh (nếu có).|
|6|DON_VI|Chuỗi|1024|Ghi tên đơn vị của người hưởng.<br>**Lưu ý:**<br>- Ghi rõ đơn vị nơi người bệnh làm việc và đóng bảo hiểm xã<br>hội theo thông tin do người đến khám bệnh cung cấp;<br>- Trường hợp con ốm thì ghi tên đơn vị mà người cha (bố) hoặc<br>mẹ đang làm việc và đóng bảo hiểm xã hội theo thông tin do<br>người đến khám bệnh cung cấp. Thực hiện việc ghi giấy chứng<br>nhận nghỉ việc hưởng BHXH theo hướng dẫn tại Thông tư số<br>18/2022/TT-BYT của Bộ trưởng Bộ Y tế.|
|7|NGAY_VAO|Chuỗi|12|Ghi thời điểm người bệnh đến KBCB, gồm 12 ký tự, theo định<br>dạng yyyymmddHHMM.<br>_Ví dụ_: người bệnh đến KBCB lúc 15 giờ 20 phút ngày<br>31/03/2017 được hiển thị là: 201703311520.|

|8|NGAY_RA H|Chuỗi|5|Ghi thời điểm người bệnh kết thúc điều trị nội trú, kết thúc<br>điều trị nội trú ban ngày, kết thúc điều trị ngoại trú hoặc kết<br>thúc khám bệnh, gồm 12 ký tự theo định dạng<br>Ví dụ: Thời điểm người bệnh kết thúc điều trị lúc 09 giờ 20<br>phút ngày 05/04/2022, khi đó được hiển thị là: 202204050920.<br>Lưu ý:<br>- Trường hợp khám bệnh (MA_LOAI_KCB = 01) thì ghi thời<br>điểm kết thúc lần khám bệnh;<br>- Trường hợp điều trị ngoại trú (MA_LOAI_KCB = 02), điều<br>trị ngoại trú các bệnh mạn tính dài ngày liên tục trong năm<br>(MA_LOAI_KCB = 05), nhận thuốc theo hẹn (không khám<br>bệnh) (MA_LOAI_KCB = 07): Ghi ngày kết thúc của đợt<br>KBCB (là ngày cuối cùng sử dụng thuốc hoặc dịch vụ theo chỉ<br>định của bác sỹ), gồm 02 ký tự giờ + 02 ký tự phút và mặc định<br>là 2359 (Thời điểm cuối cùng của ngày kết thúc đợt KBCB);<br>- Trường hợp điều trị ngoại trú các bệnh mạn tính dài ngày liên<br>tục trong năm (MA_LOAI_KCB = 08): Ghi thời điểm kết thúc<br>của đợt KBCB (Ví dụ: Trường hợp chạy thận nhân tạo thì ghi<br>ngày cuối cùng của đợt chạy thận nhân tạo);<br>- Trường hợp người bệnh được chuyển tuyến đến cơ sở KBCB<br>khác thì thời điểm người bệnh ra viện bằng thời điểm người<br>bệnh được chuyển tuyến.|
|---|---|---|---|---|
|9|CHAN_DOAN_VAO|Chuỗi||Ghi chẩn đoán của cơ sở KBCB ở thời điểm tiếp nhận người<br>bệnh (Chẩn đoán sơ bộ).|
|10|CHAN_DOAN_RV|Chuỗi||Ghi đầy đủ chẩn đoán xác định bệnh chính, bệnh kèm theo<br>và/hoặc các triệu chứng hoặc hội chứng, được bác sỹ ghi trong<br>hồ sơ KBCB tại thời điểm kết thúc KBCB đối với người bệnh.<br>**Lưu ý:**Đối với việc ghi chẩn đoán ra viện để phục vụ việc tạo<br>lập giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội thì thực<br>hiện theo hướng dẫn tại Thông tư số 18/2022/TT-BYT của Bộ<br>trưởng Bộ Y tế, trong đó:<br>- Nội dung chẩn đoán phải mô tả cụ thể về tình trạng sức khỏe<br>hoặc ghi tên bệnh hoặc mã bệnh.<br>- Trường hợp mắc bệnh cần chữa trị dài ngày thì ghi mã bệnh;<br>trường hợp chưa có mã bệnh thì ghi đầy đủ tên bệnh. Việc ghi<br>mã bệnh và tên bệnh thực hiện theo quy định tại Thông tư số<br>46/2016/TT-BYT ngày 30 tháng 12 năm 2016 của Bộ trưởng<br>Bộ Y tế ban hành danh mục bệnh dài ngày;<br>- Trường hợp điều trị dưỡng thai: Ghi rõ cụm từ “dưỡng thai”|
|11|QT_BENHLY|Chuỗi||Ghi quá trình bệnh lý và diễn biến lâm sàng.|
|12|TOMTAT_KQ|Chuỗi||Ghi tóm tắt kết quả xét nghiệm cận lâm sàng có giá trị chẩn<br>đoán.|

|13|PP_DIEUTRI|Chuỗi||Ghi phương pháp điều trị theo đúng hướng dẫn tại Thông tư số<br>18/2022/TT-BYT của Bộ trưởng Bộ Y tế.|
|---|---|---|---|---|
|14|NGAY_SINHCON|Chuỗi|8|Trường hợp con chết sau khi sinh thì nhập ngày, tháng, năm<br>sinh của con, theo định dạng yyyymmdd|
|15|NGAY_CONCHET|Chuỗi|8|Trường hợp con chết sau khi sinh thì nhập ngày, tháng, năm<br>con chết, theo định dạng yyyymmdd|
|16|SO_CONCHET|Số|2|Trường hợp con chết sau khi sinh thì nhập số con bị chết.|
|17|KET_QUA_DTRI|Số|1|Ghi mã kết quả điều trị, trong đó:<br>- Mã "1": Khỏi;<br>- Mã "2": Đỡ;<br>- Mã "3": Không thay đổi;<br>- Mã "4": Nặng hơn;<br>- Mã "5": Tử vong;<br>- Mã "6": Tiên lượng nặng xin về;<br>- Mã "7": Chưa xác định (không thuộc một trong các mã kết<br>quả điều trị nêu trên).|
|18|GHI_CHU|Chuỗi||Trường thông tin này chỉ áp dụng đối với trường hợp người<br>mất hoặc bị hạn chế năng lực hành vi dân sự hoặc trẻ em dưới<br>16 tuổi phải ghi đầy đủ họ, tên của cha (bố) hoặc của mẹ hoặc<br>người giám hộ của người bệnh theo quy định tại Phụ lục 4 ban<br>hành kèm theo Thông tư số 18/2022/TT-BYT của Bộ trưởng<br>Bộ Y tế.|
|19|MA_TTDV|Số|10|Ghi mã số định danh y tế (mã số BHXH) của người đứng đầu<br>cơ sở KBCB hoặc người được người đứng đầu cơ sở KBCB ủy<br>quyền được ký và đóng dấu của cơ sở KBCB đó.|
|20|NGAY_CT|Chuỗi|8|Ghi ngày chứng từ (Tóm tắt hồ sơ bệnh án), theo định dạng<br>yyyymmdd, là ngày Trưởng khoa hoặc Trưởng phòng hoặc<br>Phó trưởng khoa hoặc Phó trưởng phòng cấp tóm tắt hồ sơ<br>bệnh án.|
|21|MA_THE_TAM|Chuỗi|15|Ghi mã thẻ BHYT tạm thời của trẻ em sinh ra hoặc của người<br>hiến tạng nhưng chưa được cơ quan BHXH cấp thẻ BHYT. Cơ<br>sở KBCB sử dụng chức năng “Thông tuyến khám chữa<br>bệnh\Tra cứu thẻ tạm của trẻ em hoặc của người hiến tạng”<br>trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định<br>BHYT của BHXH Việt Nam để tra cứu mã thẻ BHYT tạm<br>thời.|
|22|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần thiết.|

**Ghi chú:** Cơ sở KBCB chỉ gửi dữ liệu Bảng này trong trường hợp người bệnh điều trị nội trú (MA_LOAI_KCB
= 03) hoặc điều trị nội trú ban ngày (MA_LOAI_KCB = 04) hoặc điều trị lưu tại TYT tuyến xã, PKĐKKV
(MA_LOAI_KCB = 06).

##### **Bảng 9. Chỉ tiêu dữ liệu giấy chứng sinh** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ<br>tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các<br>bảng còn lại ban hành kèm theo Quyết định này trong một lần<br>khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|MA_BHXH_NND|Số|10|Ghi mã số BHXH người nuôi dưỡng (nếu có).|
|3|MA_THE_NND|Chuỗi|15|Ghi mã thẻ BHYT người nuôi dưỡng (nếu có).|
|4|HO_TEN_NND|Chuỗi|255|Ghi họ và tên của mẹ hoặc của người nuôi dưỡng.|
|5|NGAYSINH_NND|Chuỗi|8|Ghi ngày sinh của mẹ hoặc người nuôi dưỡng, định dạng|
|6|MA_DANTOC_NND|Số|2|Ghi mã dân tộc của mẹ hoặc người nuôi dưỡng theo Danh<br>mục các dân tộc Việt Nam ban hành kèm theo Quyết định số<br>121-TCTK/PPCĐ ngày 02 tháng 3 năm 1979 của Tổng cục<br>trưởng Tổng cục Thống kê để điền chi tiết). Tra cứu mã dân<br>tộc tại đường link: http://tongdieutradanso.vn/danh-muc-cac-<br>dan-toc-viet-nam.html|
|7|SO_CCCD_NND|Số|15|Ghi số chứng minh nhân dân hoặc số căn cước công dân hoặc<br>số hộ chiếu của mẹ hoặc người nuôi dưỡng.|
|8|NGAYCAP_CCCD_NND|Chuỗi|8|Ghi ngày cấp chứng minh nhân dân hoặc căn cước công dân<br>hoặc hộ chiếu của mẹ hoặc người nuôi dưỡng, định dạng|
|9|NOICAP_CCCD_NND|Chuỗi|1024|Ghi nơi cấp chứng minh nhân dân hoặc căn cước công dân<br>hoặc hộ chiếu của mẹ hoặc người nuôi dưỡng.|
|10|NOI_CU_TRU_NND|Chuỗi|1024|Ghi địa chỉ nơi cư trú hiện tại của mẹ hoặc người nuôi dưỡng.<br>**Lưu ý**:<br>- Nếu là người Việt Nam: Ghi địa chỉ nơi cư trú theo địa danh<br>4 cấp: Thôn/bản, xã/phường/thị trấn, quận/huyện/ thành phố<br>thuộc tỉnh, tỉnh/thành phố trực thuộc trung ương;<br>- Trường hợp người nước ngoài có địa chỉ nơi cư trú tại Việt<br>Nam thì ghi giống như người Việt Nam;<br>- Trường hợp người nước ngoài không có địa chỉ nơi cư trú<br>tại Việt Nam nhưng sinh đẻ tại cơ sở y tế của Việt Nam thì<br>ghi tên tỉnh/thành phố/bang và quốc gia nơi họ đang sinh<br>sống.|
|11|MA_QUOCTICH|Số|3|Ghi mã quốc tịch của mẹ hoặc người nuôi dưỡng theo quy<br>định tại Phụ lục 2 Thông tư số 07/2016/TT-BCA ngày 01<br>tháng 2 năm 2016 của Bộ trưởng Bộ Công an.|

|12|MATINH_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp tỉnh nơi cư trú hiện tại của mẹ hoặc<br>người nuôi dưỡng. Ghi theo 02 ký tự cuối của mã đơn vị hành<br>chính của tỉnh, thành phố trực thuộc Trung ương nơi người<br>bệnh cư trú (Quy định tại Phụ lục 1 Thông tư số 07/2016/TT-<br>BCA ngày 01 tháng 2 năm 2016 của Bộ trưởng Bộ Công an).|
|---|---|---|---|---|
|13|MAHUYEN_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp huyện nơi cư trú hiện tại của mẹ<br>hoặc người nuôi dưỡng. Ghi mã đơn vị hành chính cấp huyện<br>theo Quyết định số 124/2004/QĐ-TTg ngày 08/7/2004 của<br>Thủ tướng Chính phủ ban hành danh mục mã đơn vị hành<br>chính.|
|14|MAXA_CU_TRU|Chuỗi|5|Mã đơn vị hành chính cấp xã nơi cư trú hiện tại của mẹ hoặc<br>người nuôi dưỡng. Ghi mã đơn vị hành chính cấp xã theo<br>Quyết định số 124/2004/QĐ-TTg ngày 08/7/2004 của Thủ<br>tướng Chính phủ ban hành danh mục mã đơn vị hành chính.|
|15|HO_TEN_CHA|Chuỗi|255|Ghi họ và tên cha (bố) của trẻ được cấp giấy chứng sinh.|
|16|MA_THE_TAM|Chuỗi|15|Ghi mã thẻ BHYT tạm thời của người con. Cơ sở KBCB sử<br>dụng chức năng “Thông tuyến khám chữa bệnh\Tra cứu thẻ<br>tạm của trẻ em hoặc của người hiến tạng” trên Cổng tiếp nhận<br>dữ liệu Hệ thống thông tin giám định BHYT của BHXH Việt<br>Nam để tra cứu mã thẻ BHYT tạm thời.|
|17|HO_TEN_CON|Chuỗi|255|Ghi họ và tên dự định đặt cho con (nếu có).|
|18|GIOI_TINH_CON|Số|1|Ghi giới tính con, trong đó:<br>- Mã "1": Nam;<br>- Mã "2": Nữ;<br>- Mã "3": Chưa xác định.|
|19|SO_CON|Số|2|Ghi số lượng con trong lần sinh này.|
|20|LAN_SINH|Số|2|Ghi số lần sinh con (tính cả lần sinh này).|
|21|SO_CON_SONG|Số|2|Ghi số con hiện đang sống (tính cả trẻ sinh ra lần này).|
|22|CAN_NANG_CON|Số|10|Ghi số cân nặng của con, tính theo gram (ký hiệu là: g) (ví dụ:|
|23|NGAY_SINH_CON|Chuỗi|12|Ghi ngày sinh con theo định dạng yyyymmddHHMM.|

|24|<!-- FIELD_NAME_MISSING -->|Chuỗi|1024|Ghi địa chỉ nơi con được sinh ra.<br>Lưu ý:<br>- Trường hợp trẻ em được sinh ra tại bệnh viện, thì ghi tên<br>bệnh viện và địa danh hành chính nơi trẻ em được sinh ra. Ví<br>dụ: bệnh viện đa khoa tỉnh Nam Định);<br>- Trường hợp trẻ em được sinh tại cơ sở y tế khác thì ghi tên<br>cơ sở y tế và địa danh hành chính 3 cấp nơi trẻ em sinh ra (Ví<br>dụ: Trạm y tế xã Liên Bảo, huyện Vụ Bản, tỉnh Nam Định);<br>- Trường hợp trẻ em được sinh tại nhà thì ghi địa chỉ nhà và<br>địa danh 3 cấp: cấp xã/phường, quận/huyện, tỉnh/thành phố<br>trực thuộc trung ương<br>Ví dụ: sinh tại nhà ở xã Liên Bảo, huyện Vụ Bản, tỉnh Nam<br>Định;<br>- Trường hợp trẻ em được sinh ra tại nơi khác, ngoài cơ sở<br>KBCB thì cũng ghi nơi trẻ em được sinh ra và địa danh 3 cấp<br>hành chính.<br>Ví dụ: đẻ trên đường đi, tại xã Liên Bảo, huyện Vụ Bản, tỉnh<br>Nam Định.<br>- Trường hợp trẻ em bị bỏ rơi thì ghi rõ trẻ bị bỏ rơi và nơi<br>tìm thấy trẻ, với địa danh 3 cấp hành chính.<br>Ví dụ: trẻ bị bỏ rơi tại xã Liên Bảo, huyện Vụ Bản, tỉnh Nam<br>Định.|
|---|---|---|---|---|
|25|TINH_TRANG_CON|Chuỗi||Ghi rõ tình trạng của trẻ tại thời điểm làm Giấy chứng sinh:<br>khỏe mạnh, yếu, dị tật hoặc các biểu hiện liên quan đến sức<br>khỏe khác (nếu có).<br>**Lưu ý**: Nếu trẻ bị dị dạng, dị tật, ghi cụ thể loại dị dạng, dị<br>tật, kể cả khuyết tật về hình thái của trẻ nếu phát hiện được.|
|26|SINHCON_PHAUTHUAT|Số|1|- Mã "1": sinh con phải phẫu thuật;<br>- Mã "0": sinh con không phải phẫu thuật.|
|27|SINHCON_DUOI32TUAN|Số|1|- Mã "1": sinh con dưới 32 tuần tuổi;<br>- Mã "0" là không sinh con dưới 32 tuần tuổi.|
|28|GHI_CHU|Chuỗi||Trường hợp sinh con phải phẫu thuật hoặc sinh con dưới 32<br>tuần tuổi hoặc vừa sinh con dưới 32 tuần tuổi lại vừa phải<br>phẫu thuật thì trong phần ghi chú phải ghi rõ một trong các<br>nội dung sau "Sinh con phải phẫu thuật" hoặc "Sinh con dưới<br>32 tuần tuổi" hoặc "Phẫu thuật, sinh con dưới 32 tuần tuổi".|
|29|NGUOI_DO_DE|Chuỗi|255|Ghi họ và tên người đỡ đẻ.|
|30|NGUOI_GHI_PHIEU|Chuỗi|255|Ghi họ và tên người ghi phiếu.|
|31|NGAY_CT|Chuỗi|8|Ghi ngày cấp chứng từ (Giấy chứng sinh), định dạng<br>yyyymmdd, ghi theo ngày dương lịch.|
|32|SO|Chuỗi|200|Ghi số của chứng từ (Giấy chứng sinh) tại cơ sở KBCB.|

|33|QUYEN_SO|Chuỗi|200|Ghi quyển số của chứng từ (Giấy chứng sinh) tại cơ sở|
|---|---|---|---|---|
|34|MA_TTDV|Số|10|Ghi mã số định danh y tế (mã số BHXH) của Thủ trưởng cơ<br>sở KBCB cấp giấy chứng sinh.|

**Ghi chú** : Trường hợp đẻ sinh đôi hoặc sinh nhiều hơn thì cơ sở y tế tạo lập, gửi dữ liệu XML giấy chứng sinh cho
từng trẻ.

**Bảng 10. Chỉ tiêu dữ liệu giấy chứng nhận nghỉ dưỡng thai**
##### (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng chỉ tiêu<br>tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và các bảng còn<br>lại ban hành kèm theo Quyết định này trong một lần khám bệnh,<br>chữa bệnh (PRIMARY KEY)).|
|2|SO_SERI|Chuỗi|200|Ghi số Seri chứng từ (Giấy chứng nhận nghỉ dưỡng thai) do cơ<br>sở KBCB quy định theo mẫu tại Phụ lục 6 ban hành kèm theo<br>Thông tư 56/2017/TT-BYT của Bộ trưởng Bộ Y tế.|
|3|SO_CT|Chuỗi|200|Ghi số chứng từ phục vụ việc quản lý nội bộ của cơ sở KBCB<br>quy định theo mẫu tại Phụ lục 6 ban hành kèm theo Thông tư<br>56/2017/TT-BYT của Bộ trưởng Bộ Y tế.|
|4|SO_NGAY|Số|3|Ghi số ngày nghỉ căn cứ vào tình trạng sức khỏe của người bệnh<br>(SO_NGAY = DEN_NGAY - TU_NGAY).|
|5|DON_VI|Chuỗi|1024|Ghi tên đơn vị của người hưởng.<br>**Lưu ý:**<br>- Ghi rõ đơn vị nơi người bệnh làm việc và đóng bảo hiểm xã<br>hội theo thông tin do người đến khám bệnh cung cấp;<br>- Thực hiện việc ghi giấy chứng nhận nghỉ dưỡng thai theo<br>hướng dẫn tại Phụ lục 6 ban hành kèm theo Thông tư<br>56/2017/TT-BYT của Bộ trưởng Bộ Y tế.|
|6|CHAN_DOAN_RV|Chuỗi||Ghi đầy đủ chẩn đoán xác định bệnh chính, bệnh kèm theo<br>và/hoặc các triệu chứng hoặc hội chứng, được bác sỹ ghi trong<br>hồ sơ KBCB tại thời điểm kết thúc KBCB đối với người bệnh.<br>**Lưu ý:**Đối với việc ghi chẩn đoán ra viện để phục vụ việc tạo<br>lập giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội thì thực<br>hiện theo hướng dẫn tại Thông tư số 56/2017/TT-BYT của Bộ<br>trưởng Bộ Y tế, trong đó:<br>- Nội dung chẩn đoán phải mô tả cụ thể về tình trạng sức khỏe<br>hoặc ghi tên bệnh hoặc mã bệnh.<br>- Trường hợp mắc bệnh cần chữa trị dài ngày thì ghi mã bệnh;<br>trường hợp chưa có mã bệnh thì ghi đầy đủ tên bệnh. Việc ghi<br>mã bệnh và tên bệnh thực hiện theo quy định tại Thông tư số<br>46/2016/TT-BYT ngày 30 tháng 12 năm 2016 của Bộ trưởng Bộ<br>Y tế ban hành danh mục bệnh dài ngày;<br>- Trường hợp điều trị dưỡng thai: Ghi rõ cụm từ “dưỡng thai”.|

|7|TU_NGAY|Chuỗi|8|Ghi ngày bắt đầu nghỉ dưỡng thai, theo định dạng yyyymmdd.<br>Lưu ý: Việc ghi ngày bắt đầu được nghỉ phải trùng với ngày<br>người bệnh đến khám.<br>Ví dụ: Ngày khám là ngày 13 tháng 7 năm 2018 và phải nghỉ 30<br>ngày thì tại phần số ngày nghỉ để điều trị bệnh ghi là 30 ngày và<br>ghi rõ là từ ngày 13 tháng 7 năm 2018 đến ngày 11 tháng 8 năm|
|---|---|---|---|---|
|8|DEN_NGAY|Chuỗi|8|Ghi ngày kết thúc nghỉ dưỡng thai, theo định dạng yyyymmdd|
|9|MA_TTDV|Số|10|Ghi mã số định danh y tế (mã số BHXH) của người đứng đầu cơ<br>sở KBCB hoặc người được uỷ quyền ký xác nhận giấy chứng<br>nhận nghỉ dưỡng thai.|
|10|TEN_BS|Chuỗi|255|Ghi họ và tên của Trưởng khoa hoặc Phó trưởng khoa hoặc Bác<br>sỹ hành nghề KBCB được uỷ quyền ký tên theo quy định của<br>Thủ trưởng cơ sở KBCB.|
|11|MA_BS|Chuỗi|200|Ghi mã số định danh y tế (mã số BHXH) của Trưởng khoa hoặc<br>Trưởng phòng hoặc Phó trưởng khoa hoặc Phó trưởng phòng<br>hoặc Bác sỹ hành nghề KBCB ký tên theo quy định của Thủ<br>trưởng cơ sở KBCB.|
|12|NGAY_CT|Chuỗi|8|Ghi ngày cấp chứng từ, theo định dạng yyyymmdd|

##### **Bảng 11. Chỉ tiêu dữ liệu giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của Bộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|MA_LK|Chuỗi|100|Là mã đợt điều trị duy nhất (dùng để liên kết giữa Bảng<br>chỉ tiêu tổng hợp khám bệnh, chữa bệnh (bảng XML 1) và<br>các bảng còn lại ban hành kèm theo Quyết định này trong<br>một lần khám bệnh, chữa bệnh (PRIMARY KEY)).|
|2|SO_CT|Chuỗi|200|Ghi số chứng từ, là mã lưu trữ giấy chứng nhận nghỉ việc<br>hưởng BHXH tại cơ sở KBCB.|
|3|SO_SERI|Chuỗi|200|Ghi số định danh chứng từ (Giấy chứng nhận nghỉ việc<br>hưởng BHXH) của mỗi đợt điều trị theo quy định của cơ<br>sở KBCB.|
|4|SO_KCB|Chuỗi|200|Ghi số chứng từ phục vụ việc quản lý nội bộ của cơ sở<br>KBCB theo Phụ lục 07 Thông tư 18/2022/TT-BYT của Bộ<br>trưởng Bộ Y tế.|
|5|DON_VI|Chuỗi|1024|Ghi tên đơn vị của người hưởng BHXH.<br>**Lưu ý:**<br>- Ghi rõ đơn vị nơi người bệnh làm việc và đóng bảo hiểm<br>xã hội theo thông tin do người đến khám bệnh cung cấp;<br>- Trường hợp con ốm thì ghi tên đơn vị mà người cha (bố)<br>hoặc mẹ đang làm việc và đóng bảo hiểm xã hội theo<br>thông tin do người đến khám bệnh cung cấp. Thực hiện<br>việc ghi giấy chứng nhận nghỉ việc hưởng BHXH theo<br>hướng dẫn tại Thông tư 18/2022/TT-BYT của Bộ trưởng<br>Bộ Y tế.|
|6|MA_BHXH|Số|10|Ghi mã số BHXH của người bệnh.|

7 MA_THE_BHYT Chuỗi n

Ghi mã thẻ BHYT của người bệnh do cơ quan BHXH c ~~ấ~~ p.
**Lưu ý** :

- Khi tiếp đón người bệnh, cơ sở KBCB có trách nhiệm tra cứu
trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định
BHYT của BHXH Việt Nam để kiểm tra thông tin thẻ BHYT.
Trường hợp cấp cứu mà người bệnh hoặc thân nhân người bệnh
không xuất trình được thẻ BHYT ngay thì cơ sở KBCB tra cứu
thông tin thẻ BHYT trước khi người bệnh ra viện.

- Đối với thẻ BHYT của các đối tượng có các mã QN, HC, LS,
XK, CY, CA do BHXH Bộ Quốc phòng, BHXH Bộ Công an
cấp: Tra cứu để kiểm tra thời hạn sử dụng của thẻ BHYT trong
trường hợp các đối tượng này không còn phục vụ trong lực
lượng Quân đội, Công an, Cơ yếu.

- Trường hợp trong thời gian điều trị, người bệnh được cấp thẻ
BHYT mới có thay đổi thông tin liên quan đến mã thẻ thì ghi
tiếp mã thẻ mới (mỗi mã thẻ gồm có 15 ký tự), giữa các mã thẻ
cách nhau bằng dấu chấm phẩy “;”;

- Trường hợp người bệnh chưa có thẻ BHYT, cơ sở KBCB sử
dụng chức năng “Thông tuyến khám chữa bệnh\Tra cứu thẻ tạm
của trẻ em hoặc của người hiến tạng” trên Cổng tiếp nhận dữ
liệu Hệ thống thông tin giám định BHYT của BHXH Việt Nam
để tra cứu mã thẻ BHYT tạm thời.

- Trường hợp người bệnh không KBCB BHYT thì để trống
trường thông tin này.

|8|8|Chuỗi|5|Ghi đầy đủ chẩn đoán xác định bệnh chính, bệnh kèm theo<br>và/hoặc các triệu chứng hoặc hội chứng, được bác sỹ ghi<br>trong hồ sơ KBCB tại thời điểm kết thúc KBCB đối với<br>người bệnh.<br>Lưu ý: Đối với việc ghi chẩn đoán ra viện để phục vụ việc<br>tạo lập giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội<br>thì thực hiện theo hướng dẫn tại Thông tư số 18/2022/TT-<br>BYT của Bộ trưởng Bộ Y tế, trong đó:<br>- Nội dung chẩn đoán phải mô tả cụ thể về tình trạng sức<br>khỏe hoặc ghi tên bệnh hoặc mã bệnh.<br>- Trường hợp mắc bệnh cần chữa trị dài ngày thì ghi mã<br>bệnh; trường hợp chưa có mã bệnh thì ghi đầy đủ tên<br>bệnh. Việc ghi mã bệnh và tên bệnh thực hiện theo quy<br>định tại Thông tư số 46/2016/TT-BYT ngày 30 tháng 12<br>năm 2016 của Bộ trưởng Bộ Y tế ban hành danh mục bệnh<br>dài ngày;<br>- Trường hợp điều trị dưỡng thai: Ghi rõ cụm từ “dưỡng|
|---|---|---|---|---|
|9|PP_DIEUTRI|Chuỗi||Ghi phương pháp điều trị theo đúng hướng dẫn tại Thông<br>tư số 18/2022/TT-BYT của Bộ trưởng Bộ Y tế.|
|10|MA_DINH_CHI_THAI|Số|1|Ghi mã "1" là đình chỉ thai nghén, mã "0" là không đình<br>chỉ thai nghén.<br>Trường hợp đình chỉ thai nghén bắt buộc nhập thông tin<br>vào trường thông tin tuổi thai (TUOI_THAI) và trường<br>thông tin nguyên nhân đình chỉ thai nghén<br>(NGUYENNHAN_DINHCHI).|
|11|NGUYENNHAN_DINHC|Chuỗi||Ghi nguyên nhân đình chỉ thai nghén.<br>**Lưu ý:** Bắt buộc ghi trường thông tin này khi<br>MA_DINH_CHI_THAI là mã "1".|

|12|TUOI_THAI|Số|5|Ghi tuổi thai thực tế (theo tuần), trong đó tuổi thai luôn<br>luôn lớn hơn hoặc bằng 1 và nhỏ hơn hoặc bằng tuổi 42<br>tuần tuổi.<br>Lưu ý: Bắt buộc ghi trường thông tin này khi<br>MA_DINH_CHI_THAI = 1.|
|---|---|---|---|---|
|13|SO_NGAY_NGHI|Số|3|Ghi số ngày nghỉ căn cứ vào tình trạng sức khỏe của<br>người bệnh.<br>**Lưu ý:** Việc quyết định số ngày nghỉ phải căn cứ vào tình<br>trạng sức khỏe của người bệnh nhưng tối đa không quá 30<br>ngày cho một lần cấp giấy chứng nhận nghỉ việc hưởng<br>bảo hiểm xã hội. Riêng trường hợp người bệnh điều trị<br>bệnh lao theo chương trình chống lao quốc gia thì thời<br>gian nghỉ tối đa không quá 180 ngày cho một lần cấp giấy<br>chứng nhận nghỉ việc hưởng bảo hiểm xã hội.<br>Trường hợp người lao động bị sẩy thai, phá thai, nạo, hút<br>thai, thai chết lưu mà tuổi thai từ 13 tuần tuổi trở lên thì<br>thời gian nghỉ tối đa theo quy định của Luật bảo hiểm xã<br>hội nhưng không quá 50 ngày cho một lần cấp giấy chứng<br>nhận nghỉ việc hưởng bảo hiểm xã hội.|
|14|TU_NGAY|Chuỗi|8|Ghi ngày bắt đầu hưởng chế độ, theo định dạng<br>yyyymmdd và phải trùng khớp với ngày người bệnh đến<br>khám.|
|15|DEN_NGAY|Chuỗi|8|Ghi ngày kết thúc hưởng chế độ, theo định dạng|
|16|HO_TEN_CHA|Chuỗi|255|Ghi họ và tên cha (bố) của người bệnh (nếu có) trong<br>trường hợp người bệnh là trẻ em dưới 07 tuổi theo quy<br>định tại Phụ lục 7 Thông tư số 18/2022/TT-BYT của Bộ<br>trưởng Bộ Y tế. Trường hợp không có cha (bố) thì để<br>trống trường thông tin này.|

|17|HO_TEN_ME|Chuỗi|5|Ghi họ và tên mẹ của người bệnh (nếu có) trong trường<br>hợp người bệnh là trẻ em dưới 07 tuổi theo quy định tại<br>Phụ lục 7 Thông tư số 18/2022/TT-BYT của Bộ trưởng<br>Bộ Y tế. Trường hợp không có mẹ thì để trống trường<br>thông tin này.|
|---|---|---|---|---|
|18|MA_TTDV|Số|10|Ghi mã số định danh y tế (mã số BHXH) của người đứng<br>đầu cơ sở KBCB hoặc người được người đứng đầu cơ sở<br>KBCB ủy quyền được ký và đóng dấu của cơ sở KBCB<br>đó.|
|19|MA_BS|Chuỗi|200|Ghi mã số định danh y tế (mã số BHXH) của Trưởng khoa<br>hoặc Trưởng phòng hoặc Phó trưởng khoa hoặc Phó<br>trưởng phòng hoặc Bác sỹ hành nghề KBCB ký tên theo<br>quy định của Thủ trưởng cơ sở KBCB.|
|20|NGAY_CT|Chuỗi|8|Ghi ngày cấp chứng từ (Giấy chứng nhận nghỉ việc hưởng<br>BHXH), theo định dạng yyyymmdd và phải trùng với<br>ngày người lao động đến khám bệnh. Trường hợp đợt<br>khám bệnh kéo dài từ 2 ngày trở lên thì ngày, tháng, năm<br>cấp phải trùng với ngày cuối cùng của đợt người lao động<br>đến khám bệnh và cần được chỉ định nghỉ ngoại trú.|
|21|MA_THE_TAM|Chuỗi|15|Ghi mã thẻ BHYT tạm thời của trẻ em sinh ra hoặc của<br>người hiến tạng nhưng chưa được cơ quan BHXH cấp thẻ<br>BHYT. Cơ sở KBCB sử dụng chức năng “Thông tuyến<br>khám chữa bệnh\Tra cứu thẻ tạm của trẻ em hoặc của<br>người hiến tạng” trên Cổng tiếp nhận dữ liệu Hệ thống<br>thông tin giám định BHYT của BHXH Việt Nam để tra<br>cứu mã thẻ BHYT tạm thời.|
|22|MAU_SO|Chuỗi|5|Các cơ sở KBCB sử dụng chuỗi**CT07** để xác định đây là<br>Giấy nghỉ việc hưởng bảo hiểm xã hội. Mẫu số mặc định<br>để trống không điền thì hệ thống tự điền CT07.|

##### **Bảng 12. Chỉ tiêu dữ liệu giám định y khoa** (Ban hành kèm theo Quyết định số /QĐ-BYT ngày / /2023 của B 18 01 ộ trưởng Bộ Y tế)

|STT|Chỉ tiêu|Kiểu dữ liệu|Kích thước tối đa|Diễn giải|
|---|---|---|---|---|
|1|NGUOI_CHU_TRI|Chuỗi|255|Ghi họ và tên người chủ trì trong danh mục người chủ trì hội<br>đồng giám định y khoa đã nhập trên Cổng tiếp nhận của cơ|
|2|CHUC_VU|Số|1|Ghi chức vụ của người chủ trì, trong đó: mã "1": Chủ tịch;<br>mã "2": Người ký thay chủ tịch.|
|3|NGAY_HOP|Chuỗi|8|Ghi ngày, tháng, năm họp hội đồng giám định y khoa, theo<br>định dạng yyyymmdd|
|4|HO_TEN|Chuỗi|255|Ghi họ và tên người được giám định y khoa.|
|5|NGAY_SINH|Chuỗi|8|Ghi ngày, tháng, năm sinh của người được giám định y khoa,<br>theo định dạng yyyymmdd|
|6|SO_CCCD|Số|15|Ghi số căn cước công dân hoặc số chứng minh thư nhân dân<br>hoặc số hộ chiếu của người được giám định y khoa.<br>Trường hợp không có số căn cước công dân hoặc số chứng<br>minh thư nhân dân hoặc số hộ chiếu thì sử dụng mã tài khoản<br>định danh điện tử.|
|7|NGAY_CAP_CCCD|Chuỗi|8|Ghi ngày cấp chứng minh nhân dân hoặc thẻ căn cước công<br>dân hoặc hộ chiếu của người được giám định y khoa, theo<br>định dạng yyyymmdd|
|8|NOI_CAP_CCCD|Chuỗi|1024|Ghi nơi cấp chứng minh nhân dân hoặc thẻ căn cước công<br>dân hoặc hộ chiếu của người được giám định y khoa.|
|9|DIA_CHI|Chuỗi|1024|Ghi địa chỉ**nơi cư trú hiện tại**của người được giám định y<br>**Lưu ý:**Ghi cụ thể số nhà hoặc Thôn/Xóm; phường/xã; quận,<br>huyện/thị xã/TP thuộc tỉnh; tinh, thành phố trực thuộc trung<br>ương.|
|10|MATINH_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp tỉnh nơi cư trú hiện tại của người<br>bệnh. Ghi theo 02 ký tự cuối của mã đơn vị hành chính của<br>tỉnh, thành phố trực thuộc Trung ương nơi người bệnh cư trú<br>(Quy định tại Phụ lục 1 Thông tư số 07/2016/TT-BCA của<br>Bộ trưởng Bộ Công an).|
|11|MAHUYEN_CU_TRU|Chuỗi|3|Mã đơn vị hành chính cấp huyện nơi cư trú hiện tại của người<br>bệnh. Ghi mã đơn vị hành chính cấp huyện theo Quyết định<br>số 124/2004/QĐ-TTg ngày 08/7/2004 của Thủ tướng Chính<br>phủ ban hành danh mục mã đơn vị hành chính.|
|12|MAXA_CU_TRU|Chuỗi|5|Mã đơn vị hành chính cấp xã nơi cư trú hiện tại của người<br>bệnh. Ghi mã đơn vị hành chính cấp xã theo Quyết định số<br>124/2004/QĐ-TTg ngày 08/7/2004 của Thủ tướng Chính phủ<br>ban hành danh mục mã đơn vị hành chính.|

|13|MA_BHXH|Số|10|Ghi mã số bảo hiểm xã hội của người được giám định y khoa,<br>tìm kiếm tại địa chỉ:<br>https://baohiemxahoi.gov.vn/Pages/default.aspx|
|---|---|---|---|---|
|14|MA_THE_BHYT|Chuỗi|15|Ghi mã thẻ BHYT của người được giám định y khoa (nếu<br>có).|
|15|NGHE_NGHIEP|Chuỗi|100|Ghi nghề nghiệp của người đề nghị khám giám định y khoa<br>(nếu có).|
|16|DIEN_THOAI|Chuỗi|15|Ghi số điện thoại liên hệ của người đề nghị giám định y khoa|
|17|MA_DOI_TUONG|Chuỗi|20|Ghi mã đối tượng giám định (BB: Bệnh binh; BHXH1L:<br>Hưởng BHXH 1 lần; BNN: Bệnh nghề nghiệp; CĐHH: Chất<br>độc hóa học; KNLĐH: Nghỉ hưu trước tuổi; KNLĐT: Tuất;<br>NKT: Người khuyết tật; NVQS: Khám tuyển nghĩa vụ quân<br>sự; TB: Thương binh; TH: Giám định tổng hợp; TNLĐ: Tai<br>nạn lao động).<br>**Ghi chú:** Trường hợp một đối tượng mà có từ hai mã đối<br>tượng trở lên thì liệt kê các mã đối tượng, giữa các mã đối<br>tượng cách nhau bằng dấu chấm phẩy ";".|
|18|KHAM_GIAM_DINH|Số|1|Ghi mã khám giám định, trong đó:<br>- Mã "1": Khám giám định lần đầu;<br>- Mã "2": Khám giám định lại;<br>- Mã "3": Khám giám định tái phát;<br>- Mã "4": Khám phúc quyết (vượt khả năng chuyên môn,<br>hoặc đối tượng không đồng ý, hoặc theo đề nghị của Cục<br>Quản lý KCB/Cục Người có công/BHXH);<br>- Mã "5": Khám phúc quyết lần cuối;<br>- Mã "6": Khám bổ sung;<br>- Mã "7": Khám vết thương còn sót;<br>- Mã "8": Giám định tổng hợp.|
|19|SO_BIEN_BAN|Chuỗi|200|Ghi số thứ tự trong biên bản họp hội đồng giám định y khoa.|
|20|TYLE_TTCT_CU|Số|3|Ghi tỷ lệ (%) tổn thương cơ thể do thương tật, bệnh tật, bệnh<br>nghề nghiệp của lần giám định trước (lần gần nhất) theo kết<br>luận của Hội đồng giám định y khoa.<br>**Ghi chú:** Trường thông tin này để trống nếu không có tỷ lệ<br>tổn thương cơ thể của lần giám định trước (lần gần nhất).|

|21|DANG_HUONG_CHE_D|Số|3|Ghi mã chế độ đang hưởng, trong đó:<br>- Mã "1": Thương binh;<br>- Mã "2": Bệnh, tật;<br>- Mã "3": Bệnh nghề nghiệp;<br>- Mã "4": Tai nạn lao động;<br>- Mã "5": Chất độc hoá học;<br>- Mã "6": Bệnh binh;<br>- Mã "7": Khác (không thuộc một trong các đối tượng quy<br>định từ mã "1" đến mã "6" của trường thông tin này).<br>Ghi chú:<br>- Trường hợp đang được hưởng cùng lúc nhiều chế độ khác<br>nhau thì ghi mã các chế độ đang được hưởng, phân cách bằng<br>dấu chấm phẩy “;”;<br>- Trường thông tin này để trống nếu không thuộc một trong<br>các chế độ nêu trên.|
|---|---|---|---|---|
|22|NGAY_CHUNG_TU|Chuỗi|8|Ghi ngày chứng từ (ngày họp Hội đồng giám định y khoa),<br>theo định dạng yyyymmdd|
|23|SO_GIAY_GIOI_THIEU|Chuỗi|200|Ghi số giấy giới thiệu.|
|24|NGAY_DE_NGHI|Chuỗi|8|Ghi ngày đề nghị, theo định dạng yyyymmdd|
|25|MA_DONVI|Chuỗi|200|Ghi mã cơ quan, đơn vị quản lý hoặc cơ quan, đơn vị giới<br>thiệu đối tượng khám giám định y khoa.|
|26|GIOI_THIEU_CUA|Chuỗi|1024|Ghi tên đầy đủ của cơ quan, đơn vị quản lý hoặc cơ quan, đơn<br>vị giới thiệu đối tượng khám giám định y khoa.|
|27|KET_QUA_KHAM|Chuỗi||Ghi kết quả khám của Hội đồng Giám định y khoa (được thể<br>hiện trong Biên bản giám định y khoa).|
|28|SO_VAN_BAN_CAN_CU|Chuỗi|200|Ghi số văn bản (Ghi đầy đủ số và ký tự của văn bản) làm căn<br>cứ khám giám định y khoa phù hợp với đối tượng giám định<br>(Ví dụ: Thông tư 34/2012/TTLT-BYT-BLĐTBXH; Thông tư<br>28/2013/TTLT-BYT-BLDTBXH; Thông tư 20/2016/TTLT-<br>BYT-BLĐTBXH; Thông tư 52/2017/TT-BYT; Thông tư<br>56/2017/TT-BYT; Thông tư 01/2019/TT-BLĐTBXH; Thông<br>tư 45/2014/TTLT-BYT-BLĐTBXH; Nghị định 28/2012/NĐ-<br>Nếu có nhiều văn bản làm căn cứ giám định, kết luận thì ghi<br>đầy đủ các số hiệu văn bản, giữa các số hiệu văn bản phân<br>cách bằng dấu chấm phẩy “;”.|
|29|TYLE_TTCT_MOI|Số|3|Ghi tỷ lệ (%) tổn thương cơ thể do thương tật, bệnh tật, bệnh<br>nghề nghiệp của lần giám định này theo kết luận của Hội<br>đồng giám định y khoa.|
|30|TONG_TYLE_TTCT|Số|3|Ghi tổng tỷ lệ tổn thương cơ thể, do thương tật, bệnh tật, bệnh<br>nghề nghiệp (nếu có) theo kết luận của Hội đồng giám định y<br>**Lưu ý:**chỉ ghi trường thông tin này trong trường hợp khám<br>giám định tổng hợp, khám bổ sung, khám vết thương còn sót.|

|31|DANG_KHUYETTAT|Số|1|Ghi mã dạng khuyết tật theo quy định về dạng khuyết tật tại<br>Mẫu số 01 ban hành kèm theo Thông tư số 01/2019/TT-<br>BLĐTBXH ngày 02/01/2019 của Bộ Lao động - Thương<br>binh - Xã hội, trong đó:<br>- Mã "1": Khuyết tật vận động;<br>- Mã "2": Khuyết tật nghe, nói;<br>- Mã "3": Khuyết tật nhìn;<br>- Mã "4": Khuyết tật thần kinh, tâm thần;<br>- Mã "5": Khuyết tật trí tuệ;<br>- Mã "6": Khuyết tật khác.<br>Trường thông tin này chỉ ghi trong trường hợp khám giám<br>định người khuyết tật.|
|---|---|---|---|---|
|32|MUC_DO_KHUYETTAT|Số|1|Ghi mã mức độ khuyết tật theo quy định về mức độ khuyết<br>tật tại Mẫu số 01 ban hành kèm theo Thông tư số 01/2019/TT-<br>BLĐTBXH ngày 02/01/2019 của Bộ Lao động - Thương<br>Binh - Xã hội, trong đó:<br>- Mã "1": Thực hiện được;<br>- Mã "2": Thực hiện được nhưng cần trợ giúp;<br>- Mã "3": Không thực hiện được;<br>- Mã "4: Không xác định được.<br>Trường thông tin này chỉ ghi trong trường hợp khám giám<br>định người khuyết tật.|
|33|DE_NGHI|Chuỗi||Ghi nội dung đề nghị.|
|34|DUOC_XACDINH|Chuỗi||Ghi ghi chú được xác định, ghi đầy đủ nội dung theo quy<br>định tại khoản 2 Điều 4 Thông tư số 56/2017/TT-BYT: Đối<br>với các trường hợp không tự kiểm soát hoặc không tự thực<br>hiện được các hoạt động đi lại, mặc quần áo, vệ sinh cá nhân<br>và những việc khác phục vụ nhu cầu sinh hoạt cá nhân hằng<br>ngày mà cần có người theo dõi, trợ giúp, chăm sóc hoàn toàn.|
|35|DU_PHONG|Chuỗi||Trường dữ liệu dự phòng khi cần.|

**Ghi chú:** Hiện nay các cơ sở giám định y khoa chưa kết nối liên thông với Cổng tiếp nhận dữ liệu Hệ thống
thông tin giám định BHYT của BHXH Việt Nam, vì vậy nội dung này quy định các trường thông tin cần thiết
để nhập dữ liệu trực tiếp trên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT của BHXH Việt
Nam để đáp ứng việc giải quyết chế độ cho các đối tượng giám định (Trừ giám định pháp y).
