
screen complete_the_move:
    frame:
        xalign 0.99
        yalign 0.05
        textbutton "Завершить ход" action Call("move")

label move:
    python:
        turns += 1
        import random
        random_events = random.randint(1, 25)

        # Люди едят за ход
        if (random_events != 1):
            food -= peasants + farmers + 2 * artisans + 3 * warriors

        # Ивент "Голодомор" (плохое событие)
        if (random_events == 1):
            food -= random.randint(2, 5) * (peasants + farmers + artisans + warriors)

        # Смерть
        died = 0
        if (random_events != 2):
            for y in range(10, 100, 10):
                if(y <= peasants <= y + 9 or y <= farmers <= y + 9 or y <= artisans <= y + 9 or y <= warriors <= y + 9):
                    for n in range(10, 100, 10):
                        if(n <= peasants <= n + 9):
                            x = 0
                            random_plague = random.randint(x, x + 1)
                            peasants -= random_plague
                            died += random_plague
                        if(n <= farmers <= n + 9):
                            x = 0
                            random_plague = random.randint(x, x + 1)
                            farmers -= random_plague
                            died += random_plague
                        if(n <= artisans <= n + 9):
                            x = 0
                            random_plague = random.randint(x, x + 1)
                            artisans -= random_plague
                            died += random_plague
                        if(n <= warriors <= n + 9):
                            x = 0
                            random_plague = random.randint(x, x + 0)
                            warriors -= random_plague
                            died += random_plague

        # Ивент "Чума" (плохое событие)
        if (random_events == 2):
            for y in range(10, 100, 10):
                if(y <= peasants <= y + 9 or y <= farmers <= y + 9 or y <= artisans <= y + 9 or y <= warriors <= y + 9):
                    for n in range(10, 100, 10):
                        if(n <= peasants <= n + 9):
                            x = n // 10 + 1
                            random_plague = random.randint(x, x * 5)
                            peasants -= random_plague
                            died += random_plague
                        if(n <= farmers <= n + 9):
                            x = n // 10 + 1
                            random_plague = random.randint(x, x * 5)
                            farmers -= random_plague
                            died += random_plague
                        if(n <= artisans <= n + 9):
                            x = n // 10 + 1
                            random_plague = random.randint(x, x * 5)
                            artisans -= random_plague
                            died += random_plague
                        if(n <= warriors <= n + 9):
                            x = n // 10 + 1
                            random_plague = random.randint(x, x * 5)
                            warriors -= random_plague
                            died += random_plague

        # Ивент "Нападение бандитов" (плохое событие)
        if (random_events == 3):
            bandits = random.randint((turns // 10) + 1, (turns // 5) + 1)
            if (bandits >= warriors):
                if (warriors > 0):
                    bandits -= warriors
                    warriors = 0
                if (artisans > 0 and bandits > 0):
                    bandits_temp = bandits
                    bandits = ((2 * bandits) - artisans) // 2
                    artisans -= 2 * bandits_temp
                    if (artisans < 0):
                        artisans = 0
                if (farmers > 0 and bandits > 0):
                    bandits_temp = bandits
                    bandits = ((3 * bandits) - farmers) // 3
                    farmers -= 3 * bandits_temp
                    if (farmers < 0):
                        farmers = 0
                if (peasants > 0 and bandits > 0):
                    bandits_temp = bandits
                    bandits = ((3 * bandits) - peasants) // 3
                    peasants -= 3 * bandits_temp
                    if (peasants < 0):
                        peasants = 0
            elif (bandits == warriors):
                warriors -= bandits
            elif (bandits <= warriors):
                warriors -= bandits

        # Прирост еды
        if (random_events != 4):
            food += farmers * random.randint(3, 7)

        # Ивент "Плодородный сезон" (хорошее событие)
        if (random_events == 4):
            food += farmers * random.randint(10, 15)

        # Рождение
        if (random_events != 5):
            born = 0
            random_born = random.randint(0, 1)
            peasants += random_born
            born += random_born

        # Ивент "Повышенная рождаемость" (хорошее событие)
        if (random_events == 5):
            born = 0
            random_born = random.randint(3, 10)
            peasants += random_born
            born += random_born

        # Добыча ресурсов
        if (artisans > 0):
            wood += random.randint(1, 5) * artisans
            stone += random.randint(1, 3) * artisans
            iron += 1 * artisans