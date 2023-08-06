from dataclasses import dataclass
from pathlib import Path
from ml_project import logger
from ml_project.config.configuration import DataTransformationConfigurationManager
from ml_project.components.data_transformation import DataTransformation


STAGE_NAME = "stage_03_data_transformation"


@dataclass(frozen=True)
class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1]

            if status == "True":
                config = DataTransformationConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(
                    config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception(
                    f"Your data schema is not valid, so please fix it ASAP.")

        except Exception as error:
            raise error


if __name__ == "__main__":
    try:
        logger.info(f"Stage: {STAGE_NAME} started \n")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_NAME} has completed \n")
    except Exception as error:
        raise error
