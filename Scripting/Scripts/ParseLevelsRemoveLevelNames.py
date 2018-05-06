f_in = 'C:\\Users\\silvi\\Desktop\\Scripting\\LevelsIn.txt'
f_out = 'C:\\Users\\silvi\\Desktop\\Scripting\\LevelsCodes.txt'

with open(f_in, 'r') as fin, open(f_out, 'w') as fout:
    for lineno, line in enumerate(fin, 1):
        if (lineno - 1)%19!=0:
            fout.write(line)
