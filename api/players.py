import pandas as pd

from nba_api.stats.static import players

def get_all_players_df():
	players_df = pd.DataFrame(players.get_players())
	
	return players_df

