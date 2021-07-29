from fastapi import FastAPI, UploadFile, File
import time
import pandas as pd
import os
import shutil
from os import listdir
from os.path import isfile, join
import pandas as pd
import uuid
from sqlalchemy import create_engine
from zipfile import ZipFile

def convert_upload_db(): # Converts to Byte Array and Stores File in PostgreDB Server
    '''
    Converts to Byte Array and Stores File in PostgreDB Server
    '''
    def convert_to_bytearr(filename):
        with open(filename, "rb") as image:
            f = image.read()
            b = bytearray(f)
            return b

    ### Creating and inserting values into DataFrame
    mypath = "./data" #Setting file fetch path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] #Storing filenames in array
    dataset = pd.DataFrame()
    dataset["unique_id"] = ""
    dataset['filename'] = onlyfiles
    dataset["data"] = None
    for i in range(0,len(dataset)):
        dataset['data'][i] = convert_to_bytearr(f"{mypath}/{dataset['filename'][i]}")
    dataset["unique_id"] = [uuid.uuid4() for _ in range(len(dataset.index))]
    dataset["status"] = 'Uploaded'

    ###Pushing to PostgreSQL
    engine = create_engine('postgresql://sagnik:superuser@localhost:5433/data_uploader') #Selecting Engine, Change as required
    dataset.to_sql('document_table', engine, if_exists='append',index=False)
    print("Upload Complete")

app = FastAPI()

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    '''
    Upload Files to PostgreSQL DB
    Input: Use ZIP folder input through FASTAPI interface.
    Output: Append details (uuid, filename, byte array, etc.) to PostgreSQL DB
    Run Command: uvicorn main:app --reload
    '''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/uploads/{time.time()}_{file.filename}'
    f = open(f'{filename}', 'wb')
    content = await file.read()
    f.write(content)
    with ZipFile(filename, 'r') as zipObj: #Unzipping Files for further processing and stores in ./data folder
        zipObj.extractall()
    convert_upload_db()
    try: 
        shutil.rmtree("./data") #Removes unzipped files after upload is complete
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror)) #Catch error if deletion fails
    return {"Upload Successful":filename}