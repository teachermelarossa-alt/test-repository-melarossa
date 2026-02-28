import time
import os
import random

def clear_screen():
    """Очистка консоли (для красоты анимации)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_star():
    """Рисует красивую звезду"""
    star = [
        "    ★    ",
        "   ★★★   ",
        "  ★★★★★  ",
        " ★★★★★★★ ",
        "★★★★★★★★★",
        "    ★    ",
        "   ★ ★   ",
        "  ★   ★  ",
        " ★     ★ ",
        "★       ★"
    ]
    return star

def draw_tank():
    """Рисует танк"""
    tank = [
        "       ██      ",
        "      ████     ",
        "     ██████    ",
        "████████████████",
        "████████████████",
        "  ██      ██   ",
        " ████    ████  ",
        "██████  ██████ "
    ]
    return tank

def animate_text(text, delay=0.1):
    """Анимированный вывод текста"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_firework():
    """Создаёт эффект фейерверка"""
    fireworks = [
        "      ✦       ",
        "     ✦✦✦      ",
        "    ✦✦✦✦✦     ",
        "   ✦✦✦✦✦✦✦    ",
        "  ✦✦✦✦✦✦✦✦✦   ",
        "     ✦ ✦      ",
        "    ✦   ✦     ",
        "   ✦     ✦    ",
        "  ✦       ✦   "
    ]
    return random.choice(fireworks)

def main():
    # Цвета для консоли (работает в Linux/Mac, в Windows может отображаться иначе)
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    
    try:
        # Пробуем использовать цвета
        test_color = colors['red'] + 'test' + colors['end']
    except:
        # Если не работает, используем пустые строки
        for key in colors:
            colors[key] = ''
    
    clear_screen()
    
    # Заголовок
    print(colors['bold'] + colors['red'])
    animate_text("С 23 ФЕВРАЛЯ!", 0.1)
    
    # Рисуем звезду
    print(colors['yellow'])
    star_lines = draw_star()
    for line in star_lines:
        print(" " * 10 + line)
        time.sleep(0.05)
    
    time.sleep(0.5)
    
    # Рисуем танк
    print(colors['green'])
    tank_lines = draw_tank()
    for line in tank_lines:
        print(" " * 8 + line)
        time.sleep(0.1)
    
    time.sleep(0.5)
    
    # Поздравление
    print(colors['cyan'] + colors['bold'])
    congratulations = [
        "Желаю силы, мужества, отваги,",
        "Чтоб покорялись новые вершины,",
        "Пусть ждут в жизни только благие шаги,",
        "И сбудутся заветные картины!",
        "",
        "Мирного неба над головой,",
        "Здоровья крепкого, удачи,",
        "Пусть будет счастлив путь земной,",
        "Решаются любые задачи!"
    ]
    
    for line in congratulations:
        print(" " * 5 + line)
        time.sleep(0.3)
    
    time.sleep(0.5)
    
    # Фейерверк
    print(colors['purple'])
    print("\n" + " " * 15 + create_firework())
    
    time.sleep(0.3)
    
    print(colors['red'])
    print(" " * 13 + "★" * 5)
    
    print(colors['yellow'])
    print("\n" + " " * 10 + "С ПРАЗДНИКОМ!")
    
    print(colors['end'])  # Сбрасываем цвета
    
    # Интерактивность
    print("\n" + "="*50)
    name = input("Введите имя защитника: ")
    if name:
        print(f"\n{colors['bold']}{colors['blue']}{name}, с праздником вас!{colors['end']}")

def fun_facts():
    """Интересные факты о 23 февраля"""
    facts = [
        "До 1949 года праздник назывался «День Красной армии»",
        "23 февраля 1918 года Красная армия одержала первые победы под Псковом и Нарвой",
        "С 2002 года 23 февраля - выходной день в России",
        "Этот праздник отмечают не только в России, но и в Беларуси, Таджикистане, Киргизии",
        "Первоначально праздник назывался «День Красного подарка»"
    ]
    
    print("\n" + "="*50)
    print("ИНТЕРЕСНЫЙ ФАКТ:")
    print(random.choice(facts))

if __name__ == "__main__":
    try:
        main()
        fun_facts()
        
        # Добавим интерактивный элемент
        print("\n" + "="*50)
        input("Нажмите Enter для запуска салюта...")
        
        # Мини-салют
        for i in range(5):
            clear_screen()
            print("\n" * random.randint(1, 5))
            print(" " * random.randint(10, 30) + "✦")
            time.sleep(0.1)
            print(" " * random.randint(10, 30) + "✦✦✦")
            time.sleep(0.1)
            print(" " * random.randint(10, 30) + "✦✦✦✦✦")
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        print("\n\nС праздником! :)")