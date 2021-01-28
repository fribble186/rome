from rome.routers import router


@router.get("/md/", tags=["md"])
async def md_home():
    return "md_home"


@router.get("/md/user", tags=["md"])
async def md_user():
    return "md_user"
