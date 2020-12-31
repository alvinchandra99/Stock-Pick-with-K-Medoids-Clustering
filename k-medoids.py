from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
#import getData
import kmedoids
import pandas as pd

# Mengirim data base berupa numy


def dfData():
    df = pd.read_excel('DataSaham5.xlsx',
                       sheet_name='Sheet1')
    df = df.drop('Negative PE', axis=1)
    df = df.drop('kode_saham', axis=1)
    df = df.drop('harga_sekarang', axis=1)
    df = df.drop('BVPS', axis=1)
    df = df.drop('PE', axis=1)
    df = df.drop('EPS', axis=1)
    df.drop(df.columns[df.columns.str.contains(
        'unnamed', case=False)], axis=1, inplace=True)
    return df.to_numpy()


def getResultKMedoid():
    # 3 points in dataset
    data2 = np.array([[1, 1],
                      [2, 2],
                      [10, 10]])

    data = dfData()

    # distance matrix
    D = pairwise_distances(data, metric='euclidean')

    # split into 2 clusters
    M, C = kmedoids.kMedoids(D, 2)

    # print('medoids:')
    # for point_idx in M:
    #    print(data[point_idx])

    Label0 = []
    Label1 = []

    # print('')
    #print('clustering result:')
    for label in C:
        for point_idx in C[label]:
            if label == 0:
                Label0.append(data[point_idx])
            if label == 1:
                Label1.append(data[point_idx])
            #print('label {0}:　{1}'.format(label, data[point_idx]))
    #result = {'Label1': Label1, 'Label0': Label0}
    dfLabel1 = pd.DataFrame(
        Label1, columns=['Market_Cap', 'Beta', 'Cash'])
    dfLabel1['cluster'] = 'Cluster 1'
    dfLabel0 = pd.DataFrame(
        Label0, columns=['Market_Cap', 'Beta', 'Cash'])
    dfLabel0['cluster'] = 'Cluster 0'
    df = pd.concat([dfLabel1, dfLabel0], ignore_index=True)
    return df


def getResult():
    df = pd.read_excel('DataSaham5.xlsx',
                       sheet_name='Sheet1')
    df.drop(df.columns[df.columns.str.contains(
        'unnamed', case=False)], axis=1, inplace=True)
    data = getResultKMedoid()
    print(df)

    result = pd.merge(
        df, data, on=['Market_Cap', 'Market_Cap'])

    result = result.drop('Beta_y', axis=1)
    result = result.drop('Cash_y', axis=1)
    return result.to_excel('DataSaham5.xlsx')
