# Deep-learning-in-Computational-Biology

## Predicting RNAcompete binding from RNA bind-n-seq data

### Introduction:
RNA-binding proteins (RBPs) play a significant role in various cellular processes, including mRNA splicing, transport, stability, and translation, making them essential for proper cellular functioning. Deciphering the RNA-binding preferences of RBPs is crucial for understanding the intricate regulatory networks that govern cellular processes at the molecular level. For measuring RNA binding preferences, we used data from two different technologies: RNA Bind-n-Seq and RNAcompete. For each RBP we implemented a deep learning model and use it to score RNAcompete probes to find the RNA binding preferences. In this project we aim to assign binding intensities to RNAcompete probes. We achieved this by implement an aggregation function over the model probability to produce a single binding score. 

