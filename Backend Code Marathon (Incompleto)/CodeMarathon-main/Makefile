SHELL := /bin/bash

# Setup all configurations
include config.env
ifndef BACKEND_ADDRESS
BACKEND_ADDRESS = 0.0.0.0
#BACKEND_ADDRESS = 127.0.0.1
endif
ifndef BACKEND_PORT
BACKEND_PORT = 8000
endif
ifndef PYTHON
PYTHON = python3
endif
ifndef VENV_DIR
VENV_DIR = Backend/.venv/Scripts
endif


venv = source ${VENV_DIR}/activate; \
		export PYTHONDONTWRITEBYTECODE=1;


install:
	${PYTHON} -m venv Backend/.venv --upgrade-deps
	${venv} pip install -r Backend/requirements.txt


uninstall:
	rm -rf Backend/.venv


run:
	${venv} cd Backend/app/; \
	${PYTHON} manage.py runserver ${BACKEND_ADDRESS}:${BACKEND_PORT}


migrate:
	${venv} cd Backend/app/; \
	${PYTHON} manage.py makemigrations; \
	${PYTHON} manage.py migrate


test:
	${venv} cd Backend/app/; \
	${PYTHON} manage.py test


admin:
	${venv} cd Backend/app/; \
	${PYTHON} manage.py createsuperuser


clean_db:
	rm -rf Backend/app/db.sqlite3
	rm -rf Backend/app/submissions/files
	mkdir Backend/app/submissions/files


load_data:
	${venv} cd Backend/app/; \
	${PYTHON} manage.py loaddata core/fixtures/*.yaml
