# Creating your own WBCA

Our main product is “wbca_cajal.json” as the first version of WBCA. However, you have another option that you can use the codes placed here to modify and improve our WBCA, and re-create and re-build a WBCA for your own purpose.

### Connection Matrix and Port Size
First, after downloading the WBCA from Github, cd into the Codes file and run the two commands below.

```text
python conn.py
```
```text
python portsize.py
```

Running these two commands will create files that are later going to be used to create a JSON file and a block diagram.
The files shown inside the  green stripe in the figure below indicates that they are directly drawn from the Allen Brain Atlas website and are stored in the DataAnalysis folder.

<img width="920" alt="screen shot 2017-12-25 at 14 58 14" src="https://user-images.githubusercontent.com/32238693/34351493-5462fb82-ea60-11e7-8c16-f896df319048.png">

### JSON (WBCA)
Run table2brical.py (python2.7) to get modules for BriCA. But in prior to doing so, check to see that you have prepared a total of three text files, namely connection.txt, regions.txt, and hierarchy.txt. In brief, connection.txt has a matrix consists of sources in the first column (index) and targets in the first row (header) with corresponding connectivity strengths. regions.txt has acronyms in the first and second columns and corresponding safe name in the third and fourth columns. The first and second columns have exactly the same acronyms in it. Same for the third and fourth columns. Lastly, hierarchy.txt has acronyms in the first column and corresponding major region in the second column. From the third column, it is similar to the matrix shown in the connection.txt that the third column has sources and the first row from the third column shows targets. The only difference is the values in the matrix which have numbers of port size instead of connectivity strength. Texts inside the text files are separated by tabs instead of the comma. After having these files ready, run the table2brical.py using the text files.

```text
python table2brical.py connection.txt regions.txt hierarchy.txt output.json prefix threshold_isocortex threshold_thalamus_ff threshold_thalamus_fb
```

If you've downloaded the whole WBCA and not individual files from Github, you may need to use the command down below and not the one shown above.

```text
python table2brical.py ../Release/connection.txt ../Release/regions.txt ../Release/hierarchy.txt ../Release/output.json 1.0 0.843 0.0807 0.4432
```

Inside the JSON file, the FF/FB and the connection strength are described under the comment section in each connection. As of now, the FF/FB is yet to be written using the BriCA Language. That is going to be one of our future tasks.


### Block Diagram

Finally, create a constrained block diagram using mermaid.js from JavaScript, which is a simple description of the neural wiring diagram . Running blockCreator.mmd as written below will allow you to save a block diagram as a .png file. However, you might not be able to get a clean block diagram because mermaid.js still has some bugs in it. The results of FF/FB connections found from the block diagram depicts the same findings from a previous paper ([*Berezovskii et al., J. Comp. Neurol. 519:3672–3683 (2011)*](http://onlinelibrary.wiley.com/doi/10.1002/cne.22675/abstract)), particularly with the part of visual pathways in the lower level hierarchy.


```text
mmdc -i blockCreator.mmd -o output.png -b transparent -w 1500 -H 1000
```

If you run the blockCreator.mmd command shown above, the output will look something like this. (Make sure you cd into the Wiring Diagram Folder before running the blockCreator.mmd command.) The image shows a wiring diagram of FF/FB connections when the threshold of connectivity strength in isocortex is 0.843.

![output_threshold0 843](https://user-images.githubusercontent.com/32238693/34351545-ab5f80fe-ea60-11e7-864f-0294305ba15f.png)
