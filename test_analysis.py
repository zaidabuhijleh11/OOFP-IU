from datetime import datetime , date
from habit import Habit
from habitDB import HabitDB
import pytest
from analysis import get_most_consistent_habits, get_most_struggled_habits, get_daily_habits, get_weekly_habits , calculate_completion_rate
import pickle
from Dates_Persistence import  save_dates , load_dates




class TestAnalysis:
    @pytest.fixture
    def test_habit(self):
        test_habit = Habit(name='zaidabuhijleh', period='daily', description='testing', streak=0, broken_count=0,
                           status='incomplete', created_at=datetime.now().date(), duration=100, day_week="day")
        return test_habit

    @pytest.fixture
    def test_habit1(self):
        test_habit1 = Habit(name='zaid', period='daily', description='testing', streak=0,
                            broken_count=0, status='incomplete', created_at=datetime.now().date(), duration=100,
                            day_week="day")
        return test_habit1

    @pytest.fixture
    def db(self):
        return HabitDB()

    @pytest.fixture(autouse=True)
    def clean_db(self, db):
        db.delete_all_habits()
        yield
        db.delete_all_habits()

    @pytest.fixture(autouse=True)
    def clean_pickle_files(self):
        with open('zaid_dates.pkl', 'wb') as file:
            pickle.dump([], file)

    @pytest.fixture(autouse=True)
    def clean_pickle_files1(self):
        with open('zaidabuhijleh_dates.pkl', 'wb') as file:
            pickle.dump([], file)


    def test_get_most_consistent_habits(self , db  , test_habit , test_habit1):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=100, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        save_dates(test_habit.name, datetime(2024, 11, 1).date())
        save_dates(test_habit.name, datetime(2024, 11, 2).date())
        save_dates(test_habit.name, datetime(2024, 11, 3).date())
        save_dates(test_habit.name, datetime(2024, 11, 5).date())
        save_dates(test_habit.name, datetime(2024, 11, 6).date())
        db.update_status_streak(test_habit1.name)
        db.update_status_streak(test_habit.name)
        ex_outcome =[test_habit1.name ,test_habit.name ]
        result = get_most_consistent_habits(  db ,consistency=4)
        assert result == ex_outcome


    def test_get_most_struggled_habits(self , db  , test_habit , test_habit1):
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        save_dates(test_habit.name, datetime(2024, 11, 1).date())
        save_dates(test_habit.name, datetime(2024, 11, 2).date())
        save_dates(test_habit.name, datetime(2024, 11, 3).date())
        save_dates(test_habit.name, datetime(2024, 11, 5).date())
        save_dates(test_habit.name, datetime(2024, 11, 6).date())
        db.update_status_streak( test_habit1.name)
        db.update_status_streak( test_habit.name)
        ex_outcome =[test_habit.name , test_habit1.name]
        result = get_most_struggled_habits(db,inconsistency=4)
        assert result == ex_outcome



    def test_weekly_habits(self, db, test_habit1, test_habit):
        db.create_habit(name=test_habit.name, period='weekly', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        result = get_weekly_habits(db)
        ex_outcome = [test_habit.name ]
        assert result == ex_outcome


    def test_daily_habits(self, db, test_habit1, test_habit):
        db.create_habit(name=test_habit.name, period='weekly', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        result = get_daily_habits(db)
        ex_outcome = [test_habit1.name ]
        assert result == ex_outcome



    def test_completion_rate(self ,db , test_habit , test_habit1):
        db.create_habit(name=test_habit1.name, period='weekly', description='testing', duration=5, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak( test_habit1.name)
        rate1 = calculate_completion_rate(db)
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=100, day_week='day')
        rate2 = calculate_completion_rate(db)
        assert rate2== '50.0%'
        assert rate1 != rate2
