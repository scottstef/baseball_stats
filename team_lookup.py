'''
Simple script to get a team's mlb api number if a team is given
returns all of the mlb teams if none are given
'''
import sys
from packages.stats_packages.utils import get_team_id_by_name
import statsapi


def list_all_teams():
    """Prints all MLB teams with their IDs."""

    teams = statsapi.get('teams', {'sportIds': 1})['teams']
    for team in teams:
        print(f"{team['name']} (ID: {team['id']})")


def main():
    if len(sys.argv) < 2:
        print("No team name provided. Listing all MLB teams:\n")
        list_all_teams()
        sys.exit(0)

    team_name = sys.argv[1]
    team_id = get_team_id_by_name(team_name)

    if team_id:
        print(f"Team ID for '{team_name}': {team_id}")
    else:
        print(f"No team found matching '{team_name}'.")


if __name__ == "__main__":
    main()
