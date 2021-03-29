# Игра Квест
## Суть игры:
Существует лабиринт-квест, который нужно пройти. Игрок перед началом игры выбирает N персонажей. При прохождении квеста, игрок отвечает на вопросы на логику и знания за ограниченное время. В случае, если время закончилось, но ответ на вопрос не был дан, происходит некоторое событие, справиться с которым игроку помогают баллы его выбранных персонажей,а в случае неудачи у персонажей отнимаются баллы за здоровье. Игрок теряет персонажа если его баллы за здоровье равны нулю.

## Цель игры:
Дойти до конца лабиринта хотя бы с одним персонажем.

## Персонажи:
Есть следующие 4 вида различных классов персонажей:
- **Халк** (Сила: 10, Интеллект: 2, Ловкость: 3, Здоровье: 5)
- **Шерлок Холмс** (Сила: 2, Интеллект: 10, Ловкость: 2, Здоровье: 6)
- **Человек паук** (Сила: 3, Интеллект: 3, Ловкость: 10, Здоровье: 4)
- **Иисус** (Сила: 5, Интеллект: 2, Ловкость: 3, Здоровье: 10)

У каждого класса персонажей есть 4 базовые характеристики: ум, сила, ловкость, здоровье. У каждого из них есть одна наиболее развитая характеристика, которая оценивается в 10 баллов. Сумма трех оставшихся характеристик также составляет 10 баллов. Если у игрока есть больше одного персонажа из одного класса, вместе у персонажей формируются уникальные методы, которые могут быть использованы при преодолении препятствий в ходе игры.
