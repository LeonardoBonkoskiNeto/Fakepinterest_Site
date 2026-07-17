
from flask import Flask

app = Flask(__name__)
print("ID do app em main:", id(app))

print(app.url_map)

from Fakepinterest import routes