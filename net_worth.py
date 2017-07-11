#also create api.txt file in the same folder and put your API key there

import requests, json, re, time

api_file = open("api.txt","r")
api = api_file.read()


# set header
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
# set header

interval = 3600

while True:
    request = requests.get("https://1broker.com/api/v2/user/overview.php?token={}".format(api), headers=hdr)


    geturl_readable = str(request.text)

    print (geturl_readable)

    parsed_json = json.loads(geturl_readable)

    print(parsed_json['response'])

    balance = re.findall("'net_worth': '([\d\.]+)",str(parsed_json['response']))
    print (balance[0])

    f = open('net_worth.log', 'a')
    f.write("{} {}\n".format(time.time(), balance[0]))
    f.close()

    time.sleep(interval)
