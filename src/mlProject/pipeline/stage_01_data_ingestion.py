from src.mlProject import logger
from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Data ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} has started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has finished <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
