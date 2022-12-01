""" AnswerLogic class module.
"""

from typing import List, Dict
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
    def answer(auth_service: AuthService, token_info: Dict, session: Session, username: str, discussionId: int) -> Answer:
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

        response : ResponseData = auth_service.auth(session.get('token'), token_info['user_token']['user'], "Discussion")

        if response.is_sucessful() == False:
            raise OperationError
        try:
            new_answer: Answer = Answers.answer(session, username, discussionId)
        except Exception as ex:
            raise ex
            return new_answer

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
