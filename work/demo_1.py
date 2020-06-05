import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print "start"
def read_data():
    list_name = os.listdir('data')
    print list_name
    df = pd.DataFrame(columns=('id', 'score1','score2', 'label'))
    for i in list_name:
        print "concat_{}".format(i)
        temp = pd.read_csv('data/{}'.format(i), header=0, names=['id', 'score1','score2', 'label'])
        df = df.append(temp, sort=False, ignore_index=True)
    df["label"].fillna(0, inplace=True)
    print df.head(5)
    df['label'] = df['label'].astype("int")
    return df
 
 
df = read_data()
print 'success'
print df["label"].value_counts()
label, score1,score2 = df['label'].values, df['score1'].values,df['score2'].values
 
def prc(label,score1,score2):
    precision, recall, thresholds = precision_recall_curve(label,score1)
    grade1 = auc(recall, precision)
    print grade1
    plt.plot(recall, precision,color='red',label='v1:{}'.format(round(grade1,4)))
    precision, recall, thresholds = precision_recall_curve(label, score2)
    grade2 = auc(recall, precision)
    print grade2
    plt.plot(recall, precision,color='blue',label='v2:{}'.format(round(grade2,4)))
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel("Recall Rate")
    plt.ylabel("Precision Rate")
    plt.title('PR')
    plt.legend(loc="upper right")
    plt.show()
prc(label,score1,score2)
def roc(label,score1,score2):
    fpr, tpr, _ = roc_curve(label,score1)
    roc_auc = auc(fpr, tpr)
    print roc_auc
    plt.plot(fpr, tpr,color='red',label='v1:{}'.format(round(roc_auc,4)))
 
    fpr, tpr, _ = roc_curve(label, score2)
    roc_auc = auc(fpr, tpr)
    print roc_auc
    plt.plot(fpr, tpr,color='blue',label='v1:{}'.format(round(roc_auc,4)))
 
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()
    print "roc_auc_score:{}".format(roc_auc_score(label, score1))
    print "roc_auc_score:{}".format(roc_auc_score(label, score2))
roc(label,score1,score2)
def balance(df):
    df=df[df['label']==1]
    score1, score2 = df['score1'].values, df['score2'].values
    plt.hist(score1,histtype='stepfilled', alpha=0.5, bins=10,color='red',label="XGB_DujsFeeInterceptorDetourFactV1")
    plt.hist(score2,histtype='stepfilled', alpha=0.5, bins=10,color='blue',label="XGB_interceptor-detour-fact-v2")
    plt.title("Result Display")
    plt.legend(loc="upper right")
    plt.xlim([0.0, 1.0])
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.show()
balance(df)
