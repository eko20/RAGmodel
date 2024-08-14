
## Proje Açıklaması

Bu proje, log verilerini işleyerek TF-IDF vektörleri oluşturur ve bu vektörler arasında FAISS kütüphanesi kullanarak arama yapar. Ayrıca, OpenAI GPT modelini kullanarak anlamlı yanıtlar üretir.

## Özellikler

- **TF-IDF Vektörleştirme:** Log verilerinden TF-IDF vektörleri oluşturur.
- **FAISS Arama:** TF-IDF vektörleri arasında hızlı ve etkili arama yapar.
- **GPT Entegrasyonu:** Sorgulara göre GPT modelini kullanarak anlamlı yanıtlar üretir.
- **Terminal Entegrasyonu:** Terminal üzerinden kullanıcı ile etkileşim sağlar.
- Example log ve logdan dönüştürülmüş CSV dosyası yüklenmiştir

## Gereksinimler

- Pandas
- scikit-learn
- FAISS
- OpenAI Python Client
- regex

## Gereksinimleri kurup main.py dosyasını çalıştırmak test için yeterli olucaktır

## Örnekler
![image](https://github.com/user-attachments/assets/4e153eca-a8bf-4de5-9aa9-9c889152ab70)
Örnekte görüldüğü gibi, gelen soruya uygun verileri seçerek GPT modeline gönderdi ve doğru sonuç elde etti

elde etmesini beklediğimiz sonuç:
90.181.164.84,22/Aug/2024:13:32:10 +0000,GET /contact.html HTTP/1.1,500,2503,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0

