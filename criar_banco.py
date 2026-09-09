from Fakepinterest import database, app
from Fakepinterest.models import Usuario, foto

with app.app_context():
    database.create_all()