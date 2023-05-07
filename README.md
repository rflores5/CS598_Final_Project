# CS598_Final_Project
Final Project

Google Drive (contains all files that are too large for github): https://drive.google.com/drive/folders/1MQCB4PeXko5T1h45QVjhKR_Q8TBDiduk?usp=sharing

To run the IPYNB files, we can use either jupyter notebook or Google Colab.

For the TF-IDF BiLSTM model, this can be run using the jupyter notebook file "TF-IDF-LSTM.ipynb". It reads in the symptom samples and disease labels from the file symptoms.txt in this repo. If this notebook is being run in using Google Colab, we included a few commented lines that contain code to mount a google drive and the new file path of this symptoms.txt file. It needs to be placed in the same google drive as the notebook file. The notebook can then be run normally each section in order. 

Also included in this repo related to this model are two python scripts metamap.py and extract_notes_diagnoses.py. These scripts were used during pre-processing to extract the symptom information using metamap and extract the diagnosis labels and filter the notes for discharge notes respectively. These were used to generate the file symptoms.txt, so they do not need to be run again. There is another file top_50_notes.csv not included in this github repo, but is located in the above linked google drive because it is too big. This file was generated using extract_notes_diagnoses.py and was used by metamap.py.

For the word2Vec BiLSTM model, we need to run two IPYNB files.  First, we need to run the file “Word2Vec_Word_Embedding.ipynb” for the data preprocessing and create Word2Vec embedding. This IPYNB file will read the csv from “top_50_notes.csv” (this file we can get it from the shared link for google drive. Because of the large file size, we uploaded in the google drive), which has DIAG_ID and symptoms notes. In this IPYNB file, we are doing data cleaning and saved the cleaned data into “data_preporssing_05042023.csv” file and creating word2Vec embedding on that cleaned data and save the word2vec embedding mode with the name “word2Vec_embeddings_05042023.bin”

Second, we need to run the “Word2Vec_BiLSTM.ipynb”. It will use saved word2vec embedding model (word2Vec_embeddings_05042023.bin) and will take this model as a input vector to build the BiLSTM model. Finally, We are saving word2vec + BiLSTM model in the file called “Word2Vec.pth”
