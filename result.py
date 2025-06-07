import pandas as pd

# Path CSV input
csv_path = r'.\sentimen_output.csv'

# Baca file CSV
df = pd.read_csv(csv_path)

# Tambahkan kolom label
def get_sentiment_label(score):
    if score < 0:
        return 'negatif'
    elif score == 0:
        return 'netral'
    else:
        return 'positif'

# Pastikan sentiment numeric
df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')

# Tambahkan kolom label
df['label'] = df['sentiment'].apply(get_sentiment_label)

# Tampilkan hasil
print(df[['sentiment', 'comment', 'label']])

# Simpan output ke CSV baru
output_path = r'.\sentimen_output_labeled.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"\nFile output sudah disimpan di: {output_path}")

# Hitung dan tampilkan ringkasan
positif_count = (df['label'] == 'positif').sum()
netral_count = (df['label'] == 'netral').sum()
negatif_count = (df['label'] == 'negatif').sum()

print("\nKesimpulan:")
print(f"positif: {positif_count}")
print(f"netral: {netral_count}")
print(f"negatif: {negatif_count}")
