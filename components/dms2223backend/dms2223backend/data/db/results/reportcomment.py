"""report Class Module
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE ,ForeignKey# type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase


class Reportcomment(ResultBase):
    """ Definition and storage of report ORM records.
    """

    def __init__(self, tipo : int,commentid:int ,content: str):
        """ Constructor method.

        Initializes a report record.

        Args:
            - title (str): A string with the report title.
            - content (str): A string with the report title.
        """

    
        self.tipo: int = tipo
        self.content: str = content
        self.commentid: int = commentid
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
            'reportscomment',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('content', String(250), nullable=False),
            Column('commentid', Integer, ForeignKey('comments.id'), nullable=False),
            Column('tipo', Integer ,nullable=False), # si vale 1 discusion , si vale 2 respuesta , si vale 3 comentario
            #Column('time', TIME, nullable = False),
            #Column('user', String(15), nullable=False),
            #Column('date', DATE, nullable = False)
        )
