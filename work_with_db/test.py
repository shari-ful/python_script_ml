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

def test_mongo():
    db_mongo.add_data("Alice", 30)
    db_mongo.add_data("Bob", 25)

    print("Initial data:")
    print(db_mongo.retrieve_data())

    db_mongo.update_data(db_mongo.retrieve_data()[0]["_id"], "Alice Johnson", 31)

    print("Data after update:")
    print(db_mongo.retrieve_data())

    db_mongo.delete_data(db_mongo.retrieve_data()[1]["_id"])

    print("Data after delete:")
    print(db_mongo.retrieve_data())

if __name__ == "__main__":
    test_postgres()
    test_mongo()