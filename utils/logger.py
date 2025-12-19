# utils/logger.py
import logging
import json
import allure
from requests import Response
from allure_commons.types import AttachmentType


def response_logging(response: Response):
    logging.info("Request: " + response.request.method + " " + response.request.url)
    if response.request.body:
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        logging.info("INFO Request body: " + request_body)  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)

    # Логируем статус код с правильным уровнем
    if response.status_code >= 500:
        logging.error(f"Response code {response.status_code} - Server Error")
    elif response.status_code >= 400:
        logging.warning(f"Response code {response.status_code} - Client Error")
    elif response.status_code >= 300:
        logging.info(f"Response code {response.status_code} - Redirect")
    else:
        logging.info(f"Response code {response.status_code} - Success")

    # Логируем тело ответа
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        request_body = response.request.body
        # Прикрепляем тело запроса, преобразовав в строку при необходимости
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        # логирование тела запроса если оно есть
        allure.attach(
            body=json.dumps(request_body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )