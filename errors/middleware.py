from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from errors.models import Error


class LogErrorMiddleWareError(MiddlewareMixin):
    def process_response(self, request, response):
        status_code = response.status_code
        if status_code in settings.ERROR_LOG_STATUS:
            error = response.content
            Error(status_code=status_code, error=error).save()
            res = {
                "status_code": 200,
                "error": str(error)
            }
            return JsonResponse(res)
        else:
            return response
