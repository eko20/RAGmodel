import pandas as pd

#CSV dosyasını kontrol eder eksik veya bozuk data var ise gösterir

# CSV dosyasını okuma
def load_csv(file_path):
    return pd.read_csv(file_path)

# CSV dosyasını yükleme
df = load_csv("parsed_log_data.csv")
print(df.head())  # İlk birkaç satırı görüntüleme

# Eksik verileri kontrol etme
print(df.isnull().sum())

# Eksik verileri doldurma veya silme
df = df.dropna()  # Eksik verileri içeren satırları silme

# Veri türlerini düzeltme
df['size'] = pd.to_numeric(df['size'], errors='coerce')  # 'size' sütununu sayıya dönüştür

# Durum kodlarının dağılımı
status_counts = df['status'].value_counts()
print(status_counts)

# En çok erişilen sayfalar
top_requests = df['request'].value_counts().head(10)
print("most visited sites \n")
print(top_requests)

