import pandas as pd

# Đọc tập dữ liệu từ file CSV
df = pd.read_csv("Automobile_data.csv")

# 1. In ra năm hàng đầu tiên và cuối cùng
print("Năm hàng đầu tiên:")
print(df.head(5))



print("Năm hàng cuối cùng:")
print(df.tail(5))

# 2. Làm sạch tập dữ liệu
df.replace(["?", "n.a", "NaN"], pd.NA, inplace=True)

# Cập nhật vào tệp file CSV
df.to_csv("Automobile_data_cleaned.csv", index=False)

