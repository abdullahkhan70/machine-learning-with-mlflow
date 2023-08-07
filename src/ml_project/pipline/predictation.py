import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from ml_project import logger


class PredictationPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        predictation = self.model.predict(data)
        logger.info(f"The Predictation: {predictation[0]}")
        return predictation[0]
