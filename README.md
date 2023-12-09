# End-to-end-ML-project
From Krish Naik course


## Workflows in tutorial

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```
Now,
```bash
open up you local host and port
```
## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/keenanandrew/End-to-end-ML-project.mlflow \
MLFLOW_TRACKING_USERNAME=keenanandrew \
MLFLOW_TRACKING_PASSWORD=50949a0af1030805e0f1b0018786b9f0e16b731f \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/keenanandrew/End-to-end-ML-project.mlflow

export MLFLOW_TRACKING_USERNAME=keenanandrew 

export MLFLOW_TRACKING_PASSWORD=50949a0af1030805e0f1b0018786b9f0e16b731f

```