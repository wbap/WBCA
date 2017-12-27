# Whole Brain Connectomic Architecture (WBCA)

## What is WBCA?

Whole Brain Connectomic Architecture (WBCA) is static and schematic [*WBA*](http://wba-initiative.org/en/wba/), which is a good candidate to build up artificial general intelligence (AGI), based on biological connectomes, or wiring diagram of the brain. AGI development would become more efficient by constraining connections among machine learning modules with connectomic information rather than applying the architectures developers build by their own ways. We have released our ongoing prototype of the WBCA resulting from our analysis for the future implementation.

*****
### Repository contents

This repository has 4 directories, “Release”, “Codes”, “DataAnalysis” and “BlockDiagram”. “Release” directory includes the current version of WBCA (WBCA_version.json), which is the main product of this development project. “Codes” has all algorithms we developed for data analysis and representation. “DataAnalysis” consists of original raw data from Allen Institute for Brain Science, and analytical results processed by our algorithms. BlockDiagram has input and output files for mermaid.js (written by JavaScript) to illustrate a block diagram of the whole brain architecture.

### System Requirement

・Python 2.7

### Version

1.0, Cajal: Whole brain connectivity and their strengths and the feedforward and feedback information flow of cortico-cortical pathways and thalamo-cortical pathways. Released on December 28, 2017

### Precaution, Reliability, Issues & Application Coverage

The main product is neither executable nor functional as an artificial intelligence system. It is still under development, currently, no machine learning modules included with WBCA to exert cognitive functions. This initial version of the WBCA is possibly only applicable for implementing into a brain-like simulation. 

### Why do we release WBCA ver. 1.0 : Cajal?

・To be reviewed by professionals from the field of machine learning and neuroscience  
・To broaden our views through public dialogue  
・To deepen and spread our expertise   
・To take the initiative to provide WBCA at the earliest possible time  

### Contributors

haruom  
skyair55  
businy  
Hiroto Tamura  
rinkom  
rondelion  
hymkw  

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

#### Allen Brain Atlas SDK ([*http://alleninstitute.github.io/AllenSDK/*](http://alleninstitute.github.io/AllenSDK/))
The Allen Institute provides a software development kit, the Allen Brain Atlas SDK, to collect data for neural connectivity analysis between brain regions. We have utilized the classes of Mouse Connectivity and Reference Space from Allen Brain Atlas SDK in order to create mouse brain connectome. [*Mouse Connectivity*](http://alleninstitute.github.io/AllenSDK/connectivity.html) includes data for calculating connectivity strength, feedforward and feedback information flows, etc. [*Reference Space*](http://alleninstitute.github.io/AllenSDK/reference_space.html) contains data to get a number of voxels (volume). Below is a data flow diagram for Mouse Brain Connectivity Atlas about the parameters we utilize to build WBCA.

![image_dfd](https://user-images.githubusercontent.com/32238693/34351451-1d16a16a-ea60-11e7-95c5-e41e2f128c24.png)

