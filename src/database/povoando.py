from faker import Faker
import random
import pandas as pd
from deltalake import WriterProperties, write_deltalake

path = "src/database/deltalake-veiculo"
ultimo_id = "src/database/ultimo_id.seq"
wp = WriterProperties(compression="ZSTD")

fake = Faker("pt-br")

Faker.seed(0)

tipos = {
    "Carro": [
        "Honda Civic",
        "Toyota Corolla",
        "Chevrolet Onix",
        "Volkswagen Gol",
        "Volkswagen T-Cross",
        "Ferrari",
        "Mercedes",
        "Lamborghini"
    ]
}

status = ["Disponível", "Alugado", "Em manutenção"]
cambios = ["Manual", "Automático"]
cores = ["Branco", "Preto", "Prata", "Bege", "Cinza", "Vermelho"]
combustiveis = ["Diesel", "Gasolina", "Elétrico", "Flex"]
portas = [2, 4]
categorias = ["Compacto", "SUV", "Premium", "Utilitário"]

for i in range(1000):
    next_id = 0

    with open(ultimo_id, "r") as id:
        id_atual = id.read().strip()

        if id_atual:
            next_id = int(id_atual) + 1

    tipo = random.choice(list(tipos.keys()))
    modelo = random.choice(tipos[tipo])
    ano = fake.year()
    placa = fake.license_plate()
    cambio = random.choice(cambios)
    cor = random.choice(cores)
    tipo_combustivel = random.choice(combustiveis)
    num_portas = random.choice(portas)
    quilometragem = random.randint(0, 200_000)
    categoria = random.choice(categorias)
    ar_condicionado = fake.boolean()
    valor = random.randint(50, 300)
    estado = random.choice(status)

    df_new = pd.DataFrame({"id" : [next_id], "tipo": [tipo], "modelo" : [modelo], "ano" : [ano], "placa" : [placa], "cambio" : [cambio],
                           "cor" : [cor], "tipo_combustivel" : [tipo_combustivel], "num_portas" : [num_portas], "quilometragem" : [quilometragem], 
                           "categoria" : [categoria], "ar_condicionado" : [ar_condicionado], "valor_diaria" : [valor], "status" : [estado]})
    
    write_deltalake(path, df_new, mode="append", writer_properties=wp)

    with open(ultimo_id, "w") as id:
        id.write(str(next_id))
    