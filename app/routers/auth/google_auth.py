
import os
import uuid 
from fastapi import APIRouter,Request,HTTPException
from datetime import datetime,timedelta
from authlib.integrations.starlette_client import OAuth
from fastapi.responses import RedirectResponse

import requests
from ...utils.auth_utils import create_token
router = APIRouter()


oAuth =OAuth()



oAuth.register(
    name="resume_builder",
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration', 

    client_kwargs={"scope": "openid profile email"},

)

SECRETE_KEY=os.getenv("JWT_SECRET_KEY")
ALGORITHM="HS256"






@router.get("/login",tags=["Auth"])
async def login_google(request:Request):
    """Google login gateway: It sets the redirect,frontend url and 
    send user to the consent scren"""
    request.session.clear()
    referer = request.headers.get("referer")

    referer = request.headers.get("referer")
    frontend_url=os.getenv("FRONTEND_URL")
    redirect_url =os.getenv("REDIRECT_URL")
    request.session["login_redirect"] = frontend_url

    return await oAuth.resume_builder.authorize_redirect(request,redirect_url,prompt ="consent")


    
@router.get("/auth", tags=["Auth"])
async def google_auth(request:Request):
    try:
        token = await oAuth.resume_builder.authorize_access_token(request)
    except Exception as e :
        raise HTTPException(status_code=404 ,detail="Google auth failed")
    


    try:
       user_info_endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"
       headers = {"Authorization": f'Bearer {token["access_token"]}'}
       google_response = requests.get(user_info_endpoint, headers=headers)
       user_info = google_response.json()
    except Exception as e :
        raise HTTPException(status_code=401,detail="Google authx failed ")
    



    expires_in = token.get("expires_in",3600)
    user_id = user_info.get("id")
    user_email = user_info.get("email")
    # iss=user.get("iss")
   
    # first_logged_in =datetime.utcnow()
    

    user_name = user_info.get("name")
    user_pic=user_info.get("picture")
   

    if user_id is None:
        raise HTTPException(status_code=401, detail="Google authentication failed B/c of user_id.")
    

    access_token_expires = timedelta(seconds=expires_in)
    access_token = create_token(data={"sub":user_id,"email":user_email},expires_delta=access_token_expires)

    session_id = str(uuid.uuid4())

    print("username:",user_name)
    print("user_data",google_response)
    
    # 
    # STORE_USER_TO DATABASE
    # 
    # TODO 
    # 
    redirect_url = request.session.pop("login_redirect","")
    response = RedirectResponse(redirect_url)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="strict",
    )

    return response
