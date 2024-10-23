# You can import routers from files like this
from api.users import router as router_users
from api.auth import router as router_auth

all_routers = [
    # Add imported routers
    router_users,
    router_auth
]
