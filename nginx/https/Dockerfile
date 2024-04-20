# Pass NGINX version as argument:
ARG NGINX_VERSION

# Use specified Alpine Linux NGINX version image:
FROM nginx:${NGINX_VERSION}-alpine

# Create DOMAIN_NAME environment variable:
ARG DOMAIN_NAME
ENV DOMAIN_NAME=${DOMAIN_NAME}

# Create and specify necessary volumes:
RUN mkdir -p /static-serve/
VOLUME [ "/static-serve", "/media-serve", "/vue_build" ]

# Remove default NGINX configuration and create a new custom one:
COPY ./nginx.conf /etc/nginx/templates/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf \
    && envsubst '${DOMAIN_NAME}' < /etc/nginx/templates/nginx.conf > /etc/nginx/conf.d/nginx.conf
