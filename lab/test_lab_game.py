from unittest.mock import Mock
from lab_game import get_random_item, award_badge


def test_get_random_item():
    fake_rng = Mock()
    fake_rng.choice.return_value = "sword"
    result = get_random_item("Aria", rng=fake_rng)
    assert result == "Aria found a sword"
