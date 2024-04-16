from models.state import State
from models.city import City
from models.user import User
from models.engine.db_storage import DBStorage
import os

os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'



def test_db_storage():
    # Create an instance of DBStorage
    db_storage = DBStorage()
    
    # Reload the database
    db_storage.reload()
    
    # Create and save State, City, and User objects
    state_obj = State(name='California')
    db_storage.new(state_obj)
    
    city_obj = City(name='San Francisco', state_id=state_obj.id)
    db_storage.new(city_obj)
    
    # Save changes to the database
    db_storage.save()
    
    # Query objects from the database and verify their presence
    all_states = db_storage.all(State)
    assert state_obj.id in all_states
    assert all_states[state_obj.id].name == 'California'
    
    all_cities = db_storage.all(City)
    assert city_obj.id in all_cities
    assert all_cities[city_obj.id].name == 'San Francisco'
    assert all_cities[city_obj.id].state_id == state_obj.id
    

if __name__ == "__main__":
    test_db_storage()
    print("All tests passed successfully!")
