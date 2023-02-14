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
# RUN apk del .tmp


# Copy project
COPY . /app/
COPY ./scripts /scripts


#permission
RUN chmod +x /scripts/entrypoint.sh

# creating a user and providing them access to vol 
# RUN mkdir -p /app/staticfiles/temp  
# RUN mkdir -p /app/static/this_is_a_temp
# RUN mkdir -p /app/media/this_is_a_temp

# RUN adduser -D user
# RUN chown -R user:user /app/static/*
# RUN chown -R user:user /app/staticfiles/*
# RUN chown -R user:user /app/media/*
# RUN chmod -R 777 /app/static/*
# RUN chmod -R 777 /app/media/*
# RUN chmod -R 777 /app/staticfiles/*
# USER user

# CMD ["entrypoint.sh"]
