# Nhập dữ liệu
dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))2.
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dien_tich = dai * rong
the_tich = dien_tich * cao

# In kết quả (làm tròn theo số lẻ yêu cầu)
print(f"Diện tích đáy hình chữ nhật = {round(dien_tich, so_le)} cm^2")
print(f"Thể tích hình khối = {round(the_tich, so_le)} cm^3")