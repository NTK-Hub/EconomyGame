# Панель управления королевством
screen kingdom_management:
    modal True
    frame:
        xalign 0.4
        yalign 0.05
        hbox:
            vbox:
                textbutton "Отправить на ферму" action Call("farm")
                textbutton "Вернуть из фермы" action Call("farm_back")
                textbutton "Отправить в мастерскую" action Call("workshop")
                textbutton "Вернуть из мастерской" action Call("workshop_back")
                textbutton "Отправить в казарму" action Call("barracks")
                textbutton "Вернуть из казармы" action Call("barracks_back")
                null height 15
                textbutton "Закрыть":
                    action [
                        Hide("kingdom_management"),  # Скрыть kingdom_management
                        Show("open_info_panel"),  # Показать панель info_panel
                        Show("open_kingdom_management"),  # Показать панель open_kingdom_management
                        Show("complete_the_move"),
                        Show("open_trade_panel")
                    ]

# Кнопка открытия панель управления королевством
screen open_kingdom_management:
    frame:
        xalign 0.4
        yalign 0.05
        textbutton "Управление королевством":
            action [
                Hide("open_info_panel"),  # Скрыть open_info_panel
                Hide("open_kingdom_management"),  # Скрыть open_kingdom_management
                Hide("complete_the_move"),
                Hide("open_trade_panel"),
                Show("kingdom_management")  # Показать панель kingdom_management
            ]

# Отправить на ферму
label farm:
    python:
        if (coins >= 2 and peasants >= 1):
            coins -= 2
            peasants -= 1
            farmers += 1
        else:
            "У вас недостаточно монет или крестьян."
    return

# Вернуть из фермы
label farm_back:
    python:
        if (farmers >= 1):
            farmers -= 1
            peasants += 1
        else:
            "У вас недостаточно фермеров."
    return

# Отправить в мастерскую
label workshop:
    python:
        if (coins >= 5 and peasants >= 1):
            coins -= 5
            peasants -= 1
            artisans += 1
        else:
            "У вас недостаточно монет или крестьян."
    return

# Вернуть из мастерской
label workshop_back:
    python:
        if (artisans >= 1):
            artisans -= 1
            peasants += 1
        else:
            "У вас недостаточно ремесленников."
    return

# Отправить в казарму
label barracks:
    python:
        if (coins >= 10 and peasants >= 1):
            coins -= 10
            peasants -= 1
            warriors += 1
        else:
            "У вас недостаточно монет или крестьян."
    return

# Вернуть из казармы
label barracks_back:
    python:
        if (warriors >= 1):
            warriors -= 1
            peasants += 1
        else:
            "У вас недостаточно воинов."
    return


screen trade_panel:
    modal True
    frame:
        xalign 0.7
        yalign 0.05
        hbox:
            vbox:
                textbutton "Продать девево" action Call("sell_wood")
                textbutton "Купить дерево" action Call("buy_wood")
                textbutton "Продать камень" action Call("sell_stone")
                textbutton "Купить камень" action Call("buy_stone")
                textbutton "Продать железо" action Call("sell_iron")
                textbutton "Купить железо" action Call("buy_iron")
                null height 15
                textbutton "Закрыть":
                    action [
                        Hide("trade_panel"),  # Скрыть kingdom_management
                        Show("open_kingdom_management"),  # Показать open_kingdom_management
                        Show("open_info_panel"),  # Показать панель info_panel
                        Show("open_kingdom_management"),  # Показать панель open_kingdom_management
                        Show("complete_the_move")
                    ]

# Кнопка открытия панель управления торговлей
screen open_trade_panel:
    frame:
        xalign 0.7
        yalign 0.05
        textbutton "Торговля":
            action [
                Hide("open_info_panel"),  # Скрыть open_info_panel
                Hide("open_kingdom_management"),  # Скрыть open_kingdom_management
                Hide("kingdom_management"),  # Скрыть панель open_kingdom_management
                Hide("complete_the_move"),
                Show("trade_panel")
            ]

# Продать дерево
label sell_wood:
    python:
        if (wood >= 15):
            coins += 1
            wood -= 15
        else:
            "У вас недостаточно дерева."
    return

# Купить дерево
label buy_wood:
    python:
        if (coins >= 1):
            coins -= 1
            wood += 10
        else:
            "У вас недостаточно монет."
    return

# Продать камень
label sell_stone:
    python:
        if (stone >= 10):
            coins += 1
            stone -= 10
        else:
            "У вас недостаточно камня."
    return

# Купить камень
label buy_stone:
    python:
        if (coins >= 1):
            coins -= 1
            stone += 5
        else:
            "У вас недостаточно монет."
    return

# Продать железо
label sell_iron:
    python:
        if (iron >= 5):
            coins += 1
            iron -= 5
        else:
            "У вас недостаточно железа."
    return

# Купить железо
label buy_iron:
    python:
        if (coins >= 1):
            coins -= 1
            iron += 1
        else:
            "У вас недостаточно монет."
    return