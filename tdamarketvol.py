import numpy               as np
import gudhi               as gd
import pandas              as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from persim import PersLandscapeExact
from persim.landscapes import plot_landscape_simple

#get market data
snp = pd.read_csv("my-path/S&P_500_daily_1995_2025.csv", header=[0,1,2], sep = ',')
nasdaq = pd.read_csv("/my-path/NASDAQ_daily_1995_2025.csv", header=[0,1,2], sep = ',')
russell = pd.read_csv("/my-path/Russell_2000_daily_1995_2025.csv", header=[0,1,2], sep = ',')

tickers = {
    0 : snp,
    1 : nasdaq,
    2 : russell
}

# create point clouds: for each index, and trading day, calculate the log returns. Point clouds are a set interval of days (window) and all 3 markets' log returns.
total_trading_days = len(snp.iloc[:,0])
logret_days = np.zeros((total_trading_days,3))
#initialize matrix of logreturn per day for each index

for day in range(total_trading_days):
    for ticker in tickers:
        open = tickers[ticker].iloc[day,4]
        close = tickers[ticker].iloc[day,1]
        logreturn = np.log(close/open)
        logret_days[day, ticker] = logreturn

#logret_days is our matrix with columns corresponding to each index according to the hash "tickers", and row i corresponding to the log return of that index for day i.
w = 100
#w = 50
clouds = total_trading_days - w
finalplot = np.zeros((clouds, 3))

for cloud in range(clouds):
    D = logret_days[cloud:cloud+w,:]
    D_dist = squareform(pdist(D, metric = 'euclidean'))
    #compute the Vietoris-Rips complex of each point cloud and create our simplex trees, and record our Betti numbers in the form of a persistence diagram diag_1.
    rips_complex_of_cloud = gd.RipsComplex(distance_matrix = D_dist,max_edge_length = 1)
    simplex_tree = rips_complex_of_cloud.create_simplex_tree(max_dimension=2)
    diag_1 = simplex_tree.persistence()


#CONVERT TO PERSISTANCE LANDSCAPE, record the L1, L2 norms of each landscape.
    diag_H1 = np.array([pt[1] for pt in diag_1 if pt[0] == 1])
    #filter out trivial birth-death pairs
    if diag_H1.ndim == 2 and diag_H1.shape[0] > 0:
        persistence = diag_H1[:,1] - diag_H1[:,0]
        mask = persistence > 1e-10
        diag_H1 = diag_H1[mask]
    #make sure diag_H1 is non-empty
    if diag_H1.ndim != 2 or diag_H1.shape[0] == 0:
        l1norm = 0.0
        l2norm = 0.0

    else:
        plH1 = PersLandscapeExact([diag_H1])
        l1norm = plH1.p_norm(p=1)
        l2norm = plH1.p_norm(p=2)

    finalplot[cloud][0] = cloud
    finalplot[cloud][1] = l1norm
    finalplot[cloud][2] = l2norm

#plot the graph of time versus the L1, L2 norms of our persistence landscapes with window w.
plt.figure(figsize = (8,5))
plt.plot(finalplot[7300:,0],finalplot[7300:,1], label = "L1 Norm", color = "blue")
plt.plot(finalplot[7300:,0],finalplot[7300:,2], label = "L2 Norm", color = "red")

plt.axvline(x=1310, color='black', linestyle='--', alpha=0.6, label = "Dotcom Bubble")
plt.axvline(x=3450, color='black', linestyle='--', alpha=0.6, label = "2008 Crash")
plt.axvline(x=6329, color='black', linestyle='--', alpha=0.6, label = "Covid 2020")

plt.title(f"L1, L2 norms of Persistence Landscapes vs Time -- Window = {w}")
plt.xlabel("Time")
plt.show()

