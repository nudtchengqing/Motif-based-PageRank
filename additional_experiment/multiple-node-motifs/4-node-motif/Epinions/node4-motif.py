# -*-coding: utf-8 -*-
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
import scipy.sparse
from scipy.sparse import diags


def normal_matrix(a):
    # 对于非对称的矩阵，我们的归一化的方式应该是按照行来进行归一化
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        row_sum = a.getrow(number).sum()
        if row_sum == 0:
            continue
        else:
            for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
                a[number, number_col] = a[number, number_col] / row_sum
    return a


def normal_matrix_new(a):
    # 对于对称的矩阵，我们可以使用矩阵相乘的方式来进行归一化，这样的话速度比较快。
    d = a.sum(0)
    d = np.array(d)
    d = d[0]
    dd = map(lambda x: 0 if x==0 else np.power(x, -0.5), d)
    D_matrix = diags(dd, 0)
    C = D_matrix.dot(a)
    C = C.dot(D_matrix)
    a = C
    return a


def row_read(txt_name, id):
    f = open(txt_name, 'r')
    result = []
    flag = False
    count = 0
    while True:
        line = f.readline()
        if line == ('subgraph id = %d\n' % int(id)):
            for i in range(4):
                line = f.readline()
            while True:
                line = f.readline()
                if line:
                    line = line.strip()
                    line = line.split('	')
                    if len(line) == 4:
                        result.append(line)
                        count += 1
                    else:
                        flag = True
                        break
        else:
            if flag == False:
                continue
            else:
                break
    print(len(result))
    return result


def construct_four(txt_name_out, entry_unique, type):
    # the type is the id of motif which is produced by mfinder1.21.
    # This means that you must use the corresponding txt results which record the member of each motif.
    motif_matrix = np.zeros((len(entry_unique), len(entry_unique)), dtype=np.float64)
    if type == '286':
        row_data = row_read(txt_name_out, 286)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
    if type == '222':
        row_data = row_read(txt_name_out, 222)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
    if type == '476':
        row_data = row_read(txt_name_out, 476)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '478':
        row_data = row_read(txt_name_out, 478)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '972':
        row_data = row_read(txt_name_out, 972)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
    if type == '990':
        row_data = row_read(txt_name_out, 990)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
    if type == '5086':
        row_data = row_read(txt_name_out, 5086)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
            motif_matrix[id_4][id_1] += 1
    if type == '204':
        row_data = row_read(txt_name_out, 204)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
    if type == '472':
        row_data = row_read(txt_name_out, 472)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '906':
        row_data = row_read(txt_name_out, 906)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
    if type == '922':
        row_data = row_read(txt_name_out, 922)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
    if type == '2204':
        row_data = row_read(txt_name_out, 2204)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_4] += 1
    if type == '2252':
        row_data = row_read(txt_name_out, 2252)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_4] += 1
    if type == '6552':
        row_data = row_read(txt_name_out, 6552)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_4] += 1
            motif_matrix[id_4][id_1] += 1
    if type == '2458':
        row_data = row_read(txt_name_out, 2458)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_4] += 1
    if type == '4556':
        row_data = row_read(txt_name_out, 4556)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_4][id_1] += 1
    if type == '6554':
        row_data = row_read(txt_name_out, 6554)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_4] += 1
            motif_matrix[id_4][id_1] += 1
    if type == '13142':
        row_data = row_read(txt_name_out, 13142)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
            motif_matrix[id_4][id_1] += 1
            motif_matrix[id_4][id_2] += 1
    if type == '13150':
        row_data = row_read(txt_name_out, 13150)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
            motif_matrix[id_4][id_1] += 1
            motif_matrix[id_4][id_2] += 1
    if type == '13278':
        row_data = row_read(txt_name_out, 13278)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            id_4 = np.where(entry_unique == int(row_data[number][3]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_1][id_4] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_2][id_4] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
            motif_matrix[id_4][id_1] += 1
            motif_matrix[id_4][id_2] += 1
    return motif_matrix


def construct_motif(txt_name, times, type, alpha_value):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                temp.append(int(line[i]))
            entry.append(temp)
        else:
            break
    spare_array_row = []
    spare_array_col = []
    spare_array_data = []
    entry_all = []
    for i in range(len(entry)):
        spare_array_row.append(entry[i][0])
        spare_array_col.append(entry[i][1])
        spare_array_data.append(1)
        entry_all.append(entry[i][0])
        entry_all.append(entry[i][1])
    entry_unique = np.unique(entry_all)
    newspare_array_row = []
    newspare_array_col = []
    counttt = 0
    for nnn in range(len(spare_array_row)):
        if counttt % 100000 == 0:
            print 'echo is %d' % counttt
        counttt += 1
        id1 = spare_array_row[nnn]
        id2 = spare_array_col[nnn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        newspare_array_row.append(id1new)
        newspare_array_col.append(id2new)
    maxnum = len(entry_unique)
    adjacency_matrix = csr_matrix((spare_array_data, (newspare_array_row, newspare_array_col)), shape=(maxnum, maxnum), dtype = np.float64)
    # 下面的三行代码主要是为了能够让得到的邻接矩阵为binary，如果希望是weighed，请注释
    data_array = adjacency_matrix.data
    lennn = data_array.shape[0]
    adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
    # print adjacency_matrix.shape
    print adjacency_matrix.nnz
    result_B = adjacency_matrix.copy()
    result_B = normal_matrix(result_B)

    txt_name_out = 'motif_detect/mfinder1.21/Epinions_fanmod2_MEMBERS.txt'
    # this txt record the members list of all subgraphs. For more details, please refer to the mfinder software.
    # motif is constructed by the method of sampling.
    result_D = construct_four(txt_name_out, entry_unique, type)
    result_D = csr_matrix(result_D, dtype=np.float64)
    result_D_tran = np.transpose(result_D)
    result_D = result_D + result_D_tran
    result_D = normal_matrix_new(result_D)
    result_temp1 = result_B.multiply(alpha_value).tolil()
    result_temp2 = result_D.multiply(1 - alpha_value).tolil()
    result_tt = result_temp1 + result_temp2
    result_tt = result_tt.tocsr()
    # print result_tt
    return result_tt, entry_unique


def binary(a_original):
    a = a_original.copy()
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
            a[number, number_col] = 1
    return a



