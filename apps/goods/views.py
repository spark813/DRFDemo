
from .serializers import GoodsSerializer,GoodsCategorySerializer,IndexCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins,generics
from rest_framework.pagination import PageNumberPagination

from .models import Goods,GoodsCategory

# class GoodsListView(APIView):
#     """列表页"""
#     def get(self,request,format=None):
#         all_goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(all_goods,many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)

class GoodsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100
#
# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination



from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class GoodsListViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # filter_fields = ('name',"shop_price")
    filter_class = GoodsFilter
    search_fields = ('name','goods_desc')
    ordering_fields = ('sold_num','add_time')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1  # 商品点击数+1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class GoodsCategoryViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer

class IndexCategoryViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(is_tab=True)
    serializer_class = IndexCategorySerializer






