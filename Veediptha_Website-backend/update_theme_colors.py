import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

from api.models import WebsiteTheme

def update_theme():
    theme = WebsiteTheme.objects.filter(is_active=True).first()
    if not theme:
        theme = WebsiteTheme.objects.first()
        if not theme:
            theme = WebsiteTheme(name="Main Theme", is_active=True)
    
    # Sane Organic Brand Theme
    colors = {
        "primary": "#2d4a36",     # Espalier Deep Green - readable, grounding, organic
        "secondary": "#d55b3e",   # Obstinate Orange - for buttons, call to action
        "accent": "#007e80",      # Intense Teal - for special accents/borders
        "background": "#ffffff",  # Pure White background
        "surface": "#f9f6f0",     # Very light warm surface
        "text": "#1a1a1a"         # Dark Text
    }

    theme.colors = colors
    theme.dark_mode_colors = colors
    theme.light_mode_colors = colors

    theme.save()
    print("Theme updated successfully with Sherwin-Williams (Teal, Orange, Green, White).")

if __name__ == '__main__':
    update_theme()
