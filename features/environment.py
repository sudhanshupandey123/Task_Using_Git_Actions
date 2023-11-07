from playwright.sync_api import sync_playwright
import os


Project_Root=os.getcwd()
def before_all(context):
    context.p = sync_playwright().start()
    path=Project_Root+"//videos"

    isexist = os.path.exists(path)
    if isexist == False:
        path = os.path.join(Project_Root, "videos")
        os.mkdir(path)


def before_scenario(context,scenario):
    context.browser = context.p.chromium.launch(headless=True, slow_mo=5000)
    context.tab = context.browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1500, "height": 1200}
    )
    context.page = context.tab.new_page()



def after_scenario(context,scenario):
    context.page.close()
    context.page.video.save_as(
        f"{Project_Root}//videos/{scenario.name}.webm"
    )

