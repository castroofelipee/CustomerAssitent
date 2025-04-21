from fastapi import APIRouter
from models.reservation import Reservation
from datetime import date
import json
from config import DATASET_PATH

router = APIRouter()

@router.get("/today", response_model=list[Reservation])
def get_today_reservations():
    today_str = date.today().isoformat()  # "2024-04-21"
    with open(DATASET_PATH, "r") as file:
        data = json.load(file)
    
    today_reservations = []

    for diner in data.get("diners", []):
        for reservation in diner.get("reservations", []):
            if reservation["date"] == today_str:
                today_reservations.append({
                    "id": hash((diner["name"], reservation["date"])),
                    "name": diner["name"],
                    "time": "unknown",
                    "party_size": reservation["number_of_people"],
                    "vip": False,
                    "allergies": None,
                    "special_request": None,
                    "occasion": None
                })
    
    return today_reservations

