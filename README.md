# Phân loại các trang web.

## Hướng dẫn sử dụng.


1. Môi trường thử nghiệm:

    - Hệ điều hành Ubuntu - Linux nói chung.

    - Cài đặt git và pip3.

	    ```
        $ sudo apt install git python3-dev python3-pip -y
	    ```

    - Python 3.x.

2. Cài đặt các package cần thiết:

	```
    $ git clone https://github.com/ntk148v/web_classification
    $ cd web_classification/
    $ sudo -H pip3 install -r requirements.txt
	```

3. Cấu hình các config cơ bản trong file `classification/conf.py`

4. Tiến hành training, khi này chương trình sẽ tiến hành training (fit) cho
   từng estimator (SVM, K-NN). Sau đó, lưu object class Classifier() vào file
   .pickle trong thư mục `classification/saved/`, nhằm mục đích tái sử dụng,
   tránh tốn thời gian và tài nguyên.

	```
    $ python3 example.py
	```

5. Về giải thuật được mô phỏng bằng code python (không sử dụng sklearn), tiến
   hành checkout nhánh __algorithms__.

	```
    $ git checkout -b algorithms
	```

6. Chạy giao diện hệ thống (Khi này, các file pickle đã được lưu sau khi
   training sẽ được tái sử dụng).
