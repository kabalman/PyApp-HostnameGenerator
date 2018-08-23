from flask import Flask
from flask_restful import Api
import os
from resources.host import CreateHostname, DeleteHostname, HostnameList, GetHostname

connectionstring = "postgresql://" + os.environ.get('PG_USER') + ":" + os.environ.get('PG_PASSWORD') + "@" + os.environ.get('PG_HOST') + "/" + os.environ.get('PG_DATABASE')

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = connectionstring

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(CreateHostname, '/hostname/create')
api.add_resource(DeleteHostname, '/hostname/delete/<string:hostname>')
api.add_resource(HostnameList, '/hostname/list')
api.add_resource(GetHostname, '/hostname/list/<string:hostname>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, host='0.0.0.0')
