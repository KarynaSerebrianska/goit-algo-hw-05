import sys
from collections import defaultdict

from colorama import init, Fore, Style


#Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).


#для парсингу рядків логу.
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)  # Розділяємо на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:  #Якщо рядок некоректний (менше 4 частин), ми його пропускаємо.
        return None
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}

#для завантаження логів з файлу.
def load_logs(file_path: str) -> list: #Функція, яка завантажує лог-файл і повертає список логів у вигляді словників.
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    return logs


#для фільтрації логів за рівнем.
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log['level'] == level] #Фільтруємо список — залишаємо тільки ті логи, де рівень збігається з вказаним.


#для підрахунку записів за рівнем логування.
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] +=1
    return counts


#Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. + приймає результати виконання функції count_logs_by_level.
def display_log_counts(counts: dict):    #Функція, яка виводить підраховану статистику в гарному вигляді.
    print("\nРівень логування | Кількість")
    print("------------------|----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        count = counts.get(level, 0)

        if level == "ERROR":
            level_display = Fore.MAGENTA + level + Style.RESET_ALL
        else:
            level_display = level

        print(f"{level_display:<18}| {count}")

def display_filtered_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        date_colored = Fore.GREEN + log["date"] + Style.RESET_ALL
        print(f"{date_colored} {log['time']} - {log['message']}")

#main

def main():
    if len(sys.argv) < 2 :
        print("Usage: python log_parser.py <log_file_path> [log_level]")
        return
    
    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path) #Завантажуємо всі логи з файлу.

    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        display_filtered_logs(filtered_logs, filter_level)


#Виводимо відібрані рядки в гарному форматі.

        print(f"\nFiltered logs for level {filter_level.upper()}:")
        print("---------------------------------------------")
        for log in filtered_logs:
            print(f'{log["date"]} {log["time"]} {log["level"]} {log["message"]}')
        

        #Після всього — рахуємо загальну статистику та виводимо її через display_log_counts
    counts = count_logs_by_level(logs)
    display_log_counts(counts)


if __name__ == "__main__":
    main()

"""
наче так
"""