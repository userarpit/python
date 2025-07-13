import pandas as pd

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["BCA", "BCA", "M.Tech", "BCA"],
		'score':[90, 40, 80, 98]}


df = pd.DataFrame(dict, index = [0, 1, 2, 3])

print(df.truncate(before=1,after=2))