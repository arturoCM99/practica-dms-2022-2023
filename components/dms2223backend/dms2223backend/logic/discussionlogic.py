""" DiscussionLogic class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Discussion
from dms2223backend.data.db.resultsets import Discussions
from dms2223backend.data.db.exc import DiscussionExistsError


class DiscussionLogic():
    """ Class with logic-level operations with the discussion-related use cases.
    """
    @staticmethod
    def create(session: Session, title: str, content: str) -> Discussion:
        """ Creates a new discussion record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the discussion string.
            - content (str): The content of the discussion string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `Discussion` result.
        """
        
        try:
            new_discussion: Discussion = Discussions.create(session, title, content)
           
        except Exception as ex:
            raise ex
        return new_discussion

    @staticmethod
    def list_all(session: Session) -> List[List]:
        """Lists every discussion.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Discussion]: A list of `Discussion` registers.
        """
        discussions = Discussions.list_all(session)
        list_of_discussions : List[List] = []
        for discussion in discussions:
            list_of_discussions.append(discussion)
        return list_of_discussions

    @staticmethod
    def get_discussion_by_id(session: Session, id: int,) -> Optional[Discussion]:
        """Obtains a discussion by an id.
        Args:
            - session (Session): The session object.
            - id (int): Id discussion integer.

        Returns:
            - Optional[Discussion]: The result of the `Discussion`.
        """

        try:
            discussion = Discussions.get_discussion_by_id(session, id)
        except Exception as ex:
            raise ex
        return discussion

    