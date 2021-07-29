# Uploading Contents of ZIP File to Postgresql DB

- **Step 1:** Create Environment  
`python -m venv ./env`

- **Step 2:** Activate Environment  
`./env/Scripts/activate`

- **Step 3:** Installing Required Packages in Virtual Environment  
`pip install -r requirements.txt`

- **Step 4:** Running the App  
`uvicorn main:app --reload`

- **Step 5:** Open Swagger App of FastAPI  
`http://127.0.0.1:8000/docs`

- **Step 6:** Click on Upload Dropdown, then click on  
`Try it Out`

![alt text](./img/img1.png)


- **Step 7:** Click on Choose File and select any zip file which contains multiple documents/image in any format.

- **Step 8:** Click *Execute*

![alt text](./img/img2.png)

- **Step 9:** Check if you got Successful Response. Example:  
`{
  "Upload Successful": "D:\\Coding\\Uploading Contents of ZIP File to Postgresql DB\\Uploading-Contents-of-ZIP-File-to-Postgresql-DB/uploads/1627545622.5827112_sample_med_data.zip"
}`

- **Step 10:** You may open your PostgreSQL Server and check the documents saved in byte array format. For example, you can view the files in pgAdmin 4 App.

![alt text](./img/img3.png)