
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_profile = {
    "name": "Abdulkader Baghaffar",
    "role": "Cooking connoisseur",
    "avatar": "https://placehold.co/100x147"
}

favorites = [
    {
        "title": "Sunny Egg & Toast Avocado",
        "author": "Jane Smith",
        "image": "https://placehold.co/166x208"
    }
]

ingredients = {
    "Tortilla Chips": 2,
    "Avocado": 1,
    "Red Cabbage": 9,
    "Peanuts": 1,
    "Red Onions": 1
}

related_recipes = [
    {"title": "Egg & Avo...", "image": "https://placehold.co/144x181"},
    {"title": "Bowl of r...", "image": "https://placehold.co/133x90"},
    {"title": "Chicken S...", "image": "https://placehold.co/102x128"}
]

class FavoriteItem(BaseModel):
    title: str
    author: str
    image: str

class IngredientSelection(BaseModel):
    name: str
    quantity: int

@app.get("/user")
def get_user():
    return user_profile

@app.get("/favorites")
def get_favorites():
    return favorites

@app.post("/favorites")
def add_favorite(item: FavoriteItem):
    favorites.append(item.dict())
    return {"message": "Favorite added."}

@app.delete("/favorites/{title}")
def delete_favorite(title: str):
    global favorites
    favorites = [f for f in favorites if f["title"] != title]
    return {"message": "Favorite removed."}

@app.get("/ingredients")
def get_ingredients():
    return ingredients

@app.post("/ingredients")
def update_ingredient(data: IngredientSelection):
    ingredients[data.name] = data.quantity
    return {"message": f"{data.name} updated to {data.quantity}."}

@app.get("/recipes")
def get_related_recipes():
    return related_recipes
