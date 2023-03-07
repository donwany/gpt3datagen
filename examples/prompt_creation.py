import csv
import json

# Read CSV file
with open("all_seasons.csv", "r") as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

# Create prompt and completion pairs
pairs = []
for player in data:
    prompt = f"Write a summary of {player[headers.index('Player')]}'s statistics:"
    completion = (
        f"{player[headers.index('Player')]} played {player[headers.index('GP  Games played')]} games, "
        f"starting {player[headers.index('GS  Games started')]} of them. "
        f"He had an average of {player[headers.index('MPG  Minutes Per Game')]} minutes per game, "
        f"scoring {player[headers.index('PPG  Points Per Game')]} points per game. "
        f"He made {player[headers.index('FGM  Field Goals Made')]} out of {player[headers.index('FGA  Field Goals Attempted')]} field goals, "
        f"for a field goal percentage of {player[headers.index('FG%  Field Goal Percentage')]}. "
        f"He made {player[headers.index('3FGM  Three-Point Field Goals Made')]} out of {player[headers.index('3FGA  Three-Point Field Goals Attempted')]} three-point field goals, "
        f"for a three-point field goal percentage of {player[headers.index('3FG%  Three-Point Field Goal Percentage')]}. "
        f"He made {player[headers.index('FTM  Free Throws Made')]} out of {player[headers.index('FTA  Free Throws Attempted')]} free throws, "
        f"for a free throw percentage of {player[headers.index('FT%  Free Throw Percentage')]}. "
        f"He plays as {player[headers.index('Position')]} for the {player[headers.index('Team')]}."
    )
    pairs.append({"prompt": prompt, "completion": completion})

if __name__ == "__main__":
    # Export to JSON file
    with open("prompt_completion_pairs.jsonl", "w") as f:
        json.dump(pairs, f)
