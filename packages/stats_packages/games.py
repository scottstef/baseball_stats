import requests
from datetime import datetime, timedelta


def get_games(date: str = None):
    if date is None:
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')


    url = f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={date}&endDate={date}'
    response = requests.get(url)


    if response.status_code != 200:
        raise Exception(f"Failed to fetch games: {response.status_code}")

        data = response.json()
    games = data.get('dates', [])[0].get('games', [])
    
    game_ids = [game.get('gamePk') for game in games]
    return game_ids
