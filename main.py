from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    with open('database.json') as f:
        compromissos = json.load(f)
    return templates.TemplateResponse("agenda.html", {"request": request, "agenda": compromissos})

@app.get("/excluir/{id}")
async def excluir_compromisso(request: Request, id: str):
    with open('database.json') as f:
        compromissos = json.load(f)
    compromissos.pop(id, None)
    with open('database.json', 'w') as f:
        json.dump(compromissos, f)
    return RedirectResponse("/", 303)

@app.post("/adicionar")
async def adicionar_compromisso(
    request: Request,
    data: str = Form(...),
    hora: str = Form(...),
    paciente: str = Form(...),
    procedimento: str = Form(...)
):
    data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")

    with open('database.json') as f:
        compromissos = json.load(f)

    novo = {
        "data": data_formatada,
        "hora": hora,
        "paciente": paciente,
        "procedimento": procedimento
    }

    novo_agendamento = {}
    i = 1
    for id in compromissos:
        novo_agendamento[str(i)] = compromissos[id]
        i += 1

    novo_agendamento[str(i)] = novo

    with open('database.json', 'w') as f:
        json.dump(novo_agendamento, f)

    return RedirectResponse("/", 303)
