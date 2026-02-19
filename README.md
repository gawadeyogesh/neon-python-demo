# Neon Python Demo

This is a simple Python demo project using Neon PostgreSQL.

## Features
- Connects to Neon cloud database
- Uses environment variables
- Supports CRUD operations:
  - Add student
  - View students
  - Update student marks
  - Delete student

## Technologies
- Python
- PostgreSQL (Neon)
- psycopg2
- dotenv

## How to run
1. Install dependencies:
   pip install psycopg2-binary python-dotenv

2. Create .env file:
   PGHOST=your_host  
   PGDATABASE=your_db  
   PGUSER=your_user  
   PGPASSWORD=your_password  
   PGSSLMODE=require  

3. Run:
   python main.py
