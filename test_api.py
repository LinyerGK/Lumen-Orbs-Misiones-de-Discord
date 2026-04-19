import requests

def test_detectable():
    try:
        req = requests.get("https://discord.com/api/v9/applications/detectable")
        if req.status_code == 200:
            data = req.json()
            print(f"Success! Got {len(data)} games.")
            for i in range(5):
                print(f"Game: {data[i].get('name')}, ID: {data[i].get('id')}, Exes: {data[i].get('executables')}")
            # Find Fortnite
            fortnite = next((item for item in data if item['name'] == 'Fortnite'), None)
            if fortnite:
                print("Fortnite:", fortnite)
        else:
            print("Failed:", req.status_code, req.text)
    except Exception as e:
        print("Error:", e)

test_detectable()
