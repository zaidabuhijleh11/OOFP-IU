from datetime import datetime
import pytest
from habitDB import HabitDB
from habit import Habit
from Dates_Persistence import save_dates , load_dates
import pickle
class TestHabit:

    @pytest.fixture
    def test_habit1(self):
        test_habit1 = Habit(name='zaid',period='daily',description='testing',streak=0 ,broken_count=0 , status='incomplete' , created_at= datetime.now().date(), duration=100 , day_week="day" )
        return test_habit1

    @pytest.fixture
    def db(self):
       return HabitDB()

    @pytest.fixture(autouse=True)
    def clean_db(self , db ):
        db.delete_all_habits()
        yield
        db.delete_all_habits()

    @pytest.fixture(autouse=True)
    def clean_pickle_files(self):
        with open('zaid_dates.pkl', 'wb') as file:
            pickle.dump([], file)

    def test_habit_is_done_today(self, db, test_habit1):
        db.delete_all_habits()
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        test_habit1.habit_is_done_today(test_habit1.name)
        assert datetime.now().date() in load_dates(test_habit1.name)

    def test_streak_calculation(self, test_habit1 , db ):

        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        curr_streak, broken_count = test_habit1.streak_calculations(test_habit1.name)
        assert curr_streak == 5
        assert broken_count == 0


    def test_streak_cal_for_broken_count(self , test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        curr_streak, broken_count = test_habit1.streak_calculations(test_habit1.name)
        assert broken_count ==2





    def test_longest_run_streak_for_a_given_habit(self, test_habit1, db):
        db.create_habit(name=test_habit1.name, period=test_habit1.period, description=test_habit1.description, duration=100, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 10, 1).date())
        save_dates(test_habit1.name, datetime(2024, 10, 2).date())
        save_dates(test_habit1.name, datetime(2024, 10, 3).date())
        save_dates(test_habit1.name, datetime(2024, 10, 4).date())
        save_dates(test_habit1.name, datetime(2024, 10, 5).date())
        save_dates(test_habit1.name, datetime(2024, 10, 6).date())
        save_dates(test_habit1.name, datetime(2024, 10, 7).date())
        save_dates(test_habit1.name, datetime(2024, 10, 8).date())
        save_dates(test_habit1.name, datetime(2024, 10, 10).date())
        save_dates(test_habit1.name, datetime(2024, 10, 11).date())
        save_dates(test_habit1.name, datetime(2024, 10, 12).date())
        save_dates(test_habit1.name, datetime(2024, 10, 13).date())
        save_dates(test_habit1.name, datetime(2024, 10, 15).date())
        ex_outcome = test_habit1.longest_run_streak_for_a_given_habit(test_habit1.name)
        assert ex_outcome == 7



