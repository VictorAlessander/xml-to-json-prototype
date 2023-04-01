from rest_framework.exceptions import APIException


class InvalidXMLFileAPIException(APIException):
    status_code = 400
    default_detail = (
        "Something went wrong. Ensure the file is valid and try again."
    )
