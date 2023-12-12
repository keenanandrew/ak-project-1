import os

import joblib
import pandas as pd
import numpy as np 
from sklearn.linear_model import LogisticRegressionCV  # where the model type is chosen

from mlProject import logger
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = np.ravel(train_data[[self.config.target_column]])
        test_y = test_data[[self.config.target_column]]

        # model type is set here
        lr = LogisticRegressionCV(
            penalty=self.config.penalty,
            tol=self.config.tol,
            fit_intercept=self.config.fit_intercept,
            solver=self.config.solver,
            random_state=self.config.random_state,
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
