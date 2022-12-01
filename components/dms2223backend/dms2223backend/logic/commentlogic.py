""" CommentLogic class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db.results import Comment
from dms2223backend.data.db.resultsets import Comments
from dms2223backend.logic.exc.operationerror import OperationError
from dms2223common.data.rest import ResponseData

class CommentLogic():
    """ Class responsible of table-level comments operations.
    """
    @staticmethod
    def comment(auth_service: AuthService, token_info: Dict, session: Session, username: str, answerId: int) -> Comment:
        """ Comment a comment.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - username (str): The username of the comment string.
            - discussionId (str): Id of the discussion.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        response : ResponseData = auth_service.auth(session.get('token'), token_info['user_token']['user'], "Answer")

        if response.is_sucessful() == False:
            raise OperationError
        try:
            new_comment: Comment = Comments.comment(session, username, answerId)
        except Exception as ex:
            raise ex
            return new_comment

    @staticmethod
    def list_all(session: Session) -> List[Comment]:
        """Lists every comment.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Comment]: A list of `Comment` registers.
        """
        query = session.query(Comment)
        return query.all()
