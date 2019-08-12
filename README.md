**Bee Image Classification using a CNN to determine presence of Varroa mites**

## Problem Statement:
Beekeepers must face a myriad of threats to their hives. The _Varroa (pronounced "vr-ow-uh") destructor_, or more commonly the _varroa mite_, is a natural predator to honey bees and is one of the biggest pests plaguing the bee keeping community. The sooner a keeper can begin treating for _varroa_, the less likely a [colony collapse](https://ipm.missouri.edu/MPG/2013/7/Colony-Collapse-Disorder-the-Varroa-Mite-and-Resources-for-Beekeepers/) will occur.  Early detection could mean the difference between a healthy hive and a dead one. 

We plan to create such an early detection tool by using the dataset from the [Honey Bee Annotated Image Dataset](https://www.kaggle.com/jenny18/honey-bee-annotated-images) found on Kaggle. With these annotated images, we will train a Convolutional Neural Network to classify bee images as having _varroa mites_ or not (binary classification).

A _varroa mite_ infestation can be fatal, therefore we consider falsely classifying a bee image as "healthy" could be disastrous. Therefore, recall, or sensativity, will be our metric for model selection.

## Risks & assumptions:
While creating this predictive model, we must make certain assumptions, which bear consideration.

The neural network will be trained using the provided annotated images. Regardless of how well the model classifies a bee image from the training data, classifying real world images is the true goal. Inherently, we assume the given dataset resembles bee images 'in the wild', which is a generous assumption to make.

Additionally, one of the largest assumptions we're making is to assume that bee class (worker, drone, queen), location, date and time, and bee species are all irrelevant factors in determining if a bee image can be properly categorized. There is a practical need for this assumption, however; the model's classification needs to be based solely on a user's image 'in the field' and therefore without these features. So, it only makes practical sense to train the model under these limited conditions.

Source Documentation
- [Honey Bee Annotated Image Dataset (Kaggle)](https://www.kaggle.com/jenny18/honey-bee-annotated-images)