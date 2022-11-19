import pickle
im
 
 
 
 
 
 
with open("predict_population.pickle", mode="rb") as fp:
    model = pickle.load(fp)
model.predict(np.array([[130000]]))
