""" CommentServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Comment
from dms2223backend.logic import CommentLogic

class CommentsServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def comment(answerid: int, content: str, schema: Schema) -> Dict:
        """Comments an answer.

        Args:
            - discussionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - Dict: Dictonary that contains the answer's data.
        """
      
        session: Session = schema.new_session()
        out: Dict = {}
        try:
            new_comment: Comment = CommentLogic.comment(session, answerid, content)
            
            out['id'] = new_comment.id #type: ignore
            out['answerid'] = new_comment.answerid
            out['content'] = new_comment.content

        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out


    @staticmethod
    def list_all_for_answer(answerid: int, schema: Schema) -> List[Dict]:
        """Lists the comments of a discussion if the requestor has the discussion role.

        Args:
            - disucssionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: List of dictionaries with the comments' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        comments: List[Comment] = CommentLogic.list_all_for_answer(answerid, session)
        for comment in comments:
            out.append({
                'id': comment.id, #type: ignore
                'answerid': comment.answerid,
                'content': comment.content
            })
        schema.remove_session()
        return out

    @staticmethod
    def get_comment(answerid: int, schema: Schema) -> Dict:
        """Obtains the comment of a discussion and user.

        Args:
            - username (str): Username string.
            - id: Discussion id.
            - token_info (Dict): A dictionary of information provided by the security schema handlers.

        Returns:
            - Dict: Comment of the answer.
        """
        session: Session = schema.new_session()
        out: Dict = {}
        comment: Comment = CommentLogic.get_comment(session, answerid)
        out['id'] = comment.id #type: ignore
        out['answerid'] = comment.answerid
        out['content'] = comment.content
        schema.remove_session()
        return out
