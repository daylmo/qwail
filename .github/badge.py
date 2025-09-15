import json
import math
from pathlib import Path

colors = {
    "0": "#ce222d",
    "10": "#eb5f1d",
    "20": "#fd9400",
    "30": "#ffc900",
    "40": "#ffff00",
    "50": "#d5ee13",
    "60": "#aedd22",
    "70": "#8aca2c",
    "80": "#68b733",
    "90": "#48a338",
    "100": "#288f3a",
}


def roundup(x):
    return int(math.floor(x / 10) * 10)


def main():
    path = Path("test_report")

    with open(path / "cov.json", "rb") as f:
        data = json.loads(f.read())
    percent_covered = int(data["totals"]["percent_covered"])

    badge_data = {
        "percent_display": str(percent_covered),
        "color": colors[str(roundup(percent_covered))],
        "suffix": "%",
    }

    if not path.exists():
        Path.mkdir(path)

    with open(path / "badge.json", "w") as f:
        f.write(json.dumps(badge_data))


if __name__ == "__main__":
    main()
