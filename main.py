from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/aboutmylife")
def aboutme():
    return{"rukshak":"meri zindagi jhund hai q k abhi bhi main beginner level vids dekh rha hn"}



@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data
        


@app.get('/view')
def view():
    data = load_data()


    return data


@app.get('/patients/{patient_id}')
def view_patient(patient_id : str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
        
    return{'errror' : 'pateints id not found'}