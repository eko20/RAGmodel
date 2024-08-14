import random
import datetime

#rastgele log datası oluşturur

# Rastgele ip adresi üretimi
def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Rastgele zaman damgası üretimi, gün de dahil olmak üzere
def generate_timestamp():
    current_time = datetime.datetime.now()
    time_offset = random.randint(0, 100000)  # Rastgele bir zaman farkı ekle
    random_time = current_time - datetime.timedelta(seconds=time_offset)
    random_day = random.randint(1, 28)  
    return random_time.strftime(f'{random_day}/%b/%Y:%H:%M:%S +0000')

# Rastgele HTTP metodu ve URL üretimi
def generate_request():
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    urls = ['/index.html', '/about.html', '/contact.html', '/login', '/pricing.html', '/services.html', '/products.html']
    method = random.choice(methods)
    url = random.choice(urls)
    return f'"{method} {url} HTTP/1.1"'

# Rastgele HTTP yanıt kodu ve veri boyutu üretimi
def generate_status_and_size():
    statuses = [200, 302, 404, 500]
    status = random.choice(statuses)
    size = random.randint(200, 5000)  
    return f"{status} {size}"

# Rastgele User-Agent üretimi
def generate_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    ]
    return random.choice(user_agents)

# Log dosyasını oluşturma
def generate_log_file(file_name, num_lines):
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            ip = generate_ip()
            timestamp = generate_timestamp()
            request = generate_request()
            status_and_size = generate_status_and_size()
            user_agent = generate_user_agent()
            log_entry = f"{ip} - - [{timestamp}] {request} {status_and_size} \"-\" \"{user_agent}\"\n"
            file.write(log_entry)

# 10,000 satırlık bir log dosyası oluştur
generate_log_file("log_file.log", 10000)
