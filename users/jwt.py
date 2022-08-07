from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt

class JWTAuth(BaseAuthentication):
    def authenticate(self, req):
        token = req.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Não autenticado')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token Expirado')
        user = User.objects.filter(id=payload['id']).first()
        return(user, token)
        