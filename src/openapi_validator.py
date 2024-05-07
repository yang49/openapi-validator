from openapi_core import Spec, unmarshal_request, unmarshal_response

class OpenApiValidator:

    openapi_spec: Spec = None
    def __init__(self, file_path):
        spec = Spec.from_file_path(file_path)


    def validate_request(self, request):
        return unmarshal_request(self.openapi_spec, request)

    def validate_response(self, response):
        return unmarshal_response(self.openapi_spec, response)
