#!/bin/bash

BASE_DIR=$( cd $(dirname $0); cd .. ; pwd )

if [[ $(whoami) != "root" ]]; then
    echo "Please execute with root"
    exit 1
fi

# Install requirement packages
yum install -y mariadb mariadb-devel git gcc python3 python3-devel python3-pip

# Install python lib requirements
cd ${BASE_DIR}
pip3.6 install -r requirements.txt

# Setting uwsgi.ini
cat << EOF > systemd/uwsgi.ini
[uwsgi]
socket = :3031
chdir = ${BASE_DIR}
pythonpath = ${BASE_DIR}
env = DJANGO_SETTINGS_MODULE=develop.settings
module = config.wsgi
pidfile = /var/run/uwsgi.pid
processes = 4
threads = 2
stats = :9191
EOF

# Setting systemd file
cat << EOF > systemd/uwsgi.service
[Unit]
Description=uWSGI service
[Service]
EnvironmentFile=${BASE_DIR}/systemd/env
ExecStart=/bin/bash -c 'uwsgi --ini ${BASE_DIR}/systemd/uwsgi.ini'
[Install]
WantedBy=multi-user.target
EOF

# Register uwsgi.service to systemd
cp ${BASE_DIR}/systemd/uwsgi.service /etc/systemd/system/uwsgi.service
systemctl daemon-reload
systemctl enable uwsgi.service

# Start uwsgi.service
systemctl start uwsgi.service
