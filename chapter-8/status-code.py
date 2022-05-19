def status_code_meaning(number):
    if number == 200:
        return "OK"
    if number == 301:
        return "Moved Permanently"
    if number == 401:
        return "Unauthoried"
    if number == 404:
        return "Not Found"
    elif number == 500:
        return "Internal Server Error"
    else:
        return "Wrong number!"

print(status_code_meaning(200))