#!/bin/bash
docker-composer down
docker-compose up --build -d
docker-compose logs -f