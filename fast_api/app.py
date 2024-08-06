from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_api.database import get_session
from fast_api.models import User
from fast_api.schemas import Message, UserDB, UserList, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserDB)
def create_user(user: UserSchema, session=Depends(get_session)):
    db_user = session.scalar(select(User).where(User.name == user.name))

    if db_user:
        if db_user.name == user.name:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Name already exists',
            )
    db_user = User(name=user.name, age=user.age)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session)
):
    user = session.scalars(select(User).limit(limit).offset(offset))
    return {'users': user}


@app.put('/users/{id_user}', response_model=UserDB)
def update_user(
    id_user: int, 
    user: UserSchema, 
    session: Session = Depends(get_session)
):
    db_user = session.scalar(
        select(User).where(User.id == id_user)
    )

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db_user.name = user.name
    db_user.age = user.age

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/{id_user}', response_model=Message)
def delete_user(id_user: int, session: Session = Depends(get_session)):
    
    db_user = session.scalar(
        select(User).where(User.id == id_user)
    )

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}
