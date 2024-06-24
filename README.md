# Things to install:

pip 3 install python-jose, passlib, psycopg2, sqlalchemy

# Vitural environment

Set up - python3 -m venv fastapienv

Activate - source fastapienv/bin/activate

Start the backend - uvicorn main:app --reload

Deactive - deactivate

# sqlite 3

Start - sqlite3

Quit - .quit

Show all the columns in this table - .schema

# Long hex string for SECRET

openssl rand -hex 32

# Database common command:

.mode column/markdown/box/table

# Vitural environment

Set up - python3 -m venv fastapienv

Activate - source fastapienv/bin/activate

Start the backend - uvicorn main:app --reload

Deactive - deactivate

# sqlite 3 relevant command

Start - sqlite3

Quit - .quit

Show all the columns in this table - .schema

About Alembic

1. alembic init alembic
2. Do some configuration in alembic.ini file

- which database --- the address of it

3. Do some configuration in .env file
4. alembic revision -m "Create phone number for user column"
