"""
Test script for verifying module imports and functionality in the Baseball Stats project.
"""

from packages.stats_packages import games
from sys import argv

# date = "2025-04-26"  # example custom date


if len(argv) > 1:
    game_data = games.get_games(argv[1])
else:
    game_data = games.get_games()

# You can print it to see if it's working
print(game_data)
