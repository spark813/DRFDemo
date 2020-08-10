import re
from datetime import datetime,timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from DRFDemo.settings import REGEX_MOBILE
from .models import VerifyCode

User = get_user_model()

class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self,mobile):
        if User.objects.filter(mobile = mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # settings.py配置的属性REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE,mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0,minutes=1,seconds=0)  # 前一分钟的时间
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago,mobile=mobile):  # 搜索该手机号是否有1分钟内发送验证码的记录
            raise serializers.ValidationError("发送验证码间隔小于60秒")

        return mobile

class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username","password")