# Pass Python3 version as argument:
ARG PYTHON_VERSION

# Use specified Debian Linux Python3 version image:
FROM python:${PYTHON_VERSION}-slim-bookworm

# Install dipendencies and clean build cache:
RUN apt-get update && apt-get -y upgrade && apt-get -y install \
        build-essential \
        libssl-dev \
        libffi-dev \
        cargo \
        pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install necessary Python3 requirements:
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && rm requirements.txt

# Set Python3 enviroment definitions:
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Add VERSION env variable in the container:
ARG VERSION="0.0.0"
ENV VERSION=${VERSION}

# Set APP_SERVER variable to use:
ARG APP_SERVER="gunicorn"
ENV APP_SERVER=${APP_SERVER}

# Set environment variables:
ENV BACKEND_DIR="/backend"
ENV SCRIPTS_DIR="${BACKEND_DIR}/scripts"

# Create directory to host the code and copy content inside:
ADD . ${BACKEND_DIR}
WORKDIR ${BACKEND_DIR}

# Set executable permissions to scripts:
RUN chmod -R 774 ${SCRIPTS_DIR}
ENV PATH="${SCRIPTS_DIR}:${PATH}"

# Create and specify necessary volumes:
RUN mkdir -p ./static-serve/ \
    && mkdir -p ./media-serve/
VOLUME [ "/backend/static-serve", "/backend/media-serve" ]

# Expose Django Port:
EXPOSE 8000

# Impose default start up command:
ENTRYPOINT [ "entrypoint.sh" ]
