#!/usr/bin/python3
''' module for file_storage tests '''
import os
import unittest
from datetime import datetime
import MySQLdb
from models import storage
from models.user import User

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db_storage test not supported')
class TestDBStorage(unittest.TestCase):
    '''Testing DBStorage engine'''

    def setUp(self):
        """Set up method for each test"""
        self.db_host = os.getenv('HBNB_MYSQL_HOST')
        self.db_user = os.getenv('HBNB_MYSQL_USER')
        self.db_pwd = os.getenv('HBNB_MYSQL_PWD')
        self.db_name = os.getenv('HBNB_MYSQL_DB')

    def test_new_and_save(self):
        '''Test the new and save methods'''
        db = MySQLdb.connect(user=self.db_user, host=self.db_host, passwd=self.db_pwd, port=3306, db=self.db_name)
        new_user = User(email='testuser1@example.com', password='pass123', first_name='John', last_name='Doe')
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=self.db_user, host=self.db_host, passwd=self.db_pwd, port=3306, db=self.db_name)
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()

    def test_save_to_database(self):
        """Test saving an object to the database"""
        new_user = User(email='testuser5@example.com', password='pass111', first_name='Mike', last_name='Williams')
        dbc = MySQLdb.connect(host=self.db_host, port=3306, user=self.db_user, passwd=self.db_pwd, db=self.db_name)
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users;')
        old_cnt = cursor.fetchone()[0]
        self.assertTrue(result is None)
        self.assertFalse(new_user in storage.all().values())
        new_user.save()
        dbc1 = MySQLdb.connect(host=self.db_host, port=3306, user=self.db_user, passwd=self.db_pwd, db=self.db_name)
        cursor1 = dbc1.cursor()
        cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor1.fetchone()
        cursor1.execute('SELECT COUNT(*) FROM users;')
        new_cnt = cursor1.fetchone()[0]
        self.assertFalse(result is None)
        self.assertEqual(old_cnt + 1, new_cnt)
        self.assertTrue(new_user in storage.all().values())
        cursor1.close()
        dbc1.close()
        cursor.close()
        dbc.close()

    def test_delete_user(self):
        """Test deleting a user from the database"""
        new_user = User(email='testuser3@example.com', password='pass789', first_name='Bob', last_name='Johnson')
        obj_key = 'User.{}'.format(new_user.id)
        dbc = MySQLdb.connect(host=self.db_host, port=3306, user=self.db_user, passwd=self.db_pwd, db=self.db_name)
        new_user.save()
        self.assertTrue(new_user in storage.all().values())
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('testuser3@example.com', result)
        self.assertIn('pass789', result)
        self.assertIn('Bob', result)
        self.assertIn('Johnson', result)
        self.assertIn(obj_key, storage.all(User).keys())
        new_user.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())
        cursor.close()
        dbc.close()

    def test_reload_database(self):
        """Test reloading the database session"""
        dbc = MySQLdb.connect(host=self.db_host, port=3306, user=self.db_user, passwd=self.db_pwd, db=self.db_name)
        cursor = dbc.cursor()
        cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password, first_name, last_name) ' +
            'VALUES(%s, %s, %s, %s, %s, %s, %s);',
            ['4447-by-me', str(datetime.now()), str(datetime.now()), 'testuser4@example.com', 'pass101', 'Jane', 'Doe']
        )
        self.assertNotIn('User.4447-by-me', storage.all())
        dbc.commit()
        storage.reload()
        self.assertIn('User.4447-by-me', storage.all())
        cursor.close()
        dbc.close()

    def test_add_new_user(self):
        """Test adding a new user to the database"""
        new_user = User(email='testuser2@example.com', password='pass456', first_name='Alice', last_name='Smith')
        self.assertFalse(new_user in storage.all().values())
        new_user.save()
        self.assertTrue(new_user in storage.all().values())

        dbc = MySQLdb.connect(host=self.db_host, port=3306, user=self.db_user, passwd=self.db_pwd, db=self.db_name)
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('testuser2@example.com', result)
        self.assertIn('pass456', result)
        self.assertIn('Alice', result)
        self.assertIn('Smith', result)
        cursor.close()
        dbc.close()

if __name__ == "__main__":
    unittest.main()
