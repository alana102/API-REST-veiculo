from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from deltalake import DeltaTable
import io
import zipfile

router = APIRouter(
    prefix="/exportar",
    tags=["Exportação"]
)
caminho_banco = "src/database/deltalake-veiculo"

def gerador_csv_lotes():
    yield "id,tipo,modelo,ano,placa,status\n"
    
    dt = DeltaTable(caminho_banco)
    
    lotes = dt.to_pyarrow_dataset().to_batches(batch_size=1000)
    
    for lote in lotes:
        df = lote.to_pandas()
        for v in df.to_dict(orient="records"):
            yield f"{v['id']},{v['tipo']},{v['modelo']},{v['ano']},{v['placa']},{v['status']}\n"

@router.get("/csv")
def exportar_csv():
    try:
        resposta = StreamingResponse(gerador_csv_lotes(), media_type="text/csv")
        resposta.headers["Content-Disposition"] = "attachment; filename=frota_veiculos.csv"
        return resposta
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))

def gerador_zip_lotes():
    buffer = io.BytesIO()
    
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as ficheiro_zip:
        conteudo_csv = "id,tipo,modelo,ano,placa,status\n"
        
        dt = DeltaTable(caminho_banco)
        lotes = dt.to_pyarrow_dataset().to_batches(batch_size=1000)
        
        for lote in lotes:
            df = lote.to_pandas()
            for v in df.to_dict(orient="records"):
                conteudo_csv += f"{v['id']},{v['tipo']},{v['modelo']},{v['ano']},{v['placa']},{v['status']}\n"
        
        ficheiro_zip.writestr("dados.csv", conteudo_csv)
    
    buffer.seek(0)
    yield from buffer

@router.get("/zip")
def exportar_zip():
    try:
        resposta = StreamingResponse(gerador_zip_lotes(), media_type="application/zip")
        resposta.headers["Content-Disposition"] = "attachment; filename=frota_compactada.zip"
        return resposta
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))