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

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'goods',GoodsListViewset,basename='goods') # 商品url
router.register(r'categorys',GoodsCategoryViewset,basename='categorys') # 分类url


# goods_list = GoodsListViewset.as_view({
#     'get':'list',
#     # 'post':'create'
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title="b")),
    # url(r'goods/$', GoodsListView.as_view(),name="goods-list"),
    # url(r'goods/$', goods_list,name="goods-list"),
    url(r'^',include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
