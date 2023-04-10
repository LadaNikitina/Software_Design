# Карта

### Параметры генерации
* Размер карты
* Вероятность клетки с лавой
* Вероятность клетки с колючей лозой
* Колличество ядов
* Колличество артефактов
* Колличество сокровищ
* Режим печати

Чтобы добавить другую графику достаточно в файле [map.py](https://github.com/LadaNikitina/CLI/blob/hw7/map.py) в методе `drawPieceOfMap` класса `Map` реализовать ещё один режим печати

## Вариант печати 0

### Обозначение клеток
* `█` - стены
* `░` - колючие лозы
* `▓` - лава
* `V` - яд
* `□` - артефакт
* `*` - сокровище
* `I` - персонаж

### Примеры
Сгенерированная карта выглядит так:

![](https://github.com/LadaNikitina/CLI/blob/hw7/pictures/all_map0.png)

Но игрок будет видеть только её кусочек, размер которого соответствует текущей области видимости. Например, в данном случае так:

![](https://github.com/LadaNikitina/CLI/blob/hw7/pictures/piece_of_map0.png)


## Вариант печати 1

### Обозначение клеток
* Чёрные клетки - стены
* Зелёные клетки - колючие лозы
* Красные клетки - лава
* Оранжевый - яд
* Оранжевый - артефакт
* Оранжевый - сокровище
* Голубой - персонаж

### Примеры
Оранжевый на скриншотах похож больше на жёлтый.

Сгенерированная карта выглядит так:

![](https://github.com/LadaNikitina/CLI/blob/hw7/pictures/all_map1.png)

Но игрок будет видеть только её кусочек, размер которого соответствует текущей области видимости. Например, в данном случае так:

![](https://github.com/LadaNikitina/CLI/blob/hw7/pictures/piece_of_map1.png)
