from dataclasses import dataclass
from ml_project import logger
from ml_project.config.configuration import ValidationConfigurationManager
from ml_project.components.data_validation import DataValidation
from ml_project.entity.config_entity import DataValidationConfig

STAGE_NAME = "stage_02_data_validation"

@dataclass(frozen=True)
class DataValidationPipline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        config = ValidationConfigurationManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} started \n")
        obj = DataValidationPipline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} completed \n")
    except Exception as error:
        raise error
