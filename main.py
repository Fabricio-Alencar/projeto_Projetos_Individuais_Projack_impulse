
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rendenizar_projetos.app import router as rendenizar_router
from criar_projetos.app import router as criar_router
from gerenciar_projetos.app import router as gerenciar_router
from gerenciar_colaboradores.app import router as colaboradores_router


app = FastAPI(title="API Principal")

# Configuração global de CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:5501",
    "http://localhost:5501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Registrar os módulos/microserviços
app.include_router(rendenizar_router)
app.include_router(criar_router)
app.include_router(gerenciar_router)
app.include_router(colaboradores_router)