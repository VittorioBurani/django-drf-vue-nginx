# Pass NGINX version as argument:
ARG NGINX_VERSION

# Use specified Alpine Linux NGINX version image:
FROM nginx:${NGINX_VERSION}-alpine

# Create and specify necessary volumes:
RUN mkdir -p /static-serve/ \
    && mkdir -p /media-serve/ \
    && mkdir -p /front_end/
VOLUME [ "/static-serve", "/media-serve", "/vue_build" ]

# Remove default NGINX configuration and create a new custom one:
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
