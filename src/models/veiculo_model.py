from pydantic import BaseModel, Field

class Veiculo(BaseModel):
    id: int | None = Field(default=None)
    tipo: str
    modelo: str
    ano: int
    placa: str
    cambio: str 
    cor: str
    tipo_combustivel: str
    num_portas: int | None = Field(default=None)
    quilometragem: int
    categoria: str
    ar_condicionado: bool | None = Field(default=None)
    valor_diaria: float
    status: str