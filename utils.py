import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score,balanced_accuracy_score,matthews_corrcoef

def eliberate_cuda_memory():
  import torch, gc
  gc.collect()
  torch.cuda.empty_cache()

def split_dataset(data):
  """Function to split dataset into train, val and test"""
  np.random.seed(112)
  df_train, df_val, df_test = np.split(data.sample(frac=1, random_state=42),
                                      [int(.8*len(data)), int(.9*len(data))])

  # Print dimensions
  print(len(df_train),len(df_val), len(df_test))

  return df_train, df_val, df_test

def print_metrics(y_pred, y_test,title:str = "Confusion Matrix"):

    print(f"Balanced Accuracy: {balanced_accuracy_score(y_test, y_pred)}")
    print(f"Precision: {precision_score(y_test, y_pred,average='weighted')}")
    print(f"Recall: {recall_score(y_test, y_pred,average='weighted')}")
    print(f"F1: {f1_score(y_test, y_pred,average='weighted')}")
    print(f"Metthew corr: {matthews_corrcoef(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='g')
    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()