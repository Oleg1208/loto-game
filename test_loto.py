
import unittest
from main import Card, Player, Game

class TestCard(unittest.TestCase):
    def test_str(self):
        card = Card()
        self.assertIsInstance(str(card), str)
        self.assertIn('-------------------------------', str(card))

    def test_equality(self):
        card1 = Card()
        card2 = Card()
        self.assertNotEqual(card1, card2)  # Карточки должны быть разными из-за случайной генерации
        card2.numbers = card1.numbers
        card2.marked_numbers = card1.marked_numbers
        self.assertEqual(card1, card2)

    def test_mark_number(self):
        card = Card()
        number = card.numbers[0][0]
        card.mark_number(number)
        self.assertIn(number, card.marked_numbers)
        self.assertEqual(card.numbers[0][0], 'X')

class TestPlayer(unittest.TestCase):
    def test_str(self):
        player = Player("Test Player", is_human=True)
        self.assertEqual(str(player), "Игрок: Test Player (Человек)")

    def test_equality(self):
        player1 = Player("Player 1", is_human=True)
        player2 = Player("Player 1", is_human=True)
        self.assertNotEqual(player1, player2)  # Карточки должны быть разными
        player2.card = player1.card
        self.assertEqual(player1, player2)

class TestGame(unittest.TestCase):
    def test_str(self):
        players = [Player("Player 1"), Player("Player 2")]
        game = Game(players)
        self.assertEqual(str(game), "Игра в лото с 2 игроками")

    def test_equality(self):
        players1 = [Player("Player 1"), Player("Player 2")]
        players2 = [Player("Player 1"), Player("Player 2")]
        game1 = Game(players1)
        game2 = Game(players2)
        self.assertNotEqual(game1, game2)  # Кеги должны быть разными из-за случайного перемешивания
        game2.kegs = game1.kegs
        self.assertEqual(game1, game2)

if __name__ == '__main__':
    unittest.main()
