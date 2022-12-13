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
from .webanswer import WebAnswer
from .webcomment import WebComment
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

        new_discussion = WebQuestion.create_discussion(backend_service,
                                        request.form['title'],
                                        request.form['content']
                                        )
                                    
        if not new_discussion:
            return redirect(url_for('get_discussion_discussions_new'))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_discussion_discussions')

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
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions')
        id: int = int(str(request.args.get('discussionid')))
        #answers = WebAnswer.list_answers(backend_service,id)
        return render_template('discussion/discussions/view.html', name=name, roles=session['roles'], redirect_to=redirect_to,
            discussion=WebQuestion.get_discussion(backend_service, id))

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
        discussionid: int = int(str(request.args.get('discussionid')))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions/view')
        return render_template('discussion/discussions/answer.html', name=name, roles=session['roles'],
            redirect_to=redirect_to, discussion=WebQuestion.get_discussion(backend_service, discussionid))

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

        new_answer = WebAnswer.create_answer(backend_service,
                                        int(request.form['discussionid']),
                                        request.form['content']
                                        )
                                    
        if not new_answer:
            discussionid: int = int(str(request.form['discussionid']))
            redirect_to = url_for('get_discussion_discussions_view', discussionid=discussionid)
            return redirect(url_for('get_discussion_discussions_answer', discussionid=discussionid, redirect_to=redirect_to))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            discussionid = int(str(request.form['discussionid']))
            redirect_to = url_for('get_discussion_discussions_view', discussionid=discussionid)

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
        answerid: int = int(str(request.args.get('answerid')))
        redirect_to = request.args.get('redirect_to', default='/discussion/discussions/view')
        return render_template('discussion/discussions/comment.html', name=name, roles=session['roles'],
            redirect_to=redirect_to, discussion=WebQuestion.get_discussion(backend_service, answerid))

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

        new_comment = WebComment.create_comment(backend_service,
                                        int(request.form['answerid']),
                                        request.form['content']
                                        )
                                    
        if not new_comment:
            answerid: int = int(str(request.form['answerid']))
            redirect_to = url_for('get_discussion_discussions_view', answerid=answerid)
            return redirect(url_for('get_discussion_discussions_comment', answerid=answerid, redirect_to=redirect_to))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            answerid = int(str(request.form['answerid']))
            redirect_to = url_for('get_discussion_discussions_view', answerid=answerid)

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


    