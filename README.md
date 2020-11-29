<p align="center"><img src="https://imagej.net/_images/5/5d/SNTLogo512.png" alt="SNT" width="150"></p>


# Quantitative Neuroanatomy Course
Part of the [I2K 2020](https://www.janelia.org/you-janelia/conferences/from-images-to-knowledge-with-imagej-friends) conference.

| Sessions |                                             |
| -------- | ------------------------------------------- |
| **1**    | 2020-11-30 14:00   –   2020-11-30 18:00 UTC |
| **2**    | 2020-12-01 22:00   –   2020-12-02 02:00 UTC |




## Summary

The course is organized in 3 parts:

**[Part 1](./part1-tracing/README.md#part-1):  Tracing**	

​		Overview, GUI-based controls and basic scripting

**[Part 2](./part2-visualization/README.md#part-2): Visualization**

​		Neuroanatomy viewers and their scripting capabilities  

**[Part 3](./part3-analysis/README.md#part-3): Analysis**

​		Single-cell morphometry, databases and brain atlases, and quantitative analyses of cell groups




## Requirements

SNT is available in  [Fiji](https://imagej.net/Fiji) and is currently distributed through the *NeuroAnatomy* [update site](https://imagej.net/Update_Sites).

1. Download and Install [Fiji](https://imagej.net/Fiji).
2. Subscribe to *NeuroAnatomy* [update site](https://imagej.net/Update_Sites):
   1. the Run the Fiji Updater (*Help › Update...*, the *penultimate* entry in the  *Help ›*  menu)
   2. Click *Manage update sites*
   3. Select the *Neuroanatomy* checkbox
   4. Click *Apply changes* and Restart Fiji. SNT commands are registered under _Plugins>Neuroanatomy>_ in the main menu and SNT scripts under _Templates>Neuroanatomy>_ in Fiji's Script Editor.
3. For Jupyter notebooks, you will need to install pyimagej by following [these instructions](./notebooks/README.md#to-install-pyimagej)

NB:

- We recommend to re-run the updater on the day of the course to ensure you can access the most recent versions of the demos scripts
- It is perfectly fine to keep multiple Fiji installations in your system
- Due to lack of time, we are not going to cover sciview integration, so you don't need to subscribe to the *sciview* update site 
- If you are using a laptop, an external mouse may be useful during part 1



### Resources

[SNT Manuscript](https://doi.org/10.1101/2020.07.13.179325) | [User Documentation](https://imagej.net/SNT) | [Forum](https://forum.image.sc/tags/snt) | [Source Code](https://github.com/morphonets/SNT/) | [API](https://github.com/morphonets/SNT/)