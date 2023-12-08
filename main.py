from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} has started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} has finished <<<<<<\n\n x============x")
except Exception as e:
    logger.exception(e)
    raise e