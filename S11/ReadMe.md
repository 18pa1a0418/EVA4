## S11
*. Goals of assignment:
1. Plotting triangular plot, writing new architecture, Implementing transformations like padding,randomcrop,flipLR and cutout, implementing LR range test and achieving 90% accuracy.

#### Triangular plot
*. This is the triangular plot
*. ![](https://github.com/Lakshman511/EVA4/blob/master/S11/Images/triangular_plot.png)



*. [this](https://github.com/Lakshman511/EVA4/blob/master/S11/Eva4library/plots.py) to the code of triangular plot


### Model
[this](https://github.com/Lakshman511/EVA4/blob/master/S11/Eva4library/eva4models11.py) the link to the code of new model named ResNetforS11.

#### LR range test
*. performed lr range test.
*. ![](https://github.com/Lakshman511/EVA4/blob/master/S11/Images/lr_range_test.png)


*. [this](https://github.com/Lakshman511/EVA4/blob/master/S11/Eva4library/eva4lr_range_test.py) link to the file of lr range test.
*. In lr range test i started the model from 0.0001 and increased the learning rate to 1 using stepLr.Thus I found the maxlr. I considered 1/10 th of mqx_lr as minlr.

### [code1](https://github.com/Lakshman511/EVA4/blob/master/S11/Eva4_S11.ipynb)


*. In the above code I achieved 90% accuracy.

### [code2](https://github.com/Lakshman511/EVA4/blob/master/S11/Eva4_S11_2.ipynb)
*. In the above file achieved 84% accuracy but here produced all visualisations.
*. Achieved maxlr at epoch 5.
![](https://github.com/Lakshman511/EVA4/blob/master/S11/Images/lr.png)
