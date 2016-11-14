Câu 1: các tham số đầu vào: 1 tham số thể hiện thuật toán mà người dùng muốn chọn là KNN hay SVM hay chọn cả 2.

Câu 2: Cái này e  không biết ạ vì e chưa tìm hiểu phần crawl sẽ làm gì và thu được dữ liệu như nào.

câu 3: 
- Phải biểu diễn dưới dạng vector vì mỗi quan sát sẽ có n thuộc tính => biểu diễn mỗi quan sát thành 1 vector n chiều dưới
dạng số, ví dụ nếu các thuộc tính là các từ ngữ thì có thể quy đổi ra số lần xuất hiện trong văn bản,... sau đó 
tiến hành chuẩn hóa miền giá trị, và thêm trọng số cho các thuộc tính để có thể dễ dàng tính khoảng cách giữa các điểm 
khi sử dụng KNN hay tìm ra siêu phẳng (phi tuyến) khi sử dụng SVM để phân tách.

- Các cách biểu diễn vector: 
  + import CountVectorizer từ sklearn.feature_extraction.text
  + khởi tạo vectorizer = CountVectorizer(min_df=1) để tạo vector có các thuộc tính là các từ đơn
    hoặc bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1) để tạo vector có các thuộc
    tính là đơn và từ ghép (ghép của 2 từ đơn)
  + Khởi tạo mảng corus là 1 mảng của các document 
  + Khởi tạo analyze là 1 vector chứa các Bag_of_words để tìm tần xuất xuất hiện mỗi từ trong các document.
  + Đặt X = vectorizer.fit_transform(corpus) để tìm ra ma trận có các hàng ứng với kết quả của các document trong corpus
    Để chuyền X thành mảng dùng X.toarray()
  
 Câu 4-5: câu này e chưa đọc tới ạ.@@ E đang đọc tiếp, vì phần Text feature extraction đọc docs khó hiểu quá.

 
 
