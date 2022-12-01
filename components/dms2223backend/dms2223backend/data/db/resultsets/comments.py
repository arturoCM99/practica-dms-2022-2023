""" Comments class module.
"""

import hashlib
from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Comment
from dms2223backend.data.db.exc import DiscussionExistsError
from dms2223backend.data.db.exc import UserNotFoundError

class Comments():
    """ Class responsible of table-level comments operations.
    """
    @staticmethod
    def comment(session: Session, username: str, answerId: int) -> Comment:
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
        if not username or not answerId:
            raise ValueError('An username and an Id hash are required.')
        try:
            new_comment= Comment(username, answerId)
            session.add(new_comment)
            session.commit()
            return new_comment
        except IntegrityError as ex:
            session.rollback()
            raise UserNotFoundError() from ex
        except:
            session.rollback()
            raise

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
