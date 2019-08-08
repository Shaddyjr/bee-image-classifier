## Overview:
After confirmation with my instructor, I've chosen the following project:  

**Bee Image Classification using a CNN to determine presence of Varroa mites**

<img src='bee.jpg' />

## Problem Statement:
Of the [many likely causes](https://www.sciencenewsforstudents.org/article/why-are-bees-vanishing-pesticides-disease-other-threats) behind the drastic decline in the honey bee population, the _Varroa (pronounced "vr-ow-uh") destructor_, or more commonly the _varroa mite_, is among the top contributors. As a natural predator to honey bees, the varroa mite is one of the biggest pests plaguing the bee keeping community. 


While small, these mites are difficult for bees to deal with. However, bee keepers can employ a number of treatments to help rid a hive of a varroa infestation. The sooner a bee keeper can begin treatment, the less likely a [colony collapse](https://ipm.missouri.edu/MPG/2013/7/Colony-Collapse-Disorder-the-Varroa-Mite-and-Resources-for-Beekeepers/) will occur.

Having an tool to quickly assess a colony's health could mean the difference between a healthy hive and a dead one. I plan to create that tool using the dataset from the [Honey Bee Annotated Image Dataset](https://www.kaggle.com/jenny18/honey-bee-annotated-images) found on Kaggle.

Using this dataset, I will use a Convolutional Neural Network to create a predictive model to determine if a bee image shows evidence of varroa mites or not (binary classification).

A bee hive with a varroa mite infestation can quickly end up dead from varroa collapse. As such, falsely classifying an image as clear could be disastrous. Therefore, recall, or sensativity, will be the metric I use for model selection.

Given my subject matter knowledge and comfort with neural networks, I'm confident this project is achievable and appropriatley scoped. Additionally, the main driving force behind this project stems from my contact with the [NYC Beekeeping organization](http://nycbeekeeping.org). The founder of the group explicitly expressed a need for just such an application. I hope to show a proof of concept that would set the foundation for a mobile application - beekeepers anywhere could use this tool to quickly assess their hives for varroa infestation.

I plan to have this project completed on time, if not before, August 23rd, 2019.

__My preliminary Exploratory Data Analysis can be found [here](./Preliminary%20EDA.ipynb)__

## Risks & assumptions:
While creating this predictive model, I must make certain assumptions, which bear consideration.

As I mentioned, the metric I will use is recall, which often results in a reduction of false negatives for an increase in false positives. The risk of falsely classifying an infected bee as healthy is, in my opinion, more serious than a false positive. However, there may be cases where this assumption is invalid. 

Additionally, the neural network will be trained using the provided annotated images. Regardless of how well the model classifies a bee image from the training data, classifying real world images is the true goal. Inherently, I must assume the given dataset resembles bee images 'in the wild', which is a generous assumption to make.

One of the largest assumptions I'm going to make is to assume the given annotations are irrelevant to descerning whether a bee is suffering from varroa mites or not. That is to say, bee class (worker, drone, queen), location, date and time, and bee species are all irrelevant factors in determining if a bee image can be properly categorized. There is a practical need for this assumption, however; I envision making classifications based solely on a user's image 'in the field' and therefore without these features. So, it only makes practical sense to train the model under these limited conditions.

Source Documentation
- [Honey Bee Annotated Image Dataset (Kaggle)](https://www.kaggle.com/jenny18/honey-bee-annotated-images)