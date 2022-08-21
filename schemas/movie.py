

from array import array


def movieEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "adult": item["adult"],
        "image_links": item["image_links"],
        "originalLanguage": item["originalLanguage"],
        "originalTitle": item["originalTitle"],
        "overview": item["overview"],
        "popularity": item["popularity"],
        "releaseDate": item["releaseDate"],
        "title": item["title"],
        "video": item["video"],
        "voteAverage": item["voteAverage"],
        "voteCount": item["voteCount"]
    }


def moviesEntity(entity) -> list:
    return [movieEntity(item) for item in entity]
