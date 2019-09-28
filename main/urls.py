from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import CustomTokenObtainView
from .views import ProfileViewSet
from .views import RegistrationView

urlpatterns = [
    re_path(r'^registration/$', RegistrationView.as_view(), name='registration'),
    re_path(r'^token/$', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^profile/$', ProfileViewSet.as_view(), name='profile'),
]
