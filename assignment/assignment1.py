import pandas as pd

#Excel
df_excel = pd.read_excel("Sales.xlsx")

#Get number of rows and columns 
rows_excel, columns_excel = df_excel.shape
print(f"Number of rows (Excel): {rows_excel}")
print(f"Number of columns (Excel): {columns_excel}")

#Get index 
index_excel = df_excel.index
print(f"Index (Excel): {index_excel}")

#Get list of columns name 
columns_excel_list = df_excel.columns
print(f"Columns (Excel): {columns_excel_list}")

#CSV
df_csv = pd.read_csv("data.csv")

#Get number of rows and columns 
rows_csv, columns_csv = df_csv.shape
print(f"Number of rows (CSV): {rows_csv}")
print(f"Number of columns (CSV): {columns_csv}")

#Get index 
index_csv = df_csv.index
print(f"Index (CSV): {index_csv}")

#Get list of columns name 
columns_csv_list = df_csv.columns
print(f"Columns (CSV): {columns_csv_list}")
