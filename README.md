# crawl_tool

## crawl data là gì?
- định nghĩa trên mạng crawl là 1 phương tiện giúp bạn lấy dữ liệu về máy tính
- còn đối với tôi nó là 1 công cụ giúp tôi lấy dữ liệu về máy tính thông qua phương thức lặp đi lặp lại 1 công việc đó là xác định vị trí element sau đó lấy nội dung của element về máy và sắp xếp theo 1 danh sách mà tôi cần 
```
ví dụ :
danh sách các loại động vật
```
![new](https://user-images.githubusercontent.com/61773507/147718604-e0cc6c30-643a-49cc-8767-d9c375ea3fc4.jpg)
```
kết quả sổ xố 
```
![new2](https://user-images.githubusercontent.com/61773507/147718755-e19300db-28c4-40cc-a010-990de6405f33.jpg)
## tool này có gì
- hướng dẫn bạn crawl các trang web,sắp xếp dữ liệu theo cách bạn cần bằng phần mềm selenium phiên bản 3.
- điều bạn cần làm là khai báo
```
khai báo url
khai bao số lần bạn muốn crawl
khai báo vị trí các element bạn cần crawl về
```
## bài viết sẽ hd crawl trong các trang đơn giản mà bạn thường thấy
- web thường
- facebook/twister(#youtube là trường hợp đặc biệt loại này)
- loại nhiều url
## let's go
### tool selenium crawl này có gì để giúp bạn duyệt trang web ?
- các thứ bạn thường sử dụng khi bạn làm trên web bao gồm click,điền vào vị trí nào đó sau đó enter,cuộn thanh cuốn trang web
```
click : khi bạn bấm vào 1 link nào đó hoặc 1 tab nào đó trên url web chính
điền vị trí : ví dụ như login,điền ngày tháng,điền từ cần tìm kiếm
cuộn thanh cuốn trang web như: load xuống dưới cùng của các trang youtube hay twister hay là load các comment
```
### vì lý do phức tạp nên mình chia loại crawl ra để mọi người điền cho dễ nhé
loại 1 : url thẳng : 1 cái vào là lấy data ngay không cần cuộn này nọ.web này là web thẳng
loại 2 : url vào login để crawl cần click hoặc scroll nhẹ
loại 3 : nhiều url nhập từ bên ngoài


```
form run
version 1 : 1 loop
configure.yaml have
HARD:
url
extension
scroll
LOOP:
number:
start:
xpath_?
SAVE:
name:
param:default
type:csv
run:
load HARD to open website
load SAVE to create path_save name data
before load LOOP
data=[]
columns=[?]
begin LOOP
for i in range(start,number) if have this
for i in range(len(?)):
    name_dict= ...
    name_dict[?]=val(?)
    data.append(name_dict)
df=pd.DataFrame(data,columns=columns)
write_type(path_save,df)
command line to run : python system.py
```