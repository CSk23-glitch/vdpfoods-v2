import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def test_email():
    print(f"Using EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    try:
        send_mail(
            'SMTP Test',
            'This is a test email to verify SMTP configuration.',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER], # Send to self
            fail_silently=False,
        )
        print("Successfully sent test email!")
    except Exception as e:
        print(f"Failed to send email: {type(e).__name__}: {e}")

if __name__ == "__main__":
    test_email()
