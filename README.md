# 6.819_Final_Project

Project Proposal can be found [here](https://docs.google.com/document/d/1a3bp80PlhjW0JvMrGwrFz8akmAMkwganaYelj_-uMlM/edit)

# Dependencies

# Pipeline

We obtained our dataset from the Qatar Computing Research Institute, which is avaliable for download here: 
http://crisisnlp.qcri.org/data/ASONAM17_damage_images/ASONAM17_Damage_Image_Dataset.tar.gz (5GB)

We have developed two classifiers to help responders and insurance companies understand the distribution of damage that has occured in their city as a result of an Earthquake. 

Classifier #1: By Damage Intensity 

The first classifier labels the image as containing Extreme, Mild, or No Damage present. We have chosen to train on the 2015 Nepal Earthquake and 2015 Ecuador Earthquake Datasets. In order to sort, train, and run the classifier:

1. Extract the dataset in the src directory, and run the file ``python sort.py `` to combine the Ecuador & Nepal Earthquake datasets into folders named as per their category (Extreme, Mild, and No Damage).

2. Inside the tensorflow-for-poets-2 directory, run:

``nohup python -m scripts.retrain   --bottleneck_dir=tf_files/bottlenecks   --how_many_training_steps=1500   --model_dir=tf_files/models/  --summaries_dir=tf_files/training_summaries/"inception_default"  --output_graph=tf_files/retrained_graph.pb   --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/ggImage --learning_rate=0.0001 &> nohup_damage_type_mobilenet.out&``

This will run the Inception V3 Model with the Adam Optimizer. The test accuracy will be displayed at the very end of the nohup.out file. To visualize the accuracy and cross entropy graphs via tensorboard, run, in the same directory: 

``tensorboard --logdir tf_files/training_summaries/"inception_default"``
