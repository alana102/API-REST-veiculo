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
    num_portas: int
    quilometragem: int
    categoria: str
    ar_condicionado: bool
    valor_diaria: float
    status: str