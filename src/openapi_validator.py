from openapi_core import OpenAPI


class OpenApiValidator:
    openapi: OpenAPI = None

    def __init__(self, path: str):
        self.spec = OpenAPI.from_file_path(path)

    def validate_requests_get(self, request):
        self.openapi.validate_request(request)
