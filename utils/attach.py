import os

import allure
import requests
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

import utils.file

load_dotenv(dotenv_path=utils.file.abs_path_from_project(".env.credentials"))


# запись теста с bstack
def attach_bstack_video_android(session_id):
    bstack_session = requests.get(
        f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(os.getenv("USER_NAME_BSTACK"), os.getenv("ACCESS_KEY_BSTACK")),
    ).json()

    video_url = bstack_session["automation_session"]["video_url"]

    allure.attach(
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video>"
        "</body></html>",
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )


# cкриншот
def add_screenshot_selenoid(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )


# логи
def add_logs_selenoid(browser):
    log = "".join(
        f"{text}\n"
        for text in browser.driver.execute("getLog", {"type": "browser"})["value"]
    )
    allure.attach(log, "browser_logs", AttachmentType.TEXT, ".log")


# html-код страницы
def add_html_selenoid(browser):
    html = browser.driver.page_source
    allure.attach(html, "page_source", AttachmentType.HTML, ".html")


# скринкаст для запуска с selenoid
def add_selenoid_video(browser):
    video_url = (
            f"https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
            "<html><body><video width='100%' height='100%' controls autoplay><source src='"
            + video_url
            + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html, "video_" + browser.driver.session_id, AttachmentType.HTML, ".html"
    )
