from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="API Estação Meteorológica - UNIP")

# Permitir que o dashboard aceda à API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variável em memória para guardar a última leitura da estação
ultima_leitura = {
    "temperatura": 0.0,
    "humidade": 0.0
}

class LeituraMetereologica(BaseModel):
    temperatura: float
    humidade: float

@app.post("/api/dados")
def receber_dados(leitura: LeituraMetereologica):
    global ultima_leitura
    ultima_leitura["temperatura"] = leitura.temperatura
    ultima_leitura["humidade"] = leitura.humidade
    print(f"[DADOS RECEBIDOS] Temperatura: {leitura.temperatura}°C | Humidade: {leitura.humidade}%")
    return {"status": "sucesso", "mensagem": "Dados registados com sucesso!"}

@app.get("/api/dados")
def obter_dados():
    return ultima_leitura