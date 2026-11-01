# Learning Python

A small starter project for practicing Python concepts from the freeCodeCamp Python course.

## What was created

- `pyproject.toml` defines the package and its build settings.
- `src/learning_python/` contains the Python package and runnable starter program.
- `tests/` contains a test for the starter program.
- `.gitignore` excludes the virtual environment and generated Python files.

## Get started

Use Python 3.9 or newer. After cloning the repository, go to the project directory:

```bash
git clone https://github.com/JaskiratTakhar24/Learning-Python-FreeCodeCamp.git
cd Learning-Python-FreeCodeCamp
```

Create and activate a virtual environment. This is recommended, but optional for this starter project:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode, so changes to its source are available immediately:

```bash
python -m pip install -e .
```

Run the program and tests:

```bash
python -m learning_python
python -m unittest discover -s tests
```

Without a virtual environment or package installation, run the program with the source directory on Python's module path:

```bash
PYTHONPATH=src python3 -m learning_python
```

Deactivate the virtual environment when finished:

```bash
deactivate
```

## GitHub authentication with SSH (macOS)

Create an SSH key if you do not already have one. Keep the private key secret:

```bash
ssh-keygen -t ed25519 -C "GitHub SSH key" -f ~/.ssh/github_ed25519
pbcopy < ~/.ssh/github_ed25519.pub
```

In GitHub, add the copied public key under **Settings → SSH and GPG keys → New SSH key**. Never upload or share `~/.ssh/github_ed25519` (the private key).

Configure macOS SSH to use the key and remember its passphrase in Keychain. Create or edit `~/.ssh/config` and add:

```sshconfig
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/github_ed25519
```

Load the key into the SSH agent, then test authentication:

```bash
ssh-add --apple-use-keychain ~/.ssh/github_ed25519
ssh -T git@github.com
```

Use the repository's SSH URL (only needed if `origin` is still set to HTTPS), then push:

```bash
git remote set-url origin git@github.com:JaskiratTakhar24/Learning-Python-FreeCodeCamp.git
git push
```

Once configured, the key should be used automatically for later pushes. You do not need to generate a new key for each push.

## Publish changes to GitHub

After editing files, review, commit, and push your changes:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

## Build and run the FastAPI app locally

These steps add a small web API to the learning project. Run the commands from the project root.

### 1. Create and activate a virtual environment

If you have not already created one for this checkout:

```bash
python3 -m venv .venv
```

Activate it in each new Terminal session before running the app:

```bash
source .venv/bin/activate
```

When active, the prompt usually starts with `(.venv)`.

### 2. Install FastAPI and Uvicorn

```bash
python -m pip install fastapi "uvicorn[standard]"
```

FastAPI provides the web framework. Uvicorn runs the app as a local web server.

### 3. Create the API module

Create `src/learning_python/api.py` with this starter app:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from my first FastAPI app!"}
```

The `@app.get("/")` route handles requests to the home path and returns a JSON response.

### 4. Start the development server

From the project root, run:

```bash
python -m uvicorn learning_python.api:app --reload --app-dir src
```

`--app-dir src` tells Uvicorn where to find the `learning_python` package. `--reload` restarts the server when you save code changes. Keep this Terminal session open while using the app.

If you see `Address already in use` (Errno 48), another process is already using port 8000. Stop your other server with **Control+C**, or choose a different port:

```bash
python -m uvicorn learning_python.api:app --reload --app-dir src --port 8001
```

### 5. Open and stop the app

Open the local app at [http://127.0.0.1:8000](http://127.0.0.1:8000), or use port `8001` if you selected it above. FastAPI's interactive API documentation is at `/docs` (for example, [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)).

To stop the server, focus its Terminal session and press **Control+C**. To leave the virtual environment, run `deactivate`.

## Check a lesson with Pylint

With the project's virtual environment activated, install Pylint:

```bash
python -m pip install pylint
```

From the project root, run Pylint on the function lesson:

```bash
python -m pylint src/learning_python/lessons/function.py
```

Pylint reports potential code and style issues, such as missing docstrings or a missing final newline. Review its suggestions and rerun it after making changes.

## Run Pylint automatically with GitHub Actions

The workflow in `.github/workflows/pylint.yml` runs automatically whenever you push commits to GitHub. It sets up Python 3.10, 3.11, and 3.13, installs Pylint and FastAPI, and checks all tracked Python files.

To run it:

1. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Describe your changes"
   git push
   ```
2. In your GitHub repository, open the **Actions** tab.
3. Select the **Pylint** workflow run to see whether it passed or which files need attention.

Fix any reported issues locally, then commit and push again to start another workflow run.

### Why the workflow succeeds when Pylint reports issues

The workflow initially failed because Pylint reported code and style issues. The Pylint command now includes `--exit-zero`, which makes it exit successfully even when it reports issues. GitHub Actions therefore marks the workflow as successful, while Pylint's findings remain visible in the workflow logs. This is useful while learning, but it means a successful run does not guarantee that the code passed Pylint; review the reported findings and fix them over time.

### Node.js runtime warning in GitHub Actions

GitHub Actions uses Node.js internally to run workflow actions; this is separate from the Python versions used by the project. The Pylint workflow uses `actions/checkout@v5` and `actions/setup-python@v6`, which support Node.js 24 and avoid the Node.js 20 deprecation warning. The Python version matrix remains independent of the Node.js runtime used by these actions.

### Ubuntu runner version

The workflow previously used the moving `ubuntu-latest` runner label, which triggered a warning that it would migrate to Ubuntu 26. To make the runner version explicit and avoid an unexpected operating-system change, `.github/workflows/pylint.yml` now uses `runs-on: ubuntu-24.04`. This keeps the Pylint job on Ubuntu 24.04; update this label intentionally when you decide to move to a newer runner.

## Format a lesson with Ruff

Ruff was used to format `src/learning_python/lessons/build_kitchen_inventory.py` and address many of the style warnings reported by Pylint. With the virtual environment activated, install Ruff and format that file from the project root:

```bash
python -m pip install ruff
ruff format src/learning_python/lessons/build_kitchen_inventory.py
```

Ruff's formatter handles formatting, but it does not resolve every kind of Pylint warning. Run Pylint again to review any remaining findings:

```bash
python -m pylint src/learning_python/lessons/build_kitchen_inventory.py
```
