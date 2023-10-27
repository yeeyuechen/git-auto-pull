import os
import time

print('Git仓库定时自动更新')
print('版本1.0（笑')

__path__ = input('输入Git库的绝对路径：')
__time__ = input('输入更新间隔时长（单位：秒）：')
__time__ = float(__time__)

while True:
    time.sleep(__time__)
    os.system('cd '+ __path__ +' && git pull')
