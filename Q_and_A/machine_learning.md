# Bài tập lớn học máy.

# Các bước thực hiện.

1. Web UI cho phép người dùng nhập vào đường link cần phân lớp và lựa chọn tham số đầu vào. (Có thể sử dụng link tiếng anh / tiếng việt, vote làm cả 2, thì lúc đó sẽ có 2 tập training cho tiếng anh và tiếng việt)

2. Crawl dữ liệu từ đường link trên theo các mục: title, link(url), label, content.

3. Biểu diễn content dưới định dạng vetor.

4. Tiến hành predict & classify, (Tùy theo tham số đầu vào mà lựa chọn model, model được training từ trước từ 1 tập training - vì vậy để tránh mất thời gian, nên cho train trước xong lưu model object lại bằng [pickle](https://docs.python.org/3/library/pickle.html)).

5. Cho phép người dùng so sánh & đánh giá kết quả phân loại.

6. Biểu diễn đồ thị.(optional)

# Công nghệ sử dụng.

1. Crawling: [Scrapy](https://scrapy.org).

2. Database: Mysql.

3. Python Machine Learning Package: [Sklearn](http://scikit-learn.org/stable/).

4. Web: Flask.

# Câu hỏi.

1. Những tham số đầu vào ở bước 1 có thể là gì? Đề xuất.

2. Crawl xong lưu trữ như thế nào?

3. Tại sao phải biểu diễn dưới định dạng vector, và có những cách biểu diễn nào? Nêu rõ từng cách biểu diễn cùng cách sử dụng thư viện sklearn cho từng cách biểu diễn đó.

4. Sử dụng thư viện sklearn để train và predict như thế nào? (chú ý 2 thuật toán sử dụng là K-NN và SVM).

5. Đánh giá kết quả bằng phương pháp nào? Nêu rõ từng cách cùng cách sử dụng thư viện sklearn.

6. Đọc tài liệu tham khảo + Tìm hiểu chưa? (*)

# Trả lời câu hỏi và commit câu trả lời lên github trong folder Q\_and\_A/, định dạng tên.md. Thời hạn là tối mai - 9h30, sau đấy ae sẽ bắt tay vào thiết kế và làm. Riêng @Công tiếp tục setup việc crawling, để có được tập train sớm nhất có thể, liên hệ @Đông để sử dụng server.
