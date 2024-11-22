import pickle

def save_dates(name:str, date)->None :
    """Save dates in the files 
    Args: 
       name (str):name of the habit
       date (datetime object) : date that you want to add """
    file_name = f"{name}_dates.pkl"
    try:
        with open(file_name, 'rb') as file:
            done_dates = pickle.load(file)
    except FileNotFoundError:
        done_dates = []
    done_dates.append(date)
    with open(file_name, 'wb') as file:
        pickle.dump(done_dates, file)


def load_dates(name:str) -> list:
    """Load dates
    Args: 
        name(str) : name of the habit"""
    file_name = f"{name}_dates.pkl"
    try:
        with open(file_name, 'rb') as file:
            done_dates = pickle.load(file)
        return done_dates
    except FileNotFoundError:
        return []

def delete_dates(name:str )->None :
    """Delete the file contents  if the habit got deleted so if the user want to create
    the same habit later  he will not have an issue
    Args:
       name:(str) name of the habit 
    Raises:
       None 
    
    Return:
      None 
    """
    file_name= f"{name}_dates.pkl"
    with open(file_name,'wb') as a:
        pickle.dump([],a)


