# Matplotlib prgm1: create a vertical bar  graph 
import matplotlib.pyplot as plt
x= ['one','two','three','four','five']
y = [5,24,35,67,12]
plt.bar(x,y)
plt.xlabel("Pen sold")
plt.ylabel("Price")
plt.title("Vertical Bar Graph")
plt.show()
