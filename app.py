from fastapi import FastAPI, Depends
import uvicorn
from schema import UserCreate
from models import User
from database import get_db, Base, engine


app = FastAPI()
Base.metadata.create_all(bind=engine)



@app.get("/")
def index():
    return "8081 index page!!!"


@app.post("/add-user-8081")
def add_user(user: UserCreate, db=Depends(get_db)):
    msg = ""
    if user:
        try:
            new_user = User(id=user.id, name=user.name)
            db.add(new_user)
            db.commit()
            msg = f"added user: {user}"
            return msg
        except Exception as e:
            # db.rollback()
            msg = f"error occurred while creating user!: {e}"
            return msg
        finally:
            db.close()
    else:
        msg = "send something!"
        return msg


@app.get("/get-all-users-8081")
def get_all_users(db=Depends(get_db)):
    all_users = db.query(User).all()
    return all_users


if "__name__" == "__main__":
    uvicorn.run("app:app", port=8081, host="0.0.0.0")
