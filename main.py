import random


class Card:
    def __init__(self):
        self.numbers = self.generate_card()
        self.marked_numbers = set()

    def generate_card(self):
        # Генерация карточки с тремя строками по пять случайных чисел
        card_numbers = []
        for _ in range(3):
            row = sorted(random.sample(range(1, 91), 5))
            card_numbers.append(row)
        return card_numbers

    def mark_number(self, number):
        # Отмечает число на карточке, если оно присутствует
        for row in self.numbers:
            if number in row:
                row[row.index(number)] = 'X'
                self.marked_numbers.add(number)

    def is_complete(self):
        # Проверяет, все ли числа на карточке отмечены
        return all(num == 'X' for row in self.numbers for num in row)

    def __str__(self):
        # Возвращает строковое представление карточки
        card_str = '-------------------------------\n'
        for row in self.numbers:
            card_str += ' '.join(f'{num: >2}' if num != 'X' else ' X' for num in row) + '\n'
        card_str += '-------------------------------'
        return card_str

    def __eq__(self, other):
        # Сравнивает две карточки
        if not isinstance(other, Card):
            return NotImplemented
        return self.numbers == other.numbers and self.marked_numbers == other.marked_numbers

    def __ne__(self, other):
        # Проверяет неравенство двух карточек
        return not self.__eq__(other)


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.card = Card()

    def take_turn(self, number):
        # Ход игрока
        if self.is_human:
            action = input(f"{self.name}, зачеркнуть цифру? (y/n) ").strip().lower()
            if action == 'y':
                self.card.mark_number(number)
        else:
            # Компьютер автоматически отмечает число, если оно есть на карточке
            if number in [num for row in self.card.numbers for num in row]:
                self.card.mark_number(number)

    def has_won(self):
        # Проверяет, выиграл ли игрок
        return self.card.is_complete()

    def __str__(self):
        # Возвращает строковое представление игрока
        return f"Игрок: {self.name} ({'Человек' if self.is_human else 'Компьютер'})"

    def __eq__(self, other):
        # Сравнивает двух игроков
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name and self.is_human == other.is_human and self.card == other.card

    def __ne__(self, other):
        # Проверяет неравенство двух игроков
        return not self.__eq__(other)


class Game:
    def __init__(self, players):
        self.players = players
        self.kegs = list(range(1, 91))
        random.shuffle(self.kegs)

    def play(self):
        # Основной игровой цикл
        while self.kegs:
            number = self.kegs.pop()
            print(f"Новый бочонок: {number} (осталось {len(self.kegs)})")

            for player in self.players:
                print(f"------ Карточка {player.name} -----")
                print(player.card)


