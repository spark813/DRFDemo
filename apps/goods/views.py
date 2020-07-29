
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods

class GoodstListView(APIView):
    """列表页"""
    def get(self,request,format=None):
        all_goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(all_goods,many=True)
        return Response(goods_serializer.data)