"""
ASGI config for langpal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langpal.settings")




if os.environ.get("LOCAL_DEV"):
    application_soc = get_asgi_application()
    import chatroom.routing

    application = ProtocolTypeRouter(
        {
            "http": application_soc,
            "websocket":AuthMiddlewareStack(
                URLRouter(
                    chatroom.routing.websocket_urlpatterns
                )
            )
            # Just HTTP for now. (We can add other protocols later.)
        }
    )
else:
    django.setup()
    application = get_default_application()
