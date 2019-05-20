This is a python library that helps you generate a graph
of a TV series episode ratings.

The episode ratings are extracted from [OMDB](http://omdbapi.com/). You need an [API key](http://omdbapi.com/apikey.aspx).

## Useage Example
```python3
from tvgrapher import OMDBGrapher
x = OMDBGrapher('my omdb key (replace with yours)')
x.draw_graph('Game of Thrones')
x.draw_graph('Silicon Valley')
x.draw_graph('Narcos: Mexico')

```

### Results:

![Game of Thrones ratings graph](imgs/Game%20of%20Thrones.png?raw=true "Game of Thrones ratings graph")
![Silicon Valley ratings graph](imgs/Silicon%20Valley.png?raw=true "Silicon Valley ratings graph")
![Narcos: Mexico ratings graph](imgs/Narcos:%20Mexico.png?raw=true "Narcos: Mexico ratings graph")
