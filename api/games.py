import pandas as pd

from nba_api.stats.endpoints import leaguegamefinder

def get_all_games_stats(start_season, end_season=None):
    """
    Extract regular season and playoff team stats for a season range
    """
    if not end_season:
        end_season = start_season
    for season in range(start_season, end_season + 1):
        # Generate season string in the format YYYY-YY
        season_str = f"{season}-{(season + 1) % 100:02d}"
        # Pull regular season team stats for the season range
        regular_season_df = leaguegamefinder.LeagueGameFinder(
            player_or_team_abbreviation="T",
            season_type_nullable="Regular Season",
            season_nullable=season_str,
            league_id_nullable="00"
        ).league_game_finder_results.get_data_frame()
        # Pull playoff stats for the season range
        playoff_season_df = leaguegamefinder.LeagueGameFinder(
            player_or_team_abbreviation="T",
            season_type_nullable="Playoffs",
            season_nullable=season_str,
            league_id_nullable="00"
        ).league_game_finder_results.get_data_frame()
        
        # Create columns indicating season and season type for both regular season and playoff dfs
        regular_season_df["season"], regular_season_df["season_type"] = season_str, "Regular"
        playoff_season_df["season"], playoff_season_df["season_type"] = season_str, "Playoff"
        
        full_season = pd.concat([regular_season_df, playoff_season_df], ignore_index=True)
        
        return full_season