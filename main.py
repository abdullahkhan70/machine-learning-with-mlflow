from ml_project import logger
from ml_project.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipline.stage_02_data_validation import DataValidationPipline

logger.info("This is our project for Machine Learning.")

STAGE_NAME = "state_01_data_ingestion"
STAGE_DATA_VALIDATION = "stage_02_data_validation"

try:
    logger.info(f"Stage: {STAGE_NAME} started \n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_NAME} completed \n")
except Exception as error:
    logger.exception(error)
    raise error

try:
    logger.info(f"Stage: {STAGE_DATA_VALIDATION} started \n")
    obj = DataValidationPipline()
    obj.main()
    logger.info(f"Stage: {STAGE_DATA_VALIDATION} completed \n")
except Exception as error:
    logger.exception(error)
    raise error