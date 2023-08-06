import pandas as pd


# Create the components.

class DataValidation:
    def __init__(self, config) -> None:
        self.config = config

    # Check one-by-one whether all the columns present in the CSV file from schema.yaml file.
    def validation_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as error:
            raise error
