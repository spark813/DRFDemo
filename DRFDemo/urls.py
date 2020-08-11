"""DRFDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
# from goods.views import GoodsListView
from goods.views import GoodsListViewset,GoodsCategoryViewset
from users.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset
from django.views.static import serve
from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'goods',GoodsListViewset,basename='goods') # 商品url
router.register(r'categorys',GoodsCategoryViewset,basename='categorys') # 分类url
router.register(r'code',SmsCodeViewset,basename='code')
router.register(r'reg',UserViewset,basename='reg')
router.register(r'userfavs', UserFavViewset, basename="userfavs")

# goods_list = GoodsListViewset.as_view({
#     'get':'list',
#     # 'post':'create'
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title="drf练习")),
    # url(r'goods/$', GoodsListView.as_view(),name="goods-list"),
    # url(r'goods/$', goods_list,name="goods-list"),
    url(r'^',include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^jwt-auth/', obtain_jwt_token),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
