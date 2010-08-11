def readfile(filename):
    lines = [line for line in file(filename)]

    # 最初の行は列のタイトル(出現word)
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # blog名
        rownames.append(p[0])
        # wordの出現回数
        data.append([float(x) for x in p[1:]])
    return rownames, colnames, data
