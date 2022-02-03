from django.db.models import query
from django.http import response
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.conf import settings
from users.user_serializer import UserSerializer
from users.models import User
from rest_framework.permissions import AllowAny
from helper.utils import get_paginaation_data,get_pagination
from django.db.models import Q
from rest_framework import status

# Create your views here.

class SignUp(CreateAPIView):
    permission_classes=[AllowAny,]
    serializer_class=UserSerializer

class UsersList(APIView):
    
    def get(self,request):
        print(self.request.GET)
        user_name=self.request.GET.get('user_name')
        email=self.request.GET.get('email')
        phone_number=self.request.GET.get('phone_number')
        sort_by=self.request.GET.get('sort_by')
        sort_type=self.request.GET.get('sort_type')
        per_page_rows=self.request.GET.get('per_page_rows')
        page_no=self.request.GET.get('page_no')
        search=''
        if user_name:
            search+=" and username='{}'".format(user_name)
        if email:
            search+=" and email='{}'".format(email)
        if phone_number:
            search+=" and phone_number='{}'".format(phone_number)
        if sort_by:
            search+=' order by {}'.format(sort_by)
        if not sort_by:
            search+=' order by id'
        if sort_type:
            search+=' {}'.format(sort_type)
        if per_page_rows:
            per_page_rows=int(per_page_rows)
            page_no=int(page_no)
        if not per_page_rows:
            per_page_rows=None
            page_no=None
        pagination=get_pagination(page_no=page_no,per_page_rows=per_page_rows)
        user_list_data=User.objects.raw("""select id,username,email,phone_number,address,user_type,status_id from users_user
                                        where status_id != '3'{search} limit {offset},{limit};""".format(search=search,
                                                                                                        offset=pagination['offset'],
                                                                                                        limit=pagination['limit']))
        print("raw",user_list_data)
        serialized_data=UserSerializer(user_list_data,many=True)
        print(serialized_data.data)
        return Response(data=serialized_data.data,status=200)

class UserViewAndEdit(APIView):
    def get(self,request):
        try:
            id=self.request.data['id']
        except:
            id=self.request.user.pk
        try:
            user_data=User.objects.get(Q(id=id) & ~Q(status_id=3))
            serilized_data=UserSerializer(user_data)
            return Response(status=200,data=serilized_data.data)

        except User.DoesNotExist:
            return Response({"message":"User not exist!"},status=status.HTTP_404_NOT_FOUND)

        except :
            return Response({"errors":"User details can't get!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request):
        try:
            id=self.request.data['id']
        except:
            id=self.request.user.pk
        try:
            user_data=User.objects.get(Q(id=id) & ~Q(status_id=3))
            serializers=UserSerializer(user_data,data=self.request.data,partial=True)
            serializers.is_valid()
            # print(serializers.validated_data)
            print(serializers.errors)
            serializers.save()
            return Response(status=200,data=serializers.data)
        
        except User.DoesNotExist:
            return Response({"message":"User not exist!"},status=status.HTTP_404_NOT_FOUND)

        except :
            return Response({"errors":"Can't complete the operation may be invalide data!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)