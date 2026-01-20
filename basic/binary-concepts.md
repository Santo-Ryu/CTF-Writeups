![alt text](../images/binary-concepts.png)

---

# Binary - File nhị phân

## 1️⃣ Binary Concepts (Khái niệm cơ bản về file nhị phân)
Binary = file chứa machine code mà CPU có thể chạy trực tiếp.   
Trong RE, binary là đối tượng chính mà bạn phân tích
Một binary thường gồm:
- Code -> Lệnh CPU (machine code / instruction)
- Data -> Biến, hằng số
- Metadata -> Header, section info, relocation info

Ví dụ: file ELF trên Linux, PE trên Windows

`💡 Điều quan trọng: Bạn đọc binary bằng ASM, vì CPU không hiểu trực tiếp file .c hay .py, chỉ hiểu machine code.`

---

## 2️⃣ ELF format (Executable and Linkable Format – Linux)

ELF = chuẩn file nhị phân phổ biến trên Linux
ELF gồm nhiều section, mỗi section có mục đích riêng

| Section   | Chức năng                                                    |
| --------- | ------------------------------------------------------------ |
| `.text`   | Chứa **code / instructions** → machine code CPU chạy         |
| `.data`   | Chứa **biến global/initialized** → dữ liệu thay đổi được     |
| `.rodata` | Chứa **read-only data** → hằng số, chuỗi, literal            |
| `.bss`    | Chứa **biến global/uninitialized** → được zero-fill lúc load |

---

Ví dụ trực quan:
```
.text
  ; code của hàm main
.data
  x: dq 5        ; biến global khởi tạo
.rodata
  msg: db "Hi",0 ; hằng số string
.bss
  buf: resb 16   ; buffer chưa khởi tạo
```
Khi RE, bạn cần biết section nào chứa gì để phân tích code, dữ liệu, string.

---

## 3️⃣ Calling Conventions (System V AMD64 ABI – Linux)
Calling convention = cách CPU + OS truyền tham số, trả về, và sử dụng stack/register cho hàm.

Linux x86-64 dùng System V AMD64 ABI, quy tắc chính:

| Tham số | Register     |
| ------- | ------------ |
| 1       | rdi          |
| 2       | rsi          |
| 3       | rdx          |
| 4       | rcx          |
| 5       | r8           |
| 6       | r9           |
| >6      | Stack (push) |

- Return value: rax
- Caller-saved register: rax, rcx, rdx, rsi, rdi, r8-r11 -> caller cần lưu nếu muốn giữ 
- Callee-saved register: rbx, rbp, r12-r15 -> hàm được gọi phải phục hồi

---

`💡 Ứng dụng trong RE:`
- Khi đọc ASM → biết tham số truyền vào hàm nằm ở đâu
- Khi reverse một hàm → biết register nào là input, register nào output

---

## 4️⃣ String representation
Chuỗi trong binary thường lưu dưới dạng null-terminated (kết thúc bằng 0x00)

Encoding phổ biến: ASCII hoặc hex (nhìn dưới dạng byte)

Ví dụ ASCII / null-terminated:
```
msg: db "Hello", 0
```

- Trên memory → 0x48 0x65 0x6C 0x6C 0x6F 0x00
- Khi RE → nhìn thấy chuỗi → biết giá trị string, dùng trong printf, log, flag…

---

# TÓM TẮT
| Khái niệm                 | Chức năng / Mô tả                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| **Binary**                | File machine code, chạy trực tiếp trên CPU                                                    |
| **ELF sections**          | `.text`=code, `.data`=biến init, `.rodata`=hằng số, `.bss`=biến chưa init                     |
| **Calling conventions**   | Quy tắc truyền tham số/return value/register (System V AMD64 ABI: rdi, rsi, rdx, rcx, r8, r9) |
| **String representation** | Chuỗi null-terminated, thường ASCII, có thể đọc từ `.rodata`                                  |

---

`💡 Ghi nhớ RE:`
- .text → tìm code / lệnh ASM
- .data/.bss → tìm biến / buffer
- .rodata → tìm string, flag, hằng số
- Calling convention → biết tham số và giá trị trả về nằm ở đâu

