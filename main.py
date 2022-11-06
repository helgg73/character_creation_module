# .../Dev_/character_creation_module/main.py

from random import randint

# Значение стандартой атаки.
DEFAULT_ATTACK = 5
# Стандартное значение защиты.
DEFAULT_DEFENCE = 10
# Базовое значение здоровья
DEFAULT_STAMINA = 80 


class Character:
    # Описание персонажа
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    # Константа диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Урон умения.
    SPECIAL_BUFF = 15
    # Название умения.
    SPECIAL_SKILL = 'Удача'
    # Константа диапазона очков защиты
    RANGE_VALUE_DEFENCE = (1, 5)


    def __init__(self, name):
        self.name = name


    def attack(self):
        # Вычисляем значение атаки  в переменной value_attack.
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')
   

    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')


    def special(self):
        # Печатаем значение умения.
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')


    def __str__(self):
        # Описание персонажа.
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.' 


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """

    print(f'{character.name}, ты {character.BRIEF_DESC_CHAR_CLASS}.')

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    known_actions = {
        'attack': character.attack(),
        'defence': character.defence(),
        'special': character.special()
    }
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in known_actions:
            print(known_actions[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())

start_training(warrior)