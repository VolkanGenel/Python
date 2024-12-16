from rest_framework.views import exception_handler # type: ignore
from django.db import IntegrityError
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore

def airlines_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError):
        error_message = str(exc)
        if "flight_number" in error_message:
            field = "flight_number"
        else:
            field = "unknown"

        return Response(
            {
                "error": "A unique constraint was violated.",
                "field": field
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    return response

