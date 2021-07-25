import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

era_data = pd.read_excel('average_era_allstarbreak.xlsx')
rpg_data = pd.read_excel('rpg_allstarbreak.xlsx')

combo = pd.merge(era_data, rpg_data, on='Team')
combo.drop(combo[combo['Team']=='League Average'].index.values, inplace = True)
graph = sns.regplot(x='ERA',y='Runs/Game',data = combo)

#add images
for team in combo['Team']:
    arr_img = plt.imread(team + '.png')
    imagebox = OffsetImage(arr_img, zoom = 0.02)
    ab = AnnotationBbox(imagebox, [(combo.loc[combo[combo['Team']==team].index.values]['ERA']), 
                                   (combo.loc[combo[combo['Team']==team].index.values]['Runs/Game'])])
    graph.add_artist(ab)
    
#seattle marinaras
graph.annotate("Mariners", (combo.loc[combo[combo['Team']=='Seattle Mariners'].index.values]['ERA'], 
                            combo.loc[combo[combo['Team']=='Seattle Mariners'].index.values]['Runs/Game']),
               xytext = (combo.loc[combo[combo['Team']=='Seattle Mariners'].index.values]['ERA'], 
                            combo.loc[combo[combo['Team']=='Seattle Mariners'].index.values]['Runs/Game'] -0.5),
               arrowprops = dict(arrowstyle = '->'))
#walgreens
graph.annotate("Nationals", (combo.loc[combo[combo['Team']=='Washington Nationals'].index.values]['ERA'],
                             combo.loc[combo[combo['Team']=='Washington Nationals'].index.values]['Runs/Game']),
               xytext = (combo.loc[combo[combo['Team']=='Washington Nationals'].index.values]['ERA'] -0.3,
                             combo.loc[combo[combo['Team']=='Washington Nationals'].index.values]['Runs/Game']-0.3), 
               arrowprops = dict(arrowstyle = '->'))
plt.title("Runs/Game vs. ERA")
plt.show()
plt.savefig("Runs/Game vs ERA Graph.png")