# Deep-learning-in-Computational-Biology

## Predicting RNAcompete binding from RNA bind-n-seq data

### Introduction:
RNA-binding proteins (RBPs) play a significant role in various cellular processes, including mRNA splicing, transport, stability, and translation, making them essential for proper cellular functioning. Deciphering the RNA-binding preferences of RBPs is crucial for understanding the intricate regulatory networks that govern cellular processes at the molecular level. For measuring RNA binding preferences, we used data from two different technologies: RNA Bind-n-Seq and RNAcompete. For each RBP we implemented a deep learning model and use it to score RNAcompete probes to find the RNA binding preferences. In this project we aim to assign binding intensities to RNAcompete probes. We achieved this by implement an aggregation function over the model probability to produce a single binding score. 

### Model architecture:
We implemented a Convolutional Neural Network (CNN) to predict the RNA binding preferences from RNA bind-n-seq data. The input is a one-hot encoding of size of the maximum sequence length of RNAcompete or RNA Bind-n-Seq sequences. The labels are corresponded to the different concentrations. The input file was labeled as 0, concentrations that smaller than 100nM ware labeled as 1, concentrations between 100nM and 500nM were labeled as 2 and concentrations above 500nM was labeled as 3.

![Model Architecture](model_architecture.png)

### Aggregation functions:
Our model outputs consist of 4 classes, therefore, we required an aggregation function to combine the model probabilities into a single binding score. Throughout our work, we explored various aggregation functions to attain the highest Pearson correlations between the model output and the RNAcompete score. The aggregation functions we examined were:

(1)  concentration3 + concentration2 + concentration1 - concentration0

(2)  concentration3 + concentration2 - concentration0

(3)  concentration3 + concentration2

(4)  max⁡(concentration)-min⁡(concentration)

The function that yields the highest Pearson correlation between RNAcompete scores and the output was (2).

![Agg_func](Aggregation.png)
