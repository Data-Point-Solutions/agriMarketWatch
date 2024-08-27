import os
import asyncpg
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import ORJSONResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.openapi.utils import get_openapi
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.db = await asyncpg.create_pool(dsn=os.getenv("DATABASE_URL"))


@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()