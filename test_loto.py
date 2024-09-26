
from main import Card, Player, Game

def test_card_generation():
    card = Card()
    assert len(card.numbers) == 3
    assert all(len(row) == 5 for row in card.numbers)
    assert all(1 <= num <= 90 for row in card.numbers for num in row if num != 'X')

def test_card_marking():
    card = Card()
    original_numbers = [num for row in card.numbers for num in row]
    card.mark_number(original_numbers[0])
    assert 'X' in card.numbers[0]
    assert len(card.marked_numbers) == 1

def test_player_initialization():
    player = Player("Test Player")
    assert player.name == "Test Player"
    assert player.is_human == True
    assert isinstance(player.card, Card)

def test_game_initialization():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game([player1, player2])
    assert len(game.players) == 2
    assert len(game.kegs) == 90
