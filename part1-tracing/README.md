## Part 1

In this sections students will be guided through the the multiple ways neuronal processes are reconstructed in SNT.  Exercises will focus on scripting the 'tracing' process.



#### Key Concepts

Path, Bidirectional A* search, Hessian analysis, Secondary image, Path fitting, Path filling



### Overview

1. [Walk-trough](https://imagej.net/SNT:_Manual) of GUI-based functionality

2. Usage Tips (drag & drop functionality, [shortcuts](https://imagej.net/SNT:_Key_Shortcuts), GUI-registering [scripts](https://imagej.net/SNT:_Scripting), etc.)

3. [Assisted-tracing](https://imagej.net/SNT:_Manual.html#Auto-tracing):
   1. Controls (Tracing and Editing)
   2. Idiosyncrasies ("*answer to proceed*" prompts, lack of undo buffer, start/end connectivity of Paths)
   3. Hessian-based analysis
   4. Tracing on [secondary images](https://imagej.net/SNT:_Manual.html#Tracing_on_Secondary_Image)

4. Proof-editing:
   1. [Path Manager](https://imagej.net/SNT:_Manual.html#Path_Manager) (controls, tags, morphometric filtering, etc.)
   2. [Editing controls](https://imagej.net/SNT:_Manual.html#Editing_Paths)
   3. [Path fitting](https://imagej.net/SNT:_Manual.html#Refine.2FFit)
   
5. ImageJ interoperability:
   1. Access Paths as ROIs, intensity profiles, etc.
   
6. Automated tracing (Tutor: CA)
   1. Obtaining reconstructions directly from images
   2. Proof-editing the result
   
7. Scripting basics: 
   1. [API][API] Overview
   2. [SNTService][SNTService]



### Exercises

#### Scripted tracing (primer)

1. Scripted tracing demo:
   1. Load the *ddaC neuron* sample image: File> Choose Tracing Image> From Demo...  (*Drosophila ddaC neuron (2D)*)
   2. Disable A* search (Main pane, auto-tracing widget)
   3. Make a straight-line path by clicking on the soma and a distal dendrite
   4. Drag and drop [scripted-tracingResources.groovy](./scripted-tracing.groovy) into the main ImageJ window  (or use File>New>Script... in Fiji, or simply press <kbd>[</kbd>) 

#### Path profile
1. [Dataset](./datasets) 810 
2. [intensity_profile.py](./intensity_profile.py)

#### Time profile
1. [Dataset](./datasets) 701 
2. [time_profile.py](./time_profile.py)

#### Scripted tracing
2. In the Script Editor' look for the following script in *Templates> Neuroanatomy> Tracings* ([source](https://github.com/morphonets/SNT/tree/master/src/main/resources/script_templates/Neuroanatomy/Tracing)):
   1. Scripted_Tracing_Demo_(Interactive).py
   2. Scripted_Tracing_Demo.py



### Homework

In this session we scripted an A* search from a manual path. Would would you modify the script to use a ROI (e.g., a line or a set of points) instead?

| Library                                                      | Relevant Classes                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ImageJ1](https://javadoc.scijava.org/ImageJ1/index.html?overview-summary.html) | [ImagePlus](https://javadoc.scijava.org/ImageJ1/index.html?ij/ImagePlus.html), [Roi](https://javadoc.scijava.org/ImageJ1/index.html?ij/gui/Roi.html) (including [Line](https://javadoc.scijava.org/ImageJ1/index.html?ij/gui/Line.html), and [PointRoi](https://javadoc.scijava.org/ImageJ1/index.html?ij/gui/PointRoi.html)) |
| [SNT][API]                                                   | [SNTService][SNTService], [SNT](https://morphonets.github.io/SNT/index.html?sc/fiji/snt/SNT.html), [Path](https://morphonets.github.io/SNT/index.html?sc/fiji/snt/Path.html), [PathAndFillManager](https://morphonets.github.io/SNT/index.html?sc/fiji/snt/PathAndFillManager.html), [PointInImage](https://morphonets.github.io/SNT/index.html?sc/fiji/snt/util/PointInImage.html) |

​	

[API]: https://morphonets.github.io/SNT/index.html?sc/fiji/snt/SNT.html
[SNTService]: https://morphonets.github.io/SNT/index.html?sc/fiji/snt/SNTService.html



### Resources

[SNT Manuscript](https://doi.org/10.1101/2020.07.13.179325) | [SNT Manuscript scripts](https://github.com/morphonets/SNTmanuscript) | [User Documentation](https://imagej.net/SNT) | [Forum](https://forum.image.sc/tags/snt) | [Source Code](https://github.com/morphonets/SNT/) | [API](https://morphonets.github.io/SNT/) 