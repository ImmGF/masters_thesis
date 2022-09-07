# masters_thesis

The aim of the project is to use ARA-CNN model as classifier for training set generated based on original dataset used in paper by Rączkowski et al. Through such data preparation, the model demonstrates the possibility of training on the approximation of single cells.

Folder content:
1. QuPath extraction:
  - Lung_cell_detection.groovy
  - Lung_cell_cropping.groovy
2. ARA_CNN scripts:
  - run_ara_loop_python.py
  - run_ara_loop_python_test.py
  - summary_for_ara_ccn_tuned.py

Script descriptions:
Lung_cell_detection.groovy - script detects cells in QuPath application and produces files with coordinates of cells deceted
Lung_cell_cropping.groovy - script takes coordinates of detected cells, cuts out subimages and stores them in a folder
run_ara_loop_python.py - script goes through list of possible parameters of the ARA-CNN net and runs each modified model on the given training data set.
run_ara_loop_python_test.py - script uses loops through trained models by run_ara_loop_python.py and produces classification predictions for test data set.
summary_for_ara_ccn_tuned.py - script goes through the produced results by run_ara_loop_python_test.py and summarized those in form of confusion matrixes and precision_recall plots.

*run_ara_loop_python.py, run_ara_loop_python_test.py - those scripts use the source code that is created by Ł.Rączkowski and stored in https://github.com/animgoeth/ARA-CNN
