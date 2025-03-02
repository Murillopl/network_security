from networksecurity.components.data_ingestion import DataIngestion 
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging 
from networksecurity.entity.config_entity import DataIngestionConfig 
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestion_artifacts = data_ingestion.initiate_data_ingestion()
        print(dataingestion_artifacts)
        logging.info("Ended the data ingestion")

    except NetworkSecurityException as e:
        logging.error(f"NetworkSecurityException: {e}")
    except Exception as e:
        raise NetworkSecurityException(str(e), sys)