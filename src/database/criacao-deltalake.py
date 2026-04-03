import pandas as pd
from deltalake import WriterProperties, write_deltalake, DeltaTable
import os
from models.veiculo_model import Veiculo
from database.povoando import ultimo_id
import shutil


##shutil.rmtree(path, ignore_errors=True)

class BancoVeiculo:

    def __init__(self):
        self.path = "src/database/deltalake-veiculo"
        self.ultimo_id = "src/database/ultimo_id.seq"
        self.wp = WriterProperties(compression="ZSTD")

        if not os.path.exists(self.path):
            df_vazio = pd.DataFrame({"id" : pd.Series(dtype="int64"), 
                                    "tipo" : pd.Series(dtype="string"), 
                                    "modelo" : pd.Series(dtype="string"), 
                                    "ano" : pd.Series(dtype="int64"), 
                                    "placa" : pd.Series(dtype="string"),
                                    "cambio" : pd.Series(dtype="string"),
                                    "cor" : pd.Series(dtype="string"),
                                    "tipo_combustivel" : pd.Series(dtype="string"),
                                    "num_portas" : pd.Series(dtype="int64"), 
                                    "quilometragem" : pd.Series(dtype="int64"),
                                    "categoria" : pd.Series(dtype="string"),
                                    "ar_condicionado" : pd.Series(dtype="bool"),
                                    "valor_diaria" : pd.Series(dtype="float"),
                                    "status" : pd.Series(dtype="string")})
            
            write_deltalake(self.path, df_vazio, mode = "overwrite", writer_properties = self.wp)
        
        if not os.path.exists(self.ultimo_id):
            with open(self.ultimo_id, "w") as id:
                id.write("0")

    def insert(self, veiculo:Veiculo):
        with open(self.ultimo_id, "r") as id:
            conteudo = id.read()
            id_antigo = int(conteudo)

        df_busca = DeltaTable(self.path).to_pandas(filters=[("placa", "=", veiculo.placa)])

        if not df_busca.empty:
            raise ValueError("Veículo já existente")

        df_new = pd.DataFrame({"id": [id_antigo],
                               "tipo": [veiculo.tipo],
                               "modelo": [veiculo.modelo],
                               "ano": [veiculo.ano],
                               "placa": [veiculo.placa],
                               "cambio": [veiculo.cambio],
                               "cor": [veiculo.cor],
                               "tipo_combustivel": [veiculo.tipo_combustivel],
                               "num_portas": [veiculo.num_portas],
                               "quilometragem": [veiculo.quilometragem],
                               "categoria": [veiculo.categoria],
                               "ar_condicionado": [veiculo.ar_condicionado],
                               "valor_diaria" : [veiculo.valor_diaria],
                               "status": [veiculo.status],
                               })
        write_deltalake(self.path, df_new, mode="append", writer_properties=self.wp)

        with open(self.ultimo_id, "w") as id:
            id.write(str(id_antigo + 1))

        return True

    def get(self, id: int):
        dt_busca_id = DeltaTable(self.path).to_pandas(filters=[("id", "=", id)])

        if dt_busca_id.empty:
            raise ValueError("Veículo não encontrado")

        return dt_busca_id

    def list(self, num_pg: int, tam_pg: int):
        offset = (num_pg - 1) * tam_pg
        dt_pyarrow = DeltaTable(self.path).to_pyarrow_table()
        tabela_paginada = dt_pyarrow.slice(offset=offset, length=tam_pg)
        return tabela_paginada.to_pandas()

    def update(self, id: int, veiculo:Veiculo):
        self.get(id)

        dt = DeltaTable(self.path)
        dt.update(
            predicate=f"id={id}",
            updates={
                "tipo": f"'{veiculo.tipo}'",
                "modelo": f"'{veiculo.modelo}'",
                "ano": f"{veiculo.ano}",
                "placa": f"'{veiculo.placa}'",
                "cambio": f"'{veiculo.cambio}'",
                "cor": f"'{veiculo.cor}'",
                "tipo_combustivel": f"'{veiculo.tipo_combustivel}'",
                "num_portas": f"{veiculo.num_portas}",
                "quilometragem": f"{veiculo.quilometragem}",
                "categoria": f"'{veiculo.categoria}'",
                "ar_condicionado": "true" if veiculo.ar_condicionado else "false",
                "valor_diaria" : f"{veiculo.valor_diaria}",
                "status": f"'{veiculo.status}'"
            }
        )

        return True

    def delete(self, id: int):
        self.get(id)

        DeltaTable(self.path).delete(predicate=f"id={id}")

        return True

    
    def count(self):
        dt = DeltaTable(self.path)

        total = dt.to_pyarrow_dataset().count_rows()
        return total

    def vacuum(self):
        dt = DeltaTable(self.path)
        dt.vacuum(retention_hours = 0, enforce_retention_duration=False)
        dt.optimize().compact()

        return True
        
