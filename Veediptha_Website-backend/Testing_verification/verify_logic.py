import os
import django
import sys
from unittest.mock import patch

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User
from accounts.views import EmailLoginView
from rest_framework.test import APIRequestFactory

def verify():
    factory = APIRequestFactory()
    view = EmailLoginView.as_view()
    
    admin = User.objects.filter(is_staff=True).first()
    cust = User.objects.filter(is_staff=False).first()
    
    if not admin or not cust:
        print("Required test users not found.")
        return

    print(f"Admin: {admin.email}")
    print(f"Customer: {cust.email}")

    print("\n--- Test 1: Admin trying Website Portal ---")
    with patch('accounts.views.authenticate', return_value=admin):
        req = factory.post('/api/accounts/login/', {'email': admin.email, 'password': 'any', 'portal': 'website'})
        res = view(req)
        print(f"Status: {res.status_code}")
        print(f"Content: {res.data}")
        assert res.status_code == 403
        assert "Admin account detected" in res.data['error']

    print("\n--- Test 2: Customer trying Admin Portal ---")
    with patch('accounts.views.authenticate', return_value=cust):
        req = factory.post('/api/accounts/login/', {'email': cust.email, 'password': 'any', 'portal': 'admin'})
        res = view(req)
        print(f"Status: {res.status_code}")
        print(f"Content: {res.data}")
        assert res.status_code == 403
        assert "requires staff privileges" in res.data['error']

    print("\n--- Test 3: Admin trying Admin Portal ---")
    with patch('accounts.views.authenticate', return_value=admin):
        req = factory.post('/api/accounts/login/', {'email': admin.email, 'password': 'any', 'portal': 'admin'})
        res = view(req)
        print(f"Status: {res.status_code}")
        assert res.status_code == 200
        print("Success: Admin allowed on Admin portal")

    print("\n--- Test 4: Customer trying Website Portal ---")
    with patch('accounts.views.authenticate', return_value=cust):
        req = factory.post('/api/accounts/login/', {'email': cust.email, 'password': 'any', 'portal': 'website'})
        res = view(req)
        print(f"Status: {res.status_code}")
        assert res.status_code == 200
        print("Success: Customer allowed on Website portal")

    print("\nALL TESTS PASSED!")

if __name__ == "__main__":
    verify()
