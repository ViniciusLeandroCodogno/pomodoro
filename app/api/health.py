from fastapi import APIRouter, HTTPException

from app.database.connection import engine

from sqlalchemy import text, exc

router = APIRouter(tags=["health"])

@router.get("/health")
async def health():
    try:
        async with engine.connect() as conn:
            text_conversion = text("SELECT 1")
            await conn.execute(text_conversion)
    except (exc.SQLAlchemyError, OSError) as error:
        raise HTTPException(status_code=503, detail="O servidor está temporariamente incapaz de lidar com a requisição") from error

    return {"status": "healthy"}