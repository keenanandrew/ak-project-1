from pathlib import Path

from mlProject import logger
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Data transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(
                    config=data_transformation_config
                )
                data_transformation.train_test_splitting()

            else:
                raise Exception("The data schema is not valid. Sad trombone.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} has started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
