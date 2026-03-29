import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Page, Product, Category, Story, Hero

def activate_all():
    print("Activating all content...")
    
    # Update Products (No validation issues expected)
    products = Product.objects.all()
    for p in products:
        p.is_active = True
        p.save()
    print(f"Updated {products.count()} products.")

    # Update Categories
    categories = Category.objects.all()
    for c in categories:
        c.is_active = True
        c.save()
    print(f"Updated {categories.count()} categories.")

    # Update Stories
    stories = Story.objects.all()
    for s in stories:
        s.is_active = True
        s.save()
    print(f"Updated {stories.count()} stories.")

    # Update Pages (Use validate=False to bypass missing block IDs in legacy data)
    pages = Page.objects.all()
    for p in pages:
        p.is_active = True
        p.status = "published"
        p.save(validate=False)
    print(f"Updated {pages.count()} pages (pre-validation bypassed).")

    print("Success: All content is now active and published.")

if __name__ == "__main__":
    activate_all()
