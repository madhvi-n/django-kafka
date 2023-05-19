from django.core.cache import cache
from functools import wraps
import time
from rest_framework.response import Response
from rest_framework import status


def rate_limit(rate, period):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return

            cache_key = f"rate_limit:{func.__name__}:{request.user.pk}"
            current_time = time.time()
            interval_start = cache.get(cache_key + '_interval_start', 0)
            request_count = cache.get(cache_key, 0)

            if current_time - interval_start >= period:
                # If the interval has expired, reset the request count and update the interval start time
                cache.set(cache_key, 1, period)
                cache.set(cache_key + '_interval_start', current_time, period)
                return func(self, request, *args, **kwargs)
            elif request_count < rate:
                # If still within the interval and request count is less than the rate, increment the count and proceed
                cache.incr(cache_key, 1)
                return func(self, request, *args, **kwargs)
            else:
                # If the rate limit is exceeded, return error message
                error_message = "Rate limit exceeded. Please try again later."
                return Response({"error": error_message}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        return wrapper
    return decorator
