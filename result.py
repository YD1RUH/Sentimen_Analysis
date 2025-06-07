import pandas as pd

# Path file CSV
csv_path = r'.\sentimen_output.csv'

# Baca CSV
df = pd.read_csv(csv_path)

# Tampilkan kolom yang terbaca
print("Kolom terbaca:", df.columns)

# Bersihkan spasi di nama kolom (jika ada)
df.columns = df.columns.str.strip()

# Konversi kolom sentiment ke numerik
df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')

# Hitung total bilangan positif
total_positif = df.loc[df['sentiment'] > 0, 'sentiment'].sum()

# Hitung total bilangan negatif
total_negatif = df.loc[df['sentiment'] < 0, 'sentiment'].sum()

# Hitung jumlah baris yang bernilai 0
jumlah_netral = (df['sentiment'] == 0).sum()

# Hitung total baris yang diproses
total_data = len(df)

# Tampilkan hasil
print(f"\nTotal bilangan positif: {total_positif}")
print(f"Total bilangan negatif: {total_negatif}")
print(f"Jumlah sentimen netral (0): {jumlah_netral}")
print(f"Total data sentiment yang diproses: {total_data}")
