#!/bin/bash
python migrations/setup.py
uvicorn app.main:app --host 0.0.0.0 --port 8000