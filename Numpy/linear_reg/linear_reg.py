import numpy as np

x = np.array([1,2,3,4,5],dtype=float)

y = np.array([35,45,55,70,75],dtype=float)

# line = wx + b
# these are the blind guess initially
w = 0
b = 0  

learning_rate = 0.05
epochs = 1000

for epoch in range(epochs):
    y_pred = w * x + b
    error = y_pred - y
    loss = np.mean(error**2)
    dw = 2*np.mean(error * x)    #slope of w
    db = 2*np.mean(error)
    w = w - learning_rate * dw
    b = b - learning_rate * db 
    if epoch % 100 == 0:
        print(f"Epoch {epoch:4d} | loss = {loss:4f} | w = {w:4f} | b = {b:4f}")

print(f"Final line: marks = "
f"{w:.2f} * hours + {b:.2f}")
print(round(w * 6 + b, 1))