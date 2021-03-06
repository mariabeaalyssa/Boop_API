from .. import db
from app.main.models import user, post

comment_post_rel = db.Table("comment_post_rel",
    db.Column("post_id", db.String, db.ForeignKey("post.public_id", ondelete="cascade")),
    db.Column("comm_id", db.String, db.ForeignKey("comment.public_id", ondelete="cascade"))
)

class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    comment = db.Column(db.String(300), nullable=False)
    # post_gallery = db.Column(db.String(50), nullable=True)
    posted_on = db.Column(db.DateTime, nullable=False)
    posted_by = db.Column(db.String, db.ForeignKey('user.username', ondelete="cascade"))
    post_id = db.Column(db.String, db.ForeignKey('post.public_id', ondelete="cascade"))

    post_rel = db.relationship("Post", secondary=comment_post_rel, backref=db.backref("post", lazy=True), cascade="all, delete", passive_deletes=True)


    def __repr__(self):
        return "<comment '{}'>".format(self.public_id)
