### About
This project use a Unit Of Work structure and integrated with FastAPI Users library

### Run server
1. Create virtual environment, install requirements
2. Rename `.env-example` to `.env` and change environments with yours
3. Run `python src/main.py`

### Migrations
1. In root directory run
`alembic revision --autogenerate -m "Message"`
2. Apply changes
`alembic upgrade head`
