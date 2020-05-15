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

    i_word = WordIPASerializer(many=True)
    t_word = WordTranSerializer(many=True)
    p_word = WordPhraseSerializer(many=True)
    c_word = WordCentencesSerializer(many=True)

    class Meta:
        model = Word
        fields = ('name','i_word','t_word','p_word','c_word')

