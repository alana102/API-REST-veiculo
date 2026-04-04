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

    # Construtor
    # def __init__ (self, id: int, tipo: str, modelo: str, ano: int, placa: str, cambio: str, cor : str, tipo_combustivel : str,
    #               num_portas: int, quilometragem: int, categoria: str, ar_condicionado: bool, valor_diaria: float, status: str):
    #     self.id = id
    #     self.tipo = tipo
    #     self.modelo = modelo
    #     self.ano = ano
    #     self.placa = placa
    #     self.cambio = cambio
    #     self.cor = cor
    #     self.tipo_combustivel = tipo_combustivel
    #     self.num_portas = num_portas
    #     self.quilometragem = quilometragem
    #     self.categoria = categoria
    #     self.ar_condicionado = ar_condicionado
    #     self.valor_diaria = valor_diaria
    #     self.status = status
    
    # Imprime os dados
    def __repr__(self):
        return f"Veiculo(id={self.id}, tipo='{self.tipo}', modelo='{self.modelo}', ano={self.ano}, placa='{self.placa}', câmbio='{self.cambio}', cor='{self.cor}', combustível='{self.tipo_combustivel}', nº de portas={self.num_portas}, quilometragem={self.quilometragem}, categoria='{self.categoria}', ar condicionado={self.ar_condicionado}, valor da diária={self.valor_diaria}, status='{self.status}')"
    
    # Métodos Getters
    def getId(self):
        return self.id
    
    def getTipo(self):
        return self.tipo
    
    def getModelo(self):
        return self.modelo
    
    def getAno(self):
        return self.ano
    
    def getPlaca(self):
        return self.placa
    
    def getCambio(self):
        return self.cambio
    
    def getCor(self):
        return self.cor
    
    def getTipoCombustivel(self):
        return self.tipo_combustivel
    
    def getNumPortas(self):
        return self.num_portas
    
    def getQuilometragem(self):
        return self.quilometragem
    
    def getCategoria(self):
        return self.categoria
    
    def getArCondicionado(self):
        return self.ar_condicionado
    
    def getValorDiaria(self):
        return self.valor_diaria
    
    def getStatus(self):
        return self.status
    
    # Métodos Setters
    def setId(self, id: int):
        self.id = id
    
    def setTipo(self, tipo: str):
        self.tipo = tipo
    
    def setModelo(self, modelo: str):
        self.modelo = modelo
    
    def setAno(self, ano: int):
        self.ano = ano
    
    def setPlaca(self, placa: str):
        self.placa = placa
    
    def setCambio(self, cambio: str):
        self.cambio = cambio
    
    def setCor(self, cor: str):
        self.cor = cor
    
    def setTipoCombustivel(self, tipo_combustivel: str):
        self.tipo_combustivel = tipo_combustivel
    
    def setNumPortas(self, num_portas: int):
        self.num_portas = num_portas

    def setQuilometragem(self, quilometragem: int):
        self.quilometragem = quilometragem
    
    def setCategoria(self, categoria: str):
        self.categoria = categoria
    
    def setArCondicionado(self, ar_condicionado: bool):
        self.ar_condicionado = ar_condicionado
    
    def setValorDiaria(self, valor_diaria: float):
        self.valor_diaria = valor_diaria
    
    def setStatus(self, status: str):
        self.status = status
    

