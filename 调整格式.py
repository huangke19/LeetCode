import os, re

# 遍历文件夹
pwd = os.getcwd()
dirlist = os.listdir(pwd)
dirlist.sort()

# 取未个性名字的文件夹
newdirlist = []
[newdirlist.append(dir) for dir in dirlist if re.match('\d{3}', dir) and len(dir) > 3]

# 改名，推送
for dir in newdirlist:
    oldname = dir
    newname = dir[:3]
    deletename = dir.replace(' ', '\ ') + '/' + newname + '.py'
    os.rename(oldname, newname)
    os.system('git add %s/' % newname)
    os.system('git rm -r --cached %s' % deletename)
    os.system('git commit -m "%s" %s' % (oldname, newname))
    os.system('git push')
