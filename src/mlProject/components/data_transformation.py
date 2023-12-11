import os

import pandas as pd
from sklearn.model_selection import train_test_split

from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig

# purposely simple as data transformation is not the focus of this workshop
# this is where scaling etc could be done
# all we'll do is split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data now split into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
