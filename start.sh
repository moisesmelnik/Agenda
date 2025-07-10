#!/bin/bash
export FLASK_APP=app.py
export FLASK_RUN_PORT=10000
flask run --host=0.0.0.0
