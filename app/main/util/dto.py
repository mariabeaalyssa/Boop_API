from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace("auth", description="authentication related operations")

    user_auth = api.model("user_auth", {
        "username_or_email" : fields.String(required=True, description="user username or email address"),
        "password" : fields.String(required=True, description="user password")
    })

    parser = api.parser()

    # parser.add_argument("username_or_email", type=str, help="user username or email address", location="form")
    # parser.add_argument("password", type=str, help="user password", location="form")

class UserDto:
    api = Namespace("user", description="user related operations")

    user = api.model("user", {
        "first_name" : fields.String(required=True, description="user first name"),
        "last_name" : fields.String(required=True, description="user last name"),
        "bio" : fields.String(required=True, description="user bio"),
        "email" : fields.String(required=True, description="user email"),
        "username" : fields.String(required=True, description="user username"),
        "contact_no" : fields.String(required=False, description="user contact number")
    })

    parser = api.parser()

class PetDto:
    api = Namespace("pet", description="pet related operations")

    pet = api.model("pet", {
        "public_id" : fields.String(required=True, description="pet public id"),
        "pet_name" : fields.String(required=True, description="pet name"),
        "bio" : fields.String(required=True, description="pet bio"),
        "birthday" : fields.DateTime(dt_format="rfc822", required=False, description="pet birthday"),
        "sex" : fields.String(required=True, description="pet sex"),
        "profPic_filename" : fields.String(required=True, description="pet large profile picture"),
        "specie_name" : fields.String(required=True, description="pet specie"),
        "breed_name" : fields.String(required=True, description="pet breed"),
        "pet_owner" : fields.String(required=True, decription="pet owner")
    })

    parser = api.parser()

class SpecieDto:
    api = Namespace("specie", description="specie related operations")

    specie = api.model("specie", {
        "public_id" : fields.String(required=True, description="specie public id"),
        "specie_name" : fields.String(required=True, description="specie name")
    })

    parser = api.parser()

class BreedDto:
    api = Namespace("breed", description="breed related operations")

    breed = api.model("breed", {
        "breed_name": fields.String(required=True, description="breed name"),
        "public_id" : fields.String(require=True, description="breed public id")
    })

    parser = api.parser()

class CircleDto:
    api = Namespace("circle", description="circle related operations")

    circle = api.model("circle", {
        "circle_name" : fields.String(required=True, description="circle name")
    })

    parser = api.parser()

class BusinessDto:
    api = Namespace("business", description="business related operations")

    business = api.model("business", {
        "business_name" : fields.String(required=True, description="business email address"),
        "address": fields.String(required=False, description="business address"),
        "contact_no" : fields.String(required=False, description="business contact number")
    })

    parser = api.parser()


class PostDto:
    api = Namespace("post", description="post related operations")

    post = api.model("post", {
        "post_id" : fields.String(require=True, description="post id"),
        "content" : fields.String(required=True, description="post contents"),
        "posted_on" : fields.DateTime(dt_format="rfc822", required=True, description="date posted"),
        "post_author" : fields.String(required=True, decription="post author")
    })

    parser = api.parser


class DealDto:
    api = Namespace("deal", description="pet sale/adopt related operations")

    deal = api.model("deal", {
        "public_id" : fields.String(required=True, description="transaction id"),
        "price" : fields.Fixed(decimals=2, required=True, description="pet price"),
        "for_sale" : fields.Boolean(required=True, description="pet for adoption"),
        "posted_on" : fields.Boolean(dt_format="rfc822", required=True, description="transaction post date"),
        "deal_owner" : fields.String(required=True, decription="deal owner")

    })

    parser=api.parser


class CommentDto:
    api = Namespace("comment", description="comment related operations")

    comment = api.model("comment", {
        "public_id" : fields.String(required=True, description="comment id"),
        "comment" : fields.String(required=True, description="comment contents"),
        "posted_on" : fields.DateTime(required=True, description="comment post date"),
        "posted_by" : fields.String(required=True, decription="comment by"),
        "post_id" : fields.String(required=True, decription="commented on")
    })

    parser = api.parser