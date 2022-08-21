
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


def serializeDict(a) -> dict:
    return {
        **{
            i:str(a[i]) for i in a if i == '_id'   
        },
        **{
             i:a[i] for i in a if i != '_id' 
        }
        }

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]