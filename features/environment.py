from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
import os
import allure
import shutil



Project_Root=os.path.abspath(os.path.join(os.getcwd(), os.pardir))


def before_all(context):
    context.p = sync_playwright().start()
    path=Project_Root+"\\videos"
    path2=Project_Root+"\\traces"
    if os.path.exists(path) or os.path.exists(path2):
        shutil.rmtree(path)
        shutil.rmtree(path2)
        path = os.path.join(Project_Root, "videos")
        os.mkdir(path)
        path2 = os.path.join(Project_Root, "traces")
        os.mkdir(path2)
    else:
        path = os.path.join(Project_Root, "videos")
        os.mkdir(path)
        path2 = os.path.join(Project_Root, "traces")
        os.mkdir(path2)


def before_scenario(context,scenario):
    context.browser = context.p.chromium.launch(headless=True, slow_mo=5000)
    context.tab = context.browser.new_context(
        record_video_dir=Project_Root+"\\videos",
        record_video_size={"width": 1500, "height": 1200}
        # record_trace_dir = Project_Root + "\\traces",
        # record_trace_size = {"width": 1500, "height": 1200}
    )
    context.page = context.tab.new_page()
    context.tab.tracing.start(screenshots=True, snapshots=True, sources=True)



def after_scenario(context,scenario):
    context.tab.tracing.stop(path=Project_Root+"//traces//trace.zip")
    context.page.close()
    context.page.video.save_as(os.path.join(Project_Root, f"videos/{scenario.name}"))
    with open(
            os.path.join(Project_Root, context.page.video.path()), "rb"
    ) as video_file:
        # Video
        attach(
            video_file.read(),
            name=f"videos : {scenario.name}",
            attachment_type=AttachmentType.WEBM,
        ) 
    attach.file(Project_Root+"//traces//trace.zip", name="Trace viewer logs", extension=".zip")
    context.tab.close()
    context.browser.close()



