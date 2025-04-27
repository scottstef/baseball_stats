#from utils import get_game_ids_for_team
from packages.stats_packages.utils import get_game_ids_for_team
import statsapi

# Function to get condensed game highlights for a specific game
def get_condensed_game(game_id):
    # Fetch the game data
    game_data = statsapi.get('game', {'gamePk': game_id})

    # Check if the game has been played (status "Final")
    game_status = game_data.get('status', {}).get('abstractGameState', '')
    if game_status != 'Final':
        print(f"Game {game_id} has not been played yet or is still in progress.")
        return

    highlights = statsapi.game_highlights(game_id)
    if not highlights:
        print(f"No highlights found for Game {game_id}")
        return

    # Find condensed game video
    for clip in highlights:
        if isinstance(clip, dict):  # safety check
            title = clip.get('blurb', '')
            if "Condensed Game" in title:
                url = clip.get('playbacks', [{}])[0].get('url', 'No URL available')
                print(f"Game: {game_id}")
                print(f"Title: {title}")
                print(f"URL: {url}")
                print('******************************************************************************')
                return

    print(f"No Condensed Game found for Game {game_id}")

# Main function to check Orioles games
if __name__ == "__main__":
    # Pass a specific team, date, or last game flag as needed
    team_name = "Orioles"  # You can change this to another team name if needed
    game_ids = get_game_ids_for_team(team_name=team_name, game_date=None, last_game=False)  # You can modify as needed

    if game_ids:
        for game_id in game_ids:
            print(f"Checking condensed game for {team_name} game {game_id}...")
            try:
                get_condensed_game(game_id)
            except Exception as e:
                print(f"Error processing game {game_id}: {e}")
                print('******************************************************************************')
    else:
        print(f"No games found for {team_name}.")
