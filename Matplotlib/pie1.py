import numpy as np
import matplotlib.pyplot as plt

pie_labels=['Maths','Science','English','Biology']
pie_values = [20,45,30,5]
explode_values = (0.0,0.0,0.0,0.3)
plt.pie(pie_values,labels=pie_labels,autopct='%0.1f%%',rotatelabels=True,pctdistance=0.50,
        startangle=90,shadow=True,explode=explode_values,colors=['b','c','g','k'],
        textprops={'size': 'smaller'},radius=0.70)
plt.style.use('ggplot')
plt.show()