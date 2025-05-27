import os
from appium.options.android import UiAutomator2Options
# import time
from time import sleep,time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import subprocess
def link():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "cf4b27af"
    options.app_package = "com.tencent.mm"
    options.app_activity = ".ui.LauncherUI"
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.new_command_timeout = 300
    options.set_capability("appium:forceAppLaunch", True)
    return  webdriver.Remote("http://127.0.0.1:4723", options=options)
def adb_input_text(text: str, click_pos: tuple = None, wait_after_click: float = 0.5):
    if click_pos:
        x, y = click_pos
        os.system(f"adb shell input tap {x} {y}")
        sleep(wait_after_click)
    safe_text = text.replace(" ", "%s")
    os.system(f'adb shell input text "{safe_text}"')

#主界面点击搜索按钮
def click_search_button(d):
    d.find_element(AppiumBy.ID, "com.tencent.mm:id/h5n").click()
    # d.find_element(AppiumBy.ACCESSIBILITY_ID,'搜索').click()

def search_click(driver,who:str):
    click_search_button(driver)
    sleep(1)
    adb_input_text(who)
    sleep(1)
    #点击第一个匹配的联系人
    driver.find_elements(AppiumBy.ID, "com.tencent.mm:id/mem")[1].click()

def test_14():
    driver = link()
    search_click(driver,"a")
    sleep(1)
    # 确保激活输入框
    if not driver.find_elements(By.CLASS_NAME, "android.widget.EditText"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"切换到键盘").click()
        sleep(1)
    driver.find_element(By.CLASS_NAME, "android.widget.EditText").click()
    sleep(1)
    adb_input_text("Hello")
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()

    # driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[1].click()
    driver.quit()



def test_15():
    #发送图片
    driver = link()
    sleep(1)
    search_click(driver,"a")
    sleep(1)
    # 打开“+”面板
    driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[2].click()
    sleep(1)
    #点击相册
    # driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.GridView')[1].click()
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.tencent.mm:id/a10"])[1]').click()
    sleep(1)
    driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.CheckBox')[1].click()
    sleep(1)
    driver.find_element(AppiumBy.CLASS_NAME,"android.widget.Button").click()
    driver.quit()


def test_16():
    driver = link()
    sleep(1)
    search_click(driver,'cscs')
    # search_and_enter_chat(driver, 'cscs')  # 替换为群聊名称
    if not driver.find_elements(By.CLASS_NAME, "android.widget.EditText"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,"切换到键盘").click()
        sleep(1)
    # 输入框中输入@
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").click()
    os.system("adb shell input text '@'")
    sleep(1)
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").click()
    sleep(1)
    adb_input_text('a')
    sleep(1)
    # driver.find_elements(AppiumBy.CLASS_NAME,'com.tencent.mm:id/mjc')[0].click()
    driver.find_element(By.XPATH, '//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/mjc"]').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    driver.quit()

def test_17():
    driver = link()
    sleep(1)
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, "更多功能按钮").click()
    driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.tencent.mm:id/h5n"])[2]').click()
    sleep(1)
    plus_list = driver.find_elements(By.ID, "com.tencent.mm:id/m7g")
    plus_list[2].click()
    sleep(1)
    #点击图片,这个动态的貌似难以定位故直接用坐标
    driver.tap([(1250,2740)],1)
    sleep(1)
    driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.tencent.mm:id/je0"])[1]').click()
    sleep(1)
    driver.find_elements(AppiumBy.ID,'com.tencent.mm:id/m7k')[1].click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    sleep(1)

    driver.quit()

def test_18():
    driver = link()
    #+
    driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.tencent.mm:id/h5n"])[2]').click()
    sleep(1)
    plus_list = driver.find_elements(By.ID, "com.tencent.mm:id/m7g")
    plus_list[1].click()
    sleep(1)
    # dianj
    driver.find_element(By.ID,"com.tencent.mm:id/mes").click()
    sleep(1)
    os.system("adb shell input text '13962768522'")
    sleep(2)
    driver.find_element(By.ID,"com.tencent.mm:id/mem").click()
    sleep(2)
    # driver.tap([(500,888)],1)
    driver.find_element(By.XPATH,'(//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/m7k"])[2]').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
    sleep(5)

    driver.quit()

def test_TC012_search_contact():
    driver = link()
    sleep(1)
    search_click(driver,'a')
    driver.quit()

def test_19():
    driver = link()
    sleep(1)
    search_click(driver, 'a')
    sleep(1)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/coz').click()
    sleep(1)
    items = driver.find_element(AppiumBy.ID,'com.tencent.mm:id/ceh')
    items.find_elements(AppiumBy.CLASS_NAME,'android.widget.RelativeLayout')[0].click()
    sleep(1)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/coy').click()
    sleep(1)
    #朋友的资料设置页
    doc = driver.find_element(AppiumBy.ID,'android:id/list')
    #第一个备注
    doc.find_elements(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[0].click()
    sleep(1)
    #点击使得页面修改进入备注
    driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.EditText')[0].click()
    sleep(1)
    #先定位到备注这一栏,再清空备注
    beizhu = driver.find_element(AppiumBy.ID,'com.tencent.mm:id/apu')
    beizhu.find_element(AppiumBy.CLASS_NAME,'android.widget.ImageView').click()

    # driver.find_element(AppiumBy.ID,'com.tencent.mm:id/apv').click()
    adb_input_text('a')
    driver.find_element(AppiumBy.CLASS_NAME,"android.widget.Button").click()
    sleep(1)
    driver.quit()

def test_20():
    driver = link()
    sleep(1)
    driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.tencent.mm:id/h5n"])[2]').click()
    sleep(1)
    plus_list = driver.find_elements(By.ID, "com.tencent.mm:id/m7g")
    plus_list[0].click()
    sleep(1)
    main_page = driver.find_element(AppiumBy.CLASS_NAME,'androidx.recyclerview.widget.RecyclerView')
    main_page.find_elements(AppiumBy.CLASS_NAME,'android.widget.RelativeLayout')[0].click()
    # member_list = driver.find_elements(By.XPATH, '(//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/mjc"])')
    # member_list[1].click()
    sleep(1)
    # #点击完成
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    sleep(1)

    driver.quit()


def test_21():
    driver = link()
    sleep(1)
    driver.find_elements(AppiumBy.ID, 'com.tencent.mm:id/nvt')[1].click()
    # driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tencent.mm:id/icon_tv" and @text="通讯录"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.tencent.mm:id/mg"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]').click()
    sleep(1)
    driver.find_element(By.XPATH, '(//android.widget.LinearLayout[@resource-id="com.tencent.mm:id/hs6"])[1]').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
    sleep(1)

    driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
    sleep(1)
    os.system("adb shell input text 'a'")

    sleep(1)
    driver.find_elements(By. CLASS_NAME, 'android.widget.CheckBox')[0].click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
    sleep(1)
    driver.quit()


def test_22():
    driver = link()
    sleep(1)
    driver.find_elements(AppiumBy.ID, 'com.tencent.mm:id/nvt')[3].click()
    # driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tencent.mm:id/icon_tv" and @text="我"]').click()
    sleep(1)
    #五个元素图标均相同依次
    driver.find_elements(AppiumBy.ID,'com.tencent.mm:id/h9o')[4].click()
    sleep(1)
    #个人资料唯一id
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/kbb').click()
    sleep(1)
    #前七个都适用android.widget.ImageView
    content = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')

    #修改头像
    # driver.find_element(AppiumBy.ID,'com.tencent.mm:id/kbb').click()
    # sleep(1)
    # #随便选择一张
    # driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.ImageView')[5].click()
    # sleep(1)
    # #第一个是取消,第二个是确定
    # driver.find_elements(By.CLASS_NAME, 'android.widget.Button')[1].click()

    #修改名字
    # driver.find_element(AppiumBy.ID,'com.tencent.mm:id/a4f').click()
    # sleep(1)
    # driver.find_element(AppiumBy.ID,'com.tencent.mm:id/kbb').click()
    # sleep(1)
    # for i in range(10):
    #     os.system("adb shell input keyevent 67")
    # sleep(1)
    # adb_input_text('test_name')
    # driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()

    #修改性别
    content[2].click()
    sleep(1)
    sex_list = driver.find_element(AppiumBy.ID,'android:id/list')
    #修改性别为女
    sex_list.find_elements(AppiumBy.ID,'com.tencent.mm:id/m7k')[1].click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()

    driver.quit()



def test_23():
    driver = link()
    sleep(1)
    #点击发现
    driver.find_elements(AppiumBy.ID,'com.tencent.mm:id/nvt')[2].click()
    #获取主页面
    main_page = driver.find_element(AppiumBy.ID,'android:id/list')
    main_page.find_elements(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[0].click()
    sleep(1)
    #点击右上角发朋友圈,相对布局顶部
    # top = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.RelativeLayout')
    # top.find_elements(AppiumBy.CLASS_NAME,'android.widget.ImageView')[0].click()
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/coz').click()
    sleep(1)
    #选择从相册选择
    choose = driver.find_element(AppiumBy.CLASS_NAME,'androidx.recyclerview.widget.RecyclerView')
    choose.find_elements(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[2].click()
    sleep(1)
    driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.CheckBox')[3].click()
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    sleep(1)
    driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText').click()
    adb_input_text('happy')
    sleep(1)

    #这部分是选择谁可以看
    driver.hide_keyboard()
    sleep(1)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/li5').click()
    ex = driver.find_element(AppiumBy.CLASS_NAME,'android.widget.ExpandableListView')
    ex.find_elements(By.CLASS_NAME, 'android.widget.RelativeLayout')[1].click()
    # content = driver.find_element(AppiumBy.ID,'android:id/content')
    # content.find_element(AppiumBy.CLASS_NAME,'android.widget.ImageView').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    sleep(1)


    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    driver.quit()


def test_24():
    driver = link()
    sleep(1)
    driver.find_elements(AppiumBy.ID, 'com.tencent.mm:id/nvt')[3].click()
    sleep(1)
    #找到主页面
    # main_page = driver.find_element(AppiumBy.ID,'android:id/list')
    # main_page.find_elements(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[4].click()
    #这样列id一样
    driver.find_elements(By.ID,'com.tencent.mm:id/m7k')[2].click()
    sleep(1)
    # driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.ImageView')[2].click()
    # main_page = driver.find_element(AppiumBy.CLASS_NAME,'androidx.recyclerview.widget.RecyclerView')
    # driver.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView').click()
    driver.find_element(AppiumBy.CLASS_NAME,'android.view.View').click()
    sleep(1)
    driver.find_element(AppiumBy.ID,'com.tencent.mm:id/n7z').click()
    sleep(1)
    driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.ImageView')[1].click()
    sleep(1)
    driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.Button')[1].click()
    sleep(1)
    driver.quit()

def test_25():
    driver = link()
    sleep(1)
    driver.find_elements(AppiumBy.ID, 'com.tencent.mm:id/nvt')[2].click()
    sleep(1)
    main_page = driver.find_element(AppiumBy.ID,'android:id/list')
    main_page.find_elements(AppiumBy.CLASS_NAME,'android.widget.LinearLayout')[0].click()
    sleep(1)
    # 滑动浏览朋友圈内容
    driver.swipe(500, 1500, 500, 500, 1000)
    sleep(1)
    driver.swipe(500, 1500, 500, 500, 1000)
    sleep(1)
    print("朋友圈内容正常展示")
    driver.quit()

def test_27():
    driver = link()
    sleep(1)
    search_click(driver, "a")
    sleep(1)
    driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[2].click()
    sleep(1)
    """
    adb shell svc data disable
    adb shell svc data enable
    """
    driver.swipe(1200, 2500, 400, 2500, 800)
    driver.find_elements(AppiumBy.ID,'com.tencent.mm:id/a10')[2].click()
    sleep(1)
    driver.find_element(AppiumBy.CLASS_NAME,'android.widget.CheckBox').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
    os.system('adb shell svc data disable')
    sleep(30)
    os.system('adb shell svc data enable')

    driver.quit()

package = "com.tencent.mm"
activity = "com.tencent.mm.ui.LauncherUI"
#一个冷启动时间
def get_launch_time():
    subprocess.run(["adb", "shell", "am", "force-stop", package])
    sleep(1)
    start = time()
    subprocess.run(["adb", "shell", "am", "start", "-W", f"{package}/{activity}"])
    end = time()
    return round(end - start, 2)

#20次算平均值
def test_avg_cold_start_time():
    times = []
    for i in range(20):
        t = get_launch_time()
        print(f"第{i+1}次冷启动时间：{t} 秒")
        times.append(t)
        sleep(2)

    avg = round(sum(times) / len(times), 2)
    print(f"\n平均冷启动时间：{avg} 秒")

    assert avg <= 2.0, "启动超过2秒"

# def test_15():
#     #发送图片
#     driver = link()
#     sleep(1)
#     search_click(driver,"a")
#     sleep(1)
#     # 打开“+”面板
#     driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[2].click()
#     sleep(1)
#     #点击相册
#     # driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.GridView')[1].click()
#     driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.tencent.mm:id/a10"])[1]').click()
#     sleep(1)
#     driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.CheckBox')[1].click()
#     sleep(1)
#     driver.find_element(AppiumBy.CLASS_NAME,"android.widget.Button").click()
#     driver.quit()
def test_send_10_pic():
    driver = link()
    sleep(1)
    search_click(driver, "a")
    sleep(1)
    # 打开“+”面板
    for i in range(10):
        sleep(1)
        driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")[2].click()
        sleep(1)
        # 点击相册
        # driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.GridView')[1].click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.tencent.mm:id/a10"])[1]').click()
        sleep(1)
        for i in range(10):
            driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.CheckBox')[i].click()
            sleep(1)
        driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").click()
        sleep(5)
    meminfo = subprocess.check_output(["adb", "shell", "dumpsys", "meminfo", "com.tencent.mm"])
    print(meminfo.decode())
    driver.quit()

# def test_monkey():
#     with open("monkey_log.txt", "r") as f:
#         content = f.read()
#         if "CRASH:" in content or "ANR" in content:
#             print("Monkey 测试失败")
#         else:
#             print("Monkey 测试通过")
