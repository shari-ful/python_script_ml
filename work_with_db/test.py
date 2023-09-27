from . import db_postgres
from . import db_mongo



def test_postgres():
    db_postgres.add_data("Alice", 30)
    db_postgres.add_data("Bob", 25)

    print("Initial data:")
    print(db_postgres.retrieve_data())

    db_postgres.update_data(1, "Alice Johnson", 31)

    print("Data after update:")
    print(db_postgres.retrieve_data())

    db_postgres.delete_data(2)

    print("Data after delete:")
    print(db_postgres.retrieve_data())