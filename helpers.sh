#!/bin/bash

function freezy-clean() {
    echo ">>>> Cleaning binary files"
    docker-compose run web sh -c "find . -type f -name '*.pyc' -exec rm {} +"
}

function freezy-bwd() {
    freezy-b
    yarn-deps
    python-deps
}

function python-deps() {
    echo ">>> Setting up Python dependencies:"
    docker-compose run web sh -c "python3 -m venv venv && venv/bin/pip install wheel"
    docker-compose run web sh -c "python3 -m venv venv && venv/bin/pip install -r requirements.txt"
}

function yarn-deps() {
    echo ">>> Running yarn install:"
    docker-compose run web sh -c "yarn install"
}

function freezy-b() {
    echo ">>>> Building from Dockerfile"
    docker-compose build
}


function freezy-db-rebuild() {
    docker-compose run --service-ports web sh -c "venv/bin/flask db downgrade base"
    limbus-db-create
}


function freezy-db-create() {
    freezy-db-init
    freezy-db-migrate
    freezy-db-upgrade
}


function freezy-db-init() {
    docker-compose run web sh -c "venv/bin/flask db init"

}

function freezy-db-migrate() {
    docker-compose run web sh -c "venv/bin/flask db migrate"
}

function freezy-db-upgrade() {
    docker-compose run web sh -c "venv/bin/flask db upgrade"
}

function freezy-db-nuke() {
    echo ">>> Wiping database:"
    docker-compose down -v
    docker-compose run web sh -c 'rm -rf migrations && find . -path "*/migrations/*.pyc"  -delete'
    freezy-db-create
}
