from django.contrib import admin

from goods.models import *

class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','desc']


admin.site.register(GoodsCategory,GoodsCategoryAdmin)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(Banner)

