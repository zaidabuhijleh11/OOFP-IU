OOFP-IU - Habit Tracker
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Welcome to My Project
OOFP-IU is a backend habit tracking application that helps users track their habits and transform bad habits into good ones. It offers features like calculating streaks, identifying the most consistent and most struggled habits, and generating habit reports.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Overview

This app allows users to manage their habits efficiently by:
Tracking the streaks and longest streaks of their habits.
genrating a report of progress 
Providing the ability to visualize and review habit progress.
saving data in a smooth way. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Structure
Dates_Presistance
using pickle we will save completed dates as dattime objects inside of the files and load them as objects too

Habit Class
The Habit class is used for calculating and managing completed dates for calcualtions like streak and longest streak run .

HabitDB Class
The HabitDB class handles the storage and retrieval of habit data using SQLite3. It provides functions for CRUD operations and managing habit data efficiently.

Analysis
This module contains functions for analyzing habits, graphing habits , and generating reports. It also identifies the most consistent and most struggled habits based on the tracked data.

CLI Class
The CLI class provides a command-line interface with a wide range of commands that allow users to interact with the program, manage their habits, and view their progress.

TESTS
ensuring everything works as expected using pytest  

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to Use

Installation:
git clone https://github.com/zaidabuhijleh11/OOFP-IU.git
Requirmnest:
pip install -r requirements.txt
to use the app 
python CLI.py
after running this a menu will apear in the consol you can choose any command you like 
the help command is included in the CLI so if you dont understand what does a command do you can see a description of it 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Test instruction : 

make sure you have installed pytest 
pip install pytest 
the test are class based meaning you can run the class to test the functality 
or you can see a small arrow next to the test classes 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test manually through  running this in the terminal each a time 

pytest test_Habit.py  
pytest test_habitdb.py
pytest test_analysis.py
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 







