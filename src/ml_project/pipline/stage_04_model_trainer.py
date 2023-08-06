from ml_project import logger
from ml_project.config.configuration import ModelTrainerConfirgurationManager
from ml_project.components.model_trainer import ModelTrainer


STAGE_NAME = "stage_04_model_trainer"


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        config = ModelTrainerConfirgurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} started \n")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} has completed.")
    except Exception as error:
        raise error
