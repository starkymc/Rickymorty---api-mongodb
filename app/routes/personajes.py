import hashlib
from flask import Blueprint, render_template, url_for, flash, redirect
from app.db import db
from bson import ObjectId
import requests


character_router = Blueprint('character_router', __name__)

#mostrar todos
@character_router.route("/")
def index():
  
  character = db.personajes.find()
  #character = db.personajes.find()

  #return render_template("index.html", "avatar.html", ,avatar=avt)
  return render_template("index.html", personajes=character)


#mostrar solo un personaje
@character_router.route("/uno")
def uno(id=20,idx=8):
  
  character = db.personajes.find_one({"_id": ObjectId("6380e6599452a22bd1f14e36")})
  #character = db.personajes.find()
  
  
  apix = f'''https://rickandmortyapi.com/api/episode/{id}''' 
  respx = requests.get(apix)
  datox = respx.json()

  api = f'''https://rickandmortyapi.com/api/character?page={idx}''' 
  resp = requests.get(api)
  dato = resp.json()


 


  #return render_template("index.html", "avatar.html", ,avatar=avt)
  return render_template("uno.html", personajes=character, datox=datox, dato=dato)



@character_router.route('/prueba')
def prueba(id=8,idx=22):
    api = f'''https://rickandmortyapi.com/api/character?page={id}''' 
    resp = requests.get(api)
    dato = resp.json()
    
    apix = f'''https://rickandmortyapi.com/api/episode/{idx}''' 
    respx = requests.get(apix)
    datox = respx.json()

    return render_template("prueba.html", dato=dato, datox=datox)



#guardado de data en csv
def save_data_api():
    api = '''https://rickandmortyapi.com/api/character''' 

    for i in range(len(api)):
        resp = requests.get(api)
        dato = resp.json()


    archi1 = open('rickymorth.csv','w')
    archi1.write(str(dato))
    print(dato)


def lectura_api():
    id = input("Ingresa el nro de pagina: ")
    id2 = input("Ingresa el segundo nro de pagina: ")
    api = f'''https://rickandmortyapi.com/api/character?page={id}&?page={id2}''' 
    resp = requests.get(api)
    dato = resp.json()
    for i in (dato['results']):
        print("Id:",i['id'])
        print("Name:",i['name'])
        print("Status:",i['status'])
        print("Species:",i['species'])
        print("Type:",i['type'])
        print("Gender:",i['gender'])
        print("Origin:" )
        print("    name:",i['origin']['name'])
        print("    url:",i['origin']['url'])
        print("Location:" )
        print("    name:",i['location']['name'])
        print("    name:",i['location']['url'])
        print("Image:",i['image'])
        print("Episode:")
        print("    episode:",i['episode'])
        print("Url:",i['url'])
        print("Created:",i['created'])
        print("        ")
        print("********************")
