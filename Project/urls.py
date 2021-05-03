from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegisterView, UserLoginView, ListDocsByIDView
from . import views

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),

    path('login', UserLoginView.as_view(), name='login'),

    # docs
    path('docs', views.ListCreateDocsView.as_view(), name='create_docs'),

    path('docs/<int:pk>', views.UpdateDocsView.as_view(), name='update_docs'),

    path('docs-del', views.DeleteDocsView.as_view(), name='delete_docs'),

    # category
    path('category', views.ListCreateCategoryView.as_view(), name='create_category'),\

    path('category/<int:pk>', views.UpdateCategoryView.as_view(),
         name='update_category'),

    path('category/<int:pk>', views.DeleteCategoryView.as_view(),
         name='delete_category'),

    # comment
    path('list-comment', views.ListCommentByIdView.as_view(), name='list_comment'),

    path('create-comment', views.ListCreateCommentView.as_view(),
         name='create_comment'),

    path('comment', views.CreateCmtView.as_view(), name='create_comment'),

    path('comment/<int:pk>', views.UpdateCommentView.as_view(),
         name='update_comment'),

    path('category/<int:pk>', views.DeleteCommentView.as_view(),
         name='delete_comment'),

    # user
    path('info', views.UserInfoView.as_view(), name='info'),

    path('change-password', views.ChangePasswordView.as_view(),
         name='change-password'),

    path('user-info/<int:pk>', views.UpdateInfoView.as_view(),
         name='update_information'),

    path('user-info-list',
         views.ListUsersView.as_view({'get': 'list'}), name='list_users'),

    path('list-user', views.UsersView.as_view(), name='users'),

    path('list-admin', views.AdminsView.as_view(), name='admins'),

    # list -doc
    path('list-docs', ListDocsByIDView.as_view(), name='list-docs'),
    path('list-category-docs', views.ListDocsByCategoryView.as_view(),
         name='list-category-docs'),
    # list-share
    path('list-share-read-docs', views.ListDocsShareReadByIDView.as_view(),
         name='list-share-read-docs'),
    path('list-share-fix-docs', views.ListDocsShareFixByIDView.as_view(),
         name='list-share-fix-docs'),

    path('doc-detail', views.GetDocByIDView.as_view(), name='doc-detail'),
    path('delete-doc', views.DeleteDocByIdView.as_view(), name='delete-doc'),
    path('restore-docs', views.RestoreDocsByIdView.as_view(), name='restore-docs'),
    path('delete-docs', views.ListDeleteDocsByIDView.as_view(),
         name='list-delete-docs'),
    # share-doc
    path('share', views.ListCreateUShareView.as_view(), name='share'),
    path('share-doc', views.ShareDocView.as_view(), name='share-doc'),

    path('update-share-doc', views.UpdateRoleShareDocView.as_view(),
         name='update-share-doc')
]
