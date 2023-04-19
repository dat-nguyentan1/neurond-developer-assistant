from __future__ import annotations

from datetime import timedelta

import uvicorn
from dependencies import *
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Security
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from schemas import *


app = FastAPI()


@app.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail='Incorrect username or password')
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username, 'scopes': form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get('/users/me/', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get('/users/me/items/')
async def read_own_items(
    current_user: User = Security(get_current_active_user, scopes=['items']),
):
    return [{'item_id': 'Foo', 'owner': current_user.username}]


@app.get('/status/')
async def read_system_status(current_user: User = Depends(get_current_user)):
    return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
