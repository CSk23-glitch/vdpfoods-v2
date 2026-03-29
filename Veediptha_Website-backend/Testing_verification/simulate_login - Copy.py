import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import RequestFactory
from accounts.views import EmailLoginView
from django.contrib.auth import get_user_model

User = get_user_model()
factory = RequestFactory()

email = "ddevelop776@gmail.com"
password = "Bhavana@1234"

view = EmailLoginView.as_view()
request = factory.post('/api/accounts/login/', 
                       data=json.dumps({
                           'email': email,
                           'password': password,
                           'portal': 'admin'
                       }),
                       content_type='application/json')

response = view(request)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.data}")
