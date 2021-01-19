from ..app import 

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fake"}
