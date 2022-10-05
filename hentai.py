import random
import requests
import webbrowser
def save_file (word):
    file = open("History.txt", "a")
    file.write(f"{word}")
    file.close()
url = f"https://nhentai.to/g/{random.randint(100000,700000)}"

x = requests.get(url)

if x.ok:
    webbrowser.get().open(url)
    print(url)
    save_file(f"{url}\n")
else:
    print("hentai not found run again !")
print(x.status_code)
