# 🧠 LỘ TRÌNH RE - CRACKMES.ONE EDITION

> **Mục tiêu**: Từ beginner → independent reverse engineer qua crackmes.one  
> **Timeline ước tính**: 3-6 tháng (tùy tốc độ học)

---

## 🟦 GIAI ĐOẠN 0 — Foundation Setup
### 🎯 Mục tiêu
Chuẩn bị môi trường và hiểu basic concepts trước khi bắt đầu

### 📚 Kiến thức cần có
**Assembly Basics:**
- Registers: rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp
- Instructions: mov, lea, add, sub, cmp, test, jmp, je/jne, call, ret
- Stack frame: push/pop, function prologue/epilogue

**Binary Concepts:**
- ELF format: sections (.text, .data, .rodata, .bss)
- Calling conventions: System V AMD64 ABI (Linux)
- String representation: null-terminated, ASCII/hex

**Tools Setup:**
- Ghidra/IDA Free: Decompiler chính
- gdb + gef/pwndbg: Dynamic analysis
- Linux utilities: file, strings, ltrace, strace, checksec

### 📖 Resources
- **Assembly**: "Programming from the Ground Up" (chapters 1-4)
- **Practice**: [godbolt.org](https://godbolt.org) - viết C, xem ASM output
- **Video**: LiveOverflow - "Binary Exploitation" series (ep 1-5)

### ✅ Checkpoint
- [ ] Đọc được simple assembly function và hiểu nó làm gì
- [ ] Biết dùng Ghidra để mở binary và tìm main()
- [ ] Chạy được gdb, đặt breakpoint, xem registers

### 🔍 Crackmes.one Search Params (Warm-up)
```
Difficulty between:     1 and 1
Quality between:        Any
Downloads between:      0 and any
Writeups between:       5 and any
Comments between:       0 and any
Size between:           any KB and 500 KB
Language:               C/C++
Arch:                   x86-64
Platform:               Unix/Linux etc.
Sort by:                Difficulty → Ascending
```

**Target**: 3-5 bài để làm quen workflow

**Keyword trong Crackme name/description:**
- "easy", "beginner", "tutorial", "simple", "first"

---

## 🟢 GIAI ĐOẠN 1 — Pattern Recognition
### 🎯 Mục tiêu
Nhận dạng nhanh các pattern cơ bản - "nhìn là biết"

### 🔍 Skills cần master
**Pattern Library:**
1. **String comparison**
   - strcmp() / strncmp()
   - memcmp()
   - Character-by-character loop

2. **Length checks**
   - strlen()
   - Fixed length validation

3. **Simple transformations**
   - XOR với constant
   - Character shifting (ROT13-style)
   - Reverse string

4. **Basic checksums**
   - Sum of characters
   - Simple hash functions

### 📊 Method
- **80% static analysis** (Ghidra decompiler)
- **20% dynamic** (chỉ để confirm)
- Viết lại logic bằng Python

### 🔍 Crackmes.one Search Params
```
Difficulty between:     1 and 2
Quality between:        3 and 6
Downloads between:      10 and any
Writeups between:       3 and any
Comments between:       0 and any
Size between:           any KB and 100 KB
Language:               C/C++
Arch:                   x86-64
Platform:               Unix/Linux etc.
Sort by:                Quality → Descending
```

**Keyword tìm kiếm:**
- "strcmp", "xor", "simple", "string"
- "password", "check", "validation"

**Tags cần tránh trong description:**
- "obfuscation", "anti-debug", "packer", "complex"

### 📈 Progress Tracking
Chia theo sub-categories (mỗi loại làm 2-3 bài):

- [ ] **Cat 1: strcmp-based** (3 bài)
- [ ] **Cat 2: XOR transformations** (3 bài)  
- [ ] **Cat 3: Character shifting** (2 bài)
- [ ] **Cat 4: Checksum validation** (2 bài)
- [ ] **Cat 5: Mixed patterns** (2-3 bài)

**Total: 12-15 bài**

### ✅ Checkpoint - Khi nào xong?
- [ ] Mở Ghidra → hiểu logic trong 5-10 phút
- [ ] Viết solver script không cần debug
- [ ] Nhìn loop thấy ngay: "À, đây là XOR từng byte"
- [ ] Không còn sợ pseudocode dài

### 🎓 Bài tổng hợp (Mini Boss)
```
Difficulty between:     2 and 2
Quality between:        4 and 6
Writeups between:       0 and 2 (ít người giải)
```
**Giải KHÔNG XEM writeup trước**

---

## 🟡 GIAI ĐOẠN 1.5 — Multi-Function Flow
### 🎯 Mục tiêu
Xử lý được control flow phức tạp hơn, nhiều hàm

### 🔍 Skills mới
**Control Flow:**
- Function call chains (A → B → C)
- Return value checking
- Basic state machines

**Data Structures:**
- Arrays và indexing
- Simple structs
- Buffer operations

**Loops:**
- for với counter rõ ràng
- while với exit condition đơn giản
- Nested loops (2 levels max)

### 📊 Method
- **60% static, 40% dynamic**
- Bắt đầu dùng gdb breakpoint để trace flow
- Vẽ call graph trên giấy

### 🔍 Crackmes.one Search Params
```
Difficulty between:     2 and 2
Quality between:        3 and 6
Downloads between:      5 and any
Writeups between:       2 and 20
Comments between:       0 and any
Size between:           any KB and 200 KB
Language:               C/C++
Arch:                   x86-64
Platform:               Unix/Linux etc.
Sort by:                Quality → Descending
```

**Keyword tìm kiếm:**
- "multiple", "array", "buffer", "loop"
- "function", "recursive" (tránh nếu quá phức tạp)

**Vẫn tránh:**
- "obfuscation", "vm", "anti-debug", "packed"

### 📈 Progress Tracking
- [ ] **2-3 functions chaining** (3 bài)
- [ ] **Array/buffer processing** (2 bài)
- [ ] **Nested loops** (2 bài)
- [ ] **State validation** (2 bài)

**Total: 8-10 bài**

### ✅ Checkpoint
- [ ] Trace được call flow qua 4-5 functions
- [ ] Không bị "lạc" trong nested loops
- [ ] Biết khi nào nên đặt breakpoint
- [ ] Hiểu được array indexing trong ASM

---

## 🟠 GIAI ĐOẠN 2 — Controlled Complexity
### 🎯 Mục tiêu
Xử lý được complexity cao hơn + anti-analysis nhẹ

### 🔍 Skills mới
**Advanced Control Flow:**
- Complex branching (switch-case với nhiều case)
- Recursive functions
- Function pointers
- Callback patterns

**Anti-Analysis Basics:**
- Junk instructions (NOP sled)
- Fake branches (always true/false)
- Simple opaque predicates
- Basic anti-debugging (ptrace check)

**New Techniques:**
- Binary patching (NOP out checks)
- Register tracing
- Conditional breakpoints trong gdb
- Scripting gdb với Python

### 📊 Method
- **50/50 static & dynamic**
- Bắt đầu patch binary để bypass checks
- Viết gdb scripts cho automation

### 🔍 Crackmes.one Search Params
```
Difficulty between:     2 and 3
Quality between:        4 and 6
Downloads between:      3 and any
Writeups between:       0 and 10
Comments between:       0 and any
Size between:           any KB and 500 KB
Language:               C/C++, Assembler
Arch:                   x86-64
Platform:               Unix/Linux etc., có thể thử Windows
Sort by:                Difficulty → Ascending
```

**Keyword tìm kiếm:**
- "anti-debug" (nhẹ), "obfuscation", "intermediate"
- "switch", "recursion", "complex"

**Có thể bắt đầu thử:**
- Platform: Windows (để làm quen PE format)
- Language: Assembler (inline ASM)

### 📈 Progress Tracking
- [ ] **Complex branching** (2 bài)
- [ ] **Recursion** (2 bài)
- [ ] **Anti-debug basic** (2 bài)
- [ ] **Patching practice** (2 bài)
- [ ] **Mixed complexity** (2 bài)

**Total: 10-12 bài**

### ✅ Checkpoint
- [ ] Bypass được ptrace check bằng patch/gdb
- [ ] Trace được recursive function
- [ ] Viết được gdb script đơn giản
- [ ] Không hoảng với switch-case lớn

### 🎓 Bài tổng hợp (Boss Level)
```
Difficulty between:     3 and 3
Quality between:        4 and 6
Writeups between:       0 and 3
Platform:               Windows (thử format mới)
```
**Time limit: Tối đa 2 ngày**

---

## 🔴 GIAI ĐOẠN 3 — Independent Reverse Engineer
### 🎯 Mục tiêu
Tự giải bài mới, không lệ thuộc writeup, tư duy độc lập

### 🔍 Skills mới
**Advanced Topics:**
- Custom encoding schemes
- Crypto basics (AES, RC4 implementations)
- VM-based obfuscation (nhẹ)
- Table-driven algorithms
- Self-modifying code
- Packer/unpacker basics

**Advanced Tools:**
- Ghidra scripting (Python/Java)
- angr/Z3 cho symbolic execution
- Frida cho dynamic instrumentation
- IDAPython (nếu có IDA Pro)

**Mindset Shift:**
- Không còn "giải nhanh"
- Research-driven: tự tìm techniques
- Viết tools riêng cho từng bài
- Document quá trình (writeup habit)

### 📊 Method
- **Strategy-first approach**: Plan trước khi làm
- Time-boxing: 1-3 ngày/bài, có thể lâu hơn
- Học từ failures: Stuck? Xem 1 hint, rồi tự làm tiếp

### 🔍 Crackmes.one Search Params

**Phase 3A - Advanced Techniques:**
```
Difficulty between:     3 and 4
Quality between:        4 and 6
Downloads between:      0 and any
Writeups between:       0 and 5
Comments between:       0 and any
Size between:           any KB and 2 MB
Language:               Any
Arch:                   x86-64, ARM (thử kiến trúc mới)
Platform:               Any
Sort by:                Quality → Descending
```

**Keyword:**
- "crypto", "encryption", "vm", "obfuscation"
- "custom", "algorithm", "keygen"

**Phase 3B - Tool Mastery:**
```
Difficulty between:     3 and 5
Quality between:        3 and 6
Writeups between:       0 and 3
Language:               Assembler, C/C++
Platform:               Multiplatform (thử nhiều OS)
```

**Keyword:**
- "packed", "protected", "anti-disassembly"
- "advanced", "hard", "challenge"

**Phase 3C - Expert Level:**
```
Difficulty between:     4 and 6
Quality between:        4 and 6
Downloads between:      0 and any
Writeups between:       0 and 1
Sort by:                Difficulty → Descending
```

### 📈 Progress Tracking

**Phase 3A - Advanced Techniques (5-7 bài):**
- [ ] Custom encoding scheme (2 bài)
- [ ] Crypto implementation (1-2 bài)
- [ ] VM obfuscation light (1-2 bài)
- [ ] Table lookups (1 bài)

**Phase 3B - Tool Mastery (3-5 bài):**
- [ ] Ghidra script để deobfuscate (1 bài)
- [ ] angr/Z3 solver (1-2 bài)
- [ ] Frida hooking (1 bài)
- [ ] Multi-platform (Windows + Linux) (1 bài)

**Phase 3C - Integration (ongoing):**
- [ ] Giải bài 3.5★+ không hints
- [ ] Viết full writeup cho 2 bài
- [ ] Giải 1 bài 4★+ (có thể mất 1 tuần)
- [ ] Thử ARM/MIPS architecture (1 bài)

### ✅ Checkpoint - "RE Thật Sự"
- [ ] Giải được bài 0 writeups trên crackmes.one
- [ ] Viết được keygen hoàn chỉnh (không chỉ bruteforce)
- [ ] Tự tìm được tools/techniques mới khi stuck
- [ ] Đọc writeup người khác và hiểu sâu approach
- [ ] Nhìn ASM không còn overwhelmed
- [ ] Có thể RE trên nhiều platforms (Linux, Windows, Android)

### 🏆 Final Boss (Optional)
Chọn 1 trong:
```
Search params cho Final Boss:
Difficulty between:     5 and 6
Quality between:        5 and 6
Writeups between:       0 and 0
```

Hoặc:
- **Malware RE**: Phân tích 1 malware sample thật (từ malware bazaar)
- **CTF Challenge**: Giải rev challenge từ CTF rating cao (300+ points)
- **Real Software**: Keygen cho 1 phần mềm thật (legally, for learning)

---

## 📊 STRATEGY GUIDE CHO TỪ GIAI ĐOẠN

### 🎯 Giai đoạn 1: Sort by Quality
**Tại sao?** 
- Bài quality cao = code clean, logic rõ ràng
- Dễ học patterns đúng
- Không bị mislead bởi broken challenges

**Cách search:**
```
Sort by: Quality → Descending
Filter: Difficulty 1-2, Quality ≥3
```

### 🎯 Giai đoạn 1.5-2: Sort by Difficulty
**Tại sao?**
- Cần progression tăng dần
- Tránh nhảy cóc độ khó

**Cách search:**
```
Sort by: Difficulty → Ascending
Filter từ thấp lên cao trong range
```

### 🎯 Giai đoạn 3: Sort by Quality hoặc Downloads
**Tại sao?**
- Quality cao = worth spending time
- Downloads thấp = ít người giải = thử thách thật

**Strategy:**
```
Lần 1: Sort by Quality → chọn bài chất lượng
Lần 2: Sort by Downloads → tìm hidden gems (0-5 downloads)
```

---

## 💡 TIPS SỬ DỤNG CRACKMES.ONE SEARCH

### 🔍 Filter Combinations Hiệu Quả

**Tìm bài cho beginners:**
```
Difficulty: 1-2
Quality: 4-6
Writeups: 5-any (có thể tham khảo khi stuck)
Size: <100KB
```

**Tìm bài challenge (không quá dễ):**
```
Difficulty: 2-3
Quality: 4-6
Writeups: 0-3 (ít người giải)
Downloads: 0-20
```

**Tìm hidden gems (quality tốt nhưng ít người biết):**
```
Quality: 4-6
Downloads: 0-10
Writeups: 0
Sort by: Quality
```

### 📊 Đọc Metrics Như Thế Nào?

**Downloads:**
- >100: Popular, có nhiều resources
- 10-50: Vừa phải, community support ok
- <10: Fresh hoặc niche, thử thách

**Writeups:**
- >5: Có nhiều cách giải, học được nhiều
- 1-5: Sweet spot - có hint nhưng vẫn thử thách
- 0: True challenge, cần tư duy độc lập

**Comments:**
- >10: Active discussion, có thể tìm hints
- 0-5: Ít người comment, tự lực
- Check comments trước khi download để tránh broken challenges

### 🚫 Red Flags (Tránh Ở Giai Đoạn Đầu)

**Quality < 2:**
- Có thể broken, poorly designed
- Không educational value

**Size > 5MB ở Difficulty 1-2:**
- Thường là packer/joke challenge
- Không phù hợp learning

**Keyword trong description:**
- "Impossible", "troll", "joke"
- "Unsolvable" (trừ khi bạn muốn research)

**Comments có:**
- "Broken", "doesn't work", "impossible to solve"
- "Requires specific environment" (nếu bạn chưa có)

---

## 📈 TIMELINE & PROGRESS TRACKING

### Tuần 0-2: Foundation
```
Search: Difficulty 1, Quality any, Writeups >10
Target: 3-5 bài warm-up
```

### Tuần 3-6: Pattern Recognition
```
Search: Difficulty 1-2, Quality 3-6, Writeups 3-any
Target: 12-15 bài (3 bài/tuần)
Strategy: Sort by Quality
```

### Tuần 7-9: Multi-Function
```
Search: Difficulty 2, Quality 3-6, Writeups 2-20
Target: 8-10 bài (3 bài/tuần)
Strategy: Sort by Difficulty
```

### Tuần 10-14: Controlled Complexity
```
Search: Difficulty 2-3, Quality 4-6, Writeups 0-10
Target: 10-12 bài (2-3 bài/tuần)
Strategy: Mix platforms
```

### Tháng 4-6+: Independent
```
Search: Difficulty 3-6, Quality 4-6, Writeups 0-5
Target: Không đếm bài, đếm skills
Strategy: 1 bài khó > 5 bài dễ
```

---

## 🛠️ WORKFLOW CHO MỖI BÀI

### 1. Pre-Download Checks (2 phút)
- [ ] Check quality rating
- [ ] Đọc description (không spoil solution)
- [ ] Check comments cho broken/requirements
- [ ] Verify platform & architecture match

### 2. Download & Initial Analysis (10 phút)
```bash
file crackme
strings crackme | less
checksec crackme
./crackme  # xem behavior
```

### 3. Static Analysis (30-60 phút)
- [ ] Load vào Ghidra
- [ ] Tìm main/entry point
- [ ] Identify functions of interest
- [ ] Pseudocode analysis

### 4. Dynamic Analysis (30+ phút)
```bash
gdb ./crackme
ltrace ./crackme
strace ./crackme
```

### 5. Solution & Documentation (30 phút)
- [ ] Write solver/keygen
- [ ] Document approach
- [ ] Note patterns learned
- [ ] Save for future reference

### 6. Post-Solve Review
- [ ] Xem writeups khác (nếu có) - học cách khác
- [ ] So sánh approach
- [ ] Update notes với insights mới

---

## 🎓 RESOURCES & COMMUNITY

### Crackmes.one Resources
- **Discord**: Join để hỏi hints (không spoilers)
- **Writeups section**: Học approach sau khi solve
- **Comments**: Hidden hints từ community

### External Learning
- **Ghidra**: Official documentation & training
- **Assembly**: Intel manual, online tutorials
- **RE Blogs**: ired.team, malwareunicorn, gynvael

### Practice Platforms (khi cần variety)
- **Pwnable.kr**: Reverse + exploitation
- **Reversing.kr**: Korean challenges (quality tốt)
- **CTFtime**: Live CTF competitions

---

## 🚀 BẮT ĐẦU NGAY - FIRST SEARCH

### Checklist Setup:
- [ ] Tạo account crackmes.one
- [ ] Setup VM Linux (Ubuntu/Kali)
- [ ] Install: Ghidra, gdb-gef, basic tools

### First Search Query:
```
Crackme name:           [leave blank]
Author:                 [leave blank]
Difficulty between:     1 and 1
Quality between:        4 and 6
Downloads between:      20 and any
Writeups between:       5 and any
Comments between:       0 and any
Size between:           any KB and 50 KB
Language:               C/C++
Arch:                   x86-64
Platform:               Unix/Linux etc.
Sort by:                Quality → Descending
```

**Click Search → Pick bài đầu tiên có rating tốt → Download → Bắt đầu!**

---

*Lưu search params cho từng giai đoạn để reuse!*  
*Roadmap là guideline - adjust theo progress thực tế của bạn!*