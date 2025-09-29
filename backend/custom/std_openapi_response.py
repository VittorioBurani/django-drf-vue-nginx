from rest_framework import serializers
from drf_spectacular.utils import OpenApiResponse, inline_serializer


OK_EMPTY_BODY = {
    200: None,
}

CREATED_EMPTY_BODY = {
    201: None,
}

DESTROYED_EMPTY_BODY = {
    204: None,
}

BAD_REQUEST = {
    400: OpenApiResponse(
        response = inline_serializer(
            name = "bad_request",
            fields = { "error": serializers.CharField(default="Bad request") }
        )
    ),
}

UNAUTHORIZED = {
    401: OpenApiResponse(
        response = inline_serializer(
            name = "unauthorized",
            fields = { "error": serializers.CharField(default="Unauthorized") }
        )
    ),
}

FORBIDDEN = {
    403: OpenApiResponse(
        response = inline_serializer(
            name = "forbidden",
            fields = { "error": serializers.CharField(default="Forbidden") }
        )
    ),
}

SERVER_ERROR = {
    500: OpenApiResponse(
        response = inline_serializer(
            name = "server_error",
            fields = { "error": serializers.CharField(default="Host error") }
        )
    ),
}
