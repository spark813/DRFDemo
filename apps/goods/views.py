
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins,generics
from rest_framework.pagination import PageNumberPagination

from .models import Goods

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
class GoodsListViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    # queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get('price_min',0)  # 获取前端get请求传过来的值
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset




