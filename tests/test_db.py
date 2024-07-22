from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(
        name='nicolas',
        age=18,
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.id == 1))

    assert result.id == 1
