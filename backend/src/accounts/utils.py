from .models import User
from .schemas import UserCreate
from databases import Database

DATABASE_URL = "postgresql://postgres:password@172.18.0.3:5432/voyage_imaging"
database = Database(DATABASE_URL)


async def create_admin():
    """ This function creates admin user.
    """
    print("Connecting to db")
    await database.connect()
    print("Creating admin")

    data = {'full_name': 'Admin', 'email': 'admin@admin.com', 'password': 'password'}
    user = UserCreate(**data)
    user.hash_password()
    query = User.__table__.insert().values(**user.dict()).returning(User)
    try:
        data = await database.fetch_one(query)
        print("Admin user created with email: ", data.email)
    except Exception as e:
        print("ERROR:", e)

    await database.disconnect()
