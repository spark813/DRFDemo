from django.db.models import Q
from rest_framework import serializers

from goods.models import Goods,GoodsCategory,GoodsImage,GoodsCategoryBrand

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

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"

class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandsSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = GoodsCategorySerializer2(many=True)  # 子级分类

    def get_goods(self,obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True,context={'request':self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"

