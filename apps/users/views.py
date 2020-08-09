from django.shortcuts import render

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import VerifyCode
from .serializers import SmsSerializer,UserRegSerializer


User = get_user_model()
class CustomBackend(ModelBackend):
    """自定义用户认证"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    """发送短信验证码"""
    serializer_class = SmsSerializer
    # 重写create
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # 如果执行抛异常则不往后执行，返回400状态码
        mobile = serializer.validated_data["mobile"]

        # 此处就可以编写创建逻辑代码，此处省略。下面为简略实现验证通过后的新增
        code_record = VerifyCode(code=1234,mobile=mobile)
        code_record.save()
        return Response({
            "status":"ok",
            "mobile":mobile
        },status=status.HTTP_201_CREATED)

class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    """用户注册"""
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 修改下面的内容
        user = self.perform_create(serializer)
        # 以下代码需要自行断点和查阅源码后编写，找到jwt如何生成token
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)

        headers = self.get_success_headers(serializer.data)
        # 返回时使用更新后的数据re_dict
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()  # 需要返回user对象
