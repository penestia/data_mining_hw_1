""" Utility function for doing analysis on emotion datasets """
from collections import Counter, OrderedDict
import plotly.plotly as py
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


from wordcloud import WordCloud, STOPWORDS

def get_tokens_and_frequency(token_list):
    """obtain word frequecy from pandas dataframe column of lists"""
    counter = Counter(token_list)
    counter = OrderedDict(counter.most_common()) # sort by value
    tokens = counter.keys()
    tokens_count = counter.values()

    return tokens, tokens_count

def compute_frequencies(train_data, emotion, feature, frequency=True):
    """ compute word frequency for pandas datafram column of lists"""
    tokens =  train_data.loc[(train_data["emotions"] == emotion)][feature].values.tolist()
    tokens = [item for l in tokens for item in l]
    if frequency:
        return get_tokens_and_frequency(tokens)
    else:
        return tokens

###################################
""" Visualizing Functions """
###################################
def plot_word_frequency(word_list, plot_title):
    trace1 = {
        "x": list(word_list[0]),
        "y": list(word_list[1]),
        "type": "bar"
    }

    data = go.Data([trace1])

    layout = {
     
        "title": plot_title,
        "yaxis": {"title": "Frequency"}
    }

    fig = go.Figure(data = data, layout=layout)
    return fig

def plot_heat_map(plot_x, plot_y, plot_z):
    """ Helper to plot heat map """
    trace = {
        "x": plot_x,
        "y": plot_y,
        "z": plot_z,
        "colorscale": [[0.0, "rgb(158,1,66)"], [0.1, "rgb(213,62,79)"], [0.2, "rgb(244,109,67)"], [0.3, "rgb(253,174,97)"], [0.4, "rgb(254,224,139)"], [0.5, "rgb(255,255,191)"], [0.6, "rgb(230,245,152)"], [0.7, "rgb(171,221,164)"], [0.8, "rgb(102,194,165)"], [0.9, "rgb(50,136,189)"], [1.0, "rgb(94,79,162)"]],
        "type": "heatmap"
    }

    data = go.Data([trace])
    layout = {
        "legend": {
            "bgcolor": "#F5F6F9",
            "font": {"color": "#4D5663"}
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "xaxis1": {
            "gridcolor": "#E1E5ED",
            "tickfont": {"color": "#4D5663"},
            "title": "",
            "titlefont": {"color": "#4D5663"},
            "zerolinecolor": "#E1E5ED"
        },
        "yaxis1": {
            "gridcolor": "#E1E5ED",
            "tickfont": {"color": "#4D5663"},
            "title": "",
            "titlefont": {"color": "#4D5663"},
            "zeroline": False,
            "zerolinecolor": "#E1E5ED"
        }
    }

    fig = go.Figure(data = data, layout=layout)
    return fig

def get_trace(X_pca, data, category, color):
    """ Build trace for plotly chart based on category """
    trace = go.Scatter3d(
        x=X_pca[data.apply(lambda x: True if x==category else False), 0],
        y=X_pca[data.apply(lambda x: True if x==category else False),1],
        z=X_pca[data.apply(lambda x: True if x==category else False),2],
        mode='markers',
        marker=dict(
            size=4,
            line=dict(
                color=color,
                width=0.2
            ),
            opacity=0.8
        ),
        text=data[data.apply(lambda x: True if x==category else False).tolist()]
    )
    return trace
def plot_comp(wordlist1, wordlist2):

    category_counts = go.Bar(
        x=list(wordlist1[0]),
        y=list(wordlist1[1]),
        text=list(wordlist1[1]),
        name = 'total records',
        textposition = 'auto',
        marker=dict(
            color='rgb(255,0,0)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
            ),
        opacity=0.9
    )

    sample_category_counts = go.Bar(
        x=list(wordlist2[0]),
        y=list(wordlist2[1]),
        text=list(wordlist2[1]),
        name = 'samples',
        textposition = 'auto',
        marker=dict(
            color='rgb(58,200,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5)
                
            ),
        opacity=0.9
    )

    return category_counts, sample_category_counts

"""function not used in the notebook since I used the one with mask"""

from wordcloud import WordCloud, STOPWORDS

def plot_word_cloud(text):
    """ Generate word cloud given some input text doc """
    word_cloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000).generate(text)
    plt.figure(figsize=(12,9), dpi=300)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    
    
    
    
"""here I will create a  function that I will use for the wordcloud visualization"""    


def plot_word_cloud_mask(text, mask, in_stopwords):
  stopwords = set(STOPWORDS)
  for word in in_stopwords:
      stopwords.add(word)
  
  wc = WordCloud(background_color="white", max_words=2000, mask=mask,
                  stopwords=stopwords)
  # generate word cloud
  wc.generate(text)

  # show
  plt.figure(figsize=(12,9), dpi=300)
  plt.imshow(wc, interpolation='bilinear')
  plt.axis("off")
  
    

