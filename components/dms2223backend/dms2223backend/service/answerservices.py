""" AnswerServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.rest import AuthService
from dms2223backend.data.db import Schema
from dms2223backend.data.db.results import Answer
from dms2223backend.logic import AnswerLogic


class AnswersServices():
    """ Monostate class that provides high-level services to handle user-related use cases.
    """
    @staticmethod
    def answer(auth_service: AuthService, token_info: Dict, username: str, discussionId: int, schema: Schema) -> None:
        """Answers a discussion.

        Args:
            - username (str): Username string.
            - discussionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - Dict: Dictonary that contains the answer's data.
        """
      
        session: Session = schema.new_session()
        try:
            AnswerLogic.create(auth_service, token_info, session, username, discussionId)
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()


    @staticmethod
    def list_all_for_discussion(discussionId: int, schema: Schema) -> List[Dict]:
        """Lists the answers of a discussion if the requestor has the discussion role.

        Args:
            - disucssionId (int): Discussion id.
            - schema (Schema): A database handler where the discussions are mapped into.

        Returns:
            - List[Dict]: List of dictionaries with the answers' data.
        """
        out: List[Dict] = []
        session: Session = schema.new_session()
        answers: List[Answer] = AnswerLogic.list_all_for_discussion(session, discussionId)
        for answer in answers:
            out.append({
                'id': answer.id,
                'username': answer.username
            })
        schema.remove_session()
        return out

    @staticmethod
    def get_answer(username: str, id: int, schema: Schema) -> Dict:
        """Obtains the answer of a discussion and user.

        Args:
            - username (str): Username string.
            - id: Discussion id.
            - token_info (Dict): A dictionary of information provided by the security schema handlers.

        Returns:
            - Dict: Answer of the discussion.
        """
        
        session: Session = schema.new_session()
        out: Dict = {}
        answer: Answer = AnswerLogic.get_answer(username, id, session)
        out['id'] = answer.id
        out['username'] = answer.username
        schema.remove_session()
        return out