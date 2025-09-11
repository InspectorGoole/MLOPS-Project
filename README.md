# MLOPS-Project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update app.py

MLFLOW Dagshub URI:
import dagshub
dagshub.init(repo_owner='am6499057', repo_name='MLOPS-Project', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)

## ECR URI

HERE: 509399622317.dkr.ecr.us-east-1.amazonaws.com/mlproj
