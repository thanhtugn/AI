# #Bai 1: Cho mang X = [[ 1., -1.,  2.],
# #                       [ 2.,  0.,  0.],
# #                       [ 0.,  1., -1.]]
# # Thực hiện data transform với 2 kỹ thuật Normalization & Standardization



# import numpy as np

# # Khởi tạo X
# X = np.array([[1., -1., 2.],
#               [2., 0., 0.],
#               [0., 1., -1.]])

# # Normalization - Min-Max Normalization
# min_val = np.min(X)
# max_val = np.max(X)
# normalized_X_minmax = (X - min_val) / (max_val - min_val)

# # Normalization - Z-Score Normalization
# mean_val = np.mean(X)
# std_dev = np.std(X)
# normalized_X_zscore = (X - mean_val) / std_dev

# # Standardization - Z-Score Standardization
# standardized_X = (X - mean_val) / std_dev

# print("Normalized (Min-Max):")
# print(normalized_X_minmax)
# print("")

# print("Normalized (Z-Score):")
# print(normalized_X_zscore)
# print("")

# print("Standardized (Z-Score):")
# print(standardized_X)


import pandas as pd
from sklearn.impute import KNNImputer, IterativeImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Đọc dữ liệu từ file csv
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv'
df = pd.read_csv(url)

# Xử lý missing data bằng phương pháp KNN Imputation
imputer = KNNImputer(n_neighbors=5)
df_filled_knn = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Xử lý missing data bằng phương pháp Iterative Imputation
imputer = IterativeImputer()
df_filled_iter = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Chuyển đổi dữ liệu từ string thành integer
df_filled_knn = df_filled_knn.astype(int)
df_filled_iter = df_filled_iter.astype(int)

# Loại bỏ dữ liệu trùng
df_filled_knn = df_filled_knn.drop_duplicates()
df_filled_iter = df_filled_iter.drop_duplicates()

# Thực hiện Normalization
scaler = MinMaxScaler()
normalized_knn = pd.DataFrame(scaler.fit_transform(df_filled_knn), columns=df.columns)

# Thực hiện Standardization
scaler = StandardScaler()
standardized_iter = pd.DataFrame(scaler.fit_transform(df_filled_iter), columns=df.columns)

