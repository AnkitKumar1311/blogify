
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#   url patterns
urlpatterns = [
    #   admin route
    path('admin/', admin.site.urls),

    #   own applications below here
    path('account/', include('account.urls')),
    path('blog/', include('blogapp.urls')),

    #   social auth urls below here
    path('oauth/', include('social_django.urls'), name='social'),

    #   path starting with regular expression
    path('', include('pages.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
