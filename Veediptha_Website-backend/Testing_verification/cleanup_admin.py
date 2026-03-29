import os
import django
from pymongo import MongoClient
from django.conf import settings
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def inspect_and_reset():
    uri = settings.MONGODB_URI
    db_name = settings.MONGODB_DB
    client = MongoClient(uri)
    db = client[db_name]

    print("\n--- AUTH_USER IDS ---")
    for u in db['auth_user'].find():
        print(f"Email: {u.get('email')} | _id: {u.get('_id')} (Type: {type(u.get('_id'))})")

    print("\n--- RESETTING PASSWORD ---")
    User = get_user_model()
    try:
        user = User.objects.get(email='ddevelop776@gmail.com')
        user.set_password('abcdefgh')
        user.save()
        print(f"SUCCESS: Password reset for {user.email}")
        print(f"User ID (Django): {user.id} (Type: {type(user.id)})")
    except User.DoesNotExist:
        print("ERROR: User ddevelop776@gmail.com not found in Django.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    inspect_and_reset()
