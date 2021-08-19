from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from accounts.views import custom_obtain_auth_token
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('api/accounts/', include('accounts.urls')),  
    path('api/akademik/', include('akademik.urls')),    
    path('api/emodul/', include('emodul.urls')),  
    path('api/token-auth/', custom_obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns