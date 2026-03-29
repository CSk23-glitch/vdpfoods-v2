import os
import django
import sys
import random

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import OTPStore
from accounts.views import set_otp
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

def verify_reset_logic(email):
    print(f"Simulating reset request for: '{email}'")
    # Exact logic from view:
    user = User.objects.filter(email__iexact=email).first() or User.objects.filter(username__iexact=email).first()
    
    if user:
        print(f"PASS: User found: {user.email}")
        otp = str(random.randint(100000, 999999))
        if set_otp(user, otp, 'reset'):
            print(f"PASS: OTP {otp} set in DB for {user.email}")
            try:
                if settings.EMAIL_HOST_USER:
                    send_mail('Reset Password Test', f"Code: {otp}", settings.EMAIL_HOST_USER, [user.email])
                    print(f"PASS: Email sent to {user.email}")
                else:
                    print("SKIP: EMAIL_HOST_USER not set")
            except Exception as e:
                print(f"FAIL: Email failed: {e}")
        else:
            print("FAIL: Failed to set OTP in DB")
    else:
        print("FAIL: User not found with iexact lookup!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_reset_logic(sys.argv[1])
    else:
        # Test with the known user but different casing
        verify_reset_logic("Bhavanashiva2025@gmail.com")
