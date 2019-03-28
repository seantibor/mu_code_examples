import requests

def get_joke():
    with requests.Session() as session:
        session.headers.update({'Accept': 'application/json'})
        r = session.get('https://icanhazdadjoke.com/').json()
    return r['joke']