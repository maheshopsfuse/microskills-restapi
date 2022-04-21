from app.main.model.role import Role
from app.main import db, save


def saveRole(data):
    role_name = data['role_name']
    role_desc = data['role_desc']
    role = db.session.query(Role).filter(Role.role_name == role_name).first()

    if not role:
        new_role = Role(role_name=role_name, role_desc=role_desc)
        save(new_role)
        response_object = {
            "success": True,
            "id": str(new_role.id),
            "role_name": new_role.role_name,
            "role_desc": new_role.role_desc,
        }
        return response_object, 201
    else:
        response_object = {
            'success': False,
            'message': 'Role already exists.',
        }
        return response_object, 409
