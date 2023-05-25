import time

def focus_timer(minutes):

    """

    一个简单的专注时钟函数，接受分钟数作为输入。

    """

    # 转化为秒数

    seconds = minutes * 60

    # 记录开始时间

    start_time = time.time()

    

    # 循环计时

    while True:

        # 计算已过时间

        passed_time = time.time() - start_time

        # 计算剩余时间

        remaining_time = seconds - passed_time

        

        # 没有剩余时间就退出循环

        if remaining_time <= 0:

            print("时间到了！")

            break

        

        # 将剩余时间换算为分钟和秒数

        minutes, seconds = divmod(remaining_time, 60)

        

        # 输出剩余时间，并暂停一秒

        print(f"剩余时间：{int(minutes):02d}:{int(seconds):02d}")

        time.sleep(1)的
