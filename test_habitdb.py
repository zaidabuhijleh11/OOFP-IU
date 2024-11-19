from datetime import  datetime ,date
import pytest
from habitDB import HabitDB
from habit import Habit
import pickle
from Dates_Persistence import save_dates , load_dates

class TestHabitDB:

    @pytest.fixture
    def test_habit(self):
        test_habit = Habit(name='zaidabuhijleh', period='daily', description='testing', streak=0, broken_count=0, status='incomplete', created_at=datetime.now().date(), duration=100,day_week="day")
        return test_habit

    @pytest.fixture
    def test_habit1(self):
        test_habit1 = Habit(name='zaid', period='daily', description='testing', streak=0,
                            broken_count=0, status='incomplete', created_at=datetime.now().date(), duration=100 , day_week="day" )
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

    def test_habit_exists(self , db , test_habit1):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        habit_exists = db.habit_exists(test_habit1.name)
        assert habit_exists == True
        assert db.habit_exists("zaid abu ") == False

    def test_create_habit(self,db):
        name = 'zaid'
        habits = db.get_habits()
        habits_count = len(habits)
        db.create_habit(name=name, period='daily', description='testing', duration=100, day_week='day')
        habit_new = db.get_habits()
        habits_new_count = len(habit_new)
        assert habits_new_count == habits_count + 1
        assert name in [x[0] for x in habit_new]

    def test_delete_habit(self, test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        db.delete_habit(test_habit1.name)
        after_deletion_habits = db.get_habits()
        assert test_habit1.name not in after_deletion_habits

    def test_get_completed_habits(self, test_habit1 ,db):
        initial = db.get_completed_habits()
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=5, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak(test_habit1.name)
        completed = db.get_completed_habits()
        assert test_habit1.name in completed
        assert len(completed) == len(initial) + 1

    def test_get_incomplete_habits(self, test_habit1 , db ):
        initial = db.get_incomplete_habits()
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=100, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak( test_habit1.name)
        incomplete = db.get_incomplete_habits()
        assert test_habit1.name in [habit for habit in incomplete]
        assert len(incomplete) == len(initial) + 1



    def test_get_streak(self, test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=6, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak( test_habit1.name)
        ex_outcome = db.get_streak(test_habit1.name)
        assert ex_outcome == 5


    def test_get_habits(self,test_habit, test_habit1 , db ):
        initial = db.get_habits()
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=6, day_week='day')
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=6, day_week='day')
        habits = db.get_habits()
        assert len(habits) == len(initial) + 2
        assert test_habit.name in [name[0] for name in habits ]
        assert test_habit1.name in [name[0] for name in habits]

    def test_update_description(self, test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=6, day_week='day')
        initial_desc = db.get_description(test_habit1.name)
        assert initial_desc == 'testing'
        db.update_description(test_habit1.name , 'new desc')
        new_desc = db.get_description(test_habit1.name)
        assert new_desc == 'new desc'
        assert new_desc != initial_desc





    def test_update_period(self, test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=6, day_week='day')
        initial_period = db.get_period(test_habit1.name)
        db.update_period( test_habit1.name , 10 , 'day' )
        new_period = db.get_period(test_habit1.name)
        assert new_period == 'weekly'
        assert new_period != initial_period



    def test_update_streak(self, test_habit1 , db ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak(test_habit1.name)
        streak = db.get_streak(test_habit1.name)
        assert streak == 5

    def test_update_streak2(self, db,test_habit1  ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 4).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        save_dates(test_habit1.name, datetime(2024, 11, 7).date())
        save_dates(test_habit1.name, datetime(2024, 11, 8).date())
        save_dates(test_habit1.name, datetime(2024, 11, 9).date())
        save_dates(test_habit1.name, datetime(2024, 11, 10).date())
        save_dates(test_habit1.name, datetime(2024, 11, 11).date())
        db.update_status_streak(test_habit1.name)
        streak = db.get_streak(test_habit1.name)
        completed_habit = db.get_completed_habits()
        assert streak == 10
        assert test_habit1.name in completed_habit

    def test_update_streak3(self, db,test_habit1  ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        save_dates(test_habit1.name, datetime(2024, 11, 1).date())
        save_dates(test_habit1.name, datetime(2024, 11, 2).date())
        save_dates(test_habit1.name, datetime(2024, 11, 3).date())
        save_dates(test_habit1.name, datetime(2024, 11, 5).date())
        save_dates(test_habit1.name, datetime(2024, 11, 6).date())
        db.update_status_streak(test_habit1.name)
        broken_count_post = db.get_broken_count(test_habit1.name)
        assert broken_count_post  == 1

    def test_delete_all_habits(self , db , test_habit1 , test_habit):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        db.create_habit(name=test_habit.name, period='daily', description='testing', duration=10, day_week='day')
        pre_count = db.get_habits()
        db.delete_all_habits()
        post = db.get_habits()
        assert len(post) == 0
        assert len(pre_count) == len(post) +2


# test edge cases

    def test_create_habit_that_exists(self , db  ):
        name = 'omara dszaid '
        db.create_habit(name=name, period='daily', description='testing', duration=10, day_week='day')
        with pytest.raises(ValueError):
           db.create_habit(name=name, period='daily', description='testing', duration=10, day_week='day')

    def test_delete_non_existing_habit(self , db ):
        name = 'omara dszaid '
        db.create_habit(name=name, period='daily', description='testing', duration=10, day_week='day')
        db.delete_habit(name)
        with pytest.raises(ValueError):
            db.delete_habit(name)

    def test_update_description_non_existing_habit(self , db , test_habit1 ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        db.delete_all_habits()
        with pytest.raises(ValueError):
            db.update_description(test_habit1.name , 'zaid ' )

    def test_update_period_of_non_existing_habit(self , db , test_habit1 ):
        db.create_habit(name=test_habit1.name, period='daily', description='testing', duration=10, day_week='day')
        db.delete_all_habits()
        with pytest.raises(ValueError):
            db.update_period(test_habit1.name , 10 , 'day')

    def test_update_streak_status_non_existing_habit(self , db , test_habit1 ):
        db.create_habit(name=test_habit1.name , period='daily', description='testing', duration=10, day_week='day')
        db.delete_all_habits()
        with pytest.raises(ValueError):
            db.update_status_streak( test_habit1.name)
