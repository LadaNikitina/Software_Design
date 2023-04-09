# Описание игры
Вы - отважный воин, который решился на опасное путешествие в глубины египетских гробниц. Говорят, что там спрятаны древние сокровища и магические артефакты, которые могут помочь вам в вашем нелёгком пути. Вы начинаете своё приключение поиска самого главного захоронения Тутанхамона на первом уровне гробниц.

Карта каждого уровня генерируется случайным образом, и вы видите перед собой лабиринт из коридоров и комнат, на которых могут находиться ловушки и сокровища. Вы начинаете с первого уровня. Ваша задача -- исследовать гробницы, собрать нужное для данного уровня количество сокровищ и попытаться достичь последнего уровня, где, как говорят, находится Тутанхамон. Но стоит помнить, что воздух отравлен, и у Вас есть ограниченное количество времени на поиск сокровищ.

Ваш персонаж имеет здоровье, которое падает, когда вы подвергаетесь атаке колючих лоз или когда вас захлёстывает волной лавы (да, гробницы таят в себе много тайн, уже никто даже не осмелится предположить, откуда там всё это), и повышается, когда вы используете зелье здоровья. Также на характеристики персонажа, такие как здоровье, получаемый урон, скорость ходьбы и зону видимости, могу влияти магические артефакты.

* Артефакты и зелья Вы можете найти прямо на карте, после этого они попадают в инвентарь
* Вы не будете знать, какой эффект даёт зелье или артефакт, пока не выпьете или не наденете их
* Надетый артефакт можете положить обратно в багаж, в таком случае при наведении курсора на него Вы сможете прочитать описание
* Зелья отличаются от артефактов краткосрочностью действия. Но будте внимательны, у некоторых артефактов также есть срок действия, после чего они изнашиваются и пропадают
* Некоторые артефакты нельзя положить обратно в багаж, так что вам придётся дождаться окончание их срока действия. Так же можно поступать, чтобы избавиться от ненужных артефактов и освободить место в инвентаре
* Зелья и артефакты могут оказывать не только положительный эффект!

Однако, будьте осторожны, если вы погибнете, вы не сможете загрузить предыдущее сохранение, и вам придётся начать заново на первом уровне. Так что будьте внимательны в своих приключениях, чтобы избежать гибели и достичь цели!

# Общие сведения о системе

## Назначение
Создание игры в жанре roguelike, предназначенной для развлечения пользователей.

## Границы системы
- Минималистичная консольная графика
- Поддержка только однопользовательского оффлайн режима игры
- Возможность генерации карт уровней случайным образом и загрузки карт из файлов
- Язык игры - русский
- Для управления игроком используются клавиши-стрелочки и пробел

## Контекст, в котором существует система
- Игра оффлайн, поэтому подключение к интернету не требуется
- Игра работает на Linux, MacOS и Windows
- Если хотите собрать игру из исходников, может понадобиться установка сторонних библиотек, указанных в requirements.txt

# Architectural drivers

## Технические ограничения

### Используемый язык программирования
* Python

### Поддерживаемые платформы
* Windows 10, Windows 11
* Linux Ubuntu 20.04
* MacOS Ventura

## Бизнес-ограничения
* Команда программистов из 3 человек
* Сроки работы
  * 1 неделя на подготовку документов и продумывание архитектуры
  * 2 недели на реализацию приложения
  * 1 неделя на расширение приложения

## Качественные характеристики системы
### Сопровождаемость
* Новые релизы с дополнениями, которые можно скачать

### Расширяемость
Возможные варианты:
* Увеличение числа уровней
* Добавление новых вещей
* Добавление возможности выбора сложности уровня
* Многопользовательский режим на одном устройстве
* Графика

### Масштабируемость
* Удобство в добавлении графики
* Возможность расширение карт
* Возможность задавать параметры при создании карты
* Удобство в сосдании многопользовательского режима на одном устройстве

### Производительность
* 60 кадров в секунду без задержек для любой платформы

### Безопасность
Особые ограничения не требуются

## Ключевые функциональные требования
* Консольная графика
* Случайная генерация карт
* Отсутствие сохранения
* Перемещение играка с помощью клавиатуры
* Наличие характеристик
  * Здоровье
  * Получаемый урон
  * Скорость ходьбы
  * Зона видимости
* Наличие инвентаря, в котором лежат вещи
  * Вещи влияют на характеристики
  * Вещи можно снять и надеть
  * Вещи можно найти на карте

# Роли и случаи использования игры

## Роли:
1. Игрок: основная роль. Игрок играет в нашу консольную игру, исследуя подземелье и преодолевая препятствия (колючки/лава). Он пытается найти главное сокровище, используя различные предметы и магические артефакты для улучшения своих характеристик и увеличения шансов на выживание и прохождение игры.
2. Разработчик: разработчик игры создает и отлаживает игру, обновляет ее функциональность, чтобы сделать ее более интересной.
3. Тестировщик: проверяет игру на ошибки, баги и несоответствия правилам.
4. Интернет-стример: играет в игру в прямом эфире на каком-либо стриминговом ресурсе, чтобы показать ее своим зрителям.
5. Геймер: фанат игр, который играет в игру для удовольствия и развлечения. Похож на игрока, но круче.

## Случаи использования:
1. Развлечение: человек может играть в эту игру для получения удовольствия.
2. Улучшение навыков: игра может помочь игрокам улучшить свои навыки такие как: стратегическое мышление, скорость реакции, и умение принимать быстро решения.
3. Психологическая помощь: игра может использоваться в качестве психологической помощи, чтобы улучшить настроение и снять стресс.
4. Развитие soft-skills, нетворкинг: игроки могут создать сообщество вокруг игры, общаться и обмениваться опытом и советами.
5. Соревнования: игроки могут соревноваться друг с другом за лучший результат и время, проходя одинаковые уровни и пытаясь получить максимальное количество очков.
6. Обучение: игра может использоваться для обучения программированию и созданию игр, поскольку ее механика отображает типичную структуру консольных игр.

## Типичный пользователь:
Типичный пользователь этой игры - любитель приключенческих игр, который любит играть в игры с элементами RPG и фэнтези. Он может быть мужчиной или женщиной, в возрасте от 10 до 40 лет, который хочет провести время, исследуя египетские гробницы в поисках сокровища. Он может быть как опытным геймером, так и новичком. Типичный пользователь может также принадлежать к сообществу геймеров, сидеть на форумах или в дискорде, где он обменивается опытом и советами с другими игроками.

# Диаграмма классов

![](https://github.com/LadaNikitina/CLI/blob/hw6/Class.png)


# Композиция
Под вещью понимаются различные магические артефакты.


![](https://github.com/LadaNikitina/CLI/blob/hw6/Диаграмма%20компонент.jpg)

# Взаимодействия и состояния

## Диаграмма конечных автоматов прохождения уровня игроком
<img width="898" alt="диаграмма" src="https://user-images.githubusercontent.com/57729595/229638386-a20a235b-8829-4044-995c-e08b092acd24.png">


