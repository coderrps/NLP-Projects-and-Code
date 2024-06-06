import http.client

conn = http.client.HTTPSConnection("grocery-pricing-api.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "6941834ab7mshc0a871d4a3a3d15p1c53d8jsn3e2cde2ef6c6",
    'X-RapidAPI-Host': "grocery-pricing-api.p.rapidapi.com"
}

conn.request("GET", "/searchGrocery?keyword=sweet%20potato&perPage=10&page=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))