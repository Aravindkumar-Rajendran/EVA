## Architectural Basics:

Order is like applying from top to bottom in the algorithm development process

1. Image Normalization,

   Image Normalization is an input normalization for the image input. It scales down the pixel values between 0 and 1 by dividing with 255.

   

2. Receptive Field, 

   This is the term defines amount or size of the input taken into account while doing convolution operations. Suppose the size of the image is 18 x 18 -> After convolution with 3 X 3 - receptive field is 3 X 3 -> second convolution 5 X 5 i.e. this convolution kernel learns from 5 X 5 of the input.  Global receptive field in the end of the convolution layers should be equal or slightly less than the size of the input image to get better performance from the model. 

   

3.  3x3 Convolutions, 

   This convolution is most preferred kernel for the CNN models as it requires less parameters then bigger size kernels and optimized in the hardware for faster execution.  

   

4. Batch Normalization, 

   Batch Normalization scales down the values of the input layer to the values between -1 and 1, thus improving the speed of model and reduces the complexity of the deep learning algorithms.

   

5. DropoutDropout layer is used to reduce the overfitting. 

   It works by randomly dropping out the neurons while training and making the other neurons robust enough to catch up the loss by the drop.

   

6. When do we introduce DropOut, or when do we know we have some overfitting.

   Overfitting occurs in the training of the machine algorithm  while the model fits and performance better with the training data and troubles with new data. Dropout can reduce the problem of overfitting and it is introduced in after the convolution layers.

   

7. The distance of MaxPooling from Prediction, 

   Distant of 2 or 3 convolution layers.

   

8. The distance of Batch Normalization from Prediction, 

   Before 1 convolution layer and not before prediction.

   

9. When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

   When we reach the required global receptive field or nearer to that, we can stop convolutions and go ahead with a larger size kernel to shrink down the output.



10. How many layers,

     The number of layers that we need to use to the neural network architecture, depends upon the global receptive field to be achieved in the last layer.



11. Kernels and how do we decide the number of kernels?

    Choosing the kernel does not have any standardized ways but the best practice is to choose it incrementally up to the pooling layer and decreasing after pooling then continuing incrementally up to another pooling layer so that the model can learn more from the previous one.



12. MaxPooling, 

    MaxPooling is the operation of downsampling the input by taking the maximum values i.e. useful things out of all, in order to reduce the size of input that reduce the parameters needed to be trained.



13. Position of MaxPooling, 

    MaxPooling layers should be placed 2 or 3 layer after the input and 2 or 3 layer before the output. And as required in the middle, between at least 2 convolution layers.



14. Concept of Transition Layers, 

    Transition layers concept is to form a block in which the convolution kernel numbers increases up to the pooling layer and falls back to the initial level then increases up to next pooling layer. The block of pooling layer with 1X1 kernel which reduces the number of channels is we call as transition block. 

    

15. Position of Transition Layer, 

    Placed after the completion of every convolution block.

    

16. 1x1 Convolutions, 

    This convolution (kernel) does not change dimensions of the output from input but just multiplies the value of weight with pixel values and maintain same spatial structure. It is used to reduce the channel size as it merges the channels to form the required size. 

    

17. Global Average pooling

    Used just before prediction (SoftMax) which takes all the pixels in the output of previous layer and gives the average of the all the pixels in a single channels as the output. 

    

18. SoftMax

    SoftMax is not a probability, but probability like function which amplifies the max value in the before layer and suppresses the other values. Used in most of the cases were single output is needed. Like output of single animal as Lion in the classification of total cat family.

    

19. Learning Rate, 

    It  is the rate at which the optimizer tweaks the weights of the model to reduce the loss and to improve the accuracy. It is one of the important hyperparameters in the machine learning algorithms that is chosen arbitrarily and can be tweaked and tuned to improve the performance.



20. Number of Epochs and when to increase them, 

    Number of epochs depends upon the architecture of the model. We have to see, there are parameters in the model that could still improve or it attained the max state by viewing the accuracy of the epochs (i.e. watching the convergence of the network)



21. Batch Size, and effects of batch size

    Batch size is the number of images send to the model in one forward pass and then a backpropagation. Larger the batch size requires the large space in the hardware and improves the performance of the model and speed of the training.

    

22. When to add validation checks

    To see to improvement of the model for every epoch, we can add the validation checks. In larger dataset, we can divide the divide the data into training data and validation data to make the validation separate from the test data.

    

23. LR schedule and concept behind it

    LR schedule reduces the value of the learning rate after every epoch thus improves the performance of optimization and speed of the training.



24. Adam vs SGDAdam vs Stochastic gradient descent optimizers. Adam gives the better accuracy than that of SGD.

    

25. How do we know our network is not going well, comparatively, very early

    By seeing the improvement of accuracy in the first four epochs.

