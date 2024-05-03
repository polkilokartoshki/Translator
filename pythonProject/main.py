from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from googletrans import Translator

app = FastAPI(debug=True)

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

# Инициализируем объект Translator для перевода текста
translator = Translator()

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Обработка запроса на перевод
@app.post("/translate/", response_class=HTMLResponse)
async def translate_text(request: Request, text: str = Form(...)):
    translated_text = translator.translate(text, dest='en').text
    return templates.TemplateResponse("translation_result.html", {"request": request, "translated_text": translated_text})
