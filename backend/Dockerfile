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
    && rm -rf /var/lib/apt/lists/*

# Install necessary Python3 requirements:
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && rm requirements.txt

# Create directory to host the code and copy content inside:
RUN mkdir /backend
WORKDIR /backend
COPY . .

# Create and specify necessary volumes:
RUN mkdir -p ./static-serve/ \
    && mkdir -p ./media-serve/
VOLUME [ "/backend/static-serve", "/backend/media-serve" ]

# Set Python3 enviroment definitions:
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Expose Django Port:
EXPOSE 8000

# Impose default start up command:
CMD [ "/bin/sh", "entrypoint.sh" ]
