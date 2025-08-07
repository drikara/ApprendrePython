# l'instruction match correspond à switch
def http_request(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "i'm teapot"
        case _:
            return "something's wrong with the internet"
            
        