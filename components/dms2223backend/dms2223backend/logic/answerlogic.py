""" AnswerLogic class module.
"""

from typing import List, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db.results import Answer
from dms2223backend.data.db.resultsets import Answers
from dms2223backend.logic.exc.operationerror import OperationError
from dms2223common.data.rest import ResponseData


class AnswerLogic():
    """ Class with logic-level operations with the answers-related use cases.
    """

    @staticmethod
    def answer(session: Session, discussionid: int, content: str) -> Answer:
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

        try:
            new_answer: Answer = Answers.answer(session, discussionid, content)
           
        except Exception as ex:
            raise ex
        return new_answer

    @staticmethod
    def list_all(session: Session) -> List[Answer]:
        """Lists every answer.

        Args:
            - session (Session): The session object.

        Returns:
            - List[List]: A list of `Discussion` registers.
        """
        return Answers.list_all(session)
    
    @staticmethod
    def get_answer(session: Session ,discussionid: int) -> Answer:
        """Return a answer of a certain question and user.

        Args:
            - session (Session): The session object.
            - user (str): The user name string.
            - id (int): The question id.

        Returns:
            - Answer: The Answer of the question.
        """
        try:
            answer: Answer = Answers.get_answer(session, discussionid)
        except Exception as ex:
            raise ex
        return answer