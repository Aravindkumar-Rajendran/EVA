What are Channels and Kernels (according to EVA)?

In a Pulao, the all the differnt ingredients like peas, clove, rice are channels. Kernel is actually a single piece of one ingredient.It is a feature extractor which finds the all other pieces in the whole item.



Why should we only (well mostly) use 3x3 Kernels?

Computationally effective.
* Uses less numbers of parameters.
* Hardwares are optimized for this kernel.

How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations)?

No. of times: n
    i = 199
    n=1
    while (i>1):
        print("|{0} x {0}| (3 x 3) ->".format(i),end=" ")
        i-=2
        n+=1
    print("|1 x 1|")
    print("No. of times: %d"%n)
