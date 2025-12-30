import random
import time
import sys
from pyfiglet import Figlet
print(r"""  
   _____     _____   _____   _____   _____
  |  _  |   |  _  | |  ___| |  _  | |  _  |
  | | | |   | | | | | |___  | |_| | | | | |
 _| |_| |_  | | | | |  _  | |  ___| | | | |
|  _____  | | |_| | | |_| | | |     | |_| |
|_|     |_| |_____| |_____| |_|     |_____|
 _____   _____   __  _  __  _____    ____    _____   _____   _____   _______   _
|  _  | |  _  |  \ \| |/ / |  _  |  |  _ \  |  _  | |  _  \ |  _  | |__   __| | |
| | | | | | | |   \     /  | |_| |  | | | | | | | | | |_| / | |_| |    | |    | |___
| | | | | | | |    |   |   |  _  |  | | | | | | | | |  _ |  |  _  |    | |    |  _  |
| | | | | |_| |   /     \  | | | |  | | | | | |_| | | |_| \ | | | |    | |    | |_| |
|_| |_| |_____|  /_/|_|\_\ |_| |_|  /_/ |_| |_____| |_____/ |_| |_|    |_|    |_____|""")
f = Figlet(font='small')
print(f.renderText('DRAGONY'))


dragonhp = 200
playerhp = 100

while True:
    choice = input("Выбери действие (Удар / Защита): ").lower()

    if choice == "удар":
        playerdamage = random.randint(15, 25)
        dragonhp -= playerdamage
        dragonhp = max(dragonhp, 0)
        print(f"\nТы нанёс {playerdamage} урона дракону")
        print(f"Здоровье дракона: {dragonhp}")

        if dragonhp <= 0:
            input("\n\nВы победили дракона!")
            break

        # Контратака только если дракон жив
        if random.random() < 0.5:
            dragoncounter = random.randint(18, 37)
            playerhp -= dragoncounter
            playerhp = max(playerhp, 0)
            print(f"\nДракон контр-атаковал тебя на {dragoncounter} урона")
            print(f"Ваше хп: {playerhp}")

    elif choice == "защита":
        print("\nТы защитился")
        if random.random() < 0.4:
            RegenPlayerHP = random.randint(8, 15)
            playerhp = min(playerhp + RegenPlayerHP, 100)

            if playerhp == 100:
                print("Вы достигли макс. хп - 100")
            else:
                print(f"Вы использовали аптечку, ваше хп: {playerhp}")
        else:
            print("Аптечка на перезарядке")

    else:
        print("Неверный выбор")

    if playerhp <= 0:
        input("\n\nВы проиграли игру")
        break