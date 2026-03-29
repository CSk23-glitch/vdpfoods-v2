import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import AdminProfile

User = get_user_model()

def configure_admins():
    emails = ['ddevelop776@gmail.com', 'videepthafoods1602@gmail.com']
    password = 'abcdefgh'

    for email in emails:
        user, created = User.objects.get_or_create(email=email, defaults={
            'username': email.split('@')[0],
        })
        
        if created:
            user.set_password('admin123')
            print(f"Created new Super Admin: {email} with default password 'admin123'. Please change this.")
        else:
            print(f"Verified existing Super Admin: {email}. Password unchanged.")
            
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        AdminProfile.objects.get_or_create(
            user=user,
            defaults={
                'user_type': 'super_admin'
            }
        )

if __name__ == '__main__':
    configure_admins()
