# TOTP
Serverless example how to generate TOTP that works with Google authenticator to hide a secret

## How to generate venv:
```shell
python3 -m venv 2fa
```

## How to enter venv:
```shell
source 2fa/bin/activate
```

## How to install libraries:
```shell
# Without UV:
pip install -r requirements.txt

# With UV:
pip install uv
uv pip install -r requirements.txt
```

## How to run:
```shell
python ./src/totp.py
```

## How to get out of venv:
```shell
deactivate
```

## Extra commands:
```shell
# Save all libs & version into requirements.txt
uv pip freeze > requirements.txt

# Format the code PEP8 style:
ruff format .
```

### Was tested in Ubuntu 24.04.2 LTS with Python 3.12.3