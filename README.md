# Aitu Telegram Bot

A Telegram bot built using Python and the python-telegram-bot library. This bot provides various utilities for students, such as calculating scholarship eligibility, tracking attendance, and fetching syllabi for different subjects.

## Features

### Core Commands
- **/start** - Greets the user
- **/menu** - Displays available commands

### Academic Tools
- **/attendance** - Calculates attendance percentage
- **/stepa** - Determines if a student is eligible for a scholarship based on their grades

### Syllabus Access
- **/calc_syllabus** - Retrieves the syllabus for Calculus
- **/dm_syllabus** - Retrieves the syllabus for Discrete Mathematics
- **/itp_syllabus** - Retrieves the syllabus for Introduction to Programming

## Installation & Setup

### Prerequisites

Ensure you have Python installed along with the required dependencies:

```bash
pip install python-telegram-bot --upgrade
```

### Setup & Running

1. Clone the repository:
```bash
git clone https://github.com/oiibar/ITP_Project.git
cd ITP_Project
```

2. Replace the `TOKEN` variable in the script with your own Telegram bot token.

3. Run the bot:
```bash
python main.py
```

## Commands Overview

| Command | Description |
|---------|-------------|
| `/start` | Starts the bot and greets the user |
| `/menu` | Displays a list of available commands |
| `/stepa` | Starts the scholarship eligibility conversation |
| `/attendance` | Starts the attendance tracking conversation |
| `/calc_syllabus` | Sends the Calculus syllabus |
| `/dm_syllabus` | Sends the Discrete Mathematics syllabus |
| `/itp_syllabus` | Sends the Introduction to Programming syllabus |

## Conversation Flow

### Scholarship Eligibility (/stepa)
1. The bot asks for RegMid (midterm grade)
2. The bot asks for RegEnd (end-term grade)
3. It calculates the required final exam score for scholarship eligibility
4. The user can enter the final exam score to get the final result

### Attendance Calculation (/attendance)
1. The bot asks for the number of absences
2. It calculates the attendance percentage and displays the result

## Error Handling

- If a user enters an invalid input (non-numeric), the bot prompts them to enter a valid number
- Unknown commands are handled with an appropriate response
