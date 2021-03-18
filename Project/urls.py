from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegisterView, UserLoginView
from . import views
urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('docs', views.ListCreateDocsView.as_view(), name='create_docs'),
    path('docs/<int:pk>', views.UpdateDocsView.as_view(), name='update_docs'),
    path('docs/<int:pk>', views.DeleteDocsView.as_view(), name='delete_docs'),
    path('user-info/<int:pk>', views.UpdateInfoView.as_view(),
         name='update_information'),
    path('user-info-list',
         views.ListUsersView.as_view({'get': 'list'}), name='list_users')
]
