"""
WSGI config for art_alive project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# activate_this_ps1 = os.path.join("/home/artalive/artalive.co.za/vanessa/venv", "Scripts/Activate.ps1")

# ps1_content = f"""
# $env:VIRTUAL_ENV = "{"/path/to/your/venv"}"
# . "{activate_this_ps1}"
# """

# exec(ps1_content, dict(__file__=__file__))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'art_alive.settings')

application = get_wsgi_application()
