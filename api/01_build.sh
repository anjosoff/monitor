#!/bin/bash
clear
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run -h 10.16.45.161 -p 5000