# Here your routers

from fastapi import APIRouter

from api.dependencies import UOWDep
# from schemas.users import UserSchemaAdd
# from services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# @router.post("")
# async def add_user(
#     user: UserSchemaAdd,
#     uow: UOWDep,
# ):
#     user_id = await UsersService().add_user(uow, user)
#     return {"user_id": user_id}


# @router.get("")
# async def get_users(
#     uow: UOWDep,
# ):
#     users = await UsersService().get_users(uow)
#     return users

# @router.put("/{user_id}")
# async def edit_user(
#     user_id: int,
#     user: UserSchemaAdd,
#     uow: UOWDep,
# ):
#     await UsersService().edit_user(uow, user_id, user)
#     return {"ok": True}