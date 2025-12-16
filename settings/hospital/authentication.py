from rest_framework.authentication import BaseAuthentication
from .models import CustomUser

class CookieTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('auth_token')
        if not token:
            return None

        try:
            user = CustomUser.objects.get(token=token)
        except CustomUser.DoesNotExist:
           return None
        return user, None
