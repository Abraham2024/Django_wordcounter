from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
  path("", views.index, name = "index"),
  path("counter", views.counter, name = "counter"),
  path('admin/', admin.site.urls),
  path("login", views.login, name = "login"),
  path("signup",views.signup, name = "signup"),
  path("logout", views.logout, name = "logout")

 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

