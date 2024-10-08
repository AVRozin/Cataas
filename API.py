import requests
r = requests.get('https://www.wikipedia.org/')
print(r)
print(r.headers) # мы получили заголовки
# print(r.text)

r2 = requests.get('https://catfact.ninja/fact')
f = r2.json()
print(f)
print(f['fact'])



# 1xx - информация
# 2xx - успешно
# 3xx - перенаправление
# 4xx - ошибка клиента (на вашей стороне)
# 5xx - ошибка сервера (на их стороне)
