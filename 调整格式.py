import os, re

# 遍历文件夹
def get_dirlist(cwd):
    dirlist = os.listdir(cwd)
    return dirlist

pwd = os.getcwd()
dirlist = get_dirlist(pwd)
dirlist.sort()

# 判断以3个数开头的

newdirlist = []
[newdirlist.append(dir) for dir in dirlist if re.match('\d{3}', dir) and len(dir) > 3]

for dir in newdirlist[:1]:
    oldname = dir
    newname = dir[:3]
    deletename = dir.replace(' ', '\ ') + '\\' + newname + '.py'
    print(deletename)
    os.rename(oldname, newname)
    os.system('git add %s/' % newname)
    os.system('git rm -r --cached %s' % deletename)
    os.system('git commit -m "%s" %s' % (oldname, newname))
    os.system('git push')
