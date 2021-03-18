
from rest_framework import serializers
from Project.models import Document, User

# Định nghĩa model cần serialize và các trường:


class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        # ko dùng đến updated và created
        fields = ('id', 'title', 'content', 'id_user')


class UserSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'live_at')


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
