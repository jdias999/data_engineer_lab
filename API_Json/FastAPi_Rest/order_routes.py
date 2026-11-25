from fastapi import APIRouter

order_rounter = APIRouter(prefix='/order', tags=['order'])

@order_rounter.get('/')
async def pedidos():
    return {"mensagem": "rota de pedidos"}
