import pandas as pd
from deltalake import WriterProperties, write_deltalake, DeltaTable
import shutil

path = "src/database/deltalake-veiculo"
ultimo_id = "src/database/ultimo_id.seq"

shutil.rmtree(path, ignore_errors=True)

wp = WriterProperties(compression="ZSTD")

df = pd.DataFrame({"id" : pd.Series(dtype="int64"), 
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
                   "status" : pd.Series(dtype="string")})

write_deltalake(path, df, mode="overwrite", writer_properties=wp)

with open (ultimo_id, "w") as id:
    id.write("")