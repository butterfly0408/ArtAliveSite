"""
WSGI config for art_alive project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


activate_this = os.path.join("/path/to/your/venv", "Scripts/activate_this.py")
exec(open(activate_this).read(), dict(__file__=activate_this))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'art_alive.settings')

application = get_wsgi_application()
