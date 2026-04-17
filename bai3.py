n = int(input("nhap so nguyen duong de tinh tong va tich: "))

tong = 0
tich = 1

temp = n

while temp > 0:
    digit = temp % 10
    tong += digit
    tich *= digit
    temp //= 10

print("tong: ",tong)
print("tich: ",tich)
