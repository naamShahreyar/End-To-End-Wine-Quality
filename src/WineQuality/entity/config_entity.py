from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig():
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig():
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig():
    root_dir: Path
    model_name: str
    params_grid: dict
    train_data_path: Path
    model_save_dir: Path
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig():
    root_dir: Path
    model_name: str
    train_data_path: Path
    test_data_path: Path
    model_path: Path
    evaluation_save_dir: Path
    target_column: str