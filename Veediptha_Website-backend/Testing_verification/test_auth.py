import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

email = "ddevelop776@gmail.com"
password = "Bhavana@1234"

user = User.objects.filter(email__iexact=email).first()
if user:
    authenticated_user = authenticate(email=user.email, password=password)
    if authenticated_user:
        print("Authentication SUCCESSful")
    else:
        print("Authentication FAILED (Wrong password)")
else:
    print(f"User not found: {email}")
