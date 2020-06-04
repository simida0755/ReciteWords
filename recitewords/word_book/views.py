from django.views.generic.base import View
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from recitewords.word.models import Word
from recitewords.word.serializers import WordSerializer
from recitewords.word_book.models import WordBook
from recitewords.word_book.serializers import Word_bookSerializer


class Word_bookView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = Word_bookSerializer
    queryset = WordBook.objects.all()
    #
    # lookup_field = "goods_id"

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ShopCartDetailSerializer
    #     else:
    #         return ShopCartSerializer

    # #获取购物车列表
    # def get_queryset(self):
    #     return ShoppingCart.objects.filter(user=self.request.user)

    # # 库存数-1
    # def perform_create(self, serializer):
    #     shop_cart = serializer.save()
    #     goods = shop_cart.goods
    #     goods.goods_num -= shop_cart.nums
    #     goods.save()

    # # 库存数+1
    # def perform_destroy(self, instance):
    #     goods = instance.goods
    #     goods.goods_num += instance.nums
    #     goods.save()
    #     instance.delete()

    # # 更新库存,修改可能是增加页可能是减少
    # def perform_update(self, serializer):
    #     #首先获取修改之前的库存数量
    #     existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
    #     existed_nums = existed_record.nums
    #     # 先保存之前的数据existed_nums
    #     saved_record = serializer.save()
    #     #变化的数量
    #     nums = saved_record.nums-existed_nums
    #     goods = saved_record.goods
    #     goods.goods_num -= nums
    #     goods.save()
