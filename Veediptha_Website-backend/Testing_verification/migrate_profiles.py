import os
import django
import sys
import uuid

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User, AdminProfile, CustomerProfile

def migrate_users():
    users = User.objects.all()
    print(f"Found {users.count()} users total.")
    
    for u in users:
        # Check if profile exists already
        if u.profile:
            print(f"User {u.email} already has a {u.profile.__class__.__name__}")
            continue
            
        if u.is_staff or u.is_superuser:
            # Create Admin Profile
            AdminProfile.objects.create(
                user=u,
                plain_email=u.email,
                user_type='super_admin' if u.is_superuser else 'assistant_admin',
                is_verified=True,
                profile_completed=True
            )
            print(f"Created AdminProfile for {u.email}")
        else:
            # Create Customer Profile
            CustomerProfile.objects.create(
                user=u,
                plain_email=u.email,
                is_verified=True,
                profile_completed=True
            )
            print(f"Created CustomerProfile for {u.email}")

if __name__ == "__main__":
    migrate_users()
