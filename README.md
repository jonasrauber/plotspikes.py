# plotspikes.py
A minimal python function for beautiful spike plotting because spikes should be plotted like this:
```python
plotspikes(spiketimes) # see example.py
```
![Beautiful spike plotting using plotspikes.py](images/example.png)

And **not** like this:
```python
plt.plot(spiketimes, -2.5 * np.ones(len(spiketimes)), 'o') # see ugly.py
```
![Ugly spike plotting using dots](images/ugly.png)
