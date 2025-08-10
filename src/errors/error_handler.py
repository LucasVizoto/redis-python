from src.http_types.http_response import HttpResponse
from .types.http_not_found_error import HttpNotFoundError

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError)):
        #enviar para um logger
        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [{
                    "title": error.name,
                    "detail": error.message
                }]
                }
        )
    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "InternalServerError",
                "detail": str(error)
            }]
        }
    )