# DMS 2022-2023 Frontend service

This frontend serves as the human interface for the other services of the appliance.

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

Configuration will be loaded from the default user configuration directory, subpath `dms2223frontend/config.yml`. This path is thus usually `${HOME}/.config/dms2223frontend/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `service_host` (mandatory): The service host.
- `service_port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `app_secret_key`: A secret used to sign the session cookies.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
- `backend_service`: A dictionary with the configuration needed to connect to the backend service.
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

Just run `dms2223frontend` as any other program.

## Services integration

The frontend service is integrated with both the backend and the authentication services. To do so it uses two different API keys (each must be whitelisted in its corresponding service); it is a bad practice to use the same key for different services, as those with access to the whitelist in one can create impostor clients to operate on the other.

## Authentication workflow

Most, if not all operations, require a user session as an authorization mechanism.

Users through this frontend must first log in with their credentials. If they are accepted by the authorization service, a user session token will be generated and returned to the frontend. The frontend will then store the token, encrypted and signed, as a session cookie.

Most of the interactions with the frontend check and refresh this token, so as long as the service is used, the session will be kept open.

If the frontend is kept idle for a long period of time, the session is closed (via a logout), or the token is lost with the cookie (e.g., closing the web browser) the session will be lost and the cycle must start again with a login.

## UI pages and components

The UI has the following templates hierarchy and structure:

- `base.html`: Base page. Blocks defined: `title`, `pagecontent`, `footer`.
  - `login.html`: Login form page. Macros used: `flashedmessages`, `submit_button`.
  - `base_logged_in.html`: Base page when a user is logged in. Blocks used: `pagecontent`. Blocks defined: `contentheading`, `contentsubheading`, `maincontent`. Macros used: `flashedmessages`, `navbar`.
    - `home.html`: Home page/dashboard. Blocks used: `title`, `contentheading`, `maincontent`.
    - `discussion.html`: Main discussion panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `discussioncontent`.
    - `moderator.html`: Main moderator panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `moderatorcontent`.
    - `admin.html`: Main administration panel. Blocks used: `title`, `contentheading`, `maincontent`. Blocks defined: `subtitle`, `administrationcontent`.
    - `admin/users.html`: Users administration listing. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`.
    - `admin/users/new.html`: User creation form page. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`, `submit_button`.
    - `admin/users/edit.html`: User editing form page. Blocks used: `contentsubheading`, `administrationcontent`. Macros used: `button`, `submit_button`.

The following macros/components are provided:

- `macros/navbar.html`
  - `navbar(roles)`: The top navigation bar.
    - Parameters:
      - `roles`: A list of role names.
- `macros/flashedmessages.html`
  - `flashedmessages()`: The bottom panel with the flashed messages.
- `macros/buttons.html`
  - `button(color_class, href, content, onclick=None)`: A link with the appearance of a button.
    - Parameters:
      - `color_class`: A string with a CSS class to use to colorize it (e.g., `bluebg`, `redbg`, `yellowbg`)
      - `href`: The link to follow when clicked.
      - `content`: The contents (usually a string) to display inside the button.
      - `onclick`: If provided, a JavaScript snippet to be run when clicked.
  - `submit_button(color_class, content)`: Special button that submits the containing form. Uses the `button` macro providing a blank link `'#'` as the `href` and a form-submitting statement as the `onclick` argument.
    - Parameters:
      - `color_class` (See `button`)
      - `content` (See `button`)



## Frontend

### Arquitectura
La arquitectura de la página web es una arquitectura multicapa ya que esta se encuentra dividida en diferentes capas apiladas de las distintas estructuras de diseño.
De esta forma se busca el objetivo de reducir las dependencias de forma coherente.

La arquitectura empleada es la conocida como Documento-Vista por lo que el frontend dispone de dos capas: capa de presentación y capa de origen de datos.

La capa de presentación se encarga de la gestión de la interacción entre el cliente y el sofware. En este caso la capa se encuentra en: `dms2223frontend/dms2223frontend/presentation`

Las diferentes capas de presentación implementan las funcionalidades los distintos endpoints existentes: `adminendpoints.py` `commonendpoints.py` `discussionendpoints.py` `moderatorendpoints.py` `sessionendpoints.py`. Estos se encargan de realizar las llamadas a los distintos métodos necesarias para la obtención de datos y su posterior comunicación.

La capa de origen de datos se encarga de la gestión de la comunicación con otros sistemas que contiene datos que usa la aplicación. En este caso la capa se encuentra en: `dms2223frontend/dms2223frontend/data`

En esta capa se encuentran los servicios `authservice.py` y `backendservice.py` que se encargan de la obtención de datos pertenecientes a otros servicios.

### Patrones de diseño
Para la obtención de un buen diseño del software se han usado varios principios pertenecientes a los principios SOLID: Single Responsibility y Interface Segregation.
El principio Single Responsibility considera que una clase solo debería tener una razón para cambiar y el principio Interface Segregation considera que el usuario no debería depender de métodos que no usa.

En este caso estos principios se ven reflejados en las distintas clases ya que solamente mantienen las responsabilidades necesarias de cada uno dependiendo solo de los métodos y clases necesarios para el manejo. Los endpoints están organizados de forma que cada uno se encarga solamente de su respectiva responsabilidad.

