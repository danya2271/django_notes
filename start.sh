#!/usr/bin/env sh
set -eu

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

PYTHON=".venv/bin/python"

if [ ! -x "$PYTHON" ]; then
    echo "Virtual environment is broken or incomplete. Remove .venv and run this script again."
    exit 1
fi

echo "Installing dependencies..."
"$PYTHON" -m pip install -r requirements.txt

echo "Applying migrations..."
"$PYTHON" manage.py migrate

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8000}"

echo "Starting Django server at http://$HOST:$PORT/"
exec "$PYTHON" manage.py runserver "$HOST:$PORT"
