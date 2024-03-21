from generate import generate_squad
from results import compute_results, print_standings
from simulate import simulate_season
from team import Team

ALL_TEAMS = [
    {"name": "Arsenal", "coefficient": 75},
    {"name": "Aston Villa", "coefficient": 75},
    {"name": "Brighton & Hove Albion", "coefficient": 60},
    {"name": "Burnley", "coefficient": 55},
    {"name": "Chelsea", "coefficient": 80},
    {"name": "Crystal Palace", "coefficient": 65},
    {"name": "Everton", "coefficient": 70},
    {"name": "Leeds United", "coefficient": 60},
    {"name": "Liverpool", "coefficient": 90},
    {"name": "Manchester City", "coefficient": 85},
    {"name": "Manchester United", "coefficient": 80},
    {"name": "Newcastle United", "coefficient": 60},
    {"name": "Norwich City", "coefficient": 50},
    {"name": "Southampton", "coefficient": 65},
    {"name": "Tottenham Hotspur", "coefficient": 75},
    {"name": "Watford", "coefficient": 60},
    {"name": "West Ham United", "coefficient": 70},
    {"name": "Wolverhampton Wanderers", "coefficient": 65}

]

# Create a Team object for each team
TEAMS = []
for team in ALL_TEAMS:
    # team is a dictionary containing {"name": name, "coefficient": coefficient}
    team_name =team.get('name')
    team_coefficient = team.get('coefficient')
    team_squad = generate_squad(team_name, team_coefficient)
    team = Team(team_name, team_coefficient, team_squad)
    TEAMS.append(team)

# Print the teams and their squads
for team in TEAMS:
    print(f"{team.name}: {team.coefficient}")
    print("Squad:")
    for player in team.squad:
        print(f"{player.name}: {player.coefficient}")
    print()

matches = simulate_season(TEAMS)

team_stats = compute_results(matches)
print_standings(team_stats)
