import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
rent_data={
    'Name': ["Saalihah", "Kashan", "Shivangi", "Tanmay"],
    'Score': [90, 70, 80, 95]
}
df=pd.DataFrame(rent_data)
sns.barplot(x='Name',y='Score',data=df,palette='Set2')
plt.title("Rent")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
fruit_data={
    'Fruit': ["Mango", "Orange", "Grape", "Apple"],
    'Votes': [25,30,45,20]
}
df=pd.DataFrame(fruit_data)
sns.barplot(x='Fruit',y='Votes',data=df,palette='pastel')
plt.title("Favorite fruits")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
kids_data={
    'Name': ["Saalihah", "Kashan", "Shivangi", "Tanmay"],
    'Score': [90, 70, 80, 95]
}
import pandas as pd
df=pd.DataFrame(kids_data)
sns.barplot(x='Name',y='Score',data=df,palette='colorblind')
plt.title("Test Scores")
plt.show()