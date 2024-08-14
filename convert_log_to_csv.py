import re
import pandas as pd

#log dosyasını okur ve cvs'ye dönüştürür


# Log dosyasını okuma ve satır satır ayrıştırma
def parse_log_file(file_name):
    log_data = []
    log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "-" "(?P<user_agent>[^"]+)"')

    with open(file_name, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                log_entry = match.groupdict()
                log_data.append(log_entry)
    
    return log_data

# Log dosyasını analiz etme
log_data = parse_log_file("log_file.log")

# Örnek bir kaç kayıt göster
def save_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

save_to_csv(log_data, "parsed_log_data.csv")
