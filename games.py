"""
Module to interact with the MLB Stats API and retrieve games played on a specific day defaults to yesterday
"""

from datetime import datetime, timedelta
import requests

# if you want to add a date: date = "2025-04-26"  # example custom date
def get_games(date: str = None):
"""
    Fetches MLB games for a given date using the MLB Stats API.
    
    Args:
        date (str): The date for which to fetch the games (in YYYY-MM-DD format).
    
    Returns:
        list: A list of game IDs.
"""
 
    if date is None:
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={date}&endDate={date}'
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch games: {response.status_code}")

    data = response.json()
    games = data.get('dates', [])[0].get('games', [])
        
    game_ids = [game.get('gamePk') for game in games]
    return game_ids
