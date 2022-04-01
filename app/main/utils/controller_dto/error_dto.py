from flask_restplus import Model, fields


res_error = Model("Response Error", {
    'success': fields.String(required=True, description='success'),
    'message': fields.String(required=True, description='message')
})
