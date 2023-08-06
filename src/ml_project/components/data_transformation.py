import os
import pandas as pd
from ml_project.entity.config_entity import DataTransformationConfig
from ml_project import logger
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the dataset into training and testing.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Splitting data into training and test sets")
        logger.info(f"Training Dataset Shape: {train.shape}")
        logger.info(f"Testing Dataset Shape: {test.shape}")
