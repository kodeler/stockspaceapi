myapi/
├── app/
│   ├── __init__.py
│   ├── main.py 
│   ├── api/
│   │   ├── __init__.py
│   │   ├── api_router.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   ├── items.py
│   │   │   ├── orders.py
│   │   │   └── more endpoints...
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── auth.py
│   │   ├── security.py
│   │   └── ...
│   ├── services/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── items.py
│   │   ├── orders.py
│   │   └── ...  
│   ├── models/
│   │   ├── __init__.py
│   │   ├── users.py  
│   │   ├── items.py
│   │   ├── orders.py
│   │   └── ...
│   ├── db/
│   │   ├── __init__.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   ├── items.py 
│   │   │   ├── orders.py
│   │   │   └── ...
│   │   └── database.py 
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_users.py
│   │   ├── test_items.py
│   │   └── ...
│   └── tasks/
│       ├── __init__.py
│       └── scheduled_jobs.py   
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── ...