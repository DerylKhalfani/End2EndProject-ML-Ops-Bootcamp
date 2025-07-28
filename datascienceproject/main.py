from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info("Starting data ingestion pipeline {}".format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} data ingestion pipeline COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info("Starting {}".format(STAGE_NAME))
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"{STAGE_NAME}  COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info("Starting {}".format(STAGE_NAME))
    data_validation = DataTransformationTrainingPipeline()
    data_validation.initiate_data_transformation()
    logger.info(f"{STAGE_NAME}  COMPLETED")
except Exception as e:
    logger.exception(e)
    raise e