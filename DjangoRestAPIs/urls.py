from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from DjangoRestAPIs import settings
from MyApis.views import MyUserViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('myapis/', MyUserViewset.as_view({'post': 'create',
                                           'get': 'retrieve',
                                           'put': 'update',
                                           'delete': 'destroy'}))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)