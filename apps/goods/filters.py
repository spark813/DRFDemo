import django_filters
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """商品过滤类"""
    price_min = django_filters.NumberFilter(field_name='shop_price',lookup_expr='gte')  # 作用于shop_price字段，大于等于
    price_max = django_filters.NumberFilter(field_name='shop_price',lookup_expr='lte')  # 作用于shop_price字段，小于等于
    name = django_filters.CharFilter(field_name='name',lookup_expr='contains')  # contains相当于模糊查询，icontains忽略大小写，不指定lookup_expr则表示精准匹配
    class Meta:
        model = Goods
        fields = ['price_min','price_max','name']  # 把过滤条件添加进来