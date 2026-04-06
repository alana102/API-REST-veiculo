import pandas as pd
from deltalake import WriterProperties, write_deltalake
import shutil

path = "src/database/deltalake-veiculo"
ultimo_id = "src/database/ultimo_id.seq"
wp = WriterProperties(compression="ZSTD")

shutil.rmtree(path, ignore_errors=True)

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
                        "ar_condicionado" : pd.Series(dtype="boolean"),
                        "valor_diaria" : pd.Series(dtype="float"),
                        "status" : pd.Series(dtype="string")})
            
write_deltalake(path, df_vazio, mode = "overwrite", writer_properties = wp)
        
with open(ultimo_id, "w") as id:
    id.write("0")