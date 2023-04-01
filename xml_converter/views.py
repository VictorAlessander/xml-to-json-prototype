from django.http import JsonResponse
from django.shortcuts import render

from .forms import XMLFormUpload
from .helpers import XMLConverter


def upload_page(request):
    json_result = None
    error = None

    if request.method == "POST":
        form = XMLFormUpload(None, request.FILES)

        if form.is_valid():
            try:
                xml_converter = XMLConverter(request.FILES["file"].read())
                json_result = xml_converter.to_json()
            except Exception as exc:
                # Something to log the error (not like this in a real code)
                print(exc)
                error = "Something went wrong. Ensure the file is valid and try again."

    return render(
        request, "upload_page.html", dict(data=json_result, error=error)
    )
