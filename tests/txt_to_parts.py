import os


def txt_to_parts(source_file, path_out_files, i_max, j_max):
    
    if not os.path.exists(path_out_files):
        os.mkdir(path_out_files)

    with open(source_file, "r", encoding="utf-8") as f:
        for i in range(i_max):
            for j in range(j_max):
                with open(f'{path_out_files}/text{i + 1}_{j + 1}.txt', "w", encoding="utf-8") as res:
                    res.write("\n<speak>\n")
                    c = '\n'
                    for k in range(750):
                        c = f.read(1)    
                        if (k > 700) and (c == '.'):
                            res.write(c)
                            break
                        else:
                            res.write(c)
                            if (c == '.') or (c == ' ' and k % 50 == 0):
                                res.write('\n')

                    c = f.read(1)
                    if c != ' ':
                        res.write(c)
                        for t in range(0, 100):
                            c = f.read(1)
                            if c == ' ':
                                break
                            res.write(c)
                                     
                    res.write("\n</speak>\n")


src_file = "test.txt"
path_out_files = "parts"

txt_to_parts(src_file, path_out_files, 3, 3)
