from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} has started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} has started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} has started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model training stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} has started <<<<<<")
    data_transformation = ModelTrainerTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} has started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> {STAGE_NAME} has finished <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e