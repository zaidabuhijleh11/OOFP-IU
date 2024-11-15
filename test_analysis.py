from datetime import datetime , date
from habit import Habit
from habitDB import HabitDB
import pytest
from analysis import get_most_consistent_habits, get_most_struggled_habits, get_daily_habits, get_weekly_habits , calculate_completion_rate




class TestAnalysis:
    @pytest.fixture
    def test_habit(self):
        test_habit = Habit(name='zaid', period='daily', description='testing', streak=0,
                           broken_count=0, status='incomplete', created_at=datetime.now().date(), duration=100 , day_week="day" )
        return test_habit

    @pytest.fixture
    def test_habit1(self):
        test_habit1 = Habit(name='zaidabu', period='daily', description='testing', streak=0,
                            broken_count=0, status='incomplete', created_at=datetime.now().date(), duration=100 , day_week="day" )
        return test_habit1

    @pytest.fixture
    def db(self):
        return HabitDB()

    @pytest.fixture(autouse=True)
    def clean_db(self , db ):
        yield
        db.delete_all_habits()


    def test_get_most_consistent_habits(self , db  , test_habit , test_habit1):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=100, day_week='day')
        test_habit1.completed_dates= [date(2024, 9, 30), date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 3), date(2024, 10, 4),
                date(2024, 10, 5), date(2024, 10, 6), date(2024, 10, 7)]
        test_habit.completed_dates= [date(2024, 9, 30), date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 4),
                date(2024, 10, 5), date(2024, 10, 6), date(2024, 10, 7)]
        db.update_status_streak(test_habit1 , test_habit1.name)
        db.update_status_streak(test_habit , test_habit.name)
        ex_outcome =[test_habit1.name ,test_habit.name ]
        result = get_most_consistent_habits(  db ,consistency=4)
        assert result == ex_outcome


    def test_get_most_struggled_habits(self , db  , test_habit , test_habit1):
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        test_habit1.completed_dates= [date(2024, 9, 30), date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 3), date(2024, 10, 4),
                date(2024, 10, 5), date(2024, 10, 6), date(2024, 10, 7)]
        test_habit.completed_dates= [date(2024, 9, 30), date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 4),
                date(2024, 10, 5), date(2024, 10, 6), date(2024, 10, 7)]
        db.update_status_streak(test_habit1, test_habit1.name)
        db.update_status_streak(test_habit, test_habit.name)
        ex_outcome =[test_habit.name , test_habit1.name]
        result = get_most_struggled_habits(db,inconsistency=4)
        assert result == ex_outcome



    def test_weekly_habits(self, db, test_habit1, test_habit):

        db.create_habit(name=test_habit.name, period='weekly', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        result = get_weekly_habits(db)
        ex_outcome = ['zaid']
        assert result == ex_outcome


    def test_daily_habits(self, db, test_habit1, test_habit):

        db.create_habit(name=test_habit.name, period='weekly', description='testing', duration=100, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        result = get_daily_habits(db)
        ex_outcome = [test_habit1.name ]
        assert result == ex_outcome



    def test_completion_rate(self ,db , test_habit , test_habit1):

        db.create_habit(name=test_habit.name, period='weekly', description='testing', duration=5, day_week='day')
        test_habit.completed_dates = [date(2024, 9, 30), date(2024, 10, 1), date(2024, 10, 2), date(2024, 10, 3), date(2024, 10, 4),
        date(2024, 10, 5)]
        db.update_status_streak(test_habit , test_habit.name)
        rate1 = calculate_completion_rate(db)
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        rate2 = calculate_completion_rate(db)
        assert rate2== '50.0%'
        assert rate1 != rate2
