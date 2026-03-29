import os
import django
import sys

# Setup Django
sys.path.append('d:\\GoogeAntigravity\\FreelanceProjectDirectory\\backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Story, Page
from api.serializers import StorySerializer, PageSerializer
import json
from bson import ObjectId

def test_single_story():
    print("Fetching one story...")
    story = Story.objects.first()
    if not story:
        print("No stories found.")
        return
    
    print(f"Serializing story: {story.id}")
    try:
        serializer = StorySerializer(story)
        data = serializer.data
        print("Serialization SUCCESS!")
        print(f"Data Sample: {str(data)[:500]}")
    except Exception as e:
        print(f"Serialization FAILED: {e}")
        import traceback
        traceback.print_exc()

def test_single_page():
    print("\nFetching one page...")
    page = Page.objects.first()
    if not page:
        print("No pages found.")
        return
    
    print(f"Serializing page: {page.id}")
    try:
        serializer = PageSerializer(page)
        data = serializer.data
        print("Serialization SUCCESS!")
        print(f"Data Sample: {str(data)[:500]}")
    except Exception as e:
        print(f"Serialization FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_single_story()
    test_single_page()
