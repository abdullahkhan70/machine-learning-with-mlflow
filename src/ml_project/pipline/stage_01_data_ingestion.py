
from dataclasses import dataclass
from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_ingestion import DataIngestion
from ml_project import logger

STAGE_NAME = "state_01_data_ingestion"


@dataclass(frozen=True)
class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        # Define the pipline (Excute the function step-by-step.
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} started \n")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} completed \n")
    except Exception as error:
        logger.exception(error)
        raise error
