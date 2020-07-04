from rest_framework import serializers

from recitewords.spider.github_spider import SpiderGithub
from recitewords.word.models import Word
from recitewords.word.serializers import WordSerializer
from recitewords.word_book.models import WordBook, WordCount


class WordCountSerializer(serializers.ModelSerializer):
    word = WordSerializer(read_only=True)
    class Meta:
        model = WordCount
        fields = "__all__"


class Word_bookSerializer(serializers.Serializer):
    #获取当前登录的用户
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    name = serializers.CharField(
        required=True,max_length=20,min_length=2
    )
    url = serializers.CharField(write_only = True,
        required=True,max_length=500,min_length=5
    )
    isupload = serializers.BooleanField(

    )
    w_count = WordCountSerializer(many = True, read_only=True)

    def create(self, validated_data):
        print('111111111')
        name = self.validated_data["name"]
        owner = self.context["request"].user
        url = validated_data["url"]
        isupload = validated_data["isupload"]
        w_book = WordBook.objects.create(name=name,owner= owner,isupload=isupload)
        w_book.save()

        sg = SpiderGithub(url)

        if sg.status == 200:
            if sg.words:
                for w in sg.words:
                    word = Word.get_or_spider(w)

                    if word:
                        w_count = WordCount()
                        w_count.word = word
                        w_count.count
                        w_count.uploader =owner
                        w_book = WordBook.objects.get(pk = w_book.id)
                        w_count.w_book = w_book
                        w_count.save()

        return w_book

    # def update(self, instance, validated_data):
    #     # 修改商品数量
    #     instance.nums = validated_data["nums"]
    #     instance.save()
    #     return instance


