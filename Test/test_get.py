import requests

url = "https://reqres.in/api/users"
key = {'page':'2'}

resp=requests.get(url, params=key,)
print(resp.text)
print(resp.headers.get('Content-Type'))
print(resp.json())
dmda = resp.json()

for dm in dmda['data']:
    if dm['id']==9:
        print(dm['avatar'])

print (dmda['support']['text'])

print ('#########'*30)

url2 = 'https://httpbin.org/basic-auth/gh/kl'
sep = requests.session()
sep.auth= auth=('gh', 'kl')
re=sep.get(url2)
print(re.status_code)
js= re.json()
print(js)

print ('##########'*30)
url3 = 'https://httpbin.org/delay/2'
ty = requests.get(url3, timeout = 3)
print(ty.status_code)
ty_json= ty.json()
print(ty_json)

print('############'*30)
url4 = 'https://httpbin.org/cookies'
hj = requests.session()
hj.cookies.update({'test':'selenium'})
cookie= {'co':'bo'}
lo=hj.get(url4, cookies =cookie)
print (lo.status_code)
print(lo.cookies)
lo_js = lo.json()
print(lo_js)

