#!/bin/bash

docker build --tag worldbosskafka/library-flask-app:v1.0.8 . -f Dockerfile
docker push worldbosskafka/library-flask-app:v1.0.8