from fastapi import APIRouter, HTTPException
from src.models.veiculo_model import Veiculo
from src.database.criacao_deltalake import BancoVeiculo
import hashlib

router = APIRouter(prefix="/veiculos", tags=["CRUD de Veículos"])
db = BancoVeiculo()

@router.post("/", status_code=201)
def criar_veiculo(veiculo: Veiculo):
    
    try:
        db.insert(veiculo)
        return {"mensagem": "Veículo criado com sucesso!"}
        
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))
    
@router.get("/{id}")
def buscar_veiculo(id: int):
    try:
        df_veiculo = db.get(id)
        return df_veiculo.to_dict(orient="records")[0] 
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))
    
@router.put("/{id}")
def atualizar_veiculo(id: int, veiculo: Veiculo):
    try:
        db.update(id, veiculo)
        return {"mensagem": f"Veículo {id} atualizado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar: {str(erro)}")
    
@router.delete("/{id}")
def apagar_veiculo(id: int):
    try:
        db.delete(id)
        return {"mensagem": f"Veículo {id} removido!"}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))