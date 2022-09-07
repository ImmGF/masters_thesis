import pandas as pd
import numpy as np

from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
import matplotlib.pyplot as plt

import os
import re

def summarize_ara_cnn(path, output_path):
    
    count = 0

    classes = ['BRONCHI', 'IMMUNE_CELLS', 'LUNG_TISSUE', 'MIXED_STROMA', 'NECROSIS', 'STROMA', 'TUMOR', 'VESSEL_WALL']
    image_output_path = path + "PR_curves/"
    
    if os.path.exists(image_output_path):
        os.system("rm -r {}".format(image_output_path))
        
    models = [name for name in os.listdir(path) if os.path.isdir(path + name)]
    
    os.mkdir(image_output_path)
    
    architecture_parameters = ["im_size",
                               "lr_rate",
                               "dr_rate",
                               "nb_bocks_1_path",
                               "nb_blocks_2_path",
                               "filter_nb",
                               "filter_size",
                               "strides",
                               "pooling_size",
                               "filter_nb_residual",
                               "filter_size_residual"]
    
    output_table = pd.DataFrame(columns = ["Model"] + 
                                          architecture_parameters + 
                                          ["Accuracy", "Average_precision"] + 
                                          ["Average_precision_" + cl for cl in classes])
    
    for model in models:
        
        #added#
        confusion_mat = pd.DataFrame(np.zeros((len(classes),len(classes))), columns=classes, index=classes)
        #added#


        count += 1
            
        #do_precision_and_recall
        identity_matrix = np.identity(len(classes))
        plt.rcParams['figure.figsize'] = (10, 5)
        classes_average_precision = []

        for cls_n in range(len(classes)):

            precrec_true_values = []
            precrec_softmax_values = []

            for files in classes:

                ds = pd.read_csv(path + model + "/{}/results.csv".format(files))

                for i in range(ds.shape[0]):

                    vectorized_true_value = identity_matrix[cls_n]
                    softmax_values = ds[classes].iloc[i,]                       

                    for i in range(len(softmax_values)):

                        precrec_true_values.append(vectorized_true_value[i])
                        precrec_softmax_values.append(softmax_values[i])

            precision, recall, _ = precision_recall_curve(np.array(precrec_true_values), np.array(precrec_softmax_values))
            average_precision = average_precision_score(np.array(precrec_true_values), np.array(precrec_softmax_values))

            classes_average_precision.append(average_precision)

            plt.plot(recall, precision, label = "class {}, AP {:0.2f}".format(classes[cls_n], (average_precision)))
            plt.xlabel("recall")
            plt.ylabel("precision")
            plt.legend(loc="best")
            plt.title("precision vs. recall curve")


            plt.legend()
        
        model_name = model.replace(".",",")
        plt.savefig(image_output_path + "PRCurve_ARA_CNN_{}.png".format(model_name))
        #plt.show()
        plt.close()
    
        #get_diagonal_accuracy
        true_positives = 0.0
        total = 0.0

        architecture_values = []
        
        model_dummy = model

        for a in architecture_parameters:

            model_dummy = model_dummy.replace(a, "", 1)
            model_dummy = model_dummy.strip("_")
            temp_model = model_dummy.split("_")
            architecture_values.append(temp_model[0])
            temp_model = temp_model[1::]
            model_dummy = "_".join(temp_model)
            

        for cls_n in range(len(classes)):
                        
            ds = pd.read_csv(path + model + "/{}/results.csv".format(classes[cls_n]))
            
            for i in range(ds.shape[0]):
                total += 1.0
                
                if cls_n == ds[classes].iloc[i,].tolist().index(ds[classes].iloc[i,].max()):
                    true_positives += 1.0

                ###added###

                true_class = classes[cls_n]
                predicted_class = classes[ds[classes].iloc[i,].tolist().index(ds[classes].iloc[i,].max())]

                confusion_mat.loc[[true_class],[predicted_class]] += 1

                ###added###
        
        ###added###
        confusion_mat.to_csv(output_path + model + "/"  + "confusion_matrix.csv")
        print(output_path + model + "/"  + "confusion_matrix.csv")
        ###added###
                    
                
        row = pd.DataFrame([["ara_cnn_original"] + 
                            architecture_values + 
                            [true_positives/total, np.mean(classes_average_precision)] + 
                            classes_average_precision], 
                           columns = ["Model"] + 
                                     architecture_parameters + 
                                     ["Accuracy", "Average_precision"] + 
                                     ["Average_precision_" + cl for cl in classes])

        output_table = output_table.append(row)

        print("######################")
        print()
        print(count)
        print()
        print("######################")
    
    output_table.to_csv(path + "ara_cnn_accuracies.csv")

pth = "/mnt/storage/ifilipiuk/tuned_ara_cnn/"

summarize_ara_cnn(path = pth, output_path = pth)
