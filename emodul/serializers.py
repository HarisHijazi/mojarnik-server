from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from emodul.models import EModul, EModulDetail, EModulAnnotation, EModulBookmark, EModulComment


class EModulSerializer(ModelSerializer):

    class Meta:
        model = EModul
        fields = '__all__'


class EModulDetailSerializer(ModelSerializer):

    class Meta:
        model = EModulDetail
        fields = '__all__'


class EModulAnnotationSerializer(ModelSerializer):

    class Meta:
        model = EModulAnnotation
        fields = '__all__'


class EModulBookmarkSerializer(ModelSerializer):

    class Meta:
        model = EModulBookmark
        fields = '__all__'


class EModulCommentSerializer(ModelSerializer):
    # dokumen = serializers.SerializerMethodField() 
    # user = serializers.SerializerMethodField()
    class Meta:
        model = EModulComment
        fields = '__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     try:
    #         if self.context['request'].method in ['GET']:
    #             self.dokumen = serializers.SerializerMethodField()
    #             self.user = serializers.SerializerMethodField()
    #     except KeyError:
    #         pass

    
        # fields = ('id','comment','dokumen', 'user')

    # def get_dokumen(self, instance):
    #     return instance.dokumen.judul

    # def get_user(self, instance):
    #     return instance.user.first_name + ' ' + instance.user.last_name

      

