""" DiscussionEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth


class DiscussionEndpoints():
    """ Monostate class responsible of handling the discussion web endpoint requests.
    """
    @staticmethod
    def get_discussion(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('discussion.html', name=name, roles=session['roles'])

    def get_discussion_discussions(auth_service: AuthService) -> Union[Response, Text]:
            """ Handles the GET requests to the discussion root endpoint.

            Args:
                - auth_service (AuthService): The authentication service.

            Returns:
                - Union[Response,Text]: The generated response to the request.
            """
            if not WebAuth.test_token(auth_service):
                return redirect(url_for('get_login'))
            if Role.DISCUSSION.name not in session['roles']:
                return redirect(url_for('get_home'))
            name = session['user']

            #Discussions de prueba hasta backend
            discussions=[{"title" : "Primera prueba discusion", "content" : "Contenido de la primera discusión"}, 
            {"title" : "Segunda prueba discusion", "content" : "Contenido de la segunda discusión"},
            {"title" : "Tercera prueba discusion", "content" : "Contenido de la tercera discusión"}]

            return render_template('discussion/discussions.html', name=name, roles=session['roles'], discussions=discussions)


    
    def get_discussion_discussions_new(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return render_template('discussion/discussions/new.html', name=name, roles=session['roles'], redirect_to=redirect_to)
    
    def post_discussion_discussions_new(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return redirect(redirect_to)


    def get_discussion_discussions_view(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('discussiontitle'))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return render_template('discussion/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)

    
    def get_discussion_discussions_answer(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('discussiontitle'))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions/view')
        return render_template('discussion/discussions/answer.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)


    def post_discussion_discussions_answer(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return redirect(redirect_to)

    
    def get_discussion_discussions_comment(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        title: str = str(request.args.get('discussiontitle'))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions/view')
        return render_template('discussion/discussions/comment.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)

    def post_discussion_discussions_comment(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return redirect(redirect_to)

