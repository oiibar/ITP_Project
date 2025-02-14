Aitu Telegram Bot

A Telegram bot built using Python and the python-telegram-bot library. This bot provides various utilities for students, such as calculating scholarship eligibility, tracking attendance, and fetching syllabi for different subjects.

Features

Start Command (/start) - Greets the user.

Menu Command (/menu) - Displays available commands.

Attendance Calculator (/attendance) - Calculates attendance percentage.

Scholarship Eligibility Check (/stepa) - Determines if a student is eligible for a scholarship based on their grades.

Syllabus Fetcher:

/calc_syllabus - Retrieves the syllabus for Calculus.

/dm_syllabus - Retrieves the syllabus for Discrete Mathematics.

/itp_syllabus - Retrieves the syllabus for Introduction to Programming.

Installation & Setup

Prerequisites

Ensure you have Python installed along with the required dependencies:

pip install python-telegram-bot --upgrade

Setup & Running

Clone the repository:

git clone https://github.com/yourusername/aitu-telegram-bot.git
cd aitu-telegram-bot

Replace the TOKEN variable in the script with your own Telegram bot token.

Run the bot:

python bot.py

Commands Overview

Command

Description

/start

Starts the bot and greets the user.

/menu

Displays a list of available commands.

/stepa

Starts the scholarship eligibility conversation.

/attendance

Starts the attendance tracking conversation.

/calc_syllabus

Sends the Calculus syllabus.

/dm_syllabus

Sends the Discrete Mathematics syllabus.

/itp_syllabus

Sends the Introduction to Programming syllabus.

Conversation Flow

Scholarship Eligibility (/stepa)

The bot asks for RegMid (midterm grade).

The bot asks for RegEnd (end-term grade).

It calculates the required final exam score for scholarship eligibility.

The user can enter the final exam score to get the final result.

Attendance Calculation (/attendance)

The bot asks for the number of absences.

It calculates the attendance percentage and displays the result.

Error Handling

If a user enters an invalid input (non-numeric), the bot prompts them to enter a valid number.

Unknown commands are handled with an appropriate response.

Deployment

You can deploy this bot on a cloud server or use services like Heroku or Railway.app.

License

This project is open-source and available under the MIT License.

Author

Developed by Your Name.