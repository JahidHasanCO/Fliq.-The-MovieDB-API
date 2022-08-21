def movieEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


def moviesEntity(entity) -> list:
    return [movieEntity(item) for item in entity]
