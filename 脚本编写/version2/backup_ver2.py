'''较第一版的改进是以天为名称创建一个文件夹
    并将以日分秒为名称的压缩文件放到新创建的文件夹中'''
import os
import time
source=[r'C:\Users\Administrator\Desktop\python\笔记']
target_dir=r'C:\Users\Administrator\Desktop\python'
today=target_dir+os.sep+time.strftime('%Y%m%d')
target=today+os.sep+time.strftime('%H%M%S')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)
zip_command='winRAR A -r {0} {1}'.format(target,' '.join(source))
print('zip command is:')
print(zip_command)
if os.system(zip_command)==0:
    print('Backup successful',target)
else:
    print('Backup failed')
