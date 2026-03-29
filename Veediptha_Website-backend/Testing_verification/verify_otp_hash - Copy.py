import os
import django
import sys
import hashlib

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from accounts.models import OTPStore

User = get_user_model()

def verify_stored_otp(email, otp_input):
    print(f"Verifying OTP '{otp_input}' for user '{email}'")
    user = User.objects.filter(email__iexact=email).first()
    if not user:
        print(f"FAIL: User '{email}' not found.")
        return

    otp_store = OTPStore.objects.filter(user=user).first()
    if not otp_store:
        print(f"FAIL: No OTP record for {user.email}")
        return

    input_hash = hashlib.sha256(str(otp_input).encode()).hexdigest()
    print(f"Input Hash:  {input_hash}")
    print(f"Stored Hash: {otp_store.otp_hash}")
    
    if input_hash == otp_store.otp_hash:
        print("PASS: Hashes match!")
    else:
        print("FAIL: Hashes do NOT match.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        verify_stored_otp(sys.argv[1], sys.argv[2])
    else:
        verify_stored_otp("ddevelop776@gmail.com", "517879")
