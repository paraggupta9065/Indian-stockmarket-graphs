from bsedata.bse import BSE
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time as t
stockLst = []
priceList = []
b = BSE()
i = 0


fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()



def animate(i):
    t.sleep(0.1)
    c = b.getQuote("500325")
    stockLst.append(float(c["currentValue"]))

    priceList.append(i)
    i += 1
    ax.clear()
    ax.plot(priceList, stockLst)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
