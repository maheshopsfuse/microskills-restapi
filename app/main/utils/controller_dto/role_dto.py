from flask_restplus import Namespace, fields


class RoleDto:
    api = Namespace('Role', description='role')
    req_role = api.model('Role Request', {
        'role_name': fields.String(required=True),
        'role_desc': fields.String(required=True, description='Role Description'),
    })
    res_role = api.model('Role Response', {
        'success': fields.String(required=True, description='Status'),
        'id': fields.String(required=True),
        'role_name': fields.String(required=True),
        'role_desc': fields.String(required=True, description='Role Description'),
    })
