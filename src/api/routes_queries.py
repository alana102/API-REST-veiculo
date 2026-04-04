from fastapi import APIRouter, Query, HTTPException
from src.database.criacao_deltalake import BancoVeiculo

router = APIRouter(
    prefix="/veiculos",
    tags=["Consultas de Veículos"]
)
db = BancoVeiculo()

@router.get("/contagem")
def contar_veiculos():
    try:
        total = db.count()
        return {"total_registros": total}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))

@router.get("/")
def listar_veiculos(
    pagina: int = Query(1, ge=1, description="Número da página (mínimo 1)"),
    tamanho: int = Query(10, ge=1, le=100, description="Registros por página (máx 100)")
):
    try:
        df_paginado = db.list(pagina, tamanho)
        veiculos_reais = df_paginado.to_dict(orient="records")
        
        return {
            "pagina_atual": pagina,
            "tamanho_pagina": tamanho,
            "dados": veiculos_reais
        }
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))