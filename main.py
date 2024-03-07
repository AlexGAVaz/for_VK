from collections import Counter

def find_top_10_src_ips_with_500_status(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            src_ips = []
            for line in file:
                # Разделяем каждую строку по ';' и проверяем статус
                parts = line.strip().split(';')
                if len(parts) > 2 and parts[2] == '500':
                    src_ips.append(parts[0])

            # Считаем количество появлений каждого IP
            src_ip_counts = Counter(src_ips)

            # Получаем 10 наиболее часто встречающихся SRC IP с ошибкой 500 и инвертируем список
            top_10_ips = src_ip_counts.most_common(10)
            top_10_ips.reverse()

            return top_10_ips
    except FileNotFoundError:
        print(f"Файл {log_file_path} не найден.")
        return []

# Путь к файлу лога
log_file_path = 'access.log'
top_10_src_ips = find_top_10_src_ips_with_500_status(log_file_path)

for i, (ip, count) in enumerate(top_10_src_ips, 1):
    print(f"{i}. IP: {ip}, Количество: {count}")
