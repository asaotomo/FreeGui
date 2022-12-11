'''
time: 20221127

这个文件保存的是工具的架构标识，可以自己喜好设置。
基础架构：
1--信息收集 					#工具类别
	urlfind					   #具体工具的名称
		00.txt				   #工具的笔记
		xxx.py				   #工具的源文件，启动文件，注意：请不要再新增一级目录

工具的启动类型：

python   xx.py
start  xx.exe

'''

# 工具类别目录标识
# 例如：1--信息收集,记号是mark
toolsTypeDirMark = '--'

# 具体工具
# 工具笔记文件名标识,txt是必要的
toolNoteMark = '00.txt'

# 工具的分类建议：
'''
vnlmap_0.9_py
名称-版本-类型
'''

# 窗口大小，root.geometry('2400x1600+300+200')
height = 1550
width = 2550

# 上左边距，下面的两个参数，作用是保证弹框在中间
scree = "300+200"

x = 620
y = 800
