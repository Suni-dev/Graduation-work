from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> f9f3843 (최종수정)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('check.urls', 'check'), namespace="check")),
]
<<<<<<< HEAD
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> f9f3843 (최종수정)
