""" Answers class module.
"""

import hashlib
from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Answer
from dms2223backend.data.db.exc import DiscussionExistsError
from dms2223backend.data.db.exc import UserNotFoundError


class Answers():
    """ Class responsible of table-level answers operations.
    """
    @staticmethod
    def answer(session: Session, username: str, discussionId: int) -> Answer:
        """ Answers a discussion.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - username (str): The username of the answer string.
            - discussionId (str): Id of the discussion.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        if not username or not discussionId:
            raise ValueError('An username and an Id hash are required.')
        try:
            new_answer = Answer(username, discussionId)
            session.add(new_answer)
            session.commit()
            return new_answer
        except IntegrityError as ex:
            session.rollback()
            raise UserNotFoundError() from ex
        except:
            session.rollback()
            raise

    @staticmethod
    def list_all(session: Session) -> List[Answer]:
        """Lists every answer.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Answer]: A list of `Answer` registers.
        """
        query = session.query(Answer)
        return query.all()
