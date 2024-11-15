from datetime import datetime , date
class Habit:
    """
    Represents a Class for Habit Management and Important Calculations.
    Methods:
        get_habit_objects(): Converts habit data into Habit objects.
        habit_is_done_today(): Appends the date when the user has completed their habit today.
        streak_calculations(): Calculates the streak of a habit and the broken streak count.
        longest_streak_run_for_a_given_habit(): Calculates the longest streak run for a given habit.
     """


    def __init__(self, name:str , period:str , description:str , streak:int , broken_count:int , status:str , created_at  , duration:int = None , day_week:str = None ):
        """
Args:
    name (str): Name of the habit.
    period (str): Daily or weekly period for the habit.
    description (str): Description of the habit.
    streak (int): Number of consecutive dates the streak was completed.
    broken_count (int): Number of times the streak was broken.
    status (str): Status of the habit, e.g., "completed" or "incomplete".
    created_at (date): The date when the habit was created."""
        self.name = name
        self.period = period
        self.description = description
        self.streak = streak
        self.broken_count = broken_count
        self.status = status
        self.created_at = created_at
        self.completed_dates = [] # a list for each habit not shared
        self.habits = [] # habit objects

    def get_habit_objects(self) -> None :
        """ convert habit created in the db to Habit objects
        Args:

        Raises:
            None
        Description of method:
            just converts habits created in the HabitDB class into Habit objects"""
        from habitDB import HabitDB # to avoid import error
        db = HabitDB()
        habits = [Habit(*data) for data in db.get_habits()]# Convert each tuple of habit data into a Habit object
        for habit in habits:
             if habit not in self.habits:
                 self.habits.append(habit)

    def habit_is_done_today(self, name: str = None) -> None:
        """
        Append the date of the day if the user has completed their habit.

        Args:
            name (str): Name of the habit.

        Raises:
            ValueError: If the name is not provided.
            ValueError: If the date is duplicated.

        Returns:
            None: This method just appends the date of the day to `self.completed_dates`.

        Description:
            After validating that the name is provided and exists, the current date is appended to the list of completed dates,
            after checking that the date does not exist .
        """

        if name is None:
            raise ValueError("Habit name is not provided ")

        if self.name == name:
            today = datetime.today().date()
            if today  in self.completed_dates:
                raise ValueError("Date is duplicated")
            self.completed_dates.append(today)
            print(self.completed_dates)

    def streak_calculations(self) -> tuple[int , int]:
        """
        Calculate the streak of a habit based on completed dates.

        Args:

        Raises:
            None

        Return:
            Two integers curr_streak and broken_count.

        Firstly we increment the streak and broken streak count and loop over the dates and calculate the difference.

        Description of method:
            We increment the streak and broken count and loop over the completed dates and calculate the difference
            between the dates. If the period is daily and difference == 1, curr_streak += 1. If difference is not 1,
            broken_count += 1 and set streak = 0. The same goes for the weekly period, but the difference == 7."""
        dates = self.completed_dates
        broken_count = 0
        curr_streak = 1 if len(dates) == 1 else 0
        for x in range(1, len(dates)):
            difference = (dates[x] - dates[x - 1]).days
            if self.period == "daily" :
                if difference ==1 :
                    curr_streak += 1
                else:  # if dates are not consecutive set streak to zero and plus one to broken_count
                    broken_count += 1
                    curr_streak = 0
            if self.period == "weekly" :
                if difference ==7:
                   curr_streak += 1
                else:
                 broken_count += 1
                 curr_streak = 0
        self.streak = curr_streak
        self.broken_count = broken_count
        return curr_streak, broken_count

    def longest_run_streak_for_a_given_habit(self, name: str) -> int:
        """Calculate the longest streak run in a habit's history based on dates length.
        Args:
           name: Name of the habit (str).
        Raises:
            None.
        Return::
              Integer demonstrating the longest streak run of the habit in its history.
        Description of the method:
            Loop over the habits and increment two lists: streak history and consecutive dates.
            We loop over the dates as long as they are consecutive, appending them to consecutive dates.
            After that, we append the length of consecutive dates to streak history.
            After doing so, we will have numbers in the streak history list, from which we fetch the largest one,
            which is the longest streak of a habit."""
        if self.name == name:
                dates = sorted(self.completed_dates)
                streak_history = []
                consecutive_dates = []
                gap = 1 if self.period == 'daily' else 7  # Daily streak or weekly streak
                for x in range(1, len(dates)):
                    if (dates[x] - dates[x - 1]).days == gap:
                        consecutive_dates.append(dates[x])
                    else:
                        streak_history.append(len( consecutive_dates))
                        consecutive_dates = [dates[x]]
                return max(streak_history) if streak_history else 0
