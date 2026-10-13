# tp4 secuguard

petit outil en ligne de commande pour generer un mot de passe ou analyser sa robustesse.

## installation

installer uv :

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

sur windows :

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

ou `pip install uv`. verifier avec `uv --version`.

ensuite, dans le dossier du projet :

```
uv sync
```

## lancement

generer un mot de passe (12 caracteres par defaut) :

```
uv run python -m secuguard.main
```

choisir la longueur et enlever les chiffres ou les symboles :

```
uv run python -m secuguard.main -l 16 --no-symbols
uv run python -m secuguard.main --no-digits
```

analyser un mot de passe :

```
uv run python -m secuguard.main -c "12345"
uv run python -m secuguard.main --check "P@ssw0rd2026!Secu"
```
