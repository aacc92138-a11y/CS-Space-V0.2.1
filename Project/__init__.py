from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


def create_app():
    global app
    global login_manager
    global db
    app = Flask(__name__)
    app.config["SECRET_KEY"]='hello'
    login_manager=LoginManager(app)
    login_manager.login_view='login'

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db = SQLAlchemy(app)
    Migrate(app,db)
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


    #هندلة الايرورز
    @app.errorhandler(404)
    def error(er):
        return "قريبا... شكرا لتجربتك متاح حاليا صفحة البوستات والبروفايل فقط", 404
    @app.errorhandler(502)
    def ero502(er):
        return "حصل خطأ هصلحه..",502
    @app.errorhandler(500)
    def ero500(er):
        return "سجل دخول",500

    from Project.Home import bp as homebp
    from Project.Auth import bp as authbp
    from Project.Profile import bp as profilebp
    from Project.Posts import bp as Postsbp
    from Project.admin import bp as adminbp
    app.register_blueprint(authbp)
    app.register_blueprint(homebp)
    app.register_blueprint(profilebp)
    app.register_blueprint(Postsbp)
    app.register_blueprint(adminbp)
    
    with app.app_context():
        db.create_all()
    return app