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

## Publish changes to GitHub

After editing files, review, commit, and push your changes:

```bash
git status
git add .
git commit -m "Describe your changes"
git push
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
