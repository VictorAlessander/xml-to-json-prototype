from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import ConverterSerializer


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]
    serializer_class = ConverterSerializer

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data, many=False)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, 200)
