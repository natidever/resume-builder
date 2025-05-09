
import os 

from datetime import datetime,timedelta
from jose import jwt,ExpiredSignatureError,JWTError
from fastapi import Cookie,HTTPException

SECRETE_KEY=os.getenv("JWT_SECRET_KEY")
ALGORITHM="HS256"


def create_token(data:dict,expires_delta:timedelta=None):
    """  Token is being created using user data"""
    data_to_encode=data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    data_to_encode.update({"exp":expire})

    return jwt.encode(data_to_encode,SECRETE_KEY,algorithm=ALGORITHM)

def get_current_user(token:str=Cookie(None)):
    """Getting the current user by decoding the token """
    if not token:
        raise HTTPException(status_code=401,detail="Not authenticated")
    try:
        payload =jwt.decode(token,SECRETE_KEY,algorithms=[ALGORITHM])
        return {"user_id":payload.get("sub"),"email":payload.get("email")}
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


