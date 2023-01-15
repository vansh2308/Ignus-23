from django.urls import include, path
from rest_framework import routers

from .views import (CARegisterAPIView, CookieTokenRefreshView, GoogleLoginView,
                    GoogleRegisterView, LoginView, LogoutView,
                    PreRegistrationAPIView, RegisterUserAPIView, UserDetailAPI,
                    UserProfileAPIView, UserProfileDetailsView, PreCARegistrationAPIView)

router = routers.DefaultRouter()
router.register(r'pre-register', PreRegistrationAPIView)
router.register(r'ca-pre-register', PreCARegistrationAPIView)
urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/google/', GoogleRegisterView.as_view(), name="google-register"),
    path('login/google/', GoogleLoginView.as_view(), name="google-login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('refresh/', CookieTokenRefreshView.as_view(), name="refresh"),
    path('user-details/', UserDetailAPI.as_view()),
    path('user-profile/', UserProfileAPIView.as_view(), name="create-user-profile"),
    path('user-profile-details/', UserProfileDetailsView.as_view(), name="user-details"),
    path('ca-register/', CARegisterAPIView.as_view(), name="ca-register"),
    path('', include(router.urls)),
]
