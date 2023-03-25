from django.conf import settings
from models import * 
import datetime

if not settings.configured:
    settings.configure()

def write_user():
    user_john = User(first_name='John', last_name='Doe', dob=datetime.date(1962, 7, 16))
    user_john.save()

def run():
    write_user()
