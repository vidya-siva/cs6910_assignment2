# Question 1-3
Git clone the whole repo cs6910_assignment2 for it to function

please pip install the packages required.

```
python -m pip install -r requirements.txt
```

Place the Inaturalist Dataset in the parent folder. 

to run the code, cnn_train.py does not sweep, values are hardcoded 
```
python cnn_train.py
```


Following is the sweep parameters used in PartA_1-3.ipynb file. you can use the colab [link](https://colab.research.google.com/drive/1ULbj1_DO_b9Jkok7Yk0Y_E5RofzO8riH?authuser=1#scrollTo=DOqHjP4pKvOQ)

```
sweepMethod ='bayes'
sweepConfig = {'name': sweepMethod + '-test-sweep',
                'method': sweepMethod,
                'metric' : {'name': 'val_acc', 
                            'goal': 'maximize'}
                }
  parameters = {
      
      'filterOrganisation' : {'values': [2,1,0.5]},
      'firstLayerFliterCount' : {'values': [64,32]},
      'convLayers' : {'values': [5]},
      'activation' : {'values': ['relu']},
      'denseSize' : {'values': [32,64,128]},
      'optimizer' : {'values': ['adam']},
      'num_epochs' : {'values': [10,20]},
      'kernelSize' : {'values': [3]},
      'dropOut' : {'values': [0.3,0.5]},
      'batchNorm' : {'values': [0,1]},
      'isDataAug' : {'values': [0,1]},
  }
```


#question4
to run the code, or use colab [link](https://colab.research.google.com/drive/1oNRyg8qz0XpHL27uw5DhBqlKoBUTQ4u6?authuser=1)
Download this model and put it in the same dir, of colab put it in MyDrive
```
python partA_4.py
```


