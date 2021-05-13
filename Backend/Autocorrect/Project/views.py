from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document, User, UserShare, RoleShare, RoleUser, Category, Comment
from .serializer import DocumentListSerializer, UserSerialize, UserLoginSerializer, CategorySerialize, UserDetailSerialize, PasswordSerializer, UserIDSerializer, UserShareSerialize, CommentSerialize

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.
import json


class ListDocsShareFixByIDView(APIView):
    model = Document

    def post(self, request):
        serializer = UserIDSerializer(data=request.data)
        if serializer.is_valid():
            id_user = request.data["id"]
            try:
                datas = UserShare.objects.raw(
                    'SELECT * FROM usershare WHERE id_usershare = %s AND id_role = 1', [id_user])
                docs = []
                for dt in datas:
                    id_docc = dt.id_doc
                    doc = Document.objects.raw(
                        'SELECT * FROM document WHERE id = %s AND is_deleted = 0', [id_docc])

                    category_db = Category.objects.raw(
                        'SELECT * FROM category WHERE id = %s', [doc[0].category_id])
                    user_update_last = User.objects.raw(
                        'SELECT * FROM user WHERE id = %s', [doc[0].update_last_by])
                    dc = {
                        "id": doc[0].id,
                        "title": doc[0].title,
                        "content": doc[0].content,
                        'category_name': category_db[0].name_category,
                        'category_id': doc[0].category_id,
                        'user_update_last': user_update_last[0].email,
                        'update_last_by': doc[0].update_last_by,
                        'is_deleted': doc[0].is_deleted,
                        'id_author': doc[0].id_author,
                        'created': doc[0].created,
                        'updated': doc[0].updated,
                        'role': dt.id_role
                    }
                    docs.append(dc)
                    dc = {}
                return Response(docs, status=status.HTTP_200_OK)
            except:
                return JsonResponse({
                    'message': 'error!',
                    'statusCode': 400
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({
                'message': 'error!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class ListDocsShareReadByIDView(APIView):
    model = Document

    def post(self, request):
        serializer = UserIDSerializer(data=request.data)
        if serializer.is_valid():
            id_user = request.data["id"]
            try:
                datas = UserShare.objects.raw(
                    'SELECT * FROM usershare WHERE id_usershare = %s AND id_role = 2', [id_user])
                docs = []
                for dt in datas:
                    id_docc = dt.id_doc
                    doc = Document.objects.raw(
                        'SELECT * FROM document WHERE id = %s AND is_deleted = 0', [id_docc])

                    category_db = Category.objects.raw(
                        'SELECT * FROM category WHERE id = %s', [doc[0].category_id])
                    user_update_last = User.objects.raw(
                        'SELECT * FROM user WHERE id = %s', [doc[0].update_last_by])
                    dc = {
                        "id": doc[0].id,
                        "title": doc[0].title,
                        "content": doc[0].content,
                        'category_name': category_db[0].name_category,
                        'category_id': doc[0].category_id,
                        'user_update_last': user_update_last[0].email,
                        'update_last_by': doc[0].update_last_by,
                        'is_deleted': doc[0].is_deleted,
                        'id_author': doc[0].id_author,
                        'created': doc[0].created,
                        'updated': doc[0].updated,
                        'role': dt.id_role
                    }
                    docs.append(dc)
                    dc = {}
                return Response(docs, status=status.HTTP_200_OK)
            except:
                return JsonResponse({
                    'message': 'error!',
                    'statusCode': 400
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({
                'message': 'error!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class ListDocsByIDView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        serializer = UserIDSerializer(data=request.data)
        if serializer.is_valid():
            id_user = request.data["id"]

            docs = Document.objects.raw(
                'SELECT * FROM document WHERE id_author = %s AND is_deleted = 0 ORDER BY updated DESC', [id_user])
            data = []
            for doc in docs:
                category_db = Category.objects.raw(
                    'SELECT * FROM category WHERE id = %s', [doc.category_id])
                user_update_last = User.objects.raw(
                    'SELECT * FROM user WHERE id = %s', [doc.update_last_by])
                dc = {
                    'id': doc.id,
                    'title': doc.title,
                    'content': doc.content,
                    'is_deleted': doc.is_deleted,
                    'category_name': category_db[0].name_category,
                    'category_id': doc.category_id,
                    'user_update_last': user_update_last[0].email,
                    'update_last_by': doc.update_last_by,
                    'id_author': doc.id_author,
                    'created': doc.created,
                    'updated': doc.updated
                }
                data.append(dc)
                dc = {}
            return Response(data, status=status.HTTP_200_OK)
        return JsonResponse({
            'message': 'unsuccessful!',
            'statusCode': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class ListDeleteDocsByIDView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        serializer = UserIDSerializer(data=request.data)
        if serializer.is_valid():
            id_user = request.data["id"]
            docs = Document.objects.raw(
                'SELECT * FROM document WHERE id_author = %s AND is_deleted = 1 ORDER BY updated DESC', [id_user])
            data = []
            for doc in docs:
                category_db = Category.objects.raw(
                    'SELECT * FROM category WHERE id = %s', [doc.category_id])
                user_update_last = User.objects.raw(
                    'SELECT * FROM user WHERE id = %s', [doc.update_last_by])
                dc = {
                    'id': doc.id,
                    'title': doc.title,
                    'content': doc.content,
                    'is_deleted': doc.is_deleted,
                    'category_name': category_db[0].name_category,
                    'category_id': doc.category_id,
                    'user_update_last': user_update_last[0].email,
                    'update_last_by': doc.update_last_by,
                    'id_author': doc.id_author,
                    'created': doc.created,
                    'updated': doc.updated
                }
                data.append(dc)
                dc = {}
            return Response(data, status=status.HTTP_200_OK)
        return JsonResponse({
            'message': 'unsuccessful!',
            'statusCode': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class ListDocsByCategoryView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        serializer = UserIDSerializer(data=request.data)
        if serializer.is_valid():
            id_user = request.data["id"]
            category_id = request.data["category_id"]
            docs = Document.objects.raw(
                'SELECT * FROM document WHERE id_author = %s AND is_deleted = 0 ORDER BY updated DESC', [id_user])
            data = []
            for doc in docs:
                if doc.category_id == category_id:
                    category_db = Category.objects.raw(
                        'SELECT * FROM category WHERE id = %s', [doc.category_id])
                    user_update_last = User.objects.raw(
                        'SELECT * FROM user WHERE id = %s', [doc.update_last_by])
                    dc = {
                        'id': doc.id,
                        'title': doc.title,
                        'content': doc.content,
                        'is_deleted': doc.is_deleted,
                        'category_name': category_db[0].name_category,
                        'category_id': doc.category_id,
                        'user_update_last': user_update_last[0].email,
                        'update_last_by': dc.update_last_by,
                        'id_author': doc.id_author,
                        'created': doc.created,
                        'updated': doc.updated
                    }
                    data.append(dc)
                    dc = {}
            return Response(data, status=status.HTTP_200_OK)
        return JsonResponse({
            'message': 'unsuccessful!',
            'statusCode': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class GetDocByIDView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        id_docs = request.data["id"]
        docs = Document.objects.raw(
            'SELECT * FROM document WHERE id = %s', [id_docs])
        dc = docs[0]
        if (dc.is_deleted == 0):
            category_db = Category.objects.raw(
                'SELECT * FROM category WHERE id = %s', [dc.category_id])
            user_update_last = User.objects.raw(
                'SELECT * FROM user WHERE id = %s', [dc.update_last_by])
            data = {
                'id': dc.id,
                'title': dc.title,
                'content': dc.content,
                'category_name': category_db[0].name_category,
                'category_id': dc.category_id,
                'update_last_by': dc.update_last_by,
                'user_update_last': user_update_last[0].email,
                'is_deleted': dc.is_deleted,
                'id_author': dc.id_author,
                'created': dc.created,
                'updated': dc.updated
            }
            return Response(data, status=status.HTTP_200_OK)
        return JsonResponse({
            'message': 'not found!',
            'statusCode': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class DeleteDocByIdView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        id_docs = request.data["id"]
        try:
            docs = Document.objects.raw(
                'SELECT * FROM document WHERE id = %s', [id_docs])
            dc = docs[0]
            obj = Document(id=dc.id, title=dc.title, content=dc.content, category_id=dc.category_id, is_deleted=1,
                           id_author=dc.id_author, update_last_by=dc.update_last_by, updated=dc.updated, created=dc.created)
            obj.save()
            return JsonResponse({
                'message': 'successful!',
                'statusCode': 200,
            }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'not successful!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class RestoreDocsByIdView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        id_docs = request.data["ids"]
        try:
            for id_doc in id_docs:
                doc = Document.objects.raw(
                    'SELECT * FROM document WHERE id = %s', [id_doc])
                dc = doc[0]
                obj = Document(id=dc.id, title=dc.title, content=dc.content, category_id=dc.category_id, is_deleted=0,
                               id_author=dc.id_author, update_last_by=dc.update_last_by, updated=dc.updated, created=dc.created)
                obj.save()

            return JsonResponse({
                'message': 'successful!',
                'statusCode': 200
            }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'not successful!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


# Share view

class UpdateRoleShareDocView(APIView):
    model = UserShare

    def post(self, request):
        _id = request.data["id"]
        id_doc = request.data["id_doc"]
        id_usershare = request.data["id_usershare"]
        id_role = request.data["id_role"]

        try:
            obj = UserShare(
                id=_id, id_usershare=id_usershare, id_doc=id_doc, id_role=id_role)
            obj.save()
            return JsonResponse({
                'message': 'update share successful!',
                'statusCode': 200
            }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'not update share successful!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class ShareDocView(APIView):
    model = UserShare

    def post(self, request):
        id_doc = request.data["id_doc"]
        email_share = request.data["email_share"]
        id_role = request.data["id_role"]
        try:
            users = User.objects.raw(
                'SELECT * FROM user WHERE email = %s', [email_share])

            user_share = users[0]
            docs = Document.objects.raw(
                'SELECT * FROM document WHERE id = %s', [id_doc])
            is_check = True
            # check is_valid
            user_shared = UserShare.objects.raw(
                'SELECT * FROM usershare WHERE id_usershare = %s ', [user_share.id])
            for us in user_shared:
                if (us.id_doc == id_doc):
                    is_check = False

            if user_share.id == docs[0].id_author:
                return JsonResponse({
                    'message': 'Không thể tự chia sẻ cho chính mình!',
                    'statusCode': 401
                }, status=status.HTTP_200_OK)
            elif (is_check):
                try:
                    obj = UserShare(
                        id_usershare=user_share.id, id_doc=id_doc, id_role=id_role, note="")
                    obj.save()
                    return JsonResponse({
                        'message': 'Chia sẻ thành công!',
                        'statusCode': 200
                    }, status=status.HTTP_200_OK)
                except:
                    return JsonResponse({
                        'message': 'Chia sẻ không thành công!',
                        'statusCode': 402
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({
                    'message': 'Đã chia sẻ cho email này!',
                    'statusCode': 403
                }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'Không tìm thấy email trong hệ thống!',
                'statusCode': 400
            }, status=status.HTTP_200_OK)


class ListCreateUShareView(ListCreateAPIView):
    model = UserShare
    serializer_class = UserShareSerialize

    def get_queryset(self):
        return UserShare.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserShareSerialize(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


# CRUD Category


class ListCreateCategoryView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerialize

    def get_queryset(self):
        return Category.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CategorySerialize(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerialize

    def put(self, request, *args, **kwargs):
        cate = get_object_or_404(Category, id=kwargs.get('pk'))
        serializer = CategorySerialize(cate, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Category successfully'
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not update Category successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerialize

    def delete(self, request, *args, **kwargs):
        cate = get_object_or_404(Category, id=kwargs.get('pk'))
        cate.delete()

        return JsonResponse({
            'message': 'Delete Category successful!'
        }, status=status.HTTP_200_OK)

# CRUD Comment


class CreateCmtView(ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerialize

    def get_queryset(self):
        return Comment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CommentSerialize(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Commnet successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Commnet unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class ListCreateCommentView(APIView):
    model = Comment

    def post(self, request):
        id_user = request.data['id_user']
        id_doc = request.data['id_doc']
        comment = request.data['comment']

        try:
            obj = Comment(id_doc=id_doc,
                          id_user=id_user, comment=commnet)
            obj.save()
            return JsonResponse({
                'message': 'Create a new Comment successful!'
            }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'Create a new Comment unsuccessful!'
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateCommentView(RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerialize

    def put(self, request, *args, **kwargs):
        cate = get_object_or_404(Comment, id=kwargs.get('pk'))
        serializer = CommentSerialize(cate, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Comment successfully'
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not update Comment successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentView(RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerialize

    def delete(self, request, *args, **kwargs):
        cate = get_object_or_404(Comment, id=kwargs.get('pk'))
        cate.delete()

        return JsonResponse({
            'message': 'Delete Comment successful!'
        }, status=status.HTTP_200_OK)

# List comment by doc_id


class ListCommentByIdView(APIView):
    def post(self, request):
        id_doc = request.data['id']
        try:
            comments = Comment.objects.raw(
                'SELECT * FROM comment WHERE id_doc = %s', [id_doc])

            list_cmt = []
            for cmt in comments:
                user_cmt = User.objects.raw(
                    'SELECT * FROM user WHERE id = %s', [cmt.id_user])
                comt = {
                    "id": cmt.id,
                    "comment": cmt.comment,
                    "id_user": cmt.id_user,
                    "id_doc": id_doc,
                    "user_email": user_cmt[0].email
                }
                list_cmt.append(comt)

            return Response(list_cmt, status=status.HTTP_200_OK)
        except:
            list_cmt = []
            return Response(list_cmt, status=status.HTTP_200_OK)

# CRUD Doc


class ListCreateDocsView(ListCreateAPIView):
    model = Document
    serializer_class = DocumentListSerializer

    def get_queryset(self):
        return Document.objects.all()

    def create(self, request, *args, **kwargs):
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


class DeleteDocsView(APIView):
    model = Document

    def post(self, request, *args, **kwargs):
        id_docs = request.data["ids"]
        try:
            for id_doc in id_docs:
                docs = Document.objects.raw(
                    'SELECT * FROM document WHERE id = %s', [id_doc])
                dc = docs[0]
                obj = Document(id=dc.id, title=dc.title, content=dc.content, category_id=dc.category_id, is_deleted=7,
                               id_author=dc.id_author, update_last_by=dc.update_last_by, updated=dc.updated, created=dc.created)
                obj.save()
                return JsonResponse({
                    'message': 'successful!',
                    'statusCode': 200,
                }, status=status.HTTP_200_OK)
        except:
            return JsonResponse({
                'message': 'not successful!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


# User  + Admin

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerialize(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            serializer.save()

            return JsonResponse({
                'message': 'Register successful!',
                'statusCode': 200
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not register successful!',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    model = User

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
                em = serializer.validated_data['email']
                userinfo = User.objects.raw(
                    'SELECT * FROM user WHERE email = %s', [em])

                id_user = userinfo[0].id
                email_user = userinfo[0].email
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'statusCode': 200,
                    'user_id': id_user,
                    'email': email_user,
                    'role_id': userinfo[0].role_id
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error_message': 'Email or password is incorrect!',
                    'error_code': 400
                }, status=status.HTTP_200_OK)

        else:
            return Response({
                'error_messages': serializer.errors,
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    model = User

    def post(self, request):
        id_u = request.data["id"]
        try:
            users = User.objects.raw(
                'SELECT * FROM user WHERE id = %s', [id_u])
            user = users[0]
            data = {
                "id": user.id,
                "first_name": user.first_name,
                "email": user.email,
                "last_name": user.last_name,
                "role_id": user.role_id,
                "phone": user.phone,
                "live_at": user.live_at
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Not successfully'
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
                'message': 'Update Info successfully',
                'statusCode': 200
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'message': 'Not update Info successfully',
                'statusCode': 400
            }, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    model = User

    def post(self, request):
        id_u = request.data["id"]
        old_pass = request.data["old_password"]
        password = request.data["new_password"]
        try:
            users = User.objects.raw(
                'SELECT * FROM user WHERE id = %s', [id_u])
            user = users[0]
            if check_password(old_pass, user.password):
                password = make_password(password)
                try:
                    obj = User(id=user.id, password=password, email=user.email, first_name=user.first_name, last_name=user.last_name,
                               phone=user.phone, role_id=user.role_id, live_at=user.live_at)
                    obj.save()
                    return Response({
                        'message': 'Đổi mật khẩu thành công!',
                        'type': 'is-success'
                    }, status=status.HTTP_200_OK)
                except:
                    return Response({
                        'message': 'Not successfully'
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'message': 'Mật khẩu cũ không đúng',
                    'type': 'is-danger'
                }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Not successfully'
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


class UsersView(APIView):
    model = User

    def post(self, request):
        try:
            users = User.objects.raw('SELECT * FROM user WHERE role_id = 1')

            data = []
            for user in users:
                dc = {
                    "id": user.id,
                    "email": user.email,
                    "phone": user.phone,
                    "live_at": user.live_at,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role_id": user.role_id
                }
                data.append(dc)
                dc = {}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Not successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class UsersBlockView(APIView):
    model = User

    def post(self, request):
        try:
            users = User.objects.raw('SELECT * FROM user WHERE role_id = 2')

            data = []
            for user in users:
                dc = {
                    "id": user.id,
                    "email": user.email,
                    "phone": user.phone,
                    "live_at": user.live_at,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role_id": user.role_id
                }
                data.append(dc)
                dc = {}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Not successfully'
            }, status=status.HTTP_400_BAD_REQUEST)


class AdminsView(APIView):
    model = User

    def post(self, request):
        try:
            users = User.objects.raw('SELECT * FROM user WHERE role_id = 0')

            data = []
            for user in users:
                dc = {
                    "id": user.id,
                    "email": user.email,
                    "phone": user.phone,
                    "live_at": user.live_at,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role_id": user.role_id
                }
                data.append(dc)
                dc = {}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Not successfully'
            }, status=status.HTTP_400_BAD_REQUEST)
