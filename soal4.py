import pandas as pd

# Membaca file Excel
file_path = "5_baris_dengan_total.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Sheet1')

# Mengelompokkan dan menghitung total pendapatan per kategori
rekap_penjualan = df.groupby("Kategori")["Total Harga"].sum().reset_index()
rekap_penjualan.columns = ["Kategori", "Total Pendapatan"]

# Menyimpan ke file Excel baru
output_path = "rekap_penjualan_per_kategori.xlsx"
rekap_penjualan.to_excel(output_path, index=False)

print(f"File disimpan sebagai: {output_path}")
