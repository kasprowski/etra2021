'''
Module using sklearn package to classify samples
@author: pawel@kasprowski.pl
'''

import cl_models
import matplotlib.pyplot as plt
import numpy as np

def classification(model_name,samples,labels,rangex,rangey):
    samples = np.array(samples)
    labels = np.array(labels)

    #available models from cl_models.py    
    nnmodels = {
        "PERCEPTRON": cl_models.perceptron(),
        "HIDDEN": cl_models.hidden_linear(),
        "HIDDEN_SIGMOID": cl_models.hidden_sigmoid(),
        "HIDDEN_RELU": cl_models.hidden_relu()
    }
    model = nnmodels.get(model_name)
    model.compile(loss='binary_crossentropy', optimizer="adam",metrics=['accuracy'])
    print(samples.shape)
    print(labels.shape)
    
    # fit model
    EPOCHS = 100
    H = model.fit(samples, labels, epochs=EPOCHS,batch_size=10)    

    result = np.zeros([rangex,rangey])
    samples = []
    for x in range(rangex):
        for y in range(rangey):
            samples.append((x,y))
    samples = np.array(samples)
    r = model.predict(samples)
               
    for i in range(len(samples)):
       result[samples[i,0],samples[i,1]]=r[i]
    
#     print(H.history)
#     N = np.arange(0, EPOCHS)
#     plt.style.use("ggplot")
#     plt.figure()
#     plt.plot(N, H.history["loss"], label="train_loss")
#     plt.plot(N, H.history["accuracy"], label="train_acc")
#     plt.title("Training Loss and Accuracy")
#     plt.xlabel("Epoch #")
#     plt.ylabel("Loss/Accuracy")
#     plt.legend()
#     plt.show()

    return result            
        

