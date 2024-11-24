import random # Для работы с рандомными числами
import pyperclip  # Для работы с буфером обмена

# Символы
symbols = (
    ['😀', '😂', '🙃', '🔥', '🌟', '💡', '🎉', '🚀', '❤️', '🍕'] +  # Эмодзи
    [chr(i) for i in range(0x0410, 0x044F)] +  # Кириллица
    [chr(i) for i in range(0x0600, 0x06FF)] +  # Арабский алфавит
    [chr(i) for i in range(0x0041, 0x005A)] + [chr(i) for i in range(0x0061, 0x007A)] +  # Латиница
    [str(i) for i in range(10)] +  # Числа
    ['@', '#', '$', '%', '&', '*', '!']  # Специальные символы
)
#Функция для генерации пароля
def generate_password(len=12):
    """
    Генерация пароля.
    :param len: длина пароля
    :return: строка с паролем
    """
    if len < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов.")
    return ''.join(random.choices(symbols, k=len))
#Основная функция программы
def main():
    print("Добро пожаловать в Генератор Паролей!")
    print("Вы получите уникальный и безопасный пароль")
    try:
        # Запрос длинны
        len = int(input("Введите длину пароля (минимум 6 символов): "))
        if len < 6:
            raise ValueError

        # Сгенерирован пароль
        password = generate_password(len)

        # Копировать в буфер обмена
        pyperclip.copy(password)

        # Выводим пароль и уведомляем о копировании
        print(f"Ваш пароль: {password}")
        print("✔ Пароль скопирован в буфер обмена.")
    except ValueError:
        print(" Ошибка: введите корректное число (6 или более).")
    except Exception as e:
        print(" Что-то пошло не так:")

if __name__ == "__main__":
    main()
