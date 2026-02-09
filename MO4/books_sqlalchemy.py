from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///books.db")

query = text("SELECT title FROM book ORDER BY title")

with engine.connect() as connection:
    result = connection.execute(query)
    for row in result:
        print(row[0])
