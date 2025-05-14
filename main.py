from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello():
    return{"message":'hello world'}


@app.get("/aboutmylife")
def aboutme():
    return{"rukshak":"meri zindagi jhund hai q k abhi bhi main beginner level vids dekh rha hn"}



@app.get("/meracareer")
def mycareer():
    return{"career":"abhi to main dataentry ka kaam kur rha hn felt like a failure aur mujhe kuch nahi pata ki mera kya bnay ga"}   