# Shallow NN

Explore Shallow Neural Networks Architectures

## Requirements

I highly recommend to use [uv](https://docs.astral.sh/uv/) to manage dependencies, because... it is quite comfortable and powerful!

## Before start

Using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Optionally, setup pre-commit hook

```bash
uv run pre-commit install
```

and test it

```bash
uv run pre-commit run --all-files
```

Now all python scripts can be executed as `uv run <script_name>.py`

## Repository structure

```text
├── data                                # Raw data used in project
├───── ...
|
├── src                                 # Source notebooks and scripts
├───── architectures
├───────── ...
├───── notebooks
|
├── .pre-commit-config.yaml
├── .python-version
├── pyproject.toml                      # Formatter and linter settings
├── README.md                           # The top-level README
└── uv.lock                             # Information about uv environment
```
