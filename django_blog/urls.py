from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar


urlpatterns = [
    path('', include('blog.urls')),
    path('', include('writer.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
