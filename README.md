# Uploading Contents of ZIP File to Postgresql DB

## *Steps to Run the Uploader Script:*

- **Step 1:** Create Environment  
`python -m venv ./env`

- **Step 2:** Activate Environment  
`./env/Scripts/activate`

- **Step 3:** Installing Required Packages in Virtual Environment  
`pip install -r requirements.txt`

- **Step 4:** Running the App  
`uvicorn main:app --reload`

  *Ensure to have database/table in this format, before running or change code in line 36 of main.py*
  *`postgresql://sagnik:superuser@localhost:5433/data_uploader`*

- **Step 5:** Open Swagger App of FastAPI in any browser
[Swagger App (Fast API)](http://127.0.0.1:8000/docs)

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img8.PNG)

- **Step 6:** Click on Upload Dropdown, then click on  
`Try it Out`

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img1.PNG)

- **Step 7:** Click on Choose File and select any zip file which contains multiple documents/image in any format.

- **Step 8:** Click *Execute*

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img2.PNG)

- **Step 9:** Check if you got Successful Response. Example:  
`{
  "Upload Successful": "D:\\Coding\\Uploading Contents of ZIP File to Postgresql DB\\Uploading-Contents-of-ZIP-File-to-Postgresql-DB/uploads/1627545622.5827112_sample_med_data.zip"
}`

- **Step 10:** You may open your PostgreSQL Server and check the documents saved in byte array format. For example, you can view the files in pgAdmin 4 App.

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img3.PNG)

## Note:

### *Creating DataBase in pgAdmin:*

- Create Server in pgAdmin (eg. mylocalserver)

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img4.PNG)

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img5.PNG)

- Creating Database  
`CREATE DATABASE data_uploader
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;`

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img6.PNG)

- Creating Table  
`CREATE TABLE IF NOT EXISTS public.document_table
(
    unique_id character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    data bytea,
    status character varying(255),
    PRIMARY KEY (unique_id)
);`

  `ALTER TABLE public.document_table
    OWNER to postgres;`

![alt text](https://github.com/sagnik-sudo/Uploading-Contents-of-ZIP-File-to-Postgresql-DB/blob/main/img/img7.PNG)