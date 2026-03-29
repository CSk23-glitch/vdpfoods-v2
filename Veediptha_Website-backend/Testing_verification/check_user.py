import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

email = "ddevelop776@gmail.com"
user = User.objects.filter(email__iexact=email).first()

if user:
    print(f"User found: {user.email}")
    print(f"Is staff: {user.is_staff}")
    print(f"Is superuser: {user.is_superuser}")
    print(f"Is active: {user.is_active}")
    try:
        profile = user.profile
        print(f"Profile found: {type(profile).__name__}")
        if hasattr(profile, 'user_type'):
            print(f"User type: {profile.user_type}")
    except Exception as e:
        print(f"Error getting profile: {e}")
else:
    print(f"User not found: {email}")

# Check all users
print("\nAll Users:")
for u in User.objects.all():
    print(f"- {u.email} (Staff: {u.is_staff})")
