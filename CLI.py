from datetime import datetime
from habit import Habit
from habitDB import HabitDB
from analysis import get_most_consistent_habits, get_most_struggled_habits, get_daily_habits, get_weekly_habits , calculate_completion_rate , visualization_performance_for_a_habit,report
from Dates_Persistence import load_dates ,save_dates
class CLI:
    def __init__(self):
        self.db = HabitDB()
        self.habit_ins = Habit(name='zaid', period='daily', description='erf',streak=0, broken_count=0, status='incomplete',created_at=datetime.now().date())

    def main_menu(self):
        while True:
            print("\nHabit Tracker Main Menu:")
            print("1. Create a new habit")
            print("2. Delete a habit")
            print("3. Mark a habit as completed today")
            print("4. View habit streak")
            print("5. View habit broken count")
            print("6. View all completed habits")
            print("7. View all incomplete habits")
            print("8. View the longest streak")
            print("9. View habit description")
            print("10. View habit period")
            print("11. View all habits")
            print("12. Delete all habits")
            print("13. Update habit period")
            print("14. Update habit description")
            print("15. Update habit streak and status")
            print("16. View the longest habit streak in history")
            print("17. View completion rate")
            print("18. Visualize performance")
            print("19. View most consistent habit")
            print("20. View most struggled habit")
            print("21. View weekly habits")
            print("22. View daily habits")
            print("23. Generate a progress report")
            print("24. completed dates of a habit ")
            print("25.exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter habit name: ").strip()
                period = input("Enter period (daily/weekly): ").strip()
                description = input("Enter description: ").strip()
                duration = int(input("Enter duration: "))
                day_week = input("Enter 'day' or 'week': ").strip()
                self.db.create_habit(name, period, description, duration, day_week)
                print(f"Successfully created the habit {name} and saved into the db .")

            elif choice == "2":
                name = input("Enter the name of the habit to delete: ").strip()
                self.db.delete_habit(name)
                print(f"Successfully deleted the habit '{name}'.")

            elif choice == "3":
                 name = input("Enter the name of the habit completed today: ").strip()
                 self.habit_ins.habit_is_done_today(name)
                 print(f"Successfully marked {name} as completed today.")

            elif choice == "4":
                name = input("Enter the name of the habit to view its streak: ").strip()
                print(f"Streak: {self.db.get_streak(name)}")


            elif choice == "5":
                name = input("Enter the name of the habit to view its broken count: ").strip()
                print(f"Broken Count: {self.db.get_broken_count(name)}")

            elif choice == "6":
                print("Completed habits:",self.db.get_completed_habits())


            elif choice == "7":
                print("Incomplete habits:", self.db.get_incomplete_habits())


            elif choice == "8":
                print("Longest streak of all habits:", self.db.longest_streak())

            elif choice == "9":
                name = input("Enter the name of the habit to view its description: ").strip()
                print(f"Description: {self.db.get_description(name)}")


            elif choice == "10":
                name = input("Enter the name of the habit to view its period: ").strip()
                print(f"Period: {self.db.get_period(name)}")


            elif choice == "11":
                print("All habits:", self.db.get_habits())


            elif choice == "12":
                self.db.delete_all_habits()
                print("All habits deleted.")
                print("Successfully deleted all habits.")

            elif choice == "13":
                name = input("Enter the name of the habit to update its period: ").strip()
                duration = int(input("Enter the new duration: "))
                day_week = input("Enter 'day' or 'week': ").strip()
                self.db.update_period( name ,duration, day_week)
                print(f"Successfully updated the period for '{name}'.")

            elif choice == "14":
                name = input("Enter the name of the habit to update its description: ").strip()
                new_desc = input("Enter the new description: ").strip()
                self.db.update_description( new_desc, name)
                print(f"Successfully updated the description for '{name}'.")

            elif choice == "15":
                name = input("Enter the name of the habit to update its streak and status: ").strip()

                self.db.update_status_streak(name)
                print(f"Successfully updated the streak and status for '{name}'.")

            elif choice == "16":
                name = input("Enter a habit name: ").strip()
                if name in [habit[0] for habit in self.db.get_habits()]:
                    print("Longest streak in history:", self.habit_ins.longest_run_streak_for_a_given_habit(name))


            elif choice == "17":
                print("Completion rate:", calculate_completion_rate(self.db))

            elif choice == "18":
                visualization_performance_for_a_habit(self.db)
                print("Successfully visualized the performance.")

            elif choice == "19":
                consistency = int(input("how many broken counts to consider a habit is consistent:"))
                print("Most consistent habit:", get_most_consistent_habits(self.db , consistency))


            elif choice == "20":
                inconsistency = int(input("how many broken counts to consider a habit is inconsistent: "))
                print("Most struggled habit:", get_most_struggled_habits(self.db , inconsistency))


            elif choice == "21":
                print("Weekly habits:", get_weekly_habits(self.db))


            elif choice == "22":
                print("Daily habits:", get_daily_habits(self.db))


            elif choice == "23":
                consistency = int(input("how many broken counts to consider a habit is consistent:"))
                inconsistency = int(input("how many broken counts to consider a habit is inconsistent: "))
                print(f"OverView Report:{report(self.db , consistency,inconsistency)}")

            elif choice=='24':
                name = input("enter a name:")
                if self.db.habit_exists(name):
                    print(f"Completed dates of {name}:{load_dates(name)}")


            elif choice == "25":
                print("Exiting...")
                break

            else:
                print("Invalid selection, please try again.")

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    cli = CLI()
    cli.run()
