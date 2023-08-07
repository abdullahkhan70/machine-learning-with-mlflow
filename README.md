# machine-learning-with-mlflow

# Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run?

### Steps:

## Clone the repository

```bash
git clone https://github.com/abdullahkhan70/machine-learning-with-mlflow.git
```

## Step# 01: Create a conda enviroment after opening the repository

```bash
conda create -m ml_project python=3.10.8 -y
```

```bash
conda activate ml_project
```

## Step# 02: Install the dependencies from requirement

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command.
python app.py
```

Now,
```bash
# open up your local host and port.
```

## MLFlow
[Documentation](https://mlflow.org/docs/latest/index.html)


### CMD
- mlflow ui

### Dagshub
[Daghubs](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/abdullahkhan70/machine-learning-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=abdullahkhan70 \
MLFLOW_TRACKING_PASSWORD=e0a0c2fcc0e62a10915f3820517b36b33e0968ae \
python app.py

Run this to export as env variables.

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/abdullahkhan70/machine-learning-with-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=abdullahkhan70

export MLFLOW_TRACKING_PASSWORD=PASSWORD_FROM_DAGSHUB

```