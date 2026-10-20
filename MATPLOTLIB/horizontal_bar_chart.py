# Matplotlib prgm2:  creating horizontal bar chart
import matplotlib.pyplot as plt
y= ['one','two','three','four','five']
x = [5,24,35,67,12]
plt.barh(y,x)
plt.ylabel("Pen sold")
plt.xlabel("Price")
plt.title("Horizontal barGraph")
plt.show()
