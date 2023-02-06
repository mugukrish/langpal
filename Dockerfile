# base image
FROM python:3.10.5-alpine3.15

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="scripts:${PATH}"

RUN mkdir /app

# Set work directory
WORKDIR /app

# Install dependencies
RUN apk add --update --no-cache --virtual .tmp gcc python3-dev libpq-dev postgresql-dev musl-dev libc-dev linux-headers
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt


# Copy project
COPY . /app/
COPY ./scripts /scripts



#permission
RUN chmod +x /scripts/*

# -p will make sure that the vol/web/ is created
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# creating a user and providing them access to vol 
# RUN adduser -D user
# RUN chown -R user:user /vol
# RUN chown -R 755 /vol/web
# RUN chown -R user:user /app/static/*
# RUN chown -R 755 /app/*
# RUN chown -R 755 /app/static/*
#switching user
# USER user
USER root

CMD ["entrypoint.sh"]