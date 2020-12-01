## Part 1

In this sections students will be guided through the the multiple ways neuronal processes are reconstructed in SNT.  Exercises will focus on scripting the 'tracing' process.



#### Key Concepts

Path, Bidirectional A* search, Hessian analysis, Secondary image, Path fitting, Path filling



### Exercises

1. **Scripted tracing demo:**
   1. Load the *ddaC neuron* sample image: File> Choose Tracing Image> From Demo...  (*Drosophila ddaC neuron (2D)*)
   2. Disable A* search (Main pane, auto-tracing widget)
   3. Make a straight-line path by clicking on the soma and a distal dendrite
   4. Drag and drop [scripted-tracingResources.groovy](./scripted-tracing.groovy) into the main ImageJ window  (or use File>New>Script... in Fiji, or simply press <kbd>[</kbd>) 

2. [intensity_profile.py](./intensity_profile.py)
3. [time_profile.py](./time_profile.py)

4. Scripted tracing: In the Script Editor' look for the following script in *Templates> Neuroanatomy> Tracings* ([source](https://github.com/morphonets/SNT/tree/master/src/main/resources/script_templates/Neuroanatomy/Tracing)):
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