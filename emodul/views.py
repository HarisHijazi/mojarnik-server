from rest_framework.viewsets import ModelViewSet
from emodul.serializers import EModulSerializer, EModulDetailSerializer, EModulAnnotationSerializer, EModulBookmarkSerializer, EModulCommentSerializer
from emodul.models import EModul, EModulDetail, EModulAnnotation, EModulBookmark, EModulComment



class EModulViewSet(ModelViewSet):
    queryset = EModul.objects.order_by('pk')
    serializer_class = EModulSerializer
    http_method_names = ['get', 'post']


class EModulDetailViewSet(ModelViewSet):
    queryset = EModulDetail.objects.order_by('pk')
    serializer_class = EModulDetailSerializer
    http_method_names = ['get', 'post']



class EModulAnnotationViewSet(ModelViewSet):
    queryset = EModulAnnotation.objects.order_by('pk')
    serializer_class = EModulAnnotationSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class EModulBookmarkViewSet(ModelViewSet):
    queryset = EModulBookmark.objects.order_by('pk')
    serializer_class = EModulBookmarkSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class EModulCommentViewSet(ModelViewSet):
    queryset = EModulComment.objects.order_by('pk')
    serializer_class = EModulCommentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']




