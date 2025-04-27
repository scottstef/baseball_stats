# Baseball Stats

This project collects and analyzes baseball statistics, including fetching game schedules and other related data. The code utilizes Python and some essential libraries, and it includes tools for interacting with an API to retrieve game information.

## Features

- Fetches MLB game schedules.
- Provides utilities to handle game data.
- Analyzes and processes the game data for further insights.

## Setup and Installation

### Requirements

You can install the necessary dependencies using `pip` or `Poetry`:

#### Using `pip` (with `requirements.txt`):
```bash
pip install -r requirements.txt
```

#### Using poetry
```bash
poetry install
```

### Running the code:
```
python get_boxscores.py
```

### To test the project and view the code coverage:
```
pytest --cov --cov-branch --cov-report=xml
```

[![codecov](https://codecov.io/gh/scottstef/baseball_stats/graph/badge.svg?token=LWZGBGCQHQ)](https://codecov.io/gh/scottstef/baseball_stats)



