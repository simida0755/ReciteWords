from rest_framework import serializers
from .models import Word, IPA, Trans, Phrase, Centences, Additional


class WordIPASerializer(serializers.ModelSerializer):

    class Meta:
        model = IPA
        fields = "__all__"

class WordTranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trans
        fields = "__all__"

class WordPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = "__all__"

class WordCentencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centences
        fields = "__all__"

class WordAdditionaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = "__all__"

class WordSerializer(serializers.ModelSerializer):

    IPA = WordIPASerializer(many=True)
    trans = WordTranSerializer(many=True)
    phrase = WordPhraseSerializer(many=True)
    centences = WordCentencesSerializer(many=True)

    class Meta:
        model = Word
        fields = ('name','IPA','trans','phrase','centences')



