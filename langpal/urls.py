from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('wordbox/', include('wordbox.urls')),
    path('practice/', include('practice.urls')),
    path('about/', include('about.urls')),
    path('chatroom/', include('chatroom.urls')),
    path('', include('homefeed.urls')),
    path('homefeed/', include('homefeed.urls')),
    path('portfolio/', include('portfolio.urls')),


]

urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)

