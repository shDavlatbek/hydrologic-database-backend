# You can create your own services here

# from schemas.users import UserSchemaAdd
# from utils.unitofwork import IUnitOfWork


# class UsersService:
#     async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd):
#         user_dict = user.model_dump()
#         async with uow:
#             user_id = await uow.users.add_one(user_dict)
#             await uow.commit()
#             return user_id

#     async def get_users(self, uow: IUnitOfWork):
#         async with uow:
#             users = await uow.users.find_all()
#             return users
    
#     async def edit_user(self, uow: IUnitOfWork, user_id: int, user: UserSchemaAdd):
#         user_dict = user.model_dump()
#         async with uow:
#             await uow.users.edit_one(user_id, user_dict)
#             await uow.commit()
