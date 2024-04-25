from typing import Union

from fastapi import FastAPI
from random import randint
from imcCalc import calcular_imc, classificacao_imc

app = FastAPI()


@app.get("/")
def read_root():
    return {"Start": "Welcome to the IMC API!"}


@app.get("/imc/")
async def imc(peso: float = 60.5 , altura: float = 1.6):
    return {"IMC": calcular_imc(peso, altura), "Classificacao": classificacao_imc(calcular_imc(peso, altura))}