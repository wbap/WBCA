# Whole Brain Connectomic Architecture (WBCA)
The mechanisms of information processing in the neocortex underlie brain functions based on the hierarchy of individual 
cortical areas. This study was focused on the determination of the neocortical hierarchy resulting from a clustering 
analysis of connectomic morphology with cortical layer resolution. K-means clustering effectively classified 
connectivities into two groups. And then the description of the neocortical hierarchy was simplified to a wiring 
diagram to understand how sensory information flows in the biological neural networks. In this initial work, the
validity of the resulting classification is still uncertain to describe the hierarchical relationships in the 
neocortex. However, it enables us to apply this structure as a fundamental of computational study on neural circuits to 
simulate brain functions, and it eventually can apply to our cognitive architecture “Whole Brain Architecture (WBA)” to 
develop an artificial intelligent system, which will allow us to test the success of these classifications whether it is
mimicking particular brain functions in machine learning modules.

## Data Collection
Data for creating mouse brain connectome were taken from *Allen Institute for Brain Science*(Allen).

##### *Allen Brain Atlas SDK*
We have utilized *Mouse Connectivity* and *Reference Space* modules from *Allen Brain Atlas SDK* in order to create 
mouse brain connectome. [*Mouse Connectivity*](http://alleninstitute.github.io/AllenSDK/connectivity.html) module 
includes data for calculating connectivity strength, FF/FB, etc. [*Reference Space*](http://alleninstitute.github.io/AllenSDK/reference_space.html) 
module contains data to get a number of voxels (volume).


## Data Analysis
### **Connectivity Strength**
##### Computing Method
Linear connectivity model via constrained optimization, namely non-negative least squares (NNLS) regression analysis
(Oh 2014), was applied to compute connectivity strengths among neocortex areas. In this calculation, normalized
projection volume and injection volume data taken from *Mouse Connectivity* module were used. This resulting strength 
was used as the input data (consists of 6 x 1638) for following principal component analysis (PCA), 
K-means clustering, number of voxels, and computation of thresholds.

![img](http://latex.codecogs.com/svg.latex?min_%7BW_%7BX%2CY%7D%5Cgeq%200%7D%20%5Csum_%7Bi%3D1%7D%5E%7B%7CS_E%7C%7D%20%5Cleft%20%28%5Csum_%7BX%5Cin%20%7BS_X%7D%7D%20W_%7BX%2CY%7D%20PV%28X%5Ccap%20%7BE_i%7D%29%20-PV%28Y%29%20%5Cright%29%5E2%5C%5C%20X%3A%20Source%5C%2Cregion%5C%5C%20Y%3A%20Target%5C%2Cregion%5C%5C%20W_%7BX%2CY%7D%3A%20Normalized%5C%2Cconnection%5C%2Cstrength%5C%5C%20PV%3A%20Projection%5C%2Cvolume%5C%5C%20E_i%3A%20Set%5C%2Cof%5C%2Call%5C%2Cvoxels%5C%2Ccontaining%5C%2Cneuron%5C%2Cinfected%5C%2Con%5C%2Cthe%5C%2Ci%5E%7Bth%7D%5C%2Cinjection%5C%5C)

### **Feedforward/Feedback (FF/FB) Analysis**
##### Principal Component Analysis (PCA)
Dimensionality reduction was applied to connectivity strengths from 1st to 6th layers in neocortex areas. At this point, 
we just chose visual and auditory areas to analyze using PCA since those two specific areas have more researches done in 
the past compared to other regions. Through PCA in visual areas, the primary ingredient covered 96% of contribution 
ratio, and cumulative contribution ratio including secondary ingredient was 98%; thus, we kept only the primary and 
secondary ingredients after reduction. While classifying FF/FB using PCA, it appears that 6a, 5, 2/3, and 1 layers were 
playing vital roles. Almost identical results were taken from the PCA in auditory areas, and so, we kept reduction 
within the secondary ingredient. 6a, 5 and 2/3 layers were giving important information in auditory areas during 
classification. It seems like FF and FB have been comparatively separated into clear results through PCA in both 
visual and auditory areas.

##### Clustering Analysis
Since we only had 6 x 1638 of data in our hands, we used clustering analysis instead of the classifier as a classification 
method because the amount of the data was insufficient to run classifier. The average connectivity method aforementioned 
was used with K-means clustering on these connectivity strengths. In order to examine correspondence between PCA and 
clustering results, we plotted K-means (where K=2) results on 2-dimensional PCA graph. The first principal component 
was dominant  with layer 6a. The result of the clustering analysis using K-means (where K=2) depicted more FF than FB, 
namely 1566 to 72 in ratio, respectively; however, the strengths in FB have stronger connectivity strengths.

### **Port Size**
##### Number of neurons in each brain region
As previously stated, we have obtained the volume (the number of voxels) of each of the 
regions  as well as the volume (voxels) of the major regions of the brain from the 
Allen Brain Atlas SDK. We then utilized the numbers indicating the number of neurons in 
each major regions that Ryuichi Ueda, director of CIT autonomous robots lab, has 
provided to us, and obtained the number of neurons in each region. Note that this is 
possible from examining the ratio of volume and the number of neurons in both regions 
and major regions of the brain.

##### Computing Method
The port size is equal to the sheer number of neurons that travels from one region, S, 
to the other region, T. (i.e. ViSp → VISl). In order to compute the port size, we 
decided to take into account the number of neurons in S, the connectivity strength(CS) 
from S to T, and the aggregate connectivity strength from S to the other regions. The equation is as follows.

![img](http://latex.codecogs.com/svg.latex?N_%7Bout%7D%28S%5Cto%20T%29%20%3D%20%5Cfrac%7BNs%5Cbullet%20CS%28S%5Cto%20T%29%7D%7B%5Csum%20%28CS%28S%5Cto%20%3F%29%29%7D%5C%5C%20Ns%3A%20Number%5C%2Cof%5C%2Ccells%5C%2Cin%5C%2Cregion%5C%2CA%5C%5C%20CS%3A%20Connectivity%5C%2Cstrength%5C%5C)

Finally, we created a 292 by 292 square-matrix (finale_matrix.csv), mapping the port size 
from one region, S to another region, T. (The first row corresponds to region S and 
the first column corresponds to region T).


## Output Data
### JSON
We used table2brical.py (python2.7) to get modules for BriCA. But in advance, we had to prepare a total of three text files, 
namely connection.txt, regions.txt, and hierarchy.txt. In brief, connection.txt has a matrix consists of sources in the
first column (index) and targets in the first row (header) with corresponding connectivity strengths. regions.txt has 
acronyms in the first and second columns and corresponding safe name in the third and fourth columns. The first and 
second columns have totally same acronyms in it. Same for the third and fourth columns. Lastly, hierarchy.txt has 
acronyms in the first column and corresponding parent-region in the second column. From the third column, it is similar 
to the matrix shown in the connection.txt that the third column has sources and the first row from the third column 
shows targets. The only difference is the values in the matrix which has a number of port-size instead of connectivity 
strength. Texts inside the text files are separated by tabs instead of the comma. After having these files ready, run the 
table2brical.py using the text files.

```text
python table2brical.py connection.txt regions.txt hierarchy.txt output.json prefix threshold
```

### Determination of Threshold
A threshold on connectivity strengths was implemented for better looking and understanding purposes on the wiring 
diagram (Fig. 3). We tried two different methods for finding an appropriate lower limit. One way is calculating an 
average connectivity using connectivity strengths among isocortex for the threshold. Another way is to find power law 
of connectivity strengths among isocortex and retained the top 20%, corresponding to connectivity strengths above 
0.282252. These regions mostly showed FB flows among visual areas, indicating that the most connected visual areas are 
typically FB. However, because of the resulting scarcity of FF connections, we decided to use the average method 
instead of the power-law method in order to create a comprehensive wiring diagram.

Till now, we were using a threshold of 0.259706328093, which is an average connectivity strength within neocortex, in 
order to make a wiring diagram. However, there were some cycles in feedforward wiring diagram when the average 
connectivity strength was used as a threshold. Because we had to create a wiring diagram with a finite constrained 
directed graph with no directed cycle, we needed to make another threshold which follows these restrictions.
Accordingly, we decided to gradually increase the threshold until it gets to the point where any cycles will not exist 
in the wiring diagram which results in 0.843. We might have to consider another way of determining a threshold because 
this new threshold might be too excessive.

The wiring diagram we estimated in this study would serve as a structure of biological neural network model to simulate 
a large scale brain activity, and it might be useful to build a functional brain model. Moreover, it will also be 
advantageous to technologically develop a neuro-inspired machine learning module based on the architecture where we 
would like to implement neural algorithms as an artificial intelligent system.

### Wiring Diagram
Finally, we made the constrained wiring diagram using mermaid.js from JavaScript. Running blockCreator.mmd as written 
below will allow you to save a wiring diagram as a .png file. However, you might not be able to get clean wiring diagram 
because mermaid.js still has some bugs in it. The results of FF/FB connections found from the wiring diagram depicts 
the same findings from Berezovskii’s paper (2011), particularly with the part of visual pathways in the lower level 
hierarchy.


```text
mmdc -i blockCreator.mmd -o output.png -b transparent -w 1500 -H 1000
```


## Reliability and Issues


## Application Coverage
This initial version of the WBCA is possibly only applicable for implementing into a simulation.


## Precaution



## References
1. [Allen SDK (2015)](http://alleninstitute.github.io/AllenSDK/)
2. [Oh et al., Nature 508:207-14 (2014)](https://www.nature.com/articles/nature13186)
3. [Berezovskii et al., J. Comp. Neurol. 519:3672–3683 (2011)](http://onlinelibrary.wiley.com/doi/10.1002/cne.22675/abstract)
