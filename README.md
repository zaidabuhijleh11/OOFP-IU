OOFP-IU - Habit Tracker
Welcome to My Project
OOFP-IU is a backend habit tracking application that helps users track their habits and transform bad habits into good ones. It offers features like calculating streaks, identifying the most consistent and most struggled habits, and generating habit reports.

Project Overview
This app allows users to manage their habits efficiently by:
Tracking the streaks and longest streaks of their habits.
genrating a report of progress 
Providing the ability to visualize and review habit progress.


Project Structure
Dates_Presistance
using pickle we will save completed dates as dattime objects inside of the files and load them as objects too
Habit Class
The Habit class is used for calculating and managing various habit attributes such as streaks, completion dates, and habit statuses.
HabitDB Class
The HabitDB class handles the storage and retrieval of habit data using SQLite3. It provides functions for CRUD operations and managing habit data efficiently.
Analysis
This module contains functions for analyzing habits, calculating streaks, and generating reports. It also identifies the most consistent and most struggled habits based on the tracked data.
CLI Class
The CLI class provides a command-line interface with a wide range of commands that allow users to interact with the program, manage their habits, and view their progress.

Installation:
git clone https://github.com/zaidabuhijleh11/OOFP-IU.git
Requirmnest:
pip install -r requirements.txt


to use the app 
python cli.py
you can have up to 25 cmmand to to run 
create a hait delete a habit and many  to track habit store and analyze your habits 





