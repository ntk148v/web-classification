# Đề tài: Phân loại các trang web.

## Mô tả bài toán:

Với một tập các trang Web, hệ thống cần phải gán(phân loại) mỗi trang Web vào một trong số các thể loại(vd: "Kinh doanh", "Thể thao", ...)

## Đầu vào:

Biểu diễn nội dung của một trang Web(vd: một vecto các tần xuất xuất hiện của các từ khóa)

## Đầu ra:

Thể loại phù hợp của trang Web đó.

## Phương pháp học máy:

Mạng nơ - ron nhân tạo, hoặc Máy vecto hỗ trợ...

## Tập dữ liệu:

Một các ví dụ: mỗi ví dụ bao gồm biểu diễn của một trang Web và nhãn lớp(thể loại).

## Hướng giải quyết dự kiến.

**Key word: Web classification**

1. Sử dụng thư viện scrapy, BeautifulSoup, html5lib để crawling website được đưa link vào. Sau đó biểu diễn và lưu lại định dạng csv(?) có các trường sau: 'title', 'url', 'content', 'label'.
2. Lọc ra Bag-Of-Words từ content và biểu diễn sang định dạng vector[Text feature extraction](http://scikit-learn.org/stable/modules/feature_extraction.html# text-feature-extraction)
3. Thực hiện phân loại bằng nhiều phương pháp, đưa ra kết quả và thời gian để phân loại. (Sklearn)
4. So sánh và đưa ra nhận định về kết quả hiện có.
5. Ý tưởng: Xây dựng cho 1 trang web(Django, Flask...) có giao diện cho nhập link và chọn phương pháp phân loại.

# Tài liệu tham khảo.

1. [Sklearn](http://scikit-learn.org/) - -> [Must read](http://scikit-learn.org/stable/tutorial/basic/tutorial.html)
2. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. [Scrapy](https://scrapy.org/)
4. [Multiclass classification - Concept](https://en.wikipedia.org/wiki/Multiclass_classification)
5. [Multiclass classification - Sklearn](http://scikit-learn.org/stable/modules/multiclass.html)
6. [Tunning the hyper - parameters of an estimator](http://scikit-learn.org/stable/modules/grid_search.html# grid-search)
