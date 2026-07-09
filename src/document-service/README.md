Initialized the document service using FastAPI

# Purpose
It will Store Documents.


# Folder structure
document-service/
│
├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   ├── config/
│   └── main.py
│
├── tests/
├── requirements.txt
├── README.md
└── .gitignore


# how to run 
1. start the environment
    open .venv folder -> Scripts -> copy path of Activate.ps1
    and paste it to terminal -> enter
2. run code uvicorn app.main:app --reload
and open the url http://127.0.0.1:8000
and http://127.0.0.1:8000/docs (Swagger UI)