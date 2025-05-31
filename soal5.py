import pandas as pd

# Membaca file Excel
file_path = "5_baris_dengan_total.xlsx"  
xls = pd.ExcelFile(file_path)

# Memuat data dari Sheet1
df = xls.parse('Sheet1')

# Mengurutkan data berdasarkan Total Harga (dari terbesar ke terkecil)
df_sorted = df.sort_values(by="Total Harga", ascending=False)

# Menyimpan data yang telah diurutkan ke file Excel baru
output_path = "penjualan_terurut.xlsx"
df_sorted.to_excel(output_path, index=False)

print(f"File berhasil disimpan sebagai: {output_path}")