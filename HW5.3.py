import sys
import re
from typing import List, Dict, Callable

def parse_log_line(line: str) -> Dict:
    """Парсить рядок логу і повертає словник з компонентами."""
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[Dict]:
    """Завантажує лог-файл і повертає список парсених логів."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                logs.append(log_entry)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    """Фільтрує лог-записи за рівнем логування."""
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = {}
    for log in logs:
        level = log['level']
        if level not in counts:
            counts[level] = 0
        counts[level] += 1
    return counts

def display_log_counts(counts: Dict[str, int]) -> None:
    """Форматує та виводить результати підрахунку."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")

def main(file_path: str, filter_level: str = None) -> None:
    logs = load_logs(file_path)
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
        print()
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів як аргумент командного рядка.")
        sys.exit(1)
    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None
    main(file_path, filter_level)
