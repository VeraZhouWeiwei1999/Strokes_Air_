from fastapi import FastAPI, HTTPException, status, Depends
import functions_for_api as f


app = FastAPI()


@app.get("/add-item/")
def add_item(item:str, db = Depends(f.get_db_session)):
    db.append(item)
    print(db)
    return {"message":f"added item {item}"}