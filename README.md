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

```math
min_{W_{X,Y}\geq 0}
\sum_{i=1}^{|S_E|} 
\left (\sum_{X\in {S_X}}
W_{X,Y}
PV(X\cap {E_i})
-PV(Y) \right)^2\\

\begin{align*}
X: Source\,region\\
Y: Target\,region\\
W_{X,Y}: Normalized\,connection\,strength\\
PV: Projection\,volume\\
E_i: Set\,of\,all\,voxels\,containing\,neuron\,infected\,on\,the\,i^{th}\,injection\\
\end{align*}
```

### **FF/FB Analysis**
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

##### Computing Method

```math
N_{out}(A\to B) = \frac{N\bullet C(A\to B)}{sum\,of\,C\,from\,region\,A}\\

\begin{align*}
N: Number\,of\,cells\,in\,region\,A\\
C: Connectivity\,strength\\
\end{align*}
```


## Output Data
### JSON
Used table2brical.py (python2.7) to get modules for BriCA.

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
