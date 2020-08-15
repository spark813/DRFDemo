from rest_framework import viewsets
from rest_framework import mixins
from .models import UserFav
from .serializers import UserFavSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly

class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """用户收藏功能"""
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    lookup_field = "goods_id"
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()