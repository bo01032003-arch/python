menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# a: số tiền cần trả
# b: số tiền khách đưa
a = int(input("Nhap so tien can thanh toan: "))
b = int(input("Nhap so tien khach dua: "))

# Trường hợp khách đưa thiếu
if a > b:
    print(f"Khach hang con thieu {a - b} dong")

# Trường hợp đưa đúng
elif a == b:
    print("Cam on khach hang. Hen gap lai!")

# Trường hợp cần thối tiền
else:
    tien_thoi = b - a

    print(f"\nSo tien can thoi lai: {tien_thoi}")
    print("Thoi lai bang:")

    tong_to = 0
    tong_loai = 0
    temp = tien_thoi

    for gia in menh_gia:
        so_to = temp // gia
        temp %= gia

        # Chỉ in loại tiền có số tờ > 0
        if so_to > 0:
            print(f"Loai {gia} gom {so_to} to")
            tong_loai += 1

        tong_to += so_to

    print(f"TONG CONG CO {tong_to} TO")
    print(f"Tong so loai = {tong_loai}")

    input("\nNhan Enter de ket thuc...")
    print("Cam on khach hang. Hen gap lai!")