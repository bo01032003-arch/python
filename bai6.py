s = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# chuẩn hoá về chữ thường để đếm cho chính xác
s = s.lower()
word = word.lower()

# tách thành từng từ
words = s.split()

count = 0
for w in words:
    if w.strip(".,") == word:
        count += 1

print(f"Số từ '{word}' là {count}")
s = input("Nhập chuỗi: ")

# 1. Xoá khoảng trắng đầu cuối
s = s.strip()

# 2. Xoá khoảng trắng dư thừa giữa các từ
while "  " in s:
    s = s.replace("  ", " ")

# 3. Xoá khoảng trắng trước dấu , .
s = s.replace(" ,", ",")
s = s.replace(" .", ".")

print("Chuỗi hoàn chỉnh:")
print(s)