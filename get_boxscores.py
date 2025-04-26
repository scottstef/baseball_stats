import statsapi
from sys import argv
from packages.stats_packages.games import get_games
if len(argv) > 1:
    games = get_games(argv[1])
else:
    games = get_games()

for game in games:
    try:
        highlights = statsapi.boxscore(game)
        print(highlights)
        print('******************************************************************************')
    except Exception as e:
        print(f'Error fetching highlights for game {game}: {e}')
        print('******************************************************************************')