import time

# Данные одного самолёта
flight = "AAL101"
altitude = 9000  # Высота
fuel = 5        # Топливо (количество ходов)
score = 0
dop_fuel = 1

print("=== АЭРОПОРТ МАЙАМИ: ДИСПЕТЧЕР ===")
print(f"К вам на посадку заходит рейс {flight}!\n")

while True:
    print("-" * 40)
    print(f"Самолёт: {flight}")
    print(f"Высота:  {altitude} ft")
    print(f"Топливо: {fuel} ходов")
    print("-" * 40)

    # 1. Проверка на катастрофу
    if fuel <= 0 and altitude > 0:
        print("\n[КАТАСТРОФА!] У самолёта кончилось топливо!")
        break

    # 2. Меню действий
    print("\nЧто делаем?")
    print("1 — Снизить высоту на 3000 ft")
    print("2 — Дать разрешение на посадку")
    print("3 - Подзаправить в воздухе")
    
    choice = input("Ваш выбор (1 или 3): ").strip()

    # Обработка выбора
    if choice == "1":
        if altitude > 0:
            altitude -= 3000
            fuel -= 1
            print("\n-> Самолёт снижается...")
        else:
            print("\n-> Вы уже на земле (0 ft)!")

    elif choice == "2":
        if altitude == 0:
            score += 100
            print(f"\n[УСПЕХ!] Рейс {flight} успешно сел! Вы получили {score} очков!")
            break
        else:
            print(f"\n[ОШИБКА!] Нельзя садиться с высоты {altitude} ft! Сначала снизьтесь до 0!")
            fuel -= 1

    elif choice == "3":
        if dop_fuel != 0:
            fuel += 2
            dop_fuel -= 1
            print("----")
            print(f"fuel: {fuel}")
            print("Самолет был подзаправлен.")
            print("----")
            time.sleep(2)

        else:
            print("Деспечер отклонил заявку на подзаправку.")


    else:
        print("\n-> Неверная команда, попробуйте снова.")

    time.sleep(1)