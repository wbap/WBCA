# Whole Brain Connectomic Architecture (WBCA)

## What is Whole Brain Connectomic Architecture (WBCA)?

Whole Brain Connectomic Architecture (WBCA) is schematic [*WBA*](http://wba-initiative.org/en/wba/) based on biological connectomes. AGI development would become more efficient by constraining connections among machine learning modules with connectomic information rather than the architecture the developer build by their own ways. 

*****
Version

1.0: Cajal: Whole brain connectivity and the feedforward and feedback information flow in the cerebral cortex, Released on December 28, 2017
*****

The mechanisms of information processing in the neocortex underlie brain functions based on the hierarchy of individual cortical areas. This study was focused on the determination of the neocortical hierarchy resulting from a clustering analysis of connectomic morphology with cortical layer resolution. K-means clustering effectively classified connectivities into two groups, feedforward group and feedback group. And then the description of the neocortical hierarchy was simplified to a wiring diagram to understand how sensory information flows in the biological neural networks. In this initial work, the validity of the resulting classification is still uncertain to describe the hierarchical relationships in the neocortex. However, it enables us to apply this structure as a fundamental of computational study on neural circuits to simulate brain functions, and it eventually can apply to our cognitive architecture “Whole Brain Architecture (WBA)” to develop an artificial intelligent system, which will allow us to test the success of these classifications whether it is mimicking particular brain functions in machine learning modules.


## Objectives for the release of WBCA ver. 1.0 : Cajal
・To be reviewed by professionals from the field of machine learning and neuroscience  
・To broaden our views through public dialogue  
・To deepen and spread our expertise  
・To take the initiative to provide WBCA at the earliest possible time  


## Creating WBCA ver. 1.0 : Cajal


## License
copied from Allen Brain Atlas website  

[This section explains your obligations relating to IP rights, and your rights and restrictions relating to your use of the Content.]  

You may use, copy, distribute, publicly perform, publicly display or create derivative works of the Content (except our name, trademarks or logos pursuant to the Trademarks section below) for research or other noncommercial purposes. Any derivative works (defined as "Improvements" below) are subject to the "Freedom to Innovate and Rights to Improvements" section of these Terms. In addition, where the Content contains links to downloadable software applications, services or tools, you may download and use such applications, services or tools as long as you adhere to any license terms and conditions provided with those applications, services or tools.  

You may not redistribute the Content or Improvements for commercial purposes without our written permission. For purposes of these Terms, commercial purposes is the incorporation of the Allen Institute's Content into anything that is designed for the purpose of sale; however, because we encourage use of our Content for research and academic publication, you may, without obtaining further license or permission, publish a limited set of the Content in a scholarly journal, textbook or other professional, academic or journalistic publication (with appropriate citation) and still be compliant with these Terms.  

You may not post Content on social media or other third-party websites that require you to acknowledge that you own the Content you post (e.g., YouTube, Flickr and Twitter). You agree that you will not use the Sites in any manner that would violate anyone else's rights, such as copyright, trademark, patent, privacy or other rights. This includes removing any copyright, trademark or other proprietary notices from the Content. You may not create hyperlinks to the Sites that portray the Allen Institute in a false or misleading light. You agree that you will only make lawful use of the Sites in compliance with all federal, state, and local laws and regulations.  


## Associated Technology and Terminology

#### The BriCA Language

We have used the BriCA Language to mock up the WBCA.

[*The BriCA Language*](https://wba-initiative.org/wiki/en/brica_language) is a Domain Specific Language (DSL)/Architecture Description Language (ADL) for describing modules and message passing routes in computing architecture. More specifically, it describes modules, ports on the modules, and connections among the ports. The language enables users to record, exchange, and modify architecture design. 

In this product, the module corresponds to the brain region annotated by Allen Institute for Brain Science. The port size is a representation of the diameter of neural fibers (axons), which is nearly equal to the neural connectivity strengths. 

#### Allen Brain Atlas SDK
The Allen Institute provides a software development kit, the Allen Brain Atlas SDK, to collect data for neural connectivity analysis between brain regions. We have utilized *Mouse Connectivity* and *Reference Space* modules from *Allen Brain Atlas SDK* in order to create mouse brain connectome. [*Mouse Connectivity*](http://alleninstitute.github.io/AllenSDK/connectivity.html) includes data for calculating connectivity strength, FF/FB, etc. [*Reference Space*](http://alleninstitute.github.io/AllenSDK/reference_space.html) contains data to get a number of voxels (volume).

![image_dfd](https://user-images.githubusercontent.com/32238693/34351451-1d16a16a-ea60-11e7-95c5-e41e2f128c24.png)
The data flow diagram for Mouse Brain Connectivity Atlas

## Outputting Data

### Getting Started
Our main product is “WBCA_Cajal.json” as WBCA. You can use it to develop your own WBA.

### Connection matrix and Port size
First, after downloading the WBCA from Github, cd into the codes file and run the two commands below.

```text
python conn.py
```
```text
python portsize.py
```

Running these two commands will create files that are later going to be used to create a JSON file and a block diagram.
The files shown inside the  green stripe in the figure below indicates that they are directly drawn from the Allen Brain Atlas website and are stored in the raw data folder.

<img width="920" alt="screen shot 2017-12-25 at 14 58 14" src="https://user-images.githubusercontent.com/32238693/34351493-5462fb82-ea60-11e7-8c16-f896df319048.png">

### JSON (WBCA)
Run table2brical.py (python2.7) to get modules for BriCA. But in prior to doing so, check to see that you have prepared a total of three text files, namely connection.txt, regions.txt, and hierarchy.txt. In brief, connection.txt has a matrix consists of sources in the first column (index) and targets in the first row (header) with corresponding connectivity strengths. regions.txt has acronyms in the first and second columns and corresponding safe name in the third and fourth columns. The first and second columns have totally same acronyms in it. Same for the third and fourth columns. Lastly, hierarchy.txt has acronyms in the first column and corresponding parent-region in the second column. From the third column, it is similar to the matrix shown in the connection.txt that the third column has sources and the first row from the third column shows targets. The only difference is the values in the matrix which has a number of port-size instead of connectivity strength. Texts inside the text files are separated by tabs instead of the comma. After having these files ready, run the table2brical.py using the text files.

```text
python table2brical.py connection.txt regions.txt hierarchy.txt output.json prefix threshold_isocortex threshold_thalamus_ff threshold_thalamus_fb
```

If you've downloaded the whole WBCA and not individual files from Github, you may need to use the command down below and not the one shown above.

```text
python table2brical.py ../WBCA2017/connection.txt ../WBCA2017/regions.txt ../WBCA2017/hierarchy.txt ../output.json 1.0 0.843
```

Inside the JSON file, the FF/FB and the connection strength are described under the comment section in each connection. As of now, the FF/FB is yet to be written using the BriCA Language. That is going to be one of our future tasks.


### Block Diagram
Finally, create a constrained block diagram using mermaid.js from JavaScript, which is a simple description of the neural wiring diagram . Running blockCreator.mmd as written below will allow you to save a block diagram as a .png file. However, you might not be able to get a clean block diagram because mermaid.js still has some bugs in it. The results of FF/FB connections found from the block diagram depicts the same findings from Berezovskii’s paper (2011), particularly with the part of visual pathways in the lower level hierarchy.


```text
mmdc -i blockCreator.mmd -o output.png -b transparent -w 1500 -H 1000
```

If you run the blockCreator.mmd command shown above, the output will look something like this. (Make sure you cd into the Wiring Diagram Folder before running the blockCreator.mmd command.) The image shows a wiring diagram of FF/FB connections when the threshold of connectivity strength in isocortex is 0.843.

![output_threshold0 843](https://user-images.githubusercontent.com/32238693/34351545-ab5f80fe-ea60-11e7-864f-0294305ba15f.png)



## Reliability and Issues


## Application Coverage
This initial version of the WBCA is possibly only applicable for implementing into a simulation.


## Precaution



## References
1. [Allen SDK (2015)](http://alleninstitute.github.io/AllenSDK/)
2. [Oh et al., Nature 508:207-14 (2014)](https://www.nature.com/articles/nature13186)
3. [Berezovskii et al., J. Comp. Neurol. 519:3672–3683 (2011)](http://onlinelibrary.wiley.com/doi/10.1002/cne.22675/abstract)
