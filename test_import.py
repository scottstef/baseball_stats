"""
Test script for verifying module imports and functionality in the Baseball Stats project.
"""

from packages.stats_packages import games
import sys

def test_get_games():
    """Test fetching games with or without a date."""
    if len(sys.argv) > 1:
        game_data = games.get_games(sys.argv[1])
    else:
        game_data = games.get_games()

    # Basic check: we should get a list or data back
    assert isinstance(game_data, (list, dict))
