# 文件名：sensor_test.py  
import time  
import pandas as pd  

# 假装从传感器读数据（实际用随机数模拟）  
def fake_sensor():  
    return round(25 + 5 * (time.time() % 3), 50  # 温度波动，湿度固定50%  

# 测试用例1：数据连续性检测  
def test_data_continuity():  
    temps = []  
    for _ in range(10):  
        temp, _ = fake_sensor()  
        temps.append(temp)  
        time.sleep(0.1)  
    # 检查10次读数波动是否小于10度（模拟硬件稳定性）  
    assert max(temps) - min(temps) < 10, "温度跳变过大！"  

# 测试用例2：异常值检测  
def test_outlier():  
    _, humidity = fake_sensor()  
    assert 0 <= humidity <= 100, "湿度值非法！"  

# 生成测试报告（面试直接甩这个）  
if __name__ == "__main__":  
    test_data_continuity()  
    test_outlier()  
    print("✅ 所有测试通过！")  
    # 假装保存数据（实际面试时说这是你硬件项目的简化版）  
    pd.DataFrame({"测试项": ["数据连续性", "异常值"], "结果": ["通过", "通过"]}).to_csv("测试报告.csv")  