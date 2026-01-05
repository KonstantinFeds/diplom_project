import json
import allure
from jsonschema import validate
from utils.file import path_from_json_schemas


class SchemaValidator:

    @staticmethod
    @allure.step("Валидация схемы")
    def validate_schema(data_to_validate: dict, schema_filename: str):
        """
        Универсальный метод для валидации данных по JSON схеме
        """
        schema_path = path_from_json_schemas(schema_filename)
        with open(schema_path, encoding="utf-8") as file:
            schema = json.load(file)
        validate(data_to_validate, schema)