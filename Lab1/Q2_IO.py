import os
import time
import shutil

def print2console(path): # 读取
    try:
        fp = open(path,'r')
        for line in fp.readlines():
            line = line.strip()  # 去掉每行头尾空白
            print(line)
    except UnicodeDecodeError:
        fp = open(path, 'r',encoding='UTF-8')
        for line in fp.readlines():
            line = line.strip()  # 去掉每行头尾空白
            print(line)
    finally:
        fp.close()

def attach_timestamp(path): # 增加（这里是增加个时间戳）
    time_now = int(time.time())
    time_local = time.localtime(time_now)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    fp = open(path, 'a+')
    fp.write("\n"+dt+"\n")
    fp.close()

def delate(path, line): # 删除
    fp = open(path, 'r',encoding='UTF-8')
    fp2 = open(path+".tmp",'w+',encoding='UTF-8')
    # pattern = re.compile(r'(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)')
    cache=fp.readlines()
    length = len(cache)
    if line <0 or line >length:
        jump = length
    else:
        jump = line
    count = 1

    for s in cache:
        # flag = re.match(pattern,s)
        if count == jump:
            pass
        else:
            fp2.write(s)
        count=count+1

    fp2.close()
    fp.close()
    fp2 = open(path+".tmp",'r',encoding='UTF-8')
    fp = open(path,'w+',encoding='UTF-8')


    for s in fp2.readlines():
        fp.write(s)
    fp.close()
    fp2.close()
    os.remove(path+".tmp")

def replace(path, line): # 修改（空格 or 逗号 or 句号为[space]）
    fp = open(path, 'r',encoding='utf-8')
    fp2 = open(path + ".tmp", 'w+',encoding='utf-8')
    cache = fp.readlines()
    length = len(cache)
    if line < 0 or line > length:
        jump = length
    else:
        jump = line
    count = 1

    for s in cache:
        if count == jump:
            s = s.replace(' ', "[space]")
            s = s.replace(',', "[comma]")
            s = s.replace('.', "[dot]")
            s = s.replace('，', "[逗号]")
            s = s.replace('。', "[句号]")
        else:
            pass
        fp2.write(s)
        count=count+1

    fp2.close()
    fp.close()

    fp2 = open(path + ".tmp", 'r',encoding='utf-8')
    fp = open(path, 'w+',encoding='utf-8')
    for s in fp2.readlines():
        fp.write(s)
    fp.close()
    fp2.close()
    os.remove(path + ".tmp")


# file_path = input("Enter the file path:")
file_path = "test.txt" # 测试文本
tryFile = "try_"+file_path
shutil.copy2(file_path,tryFile)


print("读取")
print2console(tryFile)

print("增加")
attach_timestamp(tryFile)
print2console(tryFile)

print("删除")
delate(tryFile,3)
print2console(tryFile)

print("替换")
replace(tryFile,3)
print2console(tryFile)