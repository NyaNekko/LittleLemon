from django.contrib import admin
from django.urls import path, include
from restaurant.views import home_page, RegisterView, CustomAuthToken, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    path("api/", include("restaurant.urls")),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/token/login/", CustomAuthToken.as_view(), name="token_login"),
    path("api/token/logout/", LogoutView.as_view(), name="token_logout"),
    path("api-auth/", include("rest_framework.urls")),
]
