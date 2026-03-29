import os
import django
from django.conf import settings
from mongoengine import connect

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from api.models import Product, Category, Story, Coupon, Hero, Navigation, Theme, Policy, Promotion, SupportTicket
from accounts.models import AdminProfile, CustomerProfile, RefreshToken

User = get_user_model()

def inspect_db():
    print("="*50)
    print("DATABASE AUDIT REPORT")
    print("="*50)

    # 1. Authentication & Users
    print("\n[1] AUTHENTICATION & USERS")
    print(f"Total Users: {User.objects.count()}")
    for user in User.objects.all():
        roles = []
        if user.is_staff: roles.append("Staff")
        if user.is_superuser: roles.append("Superuser")
        
        profile_type = "No Profile"
        try:
            if hasattr(user, 'profile'):
                profile_type = type(user.profile).__name__
        except:
            pass
            
        print(f"- {user.email} (Username: {user.username}, Roles: {', '.join(roles) or 'User'}, Profile: {profile_type})")

    # 2. Products & Categories
    print("\n[2] PRODUCTS & CATEGORIES")
    print(f"Total Categories: {Category.objects.count()}")
    for cat in Category.objects.all():
        print(f"- Category: {cat.name} (Slug: {cat.slug})")
        
    print(f"Total Products: {Product.objects.count()}")
    for prod in Product.objects.all():
        print(f"- Product: {prod.name} (Price: {prod.price}, Category: {prod.category.name if prod.category else 'None'})")

    # 3. Content & Stories
    print("\n[3] CONTENT & STORIES")
    print(f"Total Stories: {Story.objects.count()}")
    for story in Story.objects.all():
        print(f"- Story: {story.title} (Author: {story.author})")
        
    print(f"Total Pages: {Hero.objects.count()} (Hero sections count)")
    
    # 4. Marketing & Promotions
    print("\n[4] MARKETING & PROMOTIONS")
    print(f"Total Coupons: {Coupon.objects.count()}")
    for coupon in Coupon.objects.all():
        print(f"- Coupon: {coupon.code} (Value: {coupon.discount_value}, Type: {coupon.discount_type})")
        
    print(f"Total Promotions: {Promotion.objects.count()}")
    for promo in Promotion.objects.all():
        print(f"- Promotion: {promo.title} (Type: {promo.target_type})")

    # 5. Infrastructure Check
    print("\n[5] INFRASTRUCTURE")
    print(f"Total Policies: {Policy.objects.count()}")
    print(f"Total Support Tickets: {SupportTicket.objects.count()}")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    inspect_db()
