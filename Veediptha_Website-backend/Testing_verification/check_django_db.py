import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def check_db():
    db_name = settings.DATABASES['default']['NAME']
    host = settings.DATABASES['default']['CLIENT']['host']
    print(f"DATABASE NAME: {db_name}")
    print(f"CLIENT HOST: {host}")
    
    from accounts.models import User
    count = User.objects.count()
    print(f"USER COUNT (Django): {count}")
    
    if count > 0:
        u = User.objects.first()
        print(f"FIRST USER: {u.email} | ID: {u.id} | Type: {type(u.id)}")

if __name__ == "__main__":
    check_db()
