from django.forms import FileField, Form


class XMLFormUpload(Form):
    file = FileField(required=True)
