import random

class Card:
    def __init__(self):
        self.numbers = self.generate_card()
        self.marked_numbers = set()

    def generate_card(self):
        card_numbers = []
        for _ in range(3):  # Три строки
            row = sorted(random.sample(range(1, 91), 5))  # Пять случайных чисел
            card_numbers.append(row)
        return card_numbers

    def mark_number(self, number):
        for row in self.numbers:
            if number in row:
                row[row.index(number)] = 'X'
                self.marked_numbers.add(number)

    def is_complete(self):
        return all(num == 'X' for row in self.numbers for num in row)

    def __str__(self):
        card_str = '-------------------------------\n'
        for row in self.numbers:
            card_str += ' '.join(f'{num: >2}' if num != 'X' else ' X' for num in row) + '\n'
        card_str += '-------------------------------'
        return card_str


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.card = Card()

    def take_turn(self, number):
        if self.is_human:
            action = input(f"{self.name}, зачеркнуть цифру? (y/n) ").strip().lower()
            if action == 'y':
                self.card.mark_number(number)
        else:  # Если игрок - компьютер
            if number in [num for row in self.card.numbers for num in row]:
                self.card.mark_number(number)

    def has_won(self):
        return self.card.is_complete()


class Game:
    def __init__(self, players):
        self.players = players
        self.kegs = list(range(1, 91))
        random.shuffle(self.kegs)

    def play(self):
        while self.kegs:
            number = self.kegs.pop()
            print(f"Новый бочонок: {number} (осталось {len(self.kegs)})")

            for player in self.players:
                print(f"------ Карточка {player.name} -----")
                print(player.card)
                player.take_turn(number)

                if player.has_won():
                    print(f"{player.name} выиграл!")
                    return

def main():
    player1 = Player("Игрок 1", is_human=True)
    player2 = Player("Компьютер", is_human=False)

    game = Game([player1, player2])
    game.play()

if __name__ == '__main__':
    main()
