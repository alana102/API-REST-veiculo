from fastapi import FastAPI
from api.routes_crud import router as crud_router
from api.routes_queries import router as queries_router
from api.routes_utils import router as utils_router
from api.routes_export import router as export_router

app = FastAPI()

app.include_router(crud_router)
app.include_router(queries_router)
app.include_router(utils_router)
app.include_router(export_router)

@app.get("/")
def raiz():
    return {"mensagem": "API rodando!"}

def main():
    print("Hello from api-rest-veiculo!")

if __name__ == "__main__":
    main()