# Скрипт копирования и вставки пинов
# Установить модули, отфильтровать точки в 1С и выделить строку с первой точкой
# pip install pyautogui
# pip install pyperclip
# pip install keyboard

import time
import pyautogui as pg
import pyperclip
import keyboard


# Функции
def save_point() -> None:
    """Функция сохранения точки."""
    time.sleep(0.3)
    pg.hotkey("ctrl", "enter")


def copy_name() -> 'str':
    """Функция копирования текста, передаваемой как аргумент функции."""
    pg.press("enter")
    time.sleep(1)
    pg.press("tab", presses=4, interval=0.3)
    time.sleep(0.3)
    pg.hotkey("ctrl", "c")
    print(pyperclip.paste())
    return pyperclip.paste()


def paste_pin() -> None:
    """Функция вставки пина."""
    for i in range (2):
        keyboard.press_and_release('shift+tab')
        time.sleep(0.3)
    time.sleep(0.3)
    pg.hotkey("ctrl", "v")


def main(tryes: int = 100):
    for item in range(tryes):
        print(f"Объект № {item}")
        print("Скопировано имя точки: ")
        copy_name()
        paste_pin()
        save_point()
        print("Точка сохранена\n")
        time.sleep(1)
        pg.press("down")  # переход на новую точку


if __name__ == '__main__':
    time.sleep(5)  # время для переключения в 1С
    main(200)
    pg.alert("Завершено", "Завершено")
