f_inRoot = 'D:\\LastYear\\Licenta\\Scripting\\Levels\\'
f_outRoot = 'D:\\LastYear\\Licenta\\Scripting\\LevelsOut\\'
f_Name = 'Level'
f_outReplacer = 'Out'
extension = '.txt'
for i in range (1,150):
    f_in = f_inRoot + f_Name + str(i) + extension
    f_out = f_outRoot + f_Name + f_outReplacer + str(i) + extension
    with open(f_in, 'r') as fin,open(f_out,'w') as fout:
        for lineno, line in enumerate(fin, 1):
            line = line.replace("+","");
            if(lineno !=16):
                line = line.split("\"")[1] + "\n"
            else:
                line = line.split("\"")[1]
            fout.write(line)