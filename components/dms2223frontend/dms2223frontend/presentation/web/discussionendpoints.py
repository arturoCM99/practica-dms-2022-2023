""" DiscussionEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request, flash
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.backendservice import BackendService
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from .webquestion import WebQuestion


class DiscussionEndpoints():
    """ Monostate class responsible of handling the discussion web endpoint requests.
    """
    @staticmethod
    def get_discussion(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

    @staticmethod
    def get_discussion_discussions(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

        return render_template('discussion/discussions.html', name=name, roles=session['roles'], discussions=WebQuestion.list_discussions(backend_service))

    @staticmethod
    def get_discussion_discussions_new(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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
    
    @staticmethod
    def post_discussion_discussions_new(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

        # if not request.form['title'] or not request.form['content']:
        #     flash('Missing argument', 'error')
        #     return redirect(url_for('get_discussion_discussions_new'))

        new_discussion = WebQuestion.create_discussion(backend_service,
                                        request.form['title'],
                                        request.form['content']
                                        )
                                    
        if not new_discussion:
            return redirect(url_for('get_discussion_discussions_new'))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_discussion_discussions')

        #redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        return redirect(redirect_to)

    @staticmethod
    def get_discussion_discussions_view(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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
        return render_template('discussion/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title, content="Contenido de discusión", 
        answer="Respuesta a pregunta", comment="Comentario a respuesta")

    @staticmethod
    def post_discussion_discussions_view(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

        redirect_to = request.args.get('redirect_to', default='/discussion/discussions/view')
        return redirect(redirect_to)
        

    @staticmethod
    def get_discussion_discussions_answer(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

    @staticmethod
    def post_discussion_discussions_answer(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

    @staticmethod
    def get_discussion_discussions_comment(auth_service: AuthService,  backend_service: BackendService) -> Union[Response, Text]:
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

    @staticmethod
    def post_discussion_discussions_comment(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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

    @staticmethod
    def get_discussion_discussions_report(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:

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
        return render_template('discussion/discussions/report.html', name=name, roles=session['roles'], redirect_to=redirect_to, title=title)

    @staticmethod
    def post_discussion_discussions_report(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
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


    