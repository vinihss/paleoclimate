#!/bin/bash

source activate paleoclimate
export PYTHONPATH=$PYTHONPATH:/app

# Detect if running in development or production
if [ "$FASTAPI_ENV" == "production" ]; then
  uvicorn app.main:app --host 0.0.0.0 --port 8002
else
  uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload
fi
