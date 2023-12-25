from api.games import get_all_games_stats

games_df = get_all_games_stats(2023)
print(games_df.head())
