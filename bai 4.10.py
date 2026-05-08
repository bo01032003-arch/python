# iii
S = input("Nhập số điện thoại: ")

kq = []
for i in range(10):
    if str(i) not in S:
        kq.append(i)

print("Các số không xuất hiện là:", kq)
# iv
S = input("Nhập chuỗi: ")

ds = S.split()
da_gap = []

kq = None
for tu in ds:
    if tu in da_gap:
        kq = tu
        break
    da_gap.append(tu)

print(kq)