#%%
import firebase_admin
import pandas as pd
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_games():
    """
    Get all games from database
    
    Returns:
        list: list of games as dictionaries
    """
    result = []

    docs = db.collection(u'jogos').stream()
    for doc in docs:
        result.append(doc.to_dict())
    
    return result

def convert_to_pandas(games):
    """
    Convert games to pandas dataframe

    Args:
        games (list): list of games as dictionaries

    Returns:
        pandas.DataFrame: dataframe with games
    """
    df = pd.DataFrame(games)
    df = df.set_index("email")
    return df

def get_users():
    """
    Get all users from database
    
    Returns:
        list: list of users as dictionaries
    """
    result = []

    docs = db.collection(u'usuarios').stream()
    for doc in docs:
        result.append(doc.to_dict())
    
    return result

def convert_to_pandas_users(users):
    """
    Convert users to pandas dataframe

    Args:
        users (list): list of users as dictionaries

    Returns:
        pandas.DataFrame: dataframe with users
    """
    df = pd.DataFrame(users)
    df = df.set_index("email")
    return df