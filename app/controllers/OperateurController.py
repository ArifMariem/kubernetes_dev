from fastapi import APIRouter, Depends
from typing import List
from models import Operateur
from services import IOperateurService

router = APIRouter()

@router.get("/retrieve-all-operateurs", response_model=List[Operateur])
async def get_operateurs(operateur_service: IOperateurService = Depends()):
    return operateur_service.retrieve_all_operateurs()

@router.get("/retrieve-operateur/{operateur_id}", response_model=Operateur)
async def retrieve_operateur(operateur_id: int, operateur_service: IOperateurService = Depends()):
    return operateur_service.retrieve_operateur(operateur_id)

@router.post("/add-operateur", response_model=Operateur)
async def add_operateur(operateur: Operateur, operateur_service: IOperateurService = Depends()):
    return operateur_service.add_operateur(operateur)

@router.delete("/remove-operateur/{operateur_id}")
async def remove_operateur(operateur_id: int, operateur_service: IOperateurService = Depends()):
    operateur_service.delete_operateur(operateur_id)
    return {"message": "Operateur deleted successfully"}

@router.put("/modify-operateur", response_model=Operateur)
async def modify_operateur(operateur: Operateur, operateur_service: IOperateurService = Depends()):
    return operateur_service.update_operateur(operateur)
