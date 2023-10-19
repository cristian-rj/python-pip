import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Se crea la instacia
app = FastAPI()

# Se crea el recurso 
@app.get('/') # Decorador
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse) # Decorador
def get_list():
    return """
     <html>
        <head>
            <title>Platzi python pip</title>
        </head>
        <body>
            <h1>Ambientes virtuales</h1>
        </body>
    </html>    
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()