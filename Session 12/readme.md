Code Explanation:


1. Creating the customised weight initailization method to replicated the default initialization method in PyTorch.

```
def init_pytorch(shape, dtype=tf.float32, partition_info=None):
  fan = np.prod(shape[:-1])
  bound = 1 / math.sqrt(fan)
  return tf.random.uniform(shape, minval=-bound, maxval=bound, dtype=dtype)
```
Above is Kaiming He init - default weights initialization method used in PyTorch. This takes the inverse square root of the layer’s fan-in as a bound and then generates a random initial weight in the range [-bound, bound]. 

We customised this method for using it keras.

Reason:
One reason is this: different initializations lead to different scales (or, in math terms, vector norm) of the weights. For example, one method may init weights with random numbers like, 0.1, 0.2, etc., and another may init weights to be 10x bigger, like 1, 2, etc. In general, if you make a weight 10x as big, then its gradient will become 10x smaller, since calculus tells us that dy / d(10x) = dy/10dx. As a result, to get the same training results, you need to make your learning rate much bigger. In other words, if we use a different initialization method, we have to use different hyperparameters as well. That’s probably much harder than writing the above 3-line code.

2. Weight decay is upscaled to the batch_size and then multiplied with learning rate.
```
g += v * WEIGHT_DECAY * BATCH_SIZE
```

2. And the totally code is written in Tensorflow's keras and it is like PyTorch. DavidNet is orginally written in PyTorch which achieved 94% accuracy according to the author's (David C. Page) blog.

3. Tensorflow implementation turns out to be faster than PyTorch counter part in Colab K80 GPU according the author (David Yang) of the blog for tensorflow implementation.
