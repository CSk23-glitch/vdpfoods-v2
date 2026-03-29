import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import AdminProfile

User = get_user_model()

def setup_admin():
    email = "ddevelop776@gmail.com"
    password = "abcdefgh"
    
    # Check if user exists
    user, created = User.objects.get_or_create(email=email, defaults={'username': "admin_dev"})
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    
    # Setup Profile
    profile, p_created = AdminProfile.objects.get_or_create(user=user)
    profile.user_type = 'super_admin'
    profile.plain_email = email
    profile.is_verified = True
    profile.save()
    
    print(f"User {email} {'created' if created else 'updated'} and set as Admin.")

if __name__ == "__main__":
    setup_admin()
