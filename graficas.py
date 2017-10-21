import matplotlib.pyplot as plt
import subprocess
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def Graficar(docs,images,videos,music,apps):
    labels= "Docs", "Images","Videos","Music","Apps"
    sizes = [docs["docs"],images["images"],videos["videos"],music["music"],apps["apps"]]
    explode = (0,0.1,0,0,0)

    fig1,ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
    ax1.axis("equal")
    plt.show()
    
def BarGraph(docs,images,videos,music,apps):
    objects = ("Docs","Images","Videos","Music","Apps")
    y_pos = np.arange(len(objects))
    total= docs["docs"]+images["images"]+videos["videos"]+music["music"]+apps["apps"]
    d =(docs["docs"]*100)/total
    i =(images["images"]*100)/total
    m = (music["music"]*100)/total
    v =(videos["videos"]*100)/total
    a =(apps["apps"]*100)/total
    print(d,i,v,m,a)
    performance = [d,i,v,m,a]
     
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Percentage')
    plt.title('Storage')
     
    plt.show()
