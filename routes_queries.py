from fastapi import APIRouter, Query, HTTPException

router = APIRouter(
    prefix="/veiculos",
    tags=["Consultas de Veículos"]
)

@router.get("/contagem")
def contar_veiculos():
    try:
        # aqui entrara a função do delta lake
        
        total_mock = 1000 
        
        return {"total_registros": total_mock}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))

@router.get("/")
def listar_veiculos(
    pagina: int = Query(1, ge=1, description="Número da página (mínimo 1)"),
    tamanho: int = Query(10, ge=1, le=100, description="Registros por página (máx 100)")
):
    try:
        # aqui entra a logica do delta lake
        
        # simulação de uma pagina de dados retornada pelo banco:
        veiculos_mock = [
            {"id": 1, "modelo": "Honda Civic", "status": "Disponível"},
            {"id": 2, "modelo": "Toyota Corolla", "status": "Alugado"}
        ]
        
        return {
            "pagina_atual": pagina,
            "tamanho_pagina": tamanho,
            "dados": veiculos_mock
        }
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))