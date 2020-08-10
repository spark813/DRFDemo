import django_filters
from django.db.models import Q

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """商品过滤类"""
    price_min = django_filters.NumberFilter(field_name='shop_price',lookup_expr='gte')  # 作用于shop_price字段，大于等于
    price_max = django_filters.NumberFilter(field_name='shop_price',lookup_expr='lte')  # 作用于shop_price字段，小于等于
    name = django_filters.CharFilter(field_name='name',lookup_expr='contains')  # contains相当于模糊查询，icontains忽略大小写，不指定lookup_expr则表示精准匹配
    top_cateogry = django_filters.NumberFilter(method='top_category_filter')  # 自定义一个字段，它的值是方法返回的。

    def top_category_filter(self, queryset, name, value):  # 参数为默认必须，参数为value
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
        # Q实现“或”的逻辑查找关系。此处通过查找传入的value是否与自己的分类或自己父级分类、祖父级分类相同。

    class Meta:
        model = Goods
        fields = ['price_min','price_max','name','is_hot']  # 把过滤条件添加进来