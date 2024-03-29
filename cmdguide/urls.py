from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.urls', 'app'), namespace='app')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
