from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..util.decorator import token_required, admin_token_required
from ..services.user_service import *

api = UserDto.api
_user = UserDto.user
parser = UserDto.parser

@api.route("/")
class UserAuth(Resource):
    @api.doc("show current user")
    def get(self):
        data, status = get_logged_in_user(request)

        payload = data.get("data")
        
        if not payload:
            return data, status

        return payload

    @api.response(201, "User successfully created.")
    @api.doc("register a user", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_user(data=post_data)


@api.route("/<username>")
@api.param("username", "The User identifier")
@api.response(404, "User not found.")
class UserOperations(Resource):
    @token_required
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, username):
        user = get_a_user(username)

        if not user:
            api.abort(404)

        else:
            return user

    @token_required
    @api.doc("delete a user")
    def delete(self, username):
        user = delete_user(username)

        if not user:
            api.abort(404)
            
        else:
            return user

    @token_required
    @api.doc("update a user", parser=parser)
    def put(self, username):
        post_data = request.json

        return update_user(username, post_data)  

@api.route("/verify/email")
class UserByEmailExistenceCheck(Resource):
    @api.doc("check user existence by email")
    def get(self):
        data = request.json
        print(data)
        print(user_by_email_existence_check(data))
        return user_by_email_existence_check(data)

@api.route("/verify/username")
class UserByUsernameExistenceCheck(Resource):
    @api.doc("check user existence by username")
    def get(self):
        data = request.json
        print(data)
        print(user_by_username_existence_check(data))
        return user_by_username_existence_check(data)    

@api.route("/pet/<public_id>")
@api.param("public", "Owners of a specific pet")
@api.response(404, "Users not found.")
class GetPetOwnerList(Resource):
    @token_required
    @api.doc("get owners with specific pet")
    @api.marshal_list_with(_user, envelope="data")
    def get(self, public_id):
        owners = get_pet_owners(public_id=public_id)
        
        return owners

@api.route("/all")
@api.response(404, "Users not found")
class GetAllUsers(Resource):
    @admin_token_required
    @api.doc("get all users")
    @api.marshal_with(_user, envelope="data")
    def get(self):
        users = get_all_users()

        return users

    