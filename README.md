**Bee Image Classification using a CNN to determine presence of Varroa mites**

#### Author: Mahdi Shadkam-Farrokhi: [GitHub](https://github.com/Shaddyjr) | [Medium](https://medium.com/@mahdis.pw) | [LinkedIn](https://www.linkedin.com/in/mahdi-shadkam-farrokhi-m-s-8a410958/) | [mahdis.pw](http://mahdis.pw)

![](./images/bee.png)

#### This project is featured in a Medium post: ["Bee Image Classification using a CNN and Keras"](https://medium.com/@mahdis.pw/bee-image-classification-using-a-cnn-and-keras-5fd5ed90a37b)

## Problem Statement
Beekeepers must face a myriad of threats to their hives. The _Varroa (pronounced "vr-ow-uh") destructor_, or more commonly the _varroa mite_, is a natural predator to honey bees and is one of the biggest pests plaguing the bee keeping community. The sooner a keeper can begin treating for _varroa_, the less likely a [colony collapse](https://ipm.missouri.edu/MPG/2013/7/Colony-Collapse-Disorder-the-Varroa-Mite-and-Resources-for-Beekeepers/) will occur. Early detection could mean the difference between a healthy hive and a dead one. 

With the dataset from the [Honey Bee Annotated Image Dataset](https://www.kaggle.com/jenny18/honey-bee-annotated-images) found on Kaggle, we will train a Convolutional Neural Network (CNN) to classify bee images as having _varroa mites_ or not (binary classification). As a general metric, we will use accuracy to select our best model.

## Executive Summary
After an initial model using the raw image data, we thought to explore different ways to transform the data to yield better results. After rotating and mirroring the data and even altering the brightness, we eventually settled on the original model. Transforming the data usually helps make a more robust CNN, however, we found it to be a slight hinderence by causing more missclassifications.

Our best model showed a __99.3% accuracy__ on the testing dataset. Although this sounds compelling, there are a number of considerations that must be taken into account in order to better understand this score.

First, we must acknowledge the substantially low sample size of this dataset, having less than 4,500 images. Well established norms in image classification suggests having tens of thousands of observations in order to have confidence in a trained model. Surprisingly, the images of _varroa_ bees all came from the same location, and likely the same photographer. This inherently factors bias into our model. 

Other issues arose from the images themselves. Almost every image has a unique width and height, which forced us to rescale and standardize each image. This invariably lead to a loss of data quality. Lastly, after looking at many of these images direclty, it was clear many did not properly depict a complete bee. For example, some images simply featured a shadow, while others featured only parts of bees. Others were simply too vague to even be human readable. Taking these factors into perspective, it's difficult to discern if the model would perform well outside of this dataset.
## Conclusions and Recommendations

### Conclusion
We were able to successfully train a CNN to perform better than the baseline model of 76.3%. In all, __our best performing model was the No Transformation Model at 99.3% accuracy__. This model featured the most reasonable errors with the highest overall accuracy and fewest missclassifications.

There are caveats to using it, however. To optimize this model's effectiveness, images of the yellow/orange patterned honey bees work best. Additionally, the photographer should be mindful to photograph the entire bee and avoid backgrounds with a similar hue to the bees being photographed.

### Assumptions
This model was built using a number of assumptions, which we should remain mindful of. First and foremost, we used a dataset with a substantially small sample size. This CNN was trained using 3/4ths of the total 4,400 images - a paultry number considering most image classifiers are trained with tens or even hundreds of thousands of images in order to gain confidence in the model. Also, we had to rescale almost every image to 54x50, which inevitably reduced data quality.

Only a single location, Athens, Georgia, was responsible for our observation of interest, bees with _varroa mite_, which unavoidably introduces bias into our model. These bees also mostly come from the same bee subspecies, making it impossible to correctly block for during the train/test split.

Lastly, there were a number of images which we found to be too blurry or out of focus for even a human to assess, yet, the model "correctly" classified such garbled images. This may suggest the model is using more than _varroa_ detection to classify images, making it less likely be to capable of classifying real-world images.

### Recommendations
We would recommend revisiting this problem with a more robust 20k+ observaton dataset of annotated bee images such that each image has the same height and width. 

Also, it might be best to train a model specifically for each subspecies. In a real world scenario, this would allow beekeepers to select the model most optimized for their hives.

Lastly, it's important to think practically about the problem at hand. It's impractical to expect beekeepers to painstakingly photograph individual bees and feed those images into our model. It's much more intuitive to take a single photo of a group of bees and use that instead. Therefore a more realistic solution to the problem would be 2-fold:
1. First, a CNN could be trained to recognize and crop individual bee images out of a large single image, provided by the beekeeper
2. Then, those individual images are fed into another CNN, like the one we modeled. The images are classified and the beekeeper is given the percentage of bees found to have _varroa mite_.

## Source Documentation
- [Honey Bee Annotated Image Dataset (Kaggle)](https://www.kaggle.com/jenny18/honey-bee-annotated-images)
- [Jeremy Jordan on 'Normalizing your data'](https://www.jeremyjordan.me/batch-normalization/)
- [Gabriel Pierobon's post on 'Visualizing intermediate activation in Convolutional Neural Networks with Keras'](https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0)
- [Custom `ImageHandler` class demo](./image_handler/ImageHandler.py)
- [`ImageHandler` Documentation](./ImageHandler_doc.ipynb)