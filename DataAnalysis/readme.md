# Data Analysis
### **Connectivity Strength Analysis**
##### Computing Connectivity Strength 
The connectivity strength between brain areas were calculated based on the datasets in [*Allen Mouse Connectivity Atlas*](http://connectivity.brain-map.org/). Linear connectivity model via constrained optimization, namely non-negative least squares (NNLS) regression analysis (Oh 2014), was applied to compute connectivity strengths among neocortex areas. In this calculation, normalized projection volume and injection volume data taken from Mouse Connectivity module were used. This resulting strength was used as the input data (consists of 6 x 1638) for following principal component analysis (PCA), K-means clustering, number of voxels, and computation of thresholds.

![img](http://latex.codecogs.com/svg.latex?min_%7BW_%7BX%2CY%7D%5Cgeq%200%7D%20%5Csum_%7Bi%3D1%7D%5E%7B%7CS_E%7C%7D%20%5Cleft%20%28%5Csum_%7BX%5Cin%20%7BS_X%7D%7D%20W_%7BX%2CY%7D%20PV%28X%5Ccap%20%7BE_i%7D%29%20-PV%28Y%29%20%5Cright%29%5E2%5C%5C%20X%3A%20Source%5C%2Cregion%5C%5C%20Y%3A%20Target%5C%2Cregion%5C%5C%20W_%7BX%2CY%7D%3A%20Normalized%5C%2Cconnection%5C%2Cstrength%5C%5C%20PV%3A%20Projection%5C%2Cvolume%5C%5C%20E_i%3A%20Set%5C%2Cof%5C%2Call%5C%2Cvoxels%5C%2Ccontaining%5C%2Cneuron%5C%2Cinfected%5C%2Con%5C%2Cthe%5C%2Ci%5E%7Bth%7D%5C%2Cinjection%5C%5C)

### **Feedforward/Feedback (FF/FB) Analysis**

We tried to determine the information flow with feedforward (FF) and feedback (FB) in the part of mature cerebral cortex (neocortex, isocortex) by utilizing a dimension reduction and a clustering method. In this FF/FB diagram, we ignore weaker neural connections under the threshold to make it to be directed acyclic graph (DAG). 

##### Principal Component Analysis (PCA)

###### Pathways in isocortex areas  

Dimensionality reduction was applied to connectivity strengths from 1st to 6th layers in isocortex areas. At this point, we just chose visual and auditory areas to analyze using PCA since those two specific areas have more researches done in the past compared to other regions. Through PCA in visual areas, the primary ingredient covered 96% of contribution ratio, and cumulative contribution ratio including secondary ingredient was 98%; thus, we kept only the primary and secondary ingredients after reduction. While classifying FF/FB using PCA, it appears that 6a, 5, 2/3, and 1 layers were playing vital roles. Almost identical results were taken from the PCA in auditory areas, and so, we kept reduction within the secondary ingredient. 6a, 5 and 2/3 layers were giving important information in auditory areas during classification. It seems like FF and FB have been comparatively separated into clear results through PCA in both visual and auditory areas.  

###### Pathways from thalamus to isocortex  

In addition to the previous analysis of the pathways in isocortex, the same analysis was applied to the ones from thalamus to isocortex. Cumulative contribution ratio until secondary component was slightly lower than the pathways in isocortex(91%) but primary and secondary component accounted for a large percent of all cumulative contribution ratio. 5, 6a and 2/3 layers had relatively large effects on this PCA classifying.  


##### Clustering Analysis  

###### Isocortex direct pathways  

Since we only had 6 x 1638 of data in our hands, we used clustering analysis instead of the classifier as a classification method because the amount of the data was insufficient to run classifier. The average connectivity method aforementioned was used with K-means clustering, which is one of the most famous clustering methods, on these connectivity strengths. In order to examine correspondence between PCA and clustering results, we plotted K-means (where K=2) results on 2-dimensional PCA graph. The first principal component was dominant with layer 6a. The result of the clustering analysis using K-means (where K=2) depicted more FF than FB, namely 1566 to 72 in ratio, respectively; however, the strengths in FB have stronger connectivity strengths.  

###### Thalamo-cortical indirect pathways  

Aforementioned clustering analysis was conducted on the pathways from thalamus to isocortex, and the results were mapped on 2-dimensional PCA chart. Contrary to the result of isocortex areas, the number of FB is far more than FF, specifically 1376 and 22 respectively. We could not assign FF/FB of the pathways from isocortex regions to thalamus because this clustering analysis needs layer-wise connectivity strength; thus, FF/FB of the pathways from thalamus to isocortex were alloted to them. Moreover, to avoid the network complexity, FF/FB of thalamo-cortical indirect pathways were matched to those of the isocortex direct pathways.  

### Determination of Threshold on connectivity strengths

A threshold on connectivity strengths was implemented for better looking and understanding purposes on the wiring diagram. We tried two different methods for finding an appropriate lower limit. One way is calculating an average connectivity using connectivity strengths among isocortex for the threshold. Another way is to find power law of connectivity strengths among isocortex and retained the top 20%, corresponding to connectivity strengths above 0.282252. These regions mostly showed FB flows among visual areas, indicating that the most connected visual areas are typically FB. However, because of the resulting scarcity of FF connections, we decided to use the average method instead of the power-law method in order to create a comprehensive wiring diagram.  

Until now, we were using a threshold of 0.259706328093, which is an average connectivity strength within isocortex, in order to make a wiring diagram. However, there were some cycles in feedforward wiring diagram when the average connectivity strength was used as a threshold. Because we had to create a wiring diagram with a finite constrained directed graph with no directed cycle, we needed to make another threshold which follows these restrictions.  

Accordingly, we decided to gradually increase the threshold until it gets to the point where any cycles will not exist in the wiring diagram which results in 0.843. We might have to consider another way of determining a threshold because this new threshold might be too excessive. Finally, FF threshold and FB threshold of the thalamo-cortical indirect pathway were set to 0.0807 and 0.4432 respectively following the method described above.  

The wiring diagram we estimated in this study would serve as a structure of biological neural network model to simulate a large scale brain activity, and it might be useful to build a functional brain model. Moreover, it will also be advantageous to technologically develop a neuro-inspired machine learning module based on the architecture where we would like to implement neural algorithms as an artificial intelligent system.  


### **Port Size Analysis**

The port sizes are required to describe the connectivity strength between brain regions. It was calculated with both the number of neurons and the ratio of connectivity strength we calculated by the above method.  

##### Number of voxels in each brain region / major region
We obtained the volume (the number of voxels) of each of the regions as well as the volume (voxels) of the major regions of the brain from the Allen Brain Atlas SDK. The figure below illustrates the use of various methods and classes to obtain the number of voxels from the SDK.

<img width="672" alt="screen shot 2017-12-25 at 13 17 59" src="https://user-images.githubusercontent.com/32238693/34351848-78857344-ea62-11e7-85a4-a30eb37862ad.png">

The code for obtaining the number of voxels for each region / major region from the SDK is kept in the codes folder in a file called voxel_sdk.py.

##### Number of neurons in each brain region / major region
We utilized the numbers indicating the number of neurons in each major regions that Ryuichi Ueda, director of CIT autonomous robots lab, has provided to us, and obtained the number of neurons in each region of the brain. Note that this is possible from examining the ratio of voxels and the number of neurons in both regions and major regions of the brain.

##### Computing port size
As previously stated in the Associated Technology and Terminology section, we defined port size to be the sheer number of neurons that travels from one region, S, to the other region, T. (e.g. ViSp → VISl). In order to compute the port size, we decided to take into account the number of neurons in S, the connectivity strength(CS) from S to T, and the aggregate connectivity strength from S to the other regions. The equation is as follows.

![img](http://latex.codecogs.com/svg.latex?N_%7Bout%7D%28S%5Cto%20T%29%20%3D%20%5Cfrac%7BNs%5Cbullet%20CS%28S%5Cto%20T%29%7D%7B%5Csum%20%28CS%28S%5Cto%20%3F%29%29%7D%5C%5C%20Ns%3A%20Number%5C%2Cof%5C%2Ccells%5C%2Cin%5C%2Cregion%5C%2CA%5C%5C%20CS%3A%20Connectivity%5C%2Cstrength%5C%5C)

Finally, we created a 292 x 292 (all brain regions) square-matrix, mapping the port size from one region, S to another region, T, and placed inside the file called finale_matrix.csv. (The first row corresponds to region S and the first column corresponds to region T).
