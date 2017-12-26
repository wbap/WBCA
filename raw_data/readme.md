# Data Analysis
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
