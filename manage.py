from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main.model.lessons import Lesson
from app.main.model.course import Course
from app.main.model.skill import Skill
from app.main import create_app, db
from app import blueprint
app = create_app('dev')
app.register_blueprint(blueprint=blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db, compare_type=True)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    db.create_all()
    app.run(port=5001)


if __name__ == '__main__':
    manager.run()
