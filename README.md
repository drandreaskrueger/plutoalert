# plutoalert

[![codecov](https://codecov.io/gh/drandreaskrueger/plutoalert/branch/main/graph/badge.svg?token=plutoalert_token_here)](https://codecov.io/gh/drandreaskrueger/plutoalert)
[![CI](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml/badge.svg)](https://github.com/drandreaskrueger/plutoalert/actions/workflows/main.yml)

Awesome plutoalert created by drandreaskrueger

## Clone and initialize virtualenv

```bash
git clone https://github.com/drandreaskrueger/plutoalert.git drandreaskrueger_plutoalert
cd drandreaskrueger_plutoalert
make virtualenv
source .venv/bin/activate
```

## Usage

for now, only one example script is implemented:

```bash
source .venv/bin/activate
python -m plutoalert StarTrek
```
it prints all elements with '**Star Trek**' in the *name* of the series.

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
