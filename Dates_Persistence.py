import pickle

def save_dates(name, date):
    file_name = f"{name}_dates.pkl"
    try:
        with open(file_name, 'rb') as file:
            done_dates = pickle.load(file)
    except FileNotFoundError:
        done_dates = []
    done_dates.append(date)
    with open(file_name, 'wb') as file:
        pickle.dump(done_dates, file)


def load_dates(name):
    file_name = f"{name}_dates.pkl"
    try:
        with open(file_name, 'rb') as file:
            done_dates = pickle.load(file)
        return done_dates
    except FileNotFoundError:
        return []

def delete_dates(name:str ):
    file_name= f"{name}_dates.pkl"
    with open(file_name,'wb') as a:
        pickle.dump([],a)
