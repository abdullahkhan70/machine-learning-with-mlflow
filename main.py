from ml_project import logger
from ml_project.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("This is our project for Machine Learning.")

STAGE_NAME = "state_01_data_ingestion"

try:
    logger.info(f"Stage: {STAGE_NAME} started \n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_NAME} completed \n")
except Exception as error:
    logger.exception(error)
    raise error