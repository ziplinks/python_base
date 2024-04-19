# 实现功能： 读取test文件内数据，把正式数据写入到test.bak文件内

fr = open("test", "r", encoding="UTF-8")
fw = open("test.bak", "a", encoding="UTF-8")
for line in fr.readlines():
    if line.strip()[-2:] == "正式":
        fw.write(line)
fw.close()
fr.close()
