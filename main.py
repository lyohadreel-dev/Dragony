import random
print("Привет ты попал в игру - Убей дракона")

dragonhp = 200
playerhp = 100

while True:
    choice = input("Выбери действие (Удар / Защита): ").lower()

    if choice == "удар":
        playerdamage = random.randint(15, 25)
        dragonhp -= playerdamage
        print(f"\nТы нанёс {playerdamage} урона дракону")
        print(f"Здоровье дракона: {dragonhp}")

        # ФИКС: если дракон умер — сразу победа
        if dragonhp <= 0:
            input("\n\nВы победили дракона!")
            break

        # Контратака только если дракон жив
        if random.random() < 0.5:
            dragoncounter = random.randint(18, 37)
            playerhp -= dragoncounter
            print(f"\nДракон контр-атаковал тебя на {dragoncounter} урона")
            print(f"Ваше хп: {playerhp}")

    elif choice == "защита":
        print("Ты защитился")

    else:
        print("Неверный выбор")

    if playerhp <= 0:
        input("\n\nВы проиграли игру")
        break