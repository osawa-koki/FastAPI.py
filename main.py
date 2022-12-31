from typing import Union
from fastapi import *
from pydantic import BaseModel
from fastapi.responses import *

app = FastAPI()

class pokemonStruct(BaseModel):
    number: int
    name: str
    type1: str
    type2: str = None

@app.get("/")
def read_root():
    return PlainTextResponse("INDEX")

@app.get("/pokemon/{name:path}")
def read_root(name: str):
    return "{}!!!".format(name)

@app.post("/")
def read_root(poke: pokemonStruct):
    return "図鑑番号「{}」は「{}」で、タイプ1は「{}」、タイプ2は「{}」ですね、、、".format(poke.number, poke.name, poke.type1, poke.type2)

@app.get("/cookie")
def read_rott(response: Response, user_identifier: Union[str, None] = Cookie(default=None)):
    if user_identifier != None:
        return "your cookie -> {}".format(user_identifier)
    else:
        response.set_cookie(key="user_identifier", value="cookie_value_hogehoge")
        return "cookie set..."

@app.get("/html", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(content="<html><title>FastAPI</title><body><h1>Hello World</h1></body></html>", status_code=200)

@app.get("/plain", response_class=PlainTextResponse)
def read_root():
    return "PLAIN TEXT"

@app.get("/redirect", response_class=RedirectResponse)
def read_root():
    return RedirectResponse("/pokemon/chikorita")

@app.get("/stream/{name}")
def read_root(name: str):
    def iterfile(name):
        with open("contents/{}.png".format(name), mode="rb") as binary:
            yield from binary
    return StreamingResponse(iterfile(name), media_type="image/jpeg")

@app.get("/file")
async def read_root():
    return FileResponse("contents/tako.png")

# ##### ##### ##### ##### ##### ##### ##### ##### #####
# ##### ##### ##### 例外処理 Yeah!!!!! ##### ##### #####
# ##### ##### ##### ##### ##### ##### ##### ##### #####

from fastapi.exceptions import RequestValidationError

@app.get("/error")
async def read_root():
    raise HTTPException(status_code=444, detail="I am an error!!!")
    return PlainTextResponse("ex")

@app.exception_handler(RequestValidationError)
def validation_exception_handler(_a, _b):
    return PlainTextResponse("It's RequestValidationError...")
