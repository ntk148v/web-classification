**Câu 1**. Tham số đầu vào: 

 - Chọn thuật toán phân loại: SVM / k-NN
 - Chọn phân loại theo tập training Anh / Việt (optional)

**Câu 2.** Cách lưu trữ? 

 - Lưu trữ theo cây thư mục. Mỗi thư mục đại diện cho mỗi nhãn (Thể
   thao, Game, Tài chính ...)

 - Trong mỗi thư mục là các file .csv chứa các trưòng 'title', 'url',
   'content', 'label'

**Câu 3.** Phần này em cũng mới tìm hiểu được như bạn Đông thôi ạ :))

**Câu 4.** Sử dụng thư viện sklearn để train và predict

a) k-NN

 - Ta sử dụng lớp KNeighborsClassifier để train và predict - dùng k láng
   giềng gần nhất với z(ví dụ cần phân lớp) tính theo khoảng cách. Ngoài
   ra có thể dùng lớp RadiusNeighborsClassifier - dùng các làng giềng
   trong phạm vi bán kính cố định r.
 - Cần xây dụng một hàm dataset.load_data để load nội dung của webpage
   dưới định dạng các vector và một hàm dataset.load_target để load các
   nhãn lớp tương ứng với mỗi vector đó.
 - Dùng hàm model.fit(X,y) để học tập huấn luyện với:
	+ X =  dataset.load_data
	+ y = dataset.load_target
 - Cuối cùng dùng hàm model.predict(z) để trả về nhãn lớp của z (z là
   định dạng vector)

Em chưa hiểu thuộc tính weight = uniform/ distance dùng để làm gì ạ.

b) SVM (phần này em chưa tìm hiểu xong ạ)

**Câu 5**. Đánh giá bằng cách sử dụng tập testing, lấy các link trong tập testing để kiểm tra --> so sánh --> tính %. Em nghĩ dùng cái này ạ http://scikit-learn.org/stable/modules/model_evaluation.html , nhưng em chưa tìm hiểu kĩ ạ .
