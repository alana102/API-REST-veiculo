from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from enum import Enum
import hashlib

router = APIRouter(
    prefix="/utilitarios",
    tags=["Utilitários"]
)

class HashAlgoritmo(str, Enum):
    md5 = "md5"
    sha1 = "sha1"
    sha256 = "sha256"

class PedidoHash(BaseModel):
    placa: str
    algoritmo: HashAlgoritmo

@router.post("/hash")
def gerar_hash(pedido: PedidoHash):
    texto_bytes = pedido.placa.encode('utf-8')

    try:
        if pedido.algoritmo == HashAlgoritmo.md5:
            resultado = hashlib.md5(texto_bytes).hexdigest()
        elif pedido.algoritmo == HashAlgoritmo.sha1:
            resultado = hashlib.sha1(texto_bytes).hexdigest()
        elif pedido.algoritmo == HashAlgoritmo.sha256:
            resultado = hashlib.sha256(texto_bytes).hexdigest()

        return {
            "placa_original": pedido.placa,
            "algoritmo": pedido.algoritmo,
            "placa_hasheada": resultado
        }
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar hash: {str(erro)}")