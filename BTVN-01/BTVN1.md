# Bài 1:
* Python là trình biên dịch hay trình thông dịch?
Python là sự kết hợp của cả hai dựa thên trình thông dịch. Đầu tiên, đoạn mã khi chạy được biên 
dịch ngầm sang bytecode (máy không thể hiểu trực tiếp). Sau đó máy ảo Python (PVM) đọc từng 
dòng Bytecode và dịch sang mã máy tương thích với hệ điều hành và phần cứng hiện tại và thực 
thi ngay lập tức.
* tại sao?
    1. Có thể chạy được trên mọi hệ điều hành mà không cần phải chỉnh sửa hay biên dịch lại cho 
từng nền tảng cụ thể. Miễn là máy có cài máy ảo Python
    2. Test và debug trực tiếp ngay lập tức mà không cần phải chờ trình biên dịch dịch toàn dự 
án sang mã máy mỗi khi sửa code, giúp tối ưu tốc độ làm ra sản phẩm.
    3. Có thể chạy Python trong môi trường tương tác như gõ lệnh trực tiếp trong Terminal, hoặc 
dùng Jupyter Notebook vì PVM thực thi mã theo từng dòng thông qua thông dịch.

# Bài 2:
1. Các kiểu dữ liệu trong Python:
    * Nhóm Số học:
    *int*: số nguyên
    *float*: số thực
    *complex*: số phức
    * Nhóm Văn bản:
    *Str*: đặt trong dấu nháy đơn hoặc kép (ví dụ: "Hello").
    * Nhóm Tuần tự:
    ***Dùng để lưu trữ một dãy các giá trị.***
    *list*: Dãy có thể thay đổi nội dung (ví dụ: [1, 2, 3]).
    *tuple*: Dãy cố định, không thể sửa đổi sau khi tạo (ví dụ: (1, 2, 3)).
    *range*: Trình tạo chuỗi số tự động thường dùng trong vòng lặp (ví dụ: range(5)).
    * Nhóm Ánh xạ:
    *dict* (từ điển): Lưu trữ dữ liệu theo cấu trúc cặp Khóa - Giá trị 
    (ví dụ: {"name": "Python", "age": 30}).
    * Nhóm Tập hợp:
    *set* và *frozenset*: Chứa các phần tử không trùng lặp và không duy trì thứ tự.
    * Khác:
    *bool*: chỉ nhận giá trị True hoặc False
    *NoneType*: None - đại diện cho sự vắng mặt của giá trị
2. Các toán tử trong Python:
    - **Toán tử Số học**:
    Các phép toán cơ bản gồm Cộng (+), Trừ (-), Nhân (*), Chia thực (/), Chia lấy phần nguyên (//), Chia lấy phần dư (%), và Lũy thừa ().
    - **Toán tử So sánh**:
    Đối chiếu 2 giá trị, bao gồm Bằng (==), Khác (!=), Lớn hơn (>), Nhỏ hơn (<), Lớn/nhỏ hơn hoặc bằng (>=, <=). Kết quả luôn trả về True hoặc False.
    - **Toán tử Gán**:
    Gán giá trị cho biến (=). Kết hợp với toán tử số học để viết gọn (+=, -=, *=, /=,... ví dụ: a += 1 tương đương với a = a + 1).
    - **Toán tử Logic**:
    Kết hợp các điều kiện với nhau gồm and (chỉ đúng khi tất cả đều đúng), or (đúng khi ít nhất một điều kiện đúng), và not (đảo ngược giá trị logic).
    - **Toán tử Thành viên**:
    Gồm in và not in. Dùng để kiểm tra xem một giá trị cụ thể có nằm bên trong một chuỗi, list, tuple hoặc dict hay không.
    - **Toán tử Nhận dạng**:
    Gồm is và is not. Dùng để kiểm tra xem hai biến có đang trỏ đến cùng một vùng nhớ trên máy tính hay không (khác với == chỉ so sánh giá trị bề mặt).
3. Mệnh đề điều kiện và vòng lặp:
    - **Mệnh đề rẽ nhánh** (Branching):
*Chương trình kiểm tra từ trên xuống và chạy khối lệnh đầu tiên thỏa mãn điều kiện.*
*if*: Khởi đầu một khối kiểm tra điều kiện.
*elif* (Else If): Các điều kiện bổ sung nếu if sai (có thể dùng nhiều elif).
*else*: Lựa chọn cuối cùng, chạy tự động nếu mọi điều kiện if và elif ở trên đều sai.
    - **Vòng lặp** (Loops):
*Dùng để tự động hóa các thao tác lặp đi lặp lại.*
*for*: Lặp qua một cấu trúc dữ liệu đã biết trước số lượng phần tử (như List, String, Range).
*while*: Lặp vô định chừng nào một điều kiện kiểm tra vẫn còn đúng (True).
    - **Các từ khóa kiểm soát luồng**:
*break*: Lập tức cắt đứt và thoát hoàn toàn khỏi vòng lặp.
*continue*: Bỏ qua các lệnh còn lại trong chu kỳ hiện tại và nhảy sang chu kỳ lặp tiếp theo.
*pass*: Lệnh giữ chỗ rỗng. Trình biên dịch sẽ bỏ qua lệnh này, dùng để tránh lỗi cú pháp khi cần tạo một hàm/vòng lặp nhưng chưa muốn viết code xử lý bên trong.
4. Kiểu dữ liệu True, False:
    - **Hai trạng thái duy nhất**:
Bắt buộc viết hoa chữ cái đầu tiên: **True** (Đúng) và **False** (Sai).
    - **Bản chất toán học**:
Dưới nền tảng, Python định nghĩa *True* có giá trị là 1 và *False* có giá trị là 0. Có thể tính toán trực tiếp như True + True = 2.
    - **Quy tắc Falsy và Truthy**:
*Khi đưa một biến vào lệnh điều kiện (ví dụ: if x:), Python tự động ép kiểu biến đó về Boolean:*
        + *Falsy* (Tự động hiểu là False):
    Đại diện cho sự "rỗng" hoặc "không". Bao gồm: số 0, 0.0, None, chuỗi rỗng "", [], (), {}.
        + *Truthy* (Tự động hiểu là True):
    Tất cả các giá trị còn lại không nằm trong nhóm Falsy (ví dụ: "abc", [1, 2], -5).