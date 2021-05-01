import requests

def review(code, stars, amount):
    stem_url = "https://www.gedichten.nl:443/stem2.php"
    headers = {"Connection": "close", "sec-ch-ua": "\"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "sec-ch-ua-mobile": "?0", "User-Agent": "Nothing special", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://www.gedichten.nl", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    data = {"gedid": str(code), "cijfer": str(stars)}
    for i in range(amount):
        r = requests.post(stem_url, headers=headers, data=data)
        if r.status_code == 200:
            print(r.text[23:30])


#  stars go from 6-10
#  code is code found in the url,
#  https://www.gedichten.nl/nedermap/gedichten/gedicht/45554.html, the 45554 part

review(code=45554, stars=10, amount=1)
