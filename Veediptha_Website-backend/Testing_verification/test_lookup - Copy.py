import os
import django
import sys

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def test_lookup(email):
    print(f"Testing lookup for: '{email}'")
    user = User.objects.filter(email=email).first()
    if user:
        print(f"Found user: {user.email} (ID: {user.id})")
    else:
        print("User not found with exact match.")
        
    # Test case-insensitive
    user_ie = User.objects.filter(email__iexact=email).first()
    if user_ie:
        print(f"Found user (case-insensitive): {user_ie.email} (ID: {user_ie.id})")
    else:
        print("User not found even with case-insensitive match.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_lookup(sys.argv[1])
    else:
        print("Please provide an email to test.")
