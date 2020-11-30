## Outline

SNT features several viewers for neuroanatomy:

- Reconstruction Viewer (the most versatile)
- Reconstruction Plotter
- Graph Viewer
- sciview integration
- Legacy 3D Viewer integration

In this section, students will learn about the different viewers, and their scripting capabilities.

#### Key Concepts
Tree, DirectWeightedGraph, Mesh, LUT-mapping, BrainAnnotation, Annotation Graph

### Overview

1.  Overview of Legacy 3D viewer, sciview, and Reconstruction Plotter
1.  OP1 [dataset](./datasets)
2.  Overview of Graph Viewer
    1.  OP1 1 [dataset](./datasets)
    2.  Fractal Tree (demo image)
4.  Reconstruction Viewer:
   1. Overview
   2. Tips (Drag & drop, shortcuts, tags, 'recordable' commands)
   3. Handling groups of cells: Olfactory Projection Fibers: [Group1](./datasets/group1) vs [Group2](./datasets/group2)  
      1. "Import and compare groups" command
      2. Tags
      3. Analyses
   4. Interactive scripts [RecViewerScript.groovy](./RecViewerScript.groovy)

### Exercises

- Script Templates: *Neuroanatomy> Render>*



### Homework

Using `snt.demoTrees()` can you generate a montage of:

- Skeletonized images
- Viewer2D instances (MultiTreeViewer)
- Animated video (image sequence) in Viewer3D 



### Resources

[SNT Manuscript](https://doi.org/10.1101/2020.07.13.179325) | [SNT Manuscript scripts](https://github.com/morphonets/SNTmanuscript) | [User Documentation](https://imagej.net/SNT) | [Forum](https://forum.image.sc/tags/snt) | [Source Code](https://github.com/morphonets/SNT/) | [API](https://morphonets.github.io/SNT/) 