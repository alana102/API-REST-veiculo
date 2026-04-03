from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import hashlib

router = APIRouter(
    prefix="/veiculos",
)

class Veiculo(BaseModel):
    id: int | None = Field(default=None)
    tipo: str
    modelo: str
    ano: int
    placa: str
    cambio: str
    cor: str
    tipo_combustivel: str
    num_portas: int
    quilometragem: int
    categoria: str
    ar_condicionado: bool
    valor_diaria: float
    status: str

@router.post("/", status_code=201)
def criar_veiculo(veiculo: Veiculo):
    dados = veiculo.model_dump(exclude={"id"})

    placa_bytes = dados["placa"].encode('utf-8')
    dados["placa"] = hashlib.sha256(placa_bytes).hexdigest()
    
    try:
        # aqui entraria a função para inserir os dados no banco de dados

        # simulação
        novo_id = 999 
        return {"mensagem": "Veículo criado com sucesso!", "id": novo_id}
        
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))
    
@router.get("/{id}")
def buscar_veiculo(id: int):
    try:
        # aqui entraria a função para buscar o veiculo no banco de dados
        
        # simulação
        veiculo_mock = {"id": id, "modelo": "Veículo de Teste", "status": "Disponível"}
        
        if not veiculo_mock:
            raise HTTPException(status_code=404, detail="Veículo não encontrado.")
            
        return veiculo_mock
    except HTTPException:
        raise
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))
    
@router.put("/{id}")
def atualizar_veiculo(id: int, veiculo: Veiculo):
    dados_atualizados = veiculo.model_dump(exclude={"id"})
    try:
        # aqui entraria a função para atualizar os dados do veiculo no banco de dados
        return {"mensagem": f"Veículo {id} atualizado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar: {str(erro)}")
    
@router.delete("/{id}")
def apagar_veiculo(id: int):
    try:
        # aqui entraria a função para apagar o veiculo do banco de dados
        return {"mensagem": f"Veículo {id} removido permanentemente!"}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao apagar: {str(erro)}")    