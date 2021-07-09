from matplotlib import pyplot

a = [1,2,5,6,9,11,15,17,18]
fig, ax = pyplot.subplots(figsize=(12,2.5))
ax.get_yaxis().set_visible(False)
ax.hlines(0,a[0]-2,a[len(a)-1]+2, colors='k')
ax.set_xticks(range(a[0]-2,a[len(a)-1]+3))
ax.plot(a, [0]*len(a), 'o', color='b');
pyplot.show()
