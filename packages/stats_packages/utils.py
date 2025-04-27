import statsapi


def get_team_id_by_name(team_name: str):
    """Return the MLB team ID matching a partial or full team name."""
    teams = statsapi.get('teams', {'sportIds': 1})['teams']
    team_name = team_name.lower()
    for team in teams:
        if team_name in team['name'].lower():
            return team['id']
    return None

