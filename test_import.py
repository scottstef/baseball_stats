"""
Test script for verifying module imports and functionality in the Baseball Stats project.
"""

from packages.stats_packages import games

def test_get_games():
    """Test fetching games using a hardcoded date."""
    test_date = "2024-04-20"  # Pick a known good date with games
    game_data = games.get_games(test_date)

    # Basic check: we should get a list or dict back
    assert isinstance(game_data, (list, dict))
