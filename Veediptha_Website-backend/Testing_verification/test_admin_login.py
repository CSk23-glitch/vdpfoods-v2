import os
import django
from django.contrib.auth import authenticate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def test_login(email, password):
    print(f"Attempting to authenticate user: {email}")
    user = authenticate(username=email, password=password)
    if user:
        print(f"SUCCESS: User {email} authenticated correctly.")
        print(f"User Details: Staff={user.is_staff}, Superuser={user.is_superuser}")
    else:
        print(f"FAILURE: Authentication failed for {email}.")
        # Check if user exists but password mismatch
        from accounts.models import User
        try:
            u = User.objects.get(email=email)
            print(f"INFO: User exists in DB, but authentication failed (likely password mismatch).")
        except User.DoesNotExist:
            print(f"INFO: User does not exist in DB.")

if __name__ == "__main__":
    test_login('ddevelop776@gmail.com', 'abcdefgh')
