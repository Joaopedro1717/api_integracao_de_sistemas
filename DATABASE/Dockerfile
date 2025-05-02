FROM postgres:latest

ENV POSTGRES_USER=apidoscria
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=user_tasks

WORKDIR /docker-entrypoint-initdb.d

COPY sql/1_create_tables.sql ./

EXPOSE 5432