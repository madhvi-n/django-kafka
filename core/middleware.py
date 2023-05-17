import time
from django.http import HttpResponseForbidden

class RateLimiterMiddleware:
    EXEMPT_URLS = [reverse('admin:index')]

    def __init__(self, get_response):
        self.get_response = get_response
        self.last_request_time = None

    def __call__(self, request):
        if not self.should_apply_rate_limit(request):
            return self.get_response(request)

        current_time = time.time()
        if self.last_request_time is not None and current_time - self.last_request_time < 60:
            return HttpResponseForbidden("Too many requests. Please try again later.")

        self.last_request_time = current_time
        response = self.get_response(request)
        return response

    def should_apply_rate_limit(self, request):
        # Check if the request URL is exempted
        if any(request.path.startswith(url) for url in self.EXEMPT_URLS):
            return False

        return True
