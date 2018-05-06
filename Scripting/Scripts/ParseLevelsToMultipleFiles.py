f_in = 'C:\\Users\\silvi\\Desktop\\Scripting\\LevelsCodes.txt'
f_outRoot = 'C:\\Users\\silvi\\Desktop\\Scripting\\Levels\\'
f_outName = 'Level'
extension = '.txt'
level = 1
with open(f_in, 'r') as fin:
    for lineno, line in enumerate(fin, 1):
        level = (lineno-1)//18 +1;
        f_out = f_outRoot+f_outName+str(level)+extension
        if line.strip():
            with open(f_out,'a') as fout:
                 fout.write(line)