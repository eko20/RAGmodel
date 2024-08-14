import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
from openai import OpenAI
import os

# main fonksiyonu, CSV verilerini vektörlere dönüştürür. Ardından, vektörler arasında sorulan soruya göre 
# arama yapar ve ilgili logları ChatGPT'ye gönderir. Terminal aracılığıyla GPT ile etkileşim sağlar.



# CSV dosyasını okuma
df = pd.read_csv("parsed_log_data.csv")

# 'request' sütununa odaklanma
requests = df.astype(str).agg(' '.join, axis=1)

# TF-IDF vektörizer'ı oluştur
vectorizer = TfidfVectorizer()

# Verileri vektörleştir
tfidf_matrix = vectorizer.fit_transform(requests)

# TF-IDF matrisini numpy array'e çevir
tfidf_vectors = tfidf_matrix.toarray()

# Vektör boyutunu al
dimension = tfidf_vectors.shape[1]

# FAISS Index'i oluştur (L2 normu kullanarak)
index = faiss.IndexFlatL2(dimension)

# Vektörleri FAISS indexine ekle
index.add(tfidf_vectors)


client = OpenAI(api_key="")

def search_documents(query, top_k=3):
    # Sorguyu TF-IDF vektörüne dönüştür
    query_vector = vectorizer.transform([query]).toarray()
    
    # FAISS ile en yakın vektörleri bul
    distances, indices = index.search(query_vector, top_k)
    
    # Sonuçları döndür
    results = []
    for i in range(len(indices[0])):
        if indices[0][i] < len(requests):
            results.append((requests[indices[0][i]], distances[0][i]))
    return results

def generate_augmented_response(query):
    search_results = search_documents(query)
    context = "\n".join([result[0] for result in search_results])
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": context},
            {"role": "user", "content": query}
        ]
    )
    
    return completion.choices[0].message.content

# Terminal tabanlı sürekli sorgulama döngüsü
while True:
    query = input("Question (type 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    print("GPT'ye gönderilen loglar:")
    print(search_documents(query))
    print("\n")
    
    response = generate_augmented_response(query)
    print(f"Cevap: {response}")
