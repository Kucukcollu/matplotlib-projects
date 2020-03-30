from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

years = [1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018]

python = [0,0,0,0,0,0,3.61,4.79,6.49,8.04,10.10,12.24,13.66,17.52,23.10]

plt.plot(years, python, color="r", marker="x",label="Python")

cpp = [16.78,20.23,20.31,17.83,15.19,12.90,11.25,11.44,11.92,12.54,11.34,9.27,8.48,7.37,6.81]

plt.plot(years, cpp,color="b", marker="o", label="C++")

c = [57.13,70.91,71.23,60.10,47.58,32.06,19.64,13.43,12.12,12.62,10.26,7.88,7.21,6.18,5.56]

plt.plot(years, c, color="g", marker="*",label="C")

plt.xlabel("Years")
plt.ylabel("Percentage(%)")
plt.title("Programming Languages From 1980 to 2019")


plt.legend()
plt.tight_layout()
plt.savefig("rankings.png")
plt.show()
