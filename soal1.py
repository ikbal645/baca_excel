import pandas as pd

# Langkah 1: Baca file Excel asli
file_path = 'data_penjualan.xlsx'  
data = pd.read_excel(file_path)

# Langkah 2: Ambil 5 baris pertama
first_five_rows = data.head()

# Langkah 3: Simpan ke file Excel baru
output_file = '5_baris_pertama.xlsx'
first_five_rows.to_excel(output_file, index=False)

print(f"Data berhasil disimpan ke dalam file: {output_file}")