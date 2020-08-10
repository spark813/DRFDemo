from rest_framework import serializers

from goods.models import Goods,GoodsCategory,GoodsImage

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)

class GoodsCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsCategorySerializer2(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)

class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    images = GoodsImageSerializer(many=True)  # GoodsImage的外键名称是images
    class Meta:
        model = Goods
        # fields = ('name','click_num','id')  # 取出部分字段
        fields = "__all__"

