__author__      = '踢低吸'

import os
import sys
import shutil
w = shutil.get_terminal_size()[0]
print('\x1b[38;33m#'*w)
try:
	select = input('\x1b[38;5;42m' + '請輸入數字\n(1) - 下載備份整個頻道\n(2) - 備份自己的首頁影片[需要有yt.html]\n(3) - 僅備份單個影片\n\x1b[38;33m>>> ')
	if select == '1':
		arg = input('\x1b[38;5;42m(1) - 下載備份整個頻道\n請輸入頻道網址:\n\x1b[38;37m')
		os.system('python3 CHargs.py %s' % (arg))
	elif select == '2':
		arg = input('\x1b[38;5;42m(2) - 備份自己的首頁影片[需要有yt.html]\n\x1b[38;37m')
		os.system('python3 YT.py')
	elif select == '3':
		arg = input('\x1b[38;5;42m(3) - 僅備份單個影片\n請輸入網址:\n>>> \x1b[38;37m')
		os.system('python3 CHargs.py %s' % (arg))
	else:
		print('白眼。')
	print('\x1b[38;33m#'*w)
except KeyboardInterrupt:
	print('\x1b[38;96m\n掰掰~')
except:
	print('err')
