""" CommentLogic class module.
"""

from typing import List
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.results import Comment
from dms2223backend.data.db.resultsets import Comments


class CommentLogic():
    """ Class responsible of table-level comments operations.
    """
    @staticmethod
    def comment(session: Session, answerid: int, content: str) -> Comment:
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
        try:
            new_comment: Comment = Comments.answer(session, answerid, content)
           
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

        return Comments.list_all(session)

    @staticmethod
    def get_comment(session: Session ,answerid: int) -> Comment:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            answer: Comment = Comments.get_answer(session, answerid)
        except Exception as ex:
            raise ex
        return answer