"""
Simple script to enter a team name on the command line and return the team number to be able to better pull the data
"""
import sys
import statsapi

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <team name>")
        sys.exit(1)

    search_term = sys.argv[1].lower()
    teams = statsapi.get('teams', {'sportIds': 1})['teams']

    found = False
    for team in teams:
        if search_term in team['name'].lower():
            print(f"{team['name']} ID: {team['id']}")
            found = True

    if not found:
        print(f"No team found matching '{sys.argv[1]}'.")

if __name__ == "__main__":
    main()