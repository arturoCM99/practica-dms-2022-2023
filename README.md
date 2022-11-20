![pylint score](https://github.com/Kencho/practica-dms-2022-2023/workflows/pylint%20score/badge.svg)
![mypy typechecking](https://github.com/Kencho/practica-dms-2022-2023/workflows/mypy%20typechecking/badge.svg)

# DMS course project codebase, academic year 2022-2023

The goal of this project is to implement a basic questions and answers appliance deployed across several interconnected services.

## Autores
- Arturo Carretero Mateo
- Alvaro Díez Sáez
- Estela Victoria Ballester Delgado
- Baba Bendermel Houssam Eddine

## Manual de instalación
Para realizar el proceso de instalación en el equipo es necesario descargarlo de github a través de la ventana principal del repositorio. Para descargarlo se debe
clicar en "Code" y posteriormente en "Download ZIP".

Una vez se haya descargado el archivo es necesario descomprimir dicho archivo para las posteriores ejecuciones en el terminal.

## Manual de uso

## Frontend

### Arquitectura
La arquitectura de la página web es una arquitectura multicapa ya que esta se encuentra dividida en diferentes capas apiladas de las distintas estructuras de diseño.
De esta forma se busca el objetivo de reducir las dependencias de forma coherente.

La arquitectura empleada es la conocida como Documento-Vista por lo que el frontend dispone de dos capas: capa de presentación y capa de origen de datos.

La capa de presentación se encarga de la gestión de la interacción entre el cliente y el sofware. En este caso la capa se encuentra en: dms2223frontend/dms2223frontend/presentation

Las diferentes capas de presentación implementan las funcionalidades los distintos endpoints existentes: adminendpoints.py, commonendpoints.py, discussionendpoints.py, moderatorendpoints.py, sessionendpoints.py. Estos se encargan de realizar las llamadas a los distintos métodos necesarias para la obtención de datos y su posterior comunicación.

La capa de origen de datos se encarga de la gestión de la comunicación con otros sistemas que contiene datos que usa la aplicación. En este caso la capa se encuentra en: dms2223frontend/dms2223frontend/data

En esta capa se encuentran los servicios authservice.py y backendservice.py que se encargan de la obtención de datos pertenecientes a otros servicios.

### Patrones de diseño
Para la obtención de un buen diseño del software se han usado varios principios pertenecientes a los principios SOLID: Single Responsibility y Interface Segregation.
El principio Single Responsibility considera que una clase solo debería tener una razón para cambiar y el principio Interface Segregation considera que el usuario no debería depender de métodos que no usa.

En este caso estos principios se ven reflejados en las distintas clases ya que solamente mantienen las responsbilidades necesarias de cada uno dependiendo solo de los métodos y clases necesarios para el manejo. Los endpoints están organizados de forma que cada uno se encarga solamente de su respectiva responsabilidad. 

## Components

The source code of the components is available under the `components` directory.

### Services

The services comprising the appliance are:

#### `dms2223auth`

This is the authentication service. It provides the user credentials and rights functionalities of the application.

See the `README.md` file for further details on the service.

#### `dms2223backend`

This service provides the Q&A logic (definition of questions, answers/comments, etc.)

See the `README.md` file for further details on the service.

#### `dms2223frontend`

A frontend web service that allows to interact with the other services through a web browser.

See the `README.md` file for further details on the application.

### Libraries

These are auxiliar components shared by several services.

#### `dms2223core`

The shared core functionalities.

See the `README.md` file for further details on the component.

## Docker

The application comes with a pre-configured Docker setup to help with the development and testing (though it can be used as a base for more complex deployments).

To run the application using Docker Compose (`-d` "detaches" the standard I/O from the containers; i.e., they are run in background mode):

```bash
docker-compose -f docker/config/dev.yml up -d
```

When run for the first time, the required Docker images will be built. Should images be rebuilt, do it with:

```bash
docker-compose -f docker/config/dev.yml build
```

To stop and remove the containers:

```bash
docker-compose -f docker/config/dev.yml rm -sfv
```

By default data will not be persisted across executions. The configuration file `docker/config/dev.yml` can be edited to mount persistent volumes and use them for the persistent data.

To see the output of a container:

```bash
docker logs CONTAINER_NAME
# To keep printing the output as its streamed until interrupted with Ctrl+C:
# docker logs CONTAINER_NAME -f
```

To enter a running service as another subprocess to operate inside through a terminal:

```bash
docker exec -it CONTAINER_NAME /bin/bash
```

To see the status of the different containers:

```bash
docker container ps -a
```

## Helper scripts

The directory `scripts` contain several helper scripts.

- `verify-style.sh`: Runs linting (using pylint) on the components' code. This is used to verify a basic code quality. On GitHub, this CI pass will fail if the overall score falls below 7.00.
- `verify-type-correctness.sh`: Runs mypy to assess the type correctness in the components' code. It is used by GitHub to verify that no typing rules are broken in a commit.
- `verify-commit.sh`: Runs some validations before committing a changeset. Right now enforces type correctness (using `verify-type-correctness.sh`). Can be used as a Git hook to avoid committing a breaking change:
  Append at the end of `.git/hooks/pre-commit`:

  ```bash
  scripts/verify-commit.sh
  ```

## GitHub workflows and badges

This project includes some workflows configured in `.github/workflows`. They will generate the badges seen at the top of this document, so do not forget to update the URLs in this README file if the project is forked!
