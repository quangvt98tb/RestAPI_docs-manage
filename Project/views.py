from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document, User
from .serializer import DocumentListSerializer, UserSerialize, UserLoginSerializer, UserDetailSerialize, PasswordSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.


class ListCreateDocsView(ListCreateAPIView):
    model = Document
    serializer_class = DocumentListSerializer

    def get_queryset(self):
        return Document.objects.all()

    def create(self, request, *args, **kwargs):
        print(1, request.data)
        serializer = DocumentListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Docs successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Docs unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDocsView(RetrieveUpdateDestroyAPIView):
    model = Document
    serializer_class = DocumentListSerializer

    def put(self, request, *args, **kwargs):
        docs = get_object_or_404(Document, id=kwargs.get('pk'))
        serializer = DocumentListSerializer(docs, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Docs successfully'
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not update Docs successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteDocsView(RetrieveUpdateDestroyAPIView):
    model = Document
    serializer_class = DocumentListSerializer

    def delete(self, request, *args, **kwargs):
        docs = get_object_or_404(Document, id=kwargs.get('pk'))
        docs.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerialize(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            serializer.save()

            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'message': 'Not register successful!'
            }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error_message': 'Email or password is incorrect!',
                    'error_code': 400
                }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'error_messages': serializer.errors,
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateInfoView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserDetailSerialize

    def put(self, request, *args, **kwargs):
        user_info = get_object_or_404(User, id=kwargs.get('pk'))
        serializer = UserDetailSerialize(user_info, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Info successfully'
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not update Info successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class ListUsersView(viewsets.ModelViewSet):
    model = User
    serializer_class = UserDetailSerialize

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserDetailSerialize(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
