from typing import Dict, List
from fastapi import APIRouter, Request

from endpoints.models import SemanticSearchTerms, FrCard, FrWord, EnCard, EnWord, WordHistory, CardHistory
from endpoints import service

router = APIRouter()


# French
@router.post("/addFrCard")
async def addFrCard(request: Request, card: FrCard) -> Dict:
    service.addCard(card.__dict__, request.app.state.fr_card_col, request.app.state.transformerModel)

    return {"status": "success"}

@router.post("/addFrWord")
async def addFrWord(request: Request, word: FrWord) -> Dict:
    service.addWord(word.__dict__, request.app.state.fr_word_col, request.app.state.transformerModel)

    return {"status": "success"}

@router.post("/recommendFrCard")
async def recommendFrCard(request: Request, card_history: CardHistory) -> List:
    return service.recommendCards(card_history, request.app.state.fr_card_col, request.app.state.transformerModel)

# English
@router.post("/addEnCard")
async def addEnCard(request: Request, card: EnCard) -> Dict:
    service.addCard(card.__dict__, request.app.state.en_card_col, request.app.state.transformerModel)

    return {"status": "success"}

@router.post("/addEnWord")
async def addEnWord(request: Request, word: EnWord) -> Dict:
    service.addWord(word.__dict__, request.app.state.en_word_col, request.app.state.transformerModel)

    return {"status": "success"}

@router.post("/recommendEnCard")
async def recommendEnCard(request: Request, card_history: CardHistory) -> List:
    return service.recommendCards(card_history, request.app.state.en_card_col, request.app.state.transformerModel)
