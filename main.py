import os
import datetime

pattern = [
    "100100011000010010000100010000000100010011100000010000000100100",
    "100100010000010010000100010000000100010010000000010000000100100",
    "111100010000010010000100010000000111110011000000010000000111100",
    "100100010000010010000100010000000100010010000000010000000100000",
    "100100011000001001100011000000000100010011100000001110000100000",
    "000000000000000000000000000000000000000000000000000000000000000",
    "000000000000000000000000000000000000000000000000000000000000000"
]

# Get last Sunday
today = datetime.date.today()
start_date = today - datetime.timedelta(days=today.weekday() + 1 if today.weekday() != 6 else 0)

print(f"Starting from Sunday: {start_date}")

rows = len(pattern)
cols = len(pattern[0])

for col in range(cols):
    for row in range(rows):
        if pattern[row][col] == "1":
            commit_date = start_date + datetime.timedelta(days=col * 7 + row)
            for i in range(5):  # 5 commits for darker green
                os.environ["GIT_AUTHOR_DATE"] = f"{commit_date} 12:00:00"
                os.environ["GIT_COMMITTER_DATE"] = f"{commit_date} 12:00:00"
                os.system(f'git commit --allow-empty -m "Art commit on {commit_date}"')

print("✅ DARK SCRIPT pattern added! Now push to GitHub.")
