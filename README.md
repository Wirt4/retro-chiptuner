## Docker
Make sure docker is running.
Run `docker compose up --build`
Navigate to http://localhost:8000/ to check that the app is running locally

__ Note: The docker setup supports a container for a postgres database, that's not a core feature, but leaving that stubbed is a path of less resistance, and will make supporting user accounts easier later __

## Pip
To initialize a virtual environment in the route, run `python3 -m venv .venv`.
Activate the .venv with `source .venv/bin/activate`.

When using a venv for the first time, Be sure load the dependencies.
First, make sure the venv is running with `source .. activate`,
then run `python3 -m pip install -r requirements.txt` to load the requirements to  the virtual environment.

To shut off the venv, run `deactivate`.


## Testing
We use pytest and pytest-docker for test coverage. Run `pytest` in the root to run tests.
