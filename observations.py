#THIS File just used for taking notes


def one():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 500
    optimizer = 'adam'
    num_epochs = 5
    batchSize = 32
    #
    #
    #
    #Result --> ETA for 1 epoch - 17:45 Acc = 0.1(1epoch)

def two():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 32
    optimizer = 'adam'
    num_epochs = 5
    batchSize = 32
    #
    #
    #
    #Result --> ETA for 1 epoch - 17:05 Acc = 0.09(1epoch)

def three():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 32
    optimizer = 'adam'
    num_epochs = 50
    batchSize = 128
    #
    #
    #
    #Result --> ETA for 1 epoch - 1:15 overall Acc = 0.15

def three():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 32
    optimizer = 'adam'
    num_epochs = 10
    batchSize = 32
    #
    #
    #take 25% of train and val data and discard the rest
    #
    #Result --> ETA for 1 epoch - 2:50 Acc = 0.15



def four():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 32
    optimizer = 'adam'
    num_epochs = 50
    batchSize = 32
    #
    #
    #take 25% of train and val data and discard the rest
    #with tf.device('/device:GPU:0'):
    #
    #Result --> ETA for 1 epoch - 0:20 Acc = 0.67

def five():
    fOrg = 0.5
    firstLayerFliterCount = 64
    conv_layers = 5
    activation = 'relu'
    denseSize = 32
    optimizer = 'adam'
    num_epochs = 50
    batchSize = 32
    #
    #
    #
    #with tf.device('/device:GPU:0'):
    #
    #Result --> ETA for 1 epoch - 0:52 Acc = 0.13(30 epochs)




