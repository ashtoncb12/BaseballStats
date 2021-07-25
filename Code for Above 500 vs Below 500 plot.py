import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
total = 0

df = pd.read_excel('Above and Below 500.xlsx')

for record in df['Above500']:
    split = str(record).split('-')
    record1 = int(split[0]) / (int(split[0]) + int(split[1]))
    df.replace(to_replace = record, value = record1, inplace = True)
  
for score in df['Below500']:
    if type(score) != type('yankees suck'):
        pass
    else:
        split1 = str(score).split('-')
        record2 = int(split1[0]) / (int(split1[0]) + int(split1[1]))
        df.replace(to_replace = score, value = record2, inplace = True)

print(df)
graph = sns.regplot(x = 'Below500', y = 'Above500', data = df)

for team in df['Team']:
    arr_img = plt.imread(team + '.png')
    imagebox = OffsetImage(arr_img, zoom = 0.02)
    ab = AnnotationBbox(imagebox, [(df.loc[df[df['Team']==team].index.values]['Below500']), 
                                   (df.loc[df[df['Team']==team].index.values]['Above500'])])
    graph.add_artist(ab)

#white socks
graph.annotate("White Sox", (df.loc[df[df['Team']=='Chicago White Sox'].index.values]['Below500'],
                             df.loc[df[df['Team']=='Chicago White Sox'].index.values]['Above500']),
               xytext = (df.loc[df[df['Team']=='Chicago White Sox'].index.values]['Below500']-0.015,
                             df.loc[df[df['Team']=='Chicago White Sox'].index.values]['Above500']+0.05), 
               arrowprops = dict(arrowstyle = '->'),
               size = 5)
graph.set_title('Win % against >=.500 teams vs. win % against <.500 teams')
graph.set_xlabel('Win % against <.500 teams')
graph.set_ylabel('Win % against >=.500 teams')
plt.show()