from datetime import datetime, date
import pytest
from habitDB import HabitDB
from habit import Habit


class TestHabit:

    @pytest.fixture
    def test_habit(self):

        test_habit = Habit(name='abd',period='daily',description='testing',streak=0 ,broken_count=0 , status='incomplete' , created_at= datetime.now().date(), duration=100 , day_week="day" )
        return test_habit

    @pytest.fixture
    def test_habit1(self):
        test_habit1 = Habit(name='zaid',period='daily',description='testing',streak=0 ,broken_count=0 , status='incomplete' , created_at= datetime.now().date(), duration=100 , day_week="day" )
        return test_habit1

    @pytest.fixture
    def db(self):
       return HabitDB()

    @pytest.fixture(autouse=True)
    def clean_db(self , db ):
        yield
        db.delete_all_habits()



    def test_habit_is_done_today(self, db,test_habit1  ):

        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        test_habit1.get_habit_objects()
        test_habit1.habit_is_done_today(test_habit1.name)

        assert datetime.now().date() in test_habit1.completed_dates

    def test_streak_calculation(self, test_habit1 , db ):

        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        test_habit1.completed_dates = [date(2024, 10, 28), date(2024, 10, 29), date(2024, 10, 30),
                                       date(2024, 10, 31), date(2024, 11, 1), date(2024, 11, 2)]
        curr_streak, broken_count = test_habit1.streak_calculations()
        assert curr_streak == 5
        assert broken_count == 0


    def test_longest_run_streak_for_a_given_habit(self, test_habit, db):

        db.create_habit(name=test_habit.name, period=test_habit.period, description=test_habit.description, duration=100, day_week='day')
        test_habit.get_habit_objects()
        test_habit.completed_dates = [
            date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 3),
            date(2024, 10, 4), date(2024, 10, 5), date(2024, 10, 6),
            date(2024, 10, 7), date(2024, 10, 8), date(2024, 10, 9),
            date(2024, 10, 10), date(2024, 10, 11), date(2024, 10, 12),
            date(2024, 10, 13), date(2024, 10, 15),
            date(2024, 10, 16), date(2024, 10, 17), date(2024, 10, 18),
            date(2024, 10, 19), date(2024, 10, 20), date(2024, 10, 21),
            date(2024, 10, 22), date(2024, 10, 23),
            date(2024, 10, 25), date(2024, 10, 27),
            date(2024, 10, 28), date(2024, 10, 30),
            date(2024, 10, 31)]


        ex_outcome = test_habit.longest_run_streak_for_a_given_habit(test_habit.name)
        assert ex_outcome == 12
