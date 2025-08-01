from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('accounts/', include('accounts.urls')),
    path('tickets/', include('tickets.urls')),
    path('payments/', include('payments.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
