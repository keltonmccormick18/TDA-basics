# TDA-basics

Topology, and in particular Homology, is loosely the study of shapes of spaces -- how many holes are in the space, and their dimensionalities.

We face three main problems in implementing this to observe the shape of a data set -- topology usually deals with a continuous surface, instead of a point cloud, noise can easily interrupt any true underlying structure, and the shape of a data set can be difficult to properly interpret.

First, we need to take our data set (point cloud) and turn it into a topological space. We do this by constructing shapes -- known as simplices -- between points that are "close enough" to each other. This presents us with a choice of distance metric which we can define.
Second, we can compute the homology of that set of simplices, but this is very sensitive to noise.

So, to combat this problem, we would like to refine our approach in order to deal with these noisy points appropriately. A filtration on our point cloud is a sequence of nested simplicial complexes, often obtained by increasing the maximum required distance between points. A filtration lets us observe what happens to the shape of the data at different levels of sensitivity, which avoids both the issues of overfitting and being sensitive to noise. We can encode this information by using Betti numbers, which roughly correspond to the number of holes in the data -- concretely, the kth Betti number is the dimension of the kth homology group on our space X. We can plot those Betti numbers and record when they are "born" and "die". This is called a persistence diagram.

#Our project

In our case, we then converted the persistence diagrams into persistence landscapes -- for each birth-death pair, we create a tent of the appropriate length on our persistence landscape. We can then take the L1 and L2 norms of the persistence landscapes, which roughly tell us how long (with different weightings) the total lifetime of each topological feature lasted. This makes sense to do, as it again eliminates our noisy points -- those lie close to the diagonal on the persistence diagram and hence have a very small L1 and especially L2 norm.

In this example, we take data from Yahoo Finance -- 3 indices, Jan 1st, 1995 to Feb 23, 2026. We then created point clouds for each window by plotting the daily log-returns for each index on each axis, with different points corresponding to different days. In this way, the Euclidean distance between each point directly represents the volatility -- lower average distance corresponds to a more stable market over the window.

We then create a distance matrix for each point cloud, compute the Vietoris-Rips complexes, and convert that into a persistence diagram and then finally landscape. We then calculate the L1 and L2 norm of each landscape, and plot them against time.

#Results

<img width="1598" height="994" alt="Screenshot 2026-02-27 at 7 57 01 AM" src="https://github.com/user-attachments/assets/77f91de3-a40b-43fa-815a-4040ce567f6c" />

<img width="1592" height="994" alt="Screenshot 2026-02-27 at 8 01 30 AM" src="https://github.com/user-attachments/assets/56ad6df4-d3ee-4be0-b28f-cce7bbbf5862" />


We can very clearly see a correlation between market volatility and each of the three biggest crashes in the past 30 years, in both the L1 and L2 norms. However, the more interesting part is found by observing the shape of the graph leading up to those crashes. 

<img width="1586" height="988" alt="Screenshot 2026-02-27 at 8 12 49 AM" src="https://github.com/user-attachments/assets/6c1741cf-5c8b-48cd-804f-27e4c212e92a" />

<img width="1596" height="996" alt="Screenshot 2026-02-27 at 8 23 01 AM" src="https://github.com/user-attachments/assets/4a29645c-1740-42cd-8eb2-4337f6b42ba6" />

Dotcom Bubble

<img width="1590" height="992" alt="Screenshot 2026-02-27 at 8 14 32 AM" src="https://github.com/user-attachments/assets/bf75d4c4-13d2-4887-a416-5013375a6aeb" />

<img width="1578" height="978" alt="Screenshot 2026-02-27 at 8 18 37 AM" src="https://github.com/user-attachments/assets/0f882dc0-6c3f-4e5e-80b3-acda6f6c1f99" />

2008 Housing Crisis

<img width="1588" height="992" alt="Screenshot 2026-02-27 at 8 32 01 AM" src="https://github.com/user-attachments/assets/3b5b9d00-9ba7-41a1-a5ab-239324c2bd51" />

<img width="1590" height="992" alt="Screenshot 2026-02-27 at 8 31 12 AM" src="https://github.com/user-attachments/assets/a40e1d25-3047-470f-b5a4-6a10ca19402c" />

Covid 2020

<img width="1592" height="994" alt="Screenshot 2026-02-27 at 8 34 31 AM" src="https://github.com/user-attachments/assets/cb25757f-d026-481c-87ef-db0ec4b68226" />

<img width="1590" height="992" alt="Screenshot 2026-02-27 at 8 38 40 AM" src="https://github.com/user-attachments/assets/5b9cf159-d6a0-4d60-800a-8b36c884c64b" />

Present Day (Normal Market Conditions)

In each of the periods (500 days) prior to each crash, we can clearly see market normality leading up to the first 100 days prior, and then a clear upturn in volatility. We can see this especially well using a higher window value of 100, which makes this style of analysis an effective option to detect leading signals of systematic market crashes.

Attached are the files used to obtain these graphs and calculations.
