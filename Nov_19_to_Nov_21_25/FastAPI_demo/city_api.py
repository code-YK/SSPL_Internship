from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class city(BaseModel):
    id : int
    name : str
    country : str
    review : Optional[str] = None

city_db = {}

@app.post("/city/", response_model=city)
def create_city(city: city):
    if city.id in city_db:
        raise HTTPException(status_code=400, detail="City already exists")
    city_db[city.id] = city
    return city

@app.get("/city/{city_id}", response_model=city)
def read_city(city_id: int):
    city = city_db.get(city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

class UpdateCity(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    review: Optional[str] = None

@app.put("/city/{city_id}", response_model=city)
def update_city(city_id: int, city_update: UpdateCity):
    city = city_db.get(city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    if city_update.name is not None:
        city.name = city_update.name
    if city_update.country is not None:
        city.country = city_update.country
    if city_update.review is not None:
        city.review = city_update.review
    city_db[city_id] = city
    return city

@app.delete("/city/{city_id}")
def delete_city(city_id: int):
    if city_id not in city_db:
        raise HTTPException(status_code=404, detail="City not found")
    del city_db[city_id]
    return {"detail": "City deleted"}
