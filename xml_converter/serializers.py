from rest_framework.serializers import FileField, Serializer

from .exceptions import InvalidXMLFileAPIException
from .helpers import XMLConverter


class ConverterSerializer(Serializer):
    file = FileField(required=True)

    class Meta:
        fields = "__all__"

    def to_representation(self, instance):
        try:
            file_instance = instance["file"].read()

            xml_converter = XMLConverter(file_instance)

            return xml_converter.to_json()
        except Exception as exc:
            # Something to log the error (not like this in a real code)
            print(exc)
            raise InvalidXMLFileAPIException
