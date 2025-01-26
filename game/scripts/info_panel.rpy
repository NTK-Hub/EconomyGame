# Панель ресурсов
screen info_panel:
    modal True
    frame:
        xalign 0.01
        yalign 0.05
        hbox:
            vbox:
                add "info_panel/coin_05d.png"
                add "info_panel/wood_01a.png"
                add "info_panel/stoneblock_01a.png"
                add "info_panel/ingot_01c.png"
                add "info_panel/food.png"
                add "info_panel/boots_01a.png"
                add "info_panel/gloves_01a.png"
                add "info_panel/helmet_01a.png"
                add "info_panel/helmet_02b.png"
                add "info_panel/heart.png"
                add "info_panel/skull_01a.png"
            vbox:
                text "[coins]" size 40
                text "[wood]" size 40
                text "[stone]" size 40
                text "[iron]" size 40
                text "[food]" size 40
                text "[peasants]" size 40
                text "[farmers]" size 40
                text "[artisans]" size 40
                text "[warriors]" size 40
                text "[born]" size 40
                text "[died]" size 40
                text "Ход: [turns]" size 40
                textbutton "Закрыть":
                    action [
                        Hide("info_panel"),  # Скрыть open_info_panel
                        Show("open_info_panel"),  # Показать панель info_panel
                        Show("open_kingdom_management"),  # Показать панель kingdom_management
                        Show("open_trade_panel"),
                        Show("complete_the_move")
                ]

screen open_info_panel:
    frame:
        xalign 0.01
        yalign 0.05
        textbutton "Ресурсы королевства":
            action [
                Hide("open_info_panel"),  # Скрыть open_info_panel
                Hide("open_kingdom_management"),  # Скрыть open_kingdom_management
                Hide("complete_the_move"),
                Hide("open_trade_panel"),
                Show("info_panel")  # Показать панель info_panel
            ]