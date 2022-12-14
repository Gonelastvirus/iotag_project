"""
ASGI config for iotag project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iotag.settings')

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from iotapp import consumer
#from token_auth import TokenMiddleware
from django.contrib.auth.models import User


       
websocket_urlPattern=[
    path('show/<str:username>',consumer.DashConsumer.as_asgi()),
]
application=ProtocolTypeRouter({
    # 'http':
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})