from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from apps.user.views import CustomToken, RegisterAPI, UserView

router = DefaultRouter()
router.register("register", RegisterAPI, basename="register")
router.register("users", UserView, basename="users")

urlpatterns = [
    path("token/", CustomToken.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("token/logout", TokenBlacklistView.as_view(), name="logout"),
    path("users/profile/<int:pk>/", UserView.as_view({"get": "retrieve"}), name="user-profile"),
]



urlpatterns += router.urls
