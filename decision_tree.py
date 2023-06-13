import numpy as np
import pandas as pd
eps = np.finfo(float).eps
from numpy import log2 as log
df = pd.read_csv("youtube_data.csv")
Vie =df.loc[:,'Views_groups']
Lik = df.loc[:,'Likes_groups']
Sub = df.loc[:,'Subs_groups']
dis = df.loc[:,'Dislikes']
play =df.loc[:,'Play']
dataset ={'Views':Vie,'Likes':Lik,'Subscribers':Sub,'Dislikes':dis,'play':play}
df = pd.DataFrame(dataset,columns=dataset.keys())

entropy_node = 0  
values = df.play.unique()  
for value in values:
    fraction = df.play.value_counts()[value]/len(df.play)
    entropy_node += -fraction*np.log2(fraction)

print(f'Values: {values}')
print(f'entropy_node: {entropy_node}')

def ent(df,attribute):
    target_variables = df.play.unique()  
    variables = df[attribute].unique()   


    entropy_attribute = 0
    for variable in variables:
        entropy_each_feature = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute]==variable][df.play ==target_variable]) 
            den = len(df[attribute][df[attribute]==variable])  
            fraction = num/(den+eps)  #pi
            entropy_each_feature += -fraction*log(fraction+eps) 
        fraction2 = den/len(df)
        entropy_attribute += -fraction2*entropy_each_feature   

    return(abs(entropy_attribute))
a_entropy = {k:ent(df,k) for k in df.keys()[:-1]}

def ig(e_dataset,e_attr):
    return(e_dataset-e_attr)
IG = {k:ig(entropy_node,a_entropy[k]) for k in a_entropy}


def find_entropy(df):
    Class = df.keys()[-1]  
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value] / len(df[Class])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_entropy_attribute(df, attribute):
    Class = df.keys()[-1]  
    target_variables = df[Class].unique() 
    variables = df[
        attribute].unique()  
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[Class] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * log(fraction + eps)
        fraction2 = den / len(df)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        IG.append(find_entropy(df) - find_entropy_attribute(df, key))
    return df.keys()[:-1][np.argmax(IG)]


def get_subtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df, tree=None):
    Class = df.keys()[-1]  # To make the code generic, changing target variable class name


  
    node = find_winner(df)

     attValue = np.unique(df[node])
    if tree is None:
        tree = {}
        tree[node] = {}

    for value in attValue:

        subtable = get_subtable(df, node, value)
        clValue, counts = np.unique(subtable[Class], return_counts=True)

        if len(counts) == 1: 
            tree[node][value] = clValue[0]
        else:
            tree[node][value] = buildTree(subtable)  
    return tree
print(buildTree(df))
