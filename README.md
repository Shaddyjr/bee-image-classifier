# Bee Image Classification using a CNN to determine presence of Varroa mites

#### Author: Mahdi Shadkam-Farrokhi: [Medium](https://medium.com/@mahdis.pw) | [LinkedIn](https://www.linkedin.com/in/mahdi-shadkam-farrokhi-m-s-8a410958/) | [mahdis.pw](http://mahdis.pw)

<img src="./images/bee.png" width="200"/>

#### This project is featured in a Medium post: ["Bee Image Classification using a CNN and Keras"](https://medium.com/@mahdis.pw/bee-image-classification-using-a-cnn-and-keras-5fd5ed90a37b)

#### The Jupyter Notebook for this project can be found within [code/project_notebook.ipynb](./code/project_notebook.ipynb)

#### A practical application of our best CNN can be found [here](https://bee-classifier.herokuapp.com) (it may take a moment to spin up)

## Problem Statement
Honey bees contribute nearly $20 billion to the value of U.S. crop production. Meanwhile, beekeepers continue to lose up to 45 percent of their hives annually. Among the myriad of threats to their hives, beekeepers must continually monitor for the _varroa_ pest. The _Varroa (pronounced "vr-ow-uh") destructor_, or more commonly the _varroa mite_, is a natural predator to honey bees and is one of the biggest pests plaguing the bee keeping community. The sooner a keeper can begin treating for _varroa_, the less likely a [colony collapse](https://ipm.missouri.edu/MPG/2013/7/Colony-Collapse-Disorder-the-Varroa-Mite-and-Resources-for-Beekeepers/) will occur. Early detection could mean the difference between a healthy hive and a dead one. 

With the dataset from the [Honey Bee Annotated Image Dataset](https://www.kaggle.com/jenny18/honey-bee-annotated-images) found on Kaggle, we will train a Convolutional Neural Network (CNN) to classify bee images as having _varroa mites_ or not (binary classification). Such a model could serve as a practical early detection system for beekeepers. We will use accuracy to select our best model.
## Executive Summary
We used the dataset from the [Honey Bee Annotated Image Dataset](https://www.kaggle.com/jenny18/honey-bee-annotated-images) to train a CNN using various model compositions - including 1) unaltered image data, 2) rotating and mirroring the data, and 3) rotating + mirroring as well as altering image brightness. Transforming image data has been known to help make a more robust CNN.

Overall, we faced a number of challenges attempting to address this problem. We had a dataset with a relatively small sample size, having less than 4,500 images. Well established norms in image classification suggests having tens of thousands of observations in order to have confidence in a trained model. Another confounding factor came from the source of our target variable; all of the images of _varroa_ bees came from the same location, and likely the same beekeeper, which inherently factored bias into our model. 

Other issues arose from the images themselves. Almost every image had a unique width and height, which forced us to rescale and standardize each image. This invariably lead to some loss of data quality. Lastly, after looking at many of these images directly, it was clear many did not clearly depict a complete bee. For example, some images simply featured a shadow, while others featured only parts of bees. Many others were found to be too blurry to be human readable. Taking these factors into perspective, it was difficult to discern if the model would perform well on new real-world images.

There were some interesting trends that came to light. One clearly important aspect of the images turned out to be the background color. Even in our best model, we found images with a background similar in color to the bee proved difficult for the model to properly classify. When looking at convolutional layers, we found the background pixels were a significant factor forming the network's classification output.

Lastly, as a way of connecting our findings to a practical application, we created a [Bee Classifier mobel web appliction](https://bee-classifier.herokuapp.com). Beekeepers can use this application from their desktops or mobile devices at their convenience. This "proof of concept" is the direct manifestation of our best CNN in action, and could be used to further validate and test the model using real world data.

## Conclusion
We were able to successfully train a CNN to perform better than the baseline model of 76.3% accuracy. In all, __our best performing model was the Brightness Transformation Model at 98.9% training accuracy and 99.5% testing accuracy__. This model featured a high overall accuracy with a few reasonable missclassifications. The convolutional layers also show evidence the model is using _varroa_ detection to inform image classification, giving us confidence the model would perform well in the field. There is a caveat with using this model, however - for best results, images should have backgrounds that contrast well with the bee.

This model was built using a number of assumptions, which we should remain mindful of. First and foremost, we used a dataset with a substantially small sample size. This CNN was trained using 3/4ths of the total 4,400 images - a paultry number considering most image classifiers are trained with tens or even hundreds of thousands of images in order to gain confidence in the model. Additionally, only a single location, and likely only a single beekeeper, was responsible for our observations of interest, bees with _varroa mite_, which unavoidably introduces bias into our model.

Lastly, the images were inconsistent for a number of reasons. We had to rescale almost every image to a standard size of 54x50, which inevitably reduced data quality. There were also a number of images which we found to be too blurry or out of focus for human comprehension. Training the model with these garbled images could have hampered the model's accuracy.

## Recommendations
We would recommend revisiting this problem with a more robust 20k+ observation dataset of annotated bee images with each image having the same height and width. 

Additionally, we created [a Bee Classifier mobile web application](https://bee-classifier.herokuapp.com)  using the Brightness Transformation model, which users can use to classify images of a single bee. Such an application could be used to validate and test this model in a production-like setting.

Lastly, it's important to think practically about the problem at hand. It's impractical to expect beekeepers to painstakingly photograph individual bees and feed those images into our model. It's much more intuitive to take a single photo of a group of bees and use that instead. Therefore, a more realistic solution to the problem would be 2-fold:
1. First, a CNN could be trained to recognize and crop individual bee images out of a large single image, provided by the beekeeper
2. Then, those individual images are fed into another CNN, like the one we modeled. The images are classified and the beekeeper is given the percentage of bees found to have _varroa mite_.


## Source Documentation
- [Bee Classifier Application (proof of concept)](https://bee-classifier.herokuapp.com)
- [Honey Bee Annotated Image Dataset (Kaggle)](https://www.kaggle.com/jenny18/honey-bee-annotated-images)
- [Jeremy Jordan on 'Normalizing your data'](https://www.jeremyjordan.me/batch-normalization/)
- [Gabriel Pierobon's post on 'Visualizing intermediate activation in Convolutional Neural Networks with Keras'](https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0)
- [Custom `ImageHandler` class demo](./image_handler/ImageHandler.py)
- [`ImageHandler` Documentation](./ImageHandler_doc.ipynb)
