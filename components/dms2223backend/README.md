# DMS 2022-2023 Backend Service

This service provides backend logic to the appliance.

## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
pip3 install .
#   (run this instead to install locally in "editable mode"):
# pip3 install --user -e .
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2223backend/config.yml`. This path is thus usually `${HOME}/.config/dms2223backend/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `db_connection_string` (mandatory): The string used by the ORM to connect to the database.
- `host` (mandatory): The service host.
- `port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `salt`: A configurable string used to further randomize the password hashing. If changed, existing user passwords will be lost.
- `authorized_api_keys`: An array of keys (in string format) that integrated applications should provide to be granted access to certain REST operations.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
  - `apikey_secret`: The API key this service will use to present itself to the authentication service in the requests that require so. Must be included in the authentication service `authorized_api_keys` whitelist.

## Running the service

Just run `dms2223backend` as any other program.

## REST API specification

This service exposes a REST API in OpenAPI format that can be browsed at `dms2223backend/openapi/spec.yml` or in the HTTP path `/api/v1/ui/` of the service.

## Services integration

The backend service requires an API key to ensure that only the whitelisted clients can operate through the REST API.

Requesting clients must include their own, unique API key in the `X-ApiKey-Backend` header.

When a request under that security schema receives a request, the key in this header is searched in the whitelisted API keys at the service configuration (in the `authorized_api_keys` entry). If the header is not included or the key is not in the whitelist, the request will be immediately rejected, before being further processed.

This service also has its own API key to integrate itself with the authentication service. This key must be thus whitelisted in the authentication service in order to operate.

As some operations required in the authentication service require a user session, clients using this backend must obtain and keep a valid user session token, that will be passed in the requests to this service to authenticate and authorize them.


## Backend

### Arquitectura

Para el desarrollo del Backend sea ha implementado el princpio SOLID esto nos permite mantener la separación de las tareas y reducir en cierta medida el número de dependencias, esto se realiza mediante una arquitectura de 4 capas.
- Capa de datos
- Capa logica
- Capa de servicios
- Capa de presentación

El archivo `openapi/spec.yml` es el utilizado para realizar las llamadas al backend desde el frontend , este archivo especifica las diferentes rutas de acceso al backend mediante sus métodos get, post o put. Cuando se accede a alguna de estas rutas este realiza una llamada al método indicado en la capa de presentación, estas pueden ser mediante get, post o put, estas llamadas son capaces de recibir parámetros mediante un paquete json o bien insertados en la url.

Los ficheros de la capa de presentación se encuentran ubicados en `components/dms2223backend/dms2223backend/presentation/rest/`, donde encontraremos los ficheros que corresponden a `discussion.py` `answer.py` `comment.py` `report.py` y dentro de estos se encuentran los métodos de la capa de presentación, estos son los responsables de llamar a la capa de servicio, después recoger sus datos y los transformarlos para finalmente poder ser utilizados por el frontend, esto requiere devolver los datos obtenidos por capa de servicios y/o el estado HTTP asociado (HTTPStatus.ok, HTTPStatus.BAD_REQUES, HTTPStatus.Forbidden).

Los ficheros la capa de servicios se encuentran en `components/dms2223backend/dms2223backend/service/` donde encontraremos los ficheros que corresponden a `discussionservices.py` `answerservices.py` `commentservices.py` `moderatorservices.py`, en estos encontramos los diferentes métodos llamados por la capa de presentación y son los responsables de: establecer la sesión con la base de datos, también deben llamar a los métodos de la capa lógica y almacenar los resultados obtenidos en listas o diccionarios. Esto permitirá poder realizar las transformaciones necesarias de la capa de servicios a formato JSON de forma más cómoda para que estos ser utilizados finalmente por el frontend.

Los ficheros de la capa lógica se encuentran `components/dms2223backend/dms2223backend/logic/`, donde encontramos los ficheros `answerlogic.py`, `commentlogic.py`, `discussionlogic.py` y `reportlogic.py`, en estos encontramos los métodos llamados de la capa de servicio. Estos métodos se encargan de la comunicación con la capa de datos, también pueden trabajar con estos datos para obtener información más compleja y devolverla a la capa de servicio, esta también se encarga de devolver  los errores y/o excepciones que sucedan en la ejecución.

Finalmente, los ficheros de la capa de datos se encuentran en: `components/dms2223backend/dms2223backend/data/db/`, aquí encontramos la carpeta `results` y la carpeta `resulsets`. Dentro de la carpeta `resultsets` encontramos los ficheros `answers.py`, `comments.py` , `discussion.py` y `report.py` donde se encuentran los métodos que nos permiten modificar/editar estas clases. En la otra carpeta `results` encontramos los ficheros `answer.py`, `comment.py`, `discussion.py` y `report.py` en estos encontramos los métodos de definición de las tablas y el mapeo de las mismas.

## Endpoints del archivo openapi/spec.yml


