import os
import sys
import django
from django.conf import settings
import jwt
import requests
import datetime

# Add project root to sys.path
sys.path.append(r'd:\videepthaFoods\VideepthaWeb2\Veediptha_Website-backend')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Get a user (e.g. the first active user)
user = User.objects.first()
if not user:
    print("NO USER FOUND")
    sys.exit(1)

now_aware = datetime.datetime.utcnow()
exp_time = now_aware + datetime.timedelta(minutes=10)

access_payload = {
    'user_id': str(user.id),
    'exp': int(exp_time.timestamp()),
    'iat': int(now_aware.timestamp()),
    'jti': 'mock-jti-123',
    'iss': 'videeptha-auth',
    'aud': 'videeptha-app',
    'type': 'access'
}
access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

print("Fetching /api/accounts/me/ ...")
res_me = requests.get('http://localhost:8005/api/accounts/me/', headers={'Authorization': f'Bearer {access_token}'})
print(res_me.status_code, res_me.text)

print("\nFetching /api/orders/ ...")
res_orders = requests.get('http://localhost:8005/api/orders/', headers={'Authorization': f'Bearer {access_token}'})
print(res_orders.status_code, res_orders.text)

