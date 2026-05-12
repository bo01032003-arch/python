menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhap so tien X = "))

tong_to = 0
so_to = []

temp = x

# Đổi tiền
for gia in menh_gia:
    to = temp // gia
    temp %= gia

    so_to.append(to)
    tong_to += to

# In kết quả
print(f"\nSo tien {x} duoc doi thanh:")

for i in range(len(menh_gia)):
    print(f"Loai {menh_gia[i]} gom {so_to[i]} to")

print(f"TONG CONG CO {tong_to} TO")