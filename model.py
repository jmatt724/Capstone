from tkinter.ttk import Label
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.tree import DecisionTreeClassifier ,export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from matplotlib import pyplot as plt
import graphviz
import collections
import pydotplus
import pickle
import seaborn as sns

from random import randint

def main():

    diagnosis_list = ["CHF", "High Blood Sugar", "Respiratory Infection", "UTI", "Broken Bone", "Gastrointestinal Virus", "Hypertensive Crisis"]
    df = pd.read_csv(r"generated_medical_data3.csv" ,encoding='UTF8')

    encoder = LabelEncoder()

    columns = list(df.columns)

    df = pd.DataFrame(data=df.values, columns = columns)

    df_encoded = df

    for i in df_encoded:
        df_encoded[i] = encoder.fit_transform(df[i])

    df_encoded.loc[:, ~df.columns.isin(['name', 'arriveTime', 'age'])]

    diagnosis_mapping = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))

    print(diagnosis_mapping)

    X = df_encoded.iloc[:,3:21]

    Y = df_encoded.iloc[:,21]

    x_train, x_test, y_train, y_test = train_test_split(X.values, Y.values, test_size=0.3)

    model = DecisionTreeClassifier(criterion='entropy', random_state=0, max_depth = 8, min_samples_leaf=3)

    model.fit(x_train, y_train)

    new_patient = [[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]]

    print(type(model.predict(new_patient)))

    print(model.score(x_test, y_test))  

    fn = df.columns
    fn = fn.drop(['name', 'arriveTime', 'diagnosis', 'age'])
    cn = diagnosis_list

    colors = ('blue', 'yellow', 'green', 'red', 'orange', 'purple')

    edges = collections.defaultdict(list)

    visualize = tree.export_graphviz(model, out_file=None, feature_names= fn, class_names=cn, filled = True, rounded= True)
    
    graph = pydotplus.graph_from_dot_data(visualize)

    edges = collections.defaultdict(list)

    for edge in graph.get_edge_list():
        edges[edge.get_source()].append(int(edge.get_destination()))

    for edge in edges:
        edges[edge].sort()
        for i in range(2):
            color = randint(0,5)
            dest = graph.get_node(str(edges[edge][i]))[0]
            dest.set_fillcolor(colors[color])

    #graph.write_png('color_test.png')

    filename = 'new_RRTS_model.sav'
    pickle.dump(model, open(filename, 'wb'))

    y_pred = model.predict(x_test)

    matrix = confusion_matrix(y_test, y_pred)

    ax = sns.heatmap(matrix, annot=True, cmap='Blues')
    ax.set_title('Confusion Matrix')
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Actual Values  ')

    ax.xaxis.set_ticklabels(["CHF", "HBS", "RI", "UTI", "BB", "GV", "HC"])
    ax.yaxis.set_ticklabels(["CHF", "HBS", "RI", "UTI", "BB", "GV", "HC"])
    
    plt.show()






if __name__ == '__main__':
    main()
