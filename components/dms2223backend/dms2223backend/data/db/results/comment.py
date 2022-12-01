"""Comment Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, ForeignKey # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase

class Comment(ResultBase):
    """ Definition and storage of comment ORM records.
    """

    def __init__(self, user: str, id: int):
        """ Constructor method.

        Initializes a comment record.

        Args:
            - user (str): A string with the user's name.
            - id (int): A int with the answer's id.

        """
        self.user: str = user
        self.id: str = id


    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'comments',
            metadata,
            Column('id', Integer, ForeignKey('answers.id'), primary_key=True),
            Column('user', String(15), primary_key=True)
        )

    