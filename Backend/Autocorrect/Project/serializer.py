
from rest_framework import serializers
from Project.models import Document, User, UserShare, RoleShare, RoleUser, Category, Comment

# Định nghĩa model cần serialize và các trường:


class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'title', 'content', 'id_author', 'category_id', 'update_last_by',
                  'is_deleted', 'created', 'updated')


class UserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role_id',
                  'first_name', 'last_name', 'phone', 'live_at']
        extra_kwargs = {'password': {'write_only': True}}


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'role_id', 'phone', 'live_at']


class CategorySerialize(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name_category', 'note']


class CommentSerialize(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'id_user', 'id_doc', 'comment']


class UserShareSerialize(serializers.ModelSerializer):

    class Meta:
        model = UserShare
        fields = ['id', 'id_usershare', 'id_doc', 'id_role']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
