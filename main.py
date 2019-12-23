from flask import Flask
import pymysql
from user import user_bp
from user import create_db


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://elsie:123456@118.89.137.230/py1907'
create_db(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
