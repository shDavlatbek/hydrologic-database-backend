from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy
from config import settings


SECRET = settings.jwt_secret
LIFETIME = settings.jwt_lifetime

cookie_transport = CookieTransport(cookie_max_age=LIFETIME)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=LIFETIME)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)