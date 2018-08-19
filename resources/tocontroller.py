from flask_restplus import Resource
from flask import request

from flask_restplus import fields, reqparse
from api import api
from model.todomodel import TodoModel

todo_post = api.model('Todo post', {
    'text': fields.String(required=True, description='description of todo'),
    'completed': fields.Boolean(required=False, description='todo is complited or not'),
    'completedAt': fields.Float(required=False, description='todo completed time')
})

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('bool', type=bool, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                  default=10, help='Results per page {error_msg}')

ns = api.namespace('todos', description='Operations related to todo posts')


@ns.route('/')
class TodoResource(Resource):

    @api.expect(todo_post)
    def post(self):
        todo = TodoModel(**request.json)
        todo.save_to_db()
        return {'message': 'Success'}

    @api.expect(pagination_arguments)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)
        return TodoModel.find_all()

    @api.expect(todo_post)
    def put(self):
        todo = TodoModel(**request.json)
        todo.update_to_db()
        return {'message': 'Success'}
@ns.route('/<string:name>')
@api.response(404, 'todo not found.')
class TodoItem(Resource):
    def get(self, name):
        return TodoModel.find_by_name(name)
