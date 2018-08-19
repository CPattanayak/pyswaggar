from flask_restplus import Api

api = Api(version='1.0', title='Sample swagger Todo',
          description='A simple demonstration of a Flask RestPlus powered API')
@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    print(message)
