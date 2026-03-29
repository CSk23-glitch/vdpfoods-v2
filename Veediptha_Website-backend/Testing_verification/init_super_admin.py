import os
import django
import uuid

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User, AdminProfile, Address
from django.utils import timezone

def create_super_admin():
    email = "ddevelop776@gmail.com"
    username = "ddevelop"
    password = "admin123" # Simple, as requested by user previously or common dev pwd

    print(f"Creating Super Admin: {email}...")
    
    # Clean existing
    User.objects.filter(email__iexact=email).delete()
    
    # 1. Create User
    user = User.objects.create_superuser(
        email=email,
        username=username,
        password=password
    )
    
    # 2. Create Admin Profile
    profile = AdminProfile.objects.create(
        user=user,
        user_type='super_admin',
        plain_email=email,
        is_verified=True,
        profile_completed=True
    )
    profile.full_name = "Ddevelop Admin"
    profile.phone = "+919876543210"
    profile.save()
    
    # 3. Create Admin Address
    Address.objects.create(
        user=user,
        address_type='both',
        is_default=True,
        full_name="Ddevelop Office",
        phone="+919876543210",
        street_address="Village Admin Block",
        city="Agri Hub",
        state="Karnataka",
        pincode="560001",
        country="India"
    )
    
    print("\n[OK] Super Admin Created Successfully.")
    print(f"Login Email: {email}")
    print(f"Login Password: {password}")

if __name__ == "__main__":
    create_super_admin()
