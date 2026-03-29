import os
import django
import sys
from django.utils import timezone

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import OTPStore

User = get_user_model()

def inspect_users_and_otps():
    print("--- User Accounts ---")
    users = User.objects.all()
    for u in users:
        print(f"ID: {u.id}, Email: {u.email}, Username: {u.username}, Is Staff: {u.is_staff}")
    
    print("\n--- OTP Store ---")
    otps = OTPStore.objects.all()
    for o in otps:
        print(f"User Email: {o.user.email}, Type: {o.otp_type}, Expires: {o.otp_expires_at}, Attempts: {o.attempts}")
        if o.otp_expires_at < timezone.now():
            print("  [EXPIRED]")

if __name__ == "__main__":
    inspect_users_and_otps()
