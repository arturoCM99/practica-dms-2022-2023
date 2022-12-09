""" ModeratorEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.backendservice import BackendService
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from .webquestion import WebQuestion


class ModeratorEndpoints():
    """ Monostate class responsible of handing the moderator web endpoint requests.
    """
    @staticmethod
    def get_moderator(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the moderator root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('moderator.html', name=name, roles=session['roles'])

    @staticmethod
    def get_moderator_reports(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the reports root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']

        #Reportes de prueba hasta backend
        reports=[{"title" : "Primer reporte", "content" : "Contenido del primer reporte"}, 
        {"title" : "Segundo reporte", "content" : "Contenido del segundo reporte"},
        {"title" : "Tercer reporte", "content" : "Contenido del tercer reporte"}]

        return render_template('moderator/reports.html', name=name, roles=session['roles'], reports=reports)

    @staticmethod
    def get_report_view(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the report root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('reporttitle'))
        redirect_to = request.args.get('redirect_to', default='/moderator/reports')
        return render_template('moderator/moderator/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title, )

    @staticmethod
    def get_moderator_discussions(auth_service: AuthService,backend_services: BackendService) -> Union[Response, Text]:
            """ Handles the GET requests to the reports root endpoint.
            Args:
                - auth_service (AuthService): The authentication service.
            Returns:
                - Union[Response,Text]: The generated response to the request.
            """
            if not WebAuth.test_token(auth_service):
                return redirect(url_for('get_login'))
            if Role.MODERATION.name not in session['roles']:
                return redirect(url_for('get_home'))
            name = session['user']

            #Reportes de prueba hasta backend

            return render_template('moderator/discussions.html', name=name, roles=session['roles'], reports=WebQuestion.list_discussions(backend_services))

    @staticmethod
    def get_discussions_view(auth_service: AuthService) -> Union[Response, Text]:
            """ Handles the GET requests to the report root endpoint.
            Args:
                - auth_service (AuthService): The authentication service.
            Returns:
                - Union[Response,Text]: The generated response to the request.
            """
            if not WebAuth.test_token(auth_service):
                return redirect(url_for('get_login'))
            if Role.MODERATION.name not in session['roles']:
                return redirect(url_for('get_home'))
            name = session['user']
            title: str = str(request.args.get('reporttitle'))
            redirect_to = request.args.get('redirect_to', default='/moderator/discussions')
            return render_template('moderator/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title,content="Contenido de discusión", 
            answer="Respuesta a pregunta", comment="Comentario a respuesta")


    @staticmethod
    def get_moderator_resolution_report(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to the resolution report root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('reporttitle'))
        redirect_to = request.args.get('redirect_to', default='/moderator/moderator')
        return render_template('moderator/moderator/resolution.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title )


    @staticmethod
    def get_moderator_moderator_view(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('discussiontitle'))
        redirect_to = request.args.get('redirect_to', default='/moderator/reports')
        return render_template('moderator/moderator/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)


