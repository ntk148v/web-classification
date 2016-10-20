# Đề tài: Phân loại các trang web.

## Mô tả bài toán:

Với một tập các trang Web, hệ thống cần phải gán (phân loại) mỗi trang Web vào một trong số các thể loại (vd: "Kinh doanh", "Thể thao",...)

## Đầu vào:

Biểu diễn nội dung của một trang Web (vd: một vecto các tần xuất xuất hiện của các từ khóa)

## Đầu ra:

Thể loại phù hợp của trang Web đó.

## Phương pháp học máy:

Mạng nơ-ron nhân tạo, hoặc Máy vecto hỗ trợ...

## Tập dữ liệu:

Một các ví dụ: mỗi ví dụ bao gồm biểu diễn của một trang Web và nhãn lớp(thể loại).

## Hướng giải quyết dự kiến.

**Key word: Web classification**

1. Sử dụng thư viện scrapy, BeautifulSoup, html5lib để crawling website được đưa link vào. Sau đó biểu diễn nội dung của trang web.
2. Thực hiện phân loại bằng nhiều phương pháp, đưa ra kết quả và thời gian để phân loại. (Sklearn)
3. So sánh và đưa ra nhận định về kết quả hiện có.
4. Ý tưởng: Xây dựng cho 1 trang web (Django, Flask...) có giao diện cho nhập link và chọn phương pháp phân loại.

## Tài liệu tham khảo.

1. [Sklearn](http://scikit-learn.org/)
2. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. [Scrapy](https://scrapy.org/)
