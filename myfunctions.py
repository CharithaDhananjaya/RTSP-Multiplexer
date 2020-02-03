import requests
import json
from pygments import highlight, lexers, formatters


def jsonPrint(jsonobject):

    formatted_json = json.dumps(jsonobject, sort_keys=True, indent=2)
    colorful_json = highlight(
        formatted_json,
        lexers.JsonLexer(),
        formatters.TerminalFormatter())
    print(colorful_json)

    return 0


def recognize(faceimage):
    print('---------------------------------------------')
    url = "https://covi.real.com/people?insert=true&update=true&update-if-lower-quality=false&merge=true&regroup=false&detect-age=false&detect-gender=false&detect-sentiment=false&detect-occlusion=false&differentiate=false&similar_limit=0&linear-match=false&site=default&source=default&provide-face-id=true&min-cpq=-1&min-fsq=-1&min-fcq=-1&insert-profile=false&max-occlusion=-1&event=none&context=live&type=person&include-expired=false"

    payload = open(faceimage, 'rb').read()
    headers = {
        'Accept': 'application/json;charset=UTF-8',
        'X-RPC-DIRECTORY': 'main',
        'X-RPC-AUTHORIZATION': 'mobitelpvtltd3:mic@!123',
        'Content-Type': 'image/jpeg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsonPrint(json.loads(response.text.encode('utf8')))
