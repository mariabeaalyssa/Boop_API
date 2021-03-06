from flask import request
from flask_restplus import Resource
from ..util.dto import CommentDto
from ..util.decorator import token_required
from ..services.user_service import get_logged_in_user
from ..services.comment_service import *
from ..services.help import Helper
from ..models.post import Post

api = CommentDto.api
_comm = CommentDto.comment
parser = CommentDto.parser

@api.route("/<public_id>")
class CreateComment(Resource):
    @token_required
    @api.response(201, "Comment added")
    @api.doc("add comment", parser=parser)
    def post(self, public_id):
        comm_data = request.json

        user = get_logged_in_user(request)

        user_username = user[0]["data"]["username"]

        post = Post.query.filter_by(public_id=public_id).first()

        return new_comment(data=comm_data, username=user_username, public_id=post.public_id)

@api.route("/<public_id>")
@api.param("public_id", "comment identifier")
@api.response(404, "Comment not found.")
class PostOperations(Resource):
    @token_required
    @api.doc("get a comment")
    @api.marshal_with(_comm)
    def get(self, public_id):
        comment = get_a_comment(public_id)

        if not comment:
            api.abort(404)
        
        else:
            return comment


    @token_required
    @api.doc("delete a comment")
    def delete(self, public_id):
        comment = delete_comment(public_id)

        if not comment:
            api.abort(404)
            
        else:
            return comment
    
    @token_required
    @api.doc("update comment")
    def put(self, public_id):
        comm_data = request.json

        comment = edit_comment(public_id=public_id, data=comm_data)

        if not comment:
            api.abort(404)
        
        else:
            return comment


@api.route("/post/<public_id>")
@api.param("public_id", "post identifier")
@api.response(404, "Comment not found.")
class GetPostRelatedComments(Resource):
    @token_required
    @api.doc("get post related comments")
    @api.marshal_with(_comm)
    def get(self, public_id):
        comment = get_post_rel_comment(public_id)
        
        if not comment:
            return []

        else:
            return comment


@api.route("/all")
@api.response(404, "comments not found")
class GetAllPosts(Resource):
    @token_required
    @api.doc("get all comments")
    @api.marshal_with(_comm, envelope='data')
    def get(self):
        comments = get_all_comments()

        return comments
