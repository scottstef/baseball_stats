import statsapi
from datetime import datetime


def get_team_id_by_name(team_name: str):
    """Return the MLB team ID matching a partial or full team name."""
    teams = statsapi.get('teams', {'sportIds': 1})['teams']
    team_name = team_name.lower()
    for team in teams:
        if team_name in team['name'].lower():
            return team['id']
    return None


def get_game_ids_for_team(team_name="Orioles", game_date=None, last_game=False):
    """
    Fetches the game IDs for a specific team for a given date, the last game, or today by default.

    Args:
        team_name (str): The name of the team (default: 'Orioles').
        game_date (str): Optional. The date to fetch games for in YYYY-MM-DD format.
        last_game (bool): Optional. If True, fetches the last game played by the team.

    Returns:
        list: A list of game IDs for the team for the specified date or the last game,
        or an empty list if no games are found.
    """
    # Get the team ID using the provided team name (default to 'Orioles')
    team_id = get_team_id_by_name(team_name)
    if team_id is None:
        print(f"Error: {team_name} team not found.")
        return []

    if last_game:
        try:
            # Fetch the last game the team played
            game = statsapi.last_game(team_id)
            return [game['game_id']] if game else []
        except Exception as e:
            print(f"Error fetching last game for {team_name}: {e}")
            return []

    # Determine the date to fetch the schedule for
    if not game_date:
        # Default to today's date if no date is provided
        game_date = datetime.now().strftime('%Y-%m-%d')

    try:
        # Fetch the schedule for the specified date and filter for the team's games
        games_schedule = statsapi.schedule(date=game_date, team=team_id)

        if not games_schedule:
            print(f"No games found for {team_name} on {game_date}.")
            return []

        # Extract and return the game IDs
        game_ids = [game['game_id'] for game in games_schedule]
        return game_ids

    except Exception as e:
        print(f"Error fetching games for {team_name} on {game_date}: {e}")
        return []
