from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from api.permissions import HaveSecretWordOrReadOnly
from api.serializers import UrlSerializer
from shortener.models import Url



class UrlViewSet(ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [HaveSecretWordOrReadOnly]
    pagination_class = LimitOffsetPagination

