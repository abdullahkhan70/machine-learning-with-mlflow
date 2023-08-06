from ml_project import logger
from ml_project.config.configuration import ModelEvaluationConfigurationManager
from ml_project.components.model_evaluation import ModelEvaluation

STAGE_NAME = "stage_05_model_evaluation"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        config = ModelEvaluationConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} has started. \n")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} has completed. \n")
    except Exception as error:
        raise error
