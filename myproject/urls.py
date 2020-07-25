from django.contrib import admin
from django.urls import path, include
from login import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('blog/<int:blog_id>', views.detail, name="detail"),
    path('blog/write', views.create, name = "write"),
    path('blog/update/<int:blog_id>', views.update, name="update"),
    path('blog/delete/<int:blog_id>', views.delete, name="delete"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)