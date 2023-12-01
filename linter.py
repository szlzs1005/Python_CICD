import sys
from pylint import lint

THRESHOLD = 4
run = lint.Run(["main.py"], exit=False)
score = run.linter.stats.global_note

print(f"Score : {score}")

if score < THRESHOLD:
    print(f"Linter failed, Score:{score} < threshold value: {THRESHOLD}")
    sys.exit(1)
sys.exit(0)