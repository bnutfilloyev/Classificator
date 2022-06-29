# EDA-predictor

For this dataset:

Main task: ML
1. Do a preliminary data analysis. (EDA)
2. Create visualizations using seaborn and matplotlib: dependency plots, histograms, boxplot). Find the parameter with the highest correlation
3. Based on the analysis, draw some conclusions from the data
4. Pre-process the data if necessary
5. Create a model for this dataset. (you can use xgboost, lightgbm, catboost)
6. Use hyperparameter tuning, justify your choice
7. Display the metrics for the resulting model (the main metric is the confusion matrix)

Optional: Deploy
 - Create a separate python project

1. Write an API that will accept client data and return model prediction (use fastapi)
  - tutorial on the site to help
2. Raise the database (sqlite, mysql)
3. PEP 8 hello

Estimated time to complete the task:
1. model creation - 1 day
2. creating a web application without knowledge of the framework 2 days

If possible, comments on the work will be given, which will need to be taken into account. Additional time 1 day
## Development Requirements

- Python3.8.2
- Pip
- Poetry (Python Package Manager)

### M.L Model Environment

```sh
MODEL_PATH=./ml/model/
MODEL_NAME=model.pkl
```

### Update `/predict`

To update your machine learning model, add your `load` and `method` [change here](app/api/routes/predictor.py#L13) at `predictor.py`

## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    ├── datasets         - datasets for training and testing.
    ├── visualizations   - visualizations for dataset preview.
    ├── notebooks        - notebooks for data analysis and visualization.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                  - pytest
