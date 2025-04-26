import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rafi_online_classes.settings')
application = get_wsgi_application()
