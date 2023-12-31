from bloggers.ext.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from uuid import UUID

class Postcontets(db.Model):
    __tablename__ = 'postcontents'
    idpostcontent = db.Column(db.String(255), primary_key=True, nullable=False)
    idpost = db.Column(db.String(255), ForeignKey('posts.idpost'), nullable=False)
    sequence = db.Column(db.Integer(), nullable=False)
    contenttext = db.Column(LONGTEXT, nullable=True)
    imagepath = db.Column(db.String(255), nullable=True)

    def __init__(self, idpostcontent: UUID, idpost: UUID, sequence: int, contenttext: str|None = None, imagepath: str|None = None) -> None:
        self.idpostcontent = idpostcontent.__str__()
        self.idpost = idpost.__str__()
        self.sequence = sequence
        self.contenttext = contenttext
        self.imagepath = imagepath

    def to_dict(self) -> dict:
        return{
            'idpostcontent': self.idpostcontent,
            'idpost': self.idpost,
            'sequence': self.sequence,
            'contenttext': self.contenttext,
            'imagepath': self.imagepath
        }