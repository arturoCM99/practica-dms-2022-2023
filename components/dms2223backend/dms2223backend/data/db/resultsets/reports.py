""" reports class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Report
from dms2223backend.data.db.exc import ReportExistsError


class Reports():
    """ Class responsible of table-level reports operations.
    """
    @staticmethod
    def create(session: Session, title: str, content: str) -> Report:
        """ Creates a new report record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the report string.
            - content (str): The content of the report string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - UserExistsError: If a user with the same username already exists.

        Returns:
            - User: The created `report` result.
        """
        if not title or not content:
            raise ValueError('A title and a content hash are required.')
        try:
            new_report = Report(title, content)
            session.add(new_report)
            session.commit()
            return new_report
        except IntegrityError as ex:
            raise ReportExistsError(
                'A report with name ' + title + ' already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Report]:
        """Lists every report.

        Args:
            - session (Session): The session object.

        Returns:
            - List[report]: A list of `report` registers.
        """
        query = session.query(Report)
        return query.all()

    @staticmethod
    def get_report_by_id(session: Session, id: int,) -> Optional[Report]:
        """Obtains a report by an id.
        Args:
            - session (Session): The session object.
            - id (int): Id report integer.

        Returns:
            - Optional[report]: The result of the `report`.
        """

        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(report).filter_by(id=id)
            report: report = query.one()
        except NoResultFound:
            return None
        return report
