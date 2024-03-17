import json

import allure
import requests.exceptions


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        body = kwargs.get("json")
        if body:
            allure.attach(
                json.dumps(kwargs.get("json"), indent=2),
                name="Request",
                attachment_type=allure.attachment_type.JSON,
            )
        response = fn(*args, **kwargs)
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_text = response.text
            status_code = f"status code - {response.status_code}"
            allure.attach(
                response_text if len(response_text) > 0 else status_code,
                name="response.text",
                attachment_type=allure.attachment_type.TEXT,
            )
        else:
            allure.attach(
                json.dumps(response_json, indent=2),
                name="response.json",
                attachment_type=allure.attachment_type.JSON,
            )
        return response

    return wrapper
