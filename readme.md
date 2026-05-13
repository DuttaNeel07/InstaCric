# InstaCric

InstaCric is a simple Python project that tracks live IPL matches and sends desktop notifications whenever a boundary, six, or wicket happens.

The project uses Selenium to open the live cricket page, detect the current IPL match, monitor recent ball-by-ball events, and notify the user instantly.

## Features

- Detects live IPL matches automatically
- Tracks recent ball events
- Sends desktop notifications for:
  - FOUR
  - SIX
  - WICKET
- Works on Windows, macOS, and Linux
- Simple beginner-friendly code

## Tech Used

- Python
- Selenium
- webdriver-manager
- notifypy

## Installation

Clone the repository:

```bash
git clone <your-repo-link>
cd InstaCric
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3
- Google Chrome installed

## Run the Project

```bash
python script.py
```

## How It Works

1. Opens CricketWorld live matches page
2. Finds the currently live IPL match
3. Opens the IPL match page
4. Reads recent ball events
5. Detects:
   - boundaries
   - sixes
   - wickets
6. Sends desktop notifications instantly

## Example Notifications

- 🏏 FOUR — Boundary scored
- 🏏 SIX — Maximum scored
- 🏏 WICKET — Batsman Out

## Project Structure

```text
InstaCric/
│
├── script.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Support for all cricket leagues
- Sound alerts
- Faster event detection
- GUI version
- Mobile notifications

## Author

Neel Dutta