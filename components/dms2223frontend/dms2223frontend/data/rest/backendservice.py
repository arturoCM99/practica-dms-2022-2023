""" BackendService class module.
"""
from typing import Optional
import requests
from dms2223common.data import Role
from dms2223common.data.rest import ResponseData


class BackendService():
    """ REST client to connect to the backend service.
    """

    def __init__(self,
        host: str, port: int,
        api_base_path: str = '/api/v1',
        apikey_header: str = 'X-ApiKey-Backend',
        apikey_secret: str = ''
        ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The backend service host string.
            - port (int): The backend service port number.
            - api_base_path (str): The base path that is prepended to every request's path.
            - apikey_header (str): Name of the header with the API key that identifies this client.
            - apikey_secret (str): The API key that identifies this client.
        """
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    
    def list_discussions(self, token: Optional[str]) -> ResponseData:
        """ Requests a list of registered questions.

        Args:
            token (Optional[str]): The question session token.

        Returns:
            - ResponseData: If successful, the contents hold a list of user data dictionaries.
              Otherwise, the contents will be an empty list.
        """
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + '/discussions',
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )
        response_data.set_successful(response.ok)
        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
            response_data.set_content([])
        return response_data


    
    def create_discussion(self, token: Optional[str], title: str, content: str) -> ResponseData:
        """ Requests a discussion creation.

        Args:
            - token (Optional[str]): The discussion session token.
            - title: A string with the discussion title.
            - content: A string with the discussion content.

        Returns:
            - ResponseData: If successful, the contents hold a list of user data dictionaries.
              Otherwise, the contents will be an empty list.
        """
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + '/discussions',
            json={
                'title': title,
                'content': content
            },
            headers={
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            }
        )
        response_data.set_successful(response.ok)
        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
        return response_data

   