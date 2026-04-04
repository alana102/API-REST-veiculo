from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import io
import zipfile

router = APIRouter(
    prefix="/exportar",
    tags=["Exportação"]
)

def gerador_csv_lotes():
    yield "id,tipo,modelo,ano,placa,status\n"
    
    # codigo para ler o delta lake em pedaços
    
    # simulação
    lotes_simulados = [
        [{"id": 1, "tipo": "Carro", "modelo": "Civic", "ano": 2023, "placa": "ABC-123", "status": "Disponível"}],
        [{"id": 2, "tipo": "Moto", "modelo": "Biz", "ano": 2022, "placa": "XYZ-987", "status": "Alugado"}]
    ]
    
    for lote in lotes_simulados:
        for v in lote:
            linha = f"{v['id']},{v['tipo']},{v['modelo']},{v['ano']},{v['placa']},{v['status']}\n"
            yield linha

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
        
        # simulação
        lotes_simulados = [
            [{"id": 1, "tipo": "Carro", "modelo": "Civic", "ano": 2023, "placa": "ABC-123", "status": "Disponível"}]
        ]
        
        for lote in lotes_simulados:
            for v in lote:
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