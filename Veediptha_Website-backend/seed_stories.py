import os
import django
import sys
import json

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Story

pinned_stories = [
    {
        "name": "Vidya",
        "signature": "Vidya Shree",
        "content": "<p class=\"mb-4\">Our elders taught us how to live and eat. I realised sooner, hope you do as well.</p><p class=\"mb-4\">As a food lover, my question was big, but small enough to understand.</p><p class=\"mb-4 text-xl font-bold text-[var(--color-primary)]\">Why can't a marriage between tasty & healthy happen?</p><p class=\"mb-4\">I grew up eating millets and then from the past two years, I was working hard on how to reach everyone with this marriage alliance, which universally can be celebrated.</p><p class=\"mb-4\">Walk just a step ahead and join hands against Diabetes, weaker immune system & fat-related problems, and many more.</p>"
    },
    {
        "name": "Pradeep",
        "signature": "P V Pradeep",
        "content": "<p class=\"mb-4\">When initially I refused to incorporate millets in my daily life,</p><p class=\"mb-4\">My partner shared with me a simple but huge knowledge — <strong class=\"text-[var(--color-primary)]\">what millets are</strong>.</p><p class=\"mb-4\">Then now I'm replacing well with our products from the past few years.</p><p class=\"mb-4 text-xl font-bold text-[var(--color-primary)]\">As the changes must start from our own house.</p><p class=\"mb-4\">My step towards reality, healthy, fit and gut-friendly life has started.</p><p class=\"mb-4\">Do you? Let us know.</p>"
    }
]

customer_stories = [
    { "name": "Pradeep", "text": "For Deepavali, I wanted sweets my parents could enjoy without worrying about BP and sugar levels. I ordered millet sweets and halwa here, and the taste surprised everyone at home. Healthy, traditional, and truly satisfying." },
    { "name": "Selvi", "text": "As a mother, I'm always searching for healthier options for my kids. When my daughter’s school, Prarthana Public School, suggested healthier snacks, I tried the health mix and laddu kit from here. Now it has become part of our daily routine." },
    { "name": "Nirmala", "text": "Being a foodie in my 40s, I wanted food that keeps my taste buds happy without harming my health. A friend introduced me to these millet snacks and breakfast mixes. Now I enjoy my food guilt-free every day." },
    { "name": "Shivakumar", "text": "After turning 50, my doctor asked me to change my diet. I started looking for healthier alternatives and discovered these millet foods. The taste reminded me of homemade village food while taking care of my health." },
    { "name": "Shivaraj", "text": "I came across their page on social media while searching for healthy snacks. Later a friend also recommended them, so I decided to try their millet pancakes and sweets. It felt like finding the perfect balance between health and taste." },
    { "name": "Karthick", "text": "Living in the city made me miss the traditional snacks from my village. When I tried these millet laddus and murukku, it felt nostalgic. Healthy food that brings back childhood memories is truly special." },
    { "name": "Nirosha", "text": "As someone who monitors sugar levels carefully, I always hesitate to eat sweets. But these millet-based sweets gave me the confidence to enjoy a little sweetness again. Finally, desserts that care for health too." },
    { "name": "Suguna", "text": "Cooking every day became difficult with my busy schedule. The millet instant mixes here helped me prepare healthy breakfasts quickly. My family now starts the day with something nutritious." },
    { "name": "Lakshmi", "text": "I was looking for healthy snacks for my children’s evening hunger. The millet cookies and laddus became their favorite instantly. I feel happy giving them snacks that are both tasty and nutritious." },
    { "name": "Ramesh", "text": "My father has BP issues and loves traditional sweets. These millet sweets allowed him to enjoy his favorite flavors without worry. It made our family celebrations sweeter." },
    { "name": "Meena", "text": "I always believed healthy food means compromising taste. But after trying these millet chocolates and snacks, my opinion completely changed. Health can actually be delicious." },
    { "name": "Suresh", "text": "Working long hours means I often depend on instant food. The millet breakfast mixes here are quick to make and surprisingly filling. It feels like homemade food even on busy mornings." },
    { "name": "Kavitha", "text": "As a mother, my biggest concern is my family’s health. These millet laddus and health mixes gave me a natural way to add nutrition to our meals. Even my picky kids enjoy them." },
    { "name": "Rajesh", "text": "I was trying to reduce refined sugar and unhealthy snacks. These millet snacks helped me switch to better eating habits without missing taste. It’s a small change that made a big difference." },
    { "name": "Anitha", "text": "Festival seasons usually mean too many sugary sweets. This time I tried millet sweets for our family gathering. Everyone loved the taste and appreciated the healthy twist." },
    { "name": "Dinesh", "text": "My grandmother always spoke about the benefits of millets. When I tried these millet foods, it reminded me of her traditional recipes. It feels like bringing back old wisdom into modern life." },
    { "name": "Rekha", "text": "As someone trying to maintain fitness, snacks were always my weakness. These millet cookies and laddus became my perfect guilt-free treat. Healthy snacking finally feels possible." },
    { "name": "Mohan", "text": "Traveling for work made it difficult to eat healthy. These millet snacks became my go-to food during long journeys. Nutritious and easy to carry." },
    { "name": "Priya", "text": "My kids love chocolates, but I worry about sugar. The millet chocolates here gave me a healthier option without taking away their happiness. A win for both kids and parents." },
    { "name": "Arun", "text": "I was searching for something light yet filling for breakfast. The millet pancake mix here turned out to be perfect. Healthy mornings started becoming a habit." },
    { "name": "Gayathri", "text": "I wanted to introduce millets to my family but didn’t know how. These ready mixes made the transition easy and tasty. Now millets are part of our daily meals." },
    { "name": "Manjunath", "text": "My doctor suggested adding more fiber and natural foods to my diet. These millet snacks helped me follow that advice without feeling restricted. Healthier eating became enjoyable." },
    { "name": "Shobha", "text": "Evenings with tea always needed a good snack. The millet murukku and cookies became our family favorite. Crunchy, tasty, and healthier than usual snacks." },
    { "name": "Vijay", "text": "I missed the taste of homemade village sweets. When I tried these millet laddus and halwa, the flavors felt authentic and comforting. It’s like tasting tradition again." },
    { "name": "Deepa", "text": "I always look for foods that nourish both body and mind. These millet foods felt natural, wholesome, and satisfying. Sometimes the healthiest choices are also the most delicious." }
]

catering_stories = [
    { "name": "Karthick", "type": "Office Event Catering", "text": "For our office wellness event, we wanted food that was both healthy and affordable. We chose their millet-based catering menu with breakfast items, laddus, and snacks. Everyone appreciated the taste and the unique healthy concept." },
    { "name": "Nirosha", "type": "Birthday Function", "text": "For my daughter’s birthday, I wanted something different from regular junk food. Their millet snacks, sweets, and mini pancakes were perfect for kids and elders. It was healthy, tasty, and also budget-friendly for our small celebration." },
    { "name": "Suguna", "type": "Family Function", "text": "During our family gathering, we decided to try millet-based catering instead of the usual oily dishes. The food felt light, nutritious, and still very delicious. Many relatives asked us where we ordered it from." },
    { "name": "Manjunath", "type": "School Program", "text": "For a school health awareness program, we arranged millet snacks and sweets through their catering service. The food was simple, nutritious, and within our budget. It was a great way to introduce children to healthier eating." }
]

def load():
    print("Clearing out existing matching special stories...")
    Story.objects.filter(title__in=["Pinned Stories", "Customer Experiences", "Catering Stories"]).delete()

    print("Creating Pinned Stories reference document...")
    Story.objects.create(
        title="Pinned Stories",
        shortExcerpt="Features Vidya and Pradeep's pinned origin stories.",
        fullStoryContent=pinned_stories,
        is_active=True
    )

    print("Creating Customer Experiences reference document...")
    Story.objects.create(
        title="Customer Experiences",
        shortExcerpt="Collection of short customer review quotes.",
        fullStoryContent=customer_stories,
        is_active=True
    )

    print("Creating Catering Stories reference document...")
    Story.objects.create(
        title="Catering Stories",
        shortExcerpt="Collection of quotes from managed event catering.",
        fullStoryContent=catering_stories,
        is_active=True
    )

    print("Seeding completed successfully! Admins can now view these nested stories under /admin/ > Stories.")

if __name__ == "__main__":
    load()
