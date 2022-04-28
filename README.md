làm theo các bước sau 
bước 1 : tạo 1 môi trường python=3.7
```
conda create -n crawl python==3.7

conda activate crawl
```

bước 2 install các lib

```
git clone https://github.com/Tdpro1612/crawl_tool.git
cd craw_tool
pip install -r requirement.txt
```

bước 3 tải phiên bản phù hợp với chrome
lên website https://sites.google.com/a/chromium.org/chromedriver/downloads

download và bỏ vào trong thư mục chromedrive
hd tại đây : 

bước 4 chỉnh sửa file config

bước 5 run 
mở vs code hoặc terminal lên 
cd vào thư mục craw_tool
run lệnh 
```
python action.py
```
