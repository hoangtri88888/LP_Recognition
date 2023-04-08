# License-Plate-Recognition
Phương pháp mình giới thiệu lần này bao gồm 4 bước: <br>

* Xác định vùng chứa biển số xe sử dụng **Yolo v8** 
* Sử dụng thuật toán segment để tách từng kí tự trên biển số xe
* Xây dựng một model CNN để phân loại các kí tự(characters classification)
* Kết hợp thư viện paddel ocr để nhận diện biển số xe
* Định dạng lại biển số xe xác định biển số xe gồm một hay hai dòng.

## Install environments
```
pip install -r requirements.txt
Cài thủ công thêm yolov8 và ocr tùy từng hệ điều hành và phiên bản
```
Các bạn có thể chạy code trên google colab để tránh xung đột các thư viện
## Quick start
Các bạn có thể clone repo này về và chạy ngay bằng câu lệnh dưới đây. Trước đó b thay thế link_to_image bằng đường dẫn tới ảnh muốn đọc
```
python main.py --image_path=link_to_image 
```

## Kết quả
   Project nhận diện biển số xe này của mình có thể hoạt động trên cả biển một dòng hoặc hai dòng. Thậm chí đôi khi biển số xe bị che khuất một chút vẫn đọc được. :sunglasses:
   <p align="center" >
   <img src="https://images.viblo.asia/877154c3-929f-431c-a728-4a994acf6869.png" >
    Ảnh 4:  Kết quả
</p>

Tuy nhiên, nó vẫn có một số nhược điểm::worried:

* Khi ảnh đầu vào bị đặt một góc quá nghiên thì một vài kí tự sẽ bị nhầm dòng. Có một cách giải quyết là dùng một mạng transformer xoay ảnh nghiêng về ảnh thẳng.
* Đôi khi bị nhận dạng nhầm giữa 8 và B, 0 và D
*  Hoạt động kém khi bức ảnh quá mờ
* Kết quả thư viện ocr vẫn tốt hơn cnn
* Chỉ thích hợp với nhận diện biển số xe máy việt nam ở các tầng hầm chung cư mini dưới điều kiện ánh sáng phù hợp
* Chưa tốt khi tham gia dự đoán các biển số xe chạy ngoài trời.
