
def parseJQUERY(dat):
    output = {}

    for object in dat:
        output[object["name"]]=object["value"]
    return output
