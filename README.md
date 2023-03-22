# 1. Диаграмма классов
![](https://github.com/LadaNikitina/CLI/blob/main/Диаграмма_классов.png)
1. Класс "Ремонтная зона". Представляет ремонтную зону, в которой происходит ремонт автомобилей.

Атрибуты класса:

- id: int - уникальный идентификатор ремонтной зоны
- name: str - название ремонтной зоны
- capacity: int - вместимость ремонтной зоны
- team: RepairTeam - ремонтная бригада, которая обслуживает ремонтную зону
- locations: List[RepairLocation] - список ремонтных мест в ремонтной зоне
- cars: List[Car] - список автомобилей, находящихся в ремонтной зоне
- conveyor_section: ConveyorSection - участок конвейера

Методы класса:

- add_location(location: RepairLocation) -> None - добавление ремонтного места в ремонтную зону
- remove_location(location: RepairLocation) -> None - удаление ремонтного места из ремонтной зоны
- add_car(car: Car) -> None - добавление автомобиля в ремонтную зону
- remove_car(car: Car) -> None - удаление автомобиля из ремонтной зоны

2. Класс "Место ремонта". Представляет собой место внутри ремонтной зоны, где проводится ремонт автомобиля. Атрибуты класса:

- id: int - уникальный идентификатор места ремонта
- name: str - название места ремонта
- zone: RepairZone - ремонтная зона, в которой находится место ремонта
- worker: RepairWorker - рабочий, который в данный момент выполняет ремонт на этом месте, None, если место свободно
- car: Car - автомобиль, который находится на ремонте на этом месте в данный момент, None, если место свободно
- start_time: datetime - время начала ремонта в данный момент на этом месте, None, если место свободно
- defect: Defect - дефект, который был обнаружен на автомобиле и зафиксирован на этом месте ремонта в данный момент, None, если место свободно

Методы класса:

- start_repair(worker: RepairWorker, car: Car, defect: Defect) -> None - начало ремонта на этом месте, указание рабочего, автомобиля и дефекта, на основе которых начинается ремонт
- end_repair() -> None - окончание ремонта на этом месте, освобождение места ремонта

3. Класс "RepairTeam". Этот класс представляет собой ремонтную бригаду, которая выполняет работы по ремонту автомобилей. Атрибуты класса:

- id: int - уникальный идентификатор ремонтной бригады
- name: str - название ремонтной бригады
- leader: RepairWorker - бригадир, ответственный за работу бригады
- workers: List[RepairWorker] - список рабочих, работающих в бригаде

Методы класса:

- add_worker(worker: RepairWorker) -> None - добавление рабочего в бригаду
- remove_worker(worker: RepairWorker) -> None - удаление рабочего из бригады
- change_leader(worker: RepairWorker) -> None - назначение нового бригадира

4. Класс "RepairWorker". Этот класс представляет собой рабочего, который выполняет работы по ремонту автомобилей. Атрибуты класса:

- id: int - уникальный идентификатор рабочего
- name: str - имя рабочего
- is_leader: bool - флаг, указывающий, является ли бригадиром рабочий
- available: bool - флаг, указывающий на доступность рабочего для выполнения работ
- team: RepairTeam - бригада, в которой работает рабочий
- repairs: List[Repair] - список ремонтов, которые назначены на рабочего

Методы класса:

- assign_repair(repair: Repair) -> None - назначение ремонта на рабочего
- start_repair(repair: Repair) -> None - начало выполнения ремонта рабочим
- finish_repair(repair: Repair) -> None - окончание выполнения ремонта рабочим

5. Класс "Defect". Этот класс представляет собой дефект автомобиля, который был зарегистрирован при диагностике. Атрибуты класса:

- id: int - уникальный идентификатор дефекта
- location: str - место дефекта, отмечаемое на схеме автомобиля
- cause: str - возможная причина дефекта
- car: Car - автомобиль, на котором был обнаружен дефект
- report_date: datetime - дата и время регистрации дефекта
- diagnosed_by: RepairWorker - рабочий, выполнявший диагностику
- repaired_by: RepairWorker - рабочий, выполнивший ремонт

Методы класса:

Отсутствуют, так как класс Defect представляет только данные о дефекте.

6. Класс Repair:
Этот класс представляет собой объект одного ремонта автомобиля. Атрибуты класса:

- id: int - уникальный идентификатор ремонта
- start_time: datetime - время начала ремонта
- end_time: datetime - время окончания ремонта
- worker: RepairWorker - рабочий, выполнивший ремонт
- defect: Defect - дефект, который был исправлен
- car: Car - автомобиль, который проходил ремонт

Методы класса:

Отсутствуют, так как класс Repair представляет только данные о ремонте.

7. Класс Car:
Этот класс представляет собой автомобиль. Атрибуты класса:

- id: int - уникальный идентификатор автомобиля
- defects: List[Defect] - список дефектов автомобиля
- repairs: List[Repair] - список ремонтов автомобиля

Методы класса:

- add_defect(defect: Defect) -> None - добавление дефекта автомобиля
- remove_defect(defect: Defect) -> None - удаление дефекта автомобиля
- add_repair(repair: Repair) -> None - добавление ремонта автомобиля
- remove_repair(repair: Repair) -> None - удаление ремонта автомобиля

8. Класс ConveyorSection:
Этот класс представляет собой участок конвейера. Атрибуты класса:

- id: int - уникальный идентификатор конвейера
- repair_zones: List[RepairZone] - список зон конвейера

Методы класса:

- add_repair_zone(repair_zone: RepairZone) -> None - добавление зоны ремонта
- remove_repair_zone(repair_zone: RepairZone) -> None - удаление зоны ремонта

9. Класс RepairStat:
Этот класс представляет собой общую информацию о заводе по части дефектов. Атрибуты класса:

- repairs: List[Repair] - список ремонтов
- repair_teams: List[RepairTeam] - список ремонтных бригад
- conveyor_sections: List[ConveyorSection] - список участков конвейера

Методы класса:

- add_repair(repair: Repair) -> None - добавление ремонта
- remove_repair(repair: Repair) -> None - удаление ремонта
- add_repair_team(repair_team: RepairTeam) -> None - добавление рабочей бригады
- remove_repair_team(repair_team: RepairTeam) -> None - удаление рабочей бригады
- add_conveyor(conveyor_section: ConveyorSection) -> None - добавление участка конвейера
- remove_conveyor(conveyor_section: ConveyorSection) -> None - удаление участка конвейера

# 2. Диаграмма компонентов требуемой системы
# 3. Диаграмма развёртывания
