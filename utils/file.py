import utils
from pathlib import Path


def path_from_json_schemas(relative_path: str):
    relative_path = f"api/json_schemas/{relative_path}"

    return (
        Path(utils.__file__).parent.parent.joinpath(relative_path).absolute().__str__()
    )


def abs_path_from_project(relative_path: str):

    return (
        Path(utils.__file__).parent.parent.joinpath(relative_path).absolute().__str__()
    )
