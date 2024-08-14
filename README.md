
## Proje Açıklaması

Bu proje, log verilerini işleyerek TF-IDF vektörleri oluşturur ve bu vektörler arasında FAISS kütüphanesi kullanarak arama yapar. Ayrıca, OpenAI GPT modelini kullanarak anlamlı yanıtlar üretir.

TF-IDF vektörleme yöntemi, kelimeleri frekanslarına göre vektörler. Bu vektörler daha sonra FAISS vektör veritabanına yüklenir. İstenilen soru üzerine veritabanında arama yapılır ve en yakın sonuçlar, ChatGPT API'si aracılığıyla anlamlı bir yanıt elde etmek üzere gönderilir. Bu vektörleme yöntemi, hızlı bir şekilde arama ve dönüştürme işlemleri sağlar.

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

![image](https://github.com/user-attachments/assets/3ebbcdf7-0cbf-4d26-be84-b7d69da446d0)

elde etmesini beklediğimiz sonuç yine doğrudur:
95.34.211.109,26/Aug/2024:21:03:41 +0000,PUT /contact.html HTTP/1.1,500,1819,"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"



