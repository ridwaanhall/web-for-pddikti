import requests

url = "https://api-frontend.kemdikbud.go.id/search_mhs"
payload = {
    "nama": "Ridwan Halim",
    "nipd": "5210411257",
    "pt": "8720F92C-DD22-4D57-B70B-56C72E5EFDC0",
    "prodi": "67E6732E-BA0C-47ED-8759-3D73EFAFCCE5"
}
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
