# Quantitative Neuroanatomy Course
Part of the [I2K 2020](https://www.janelia.org/you-janelia/conferences/from-images-to-knowledge-with-imagej-friends) conference.

## Sessions

## Summary


## Requirements

1. Download and install Fiji.
2. Subscribe to the Neuroanatomy update site. Due to lack of time we are not going to cover sciview integration, so you don't need to subscribe to the sciview update site
3. For python notebooks, you will need to install pyimagej by following [these instructions](https://github.com/morphonets/SNT/tree/master/notebooks#to-install-pyimagej)  

NOTE: As of 11/27/2020, with the most recent Fiji, attempting to initialize pyimagej with a local Fiji installation via:  
```python
import imagej
ij = imagej.init("/path/to/your/Fiji.app", headless=False)
```  
may result in the following error:  
`JavaException: JVM exception occurred: Invalid service: sc.fiji.filamentdetector.gui.GUIStatusService`

A workaround is described [here](https://forum.image.sc/t/fiji-fails-to-launch-after-update/44582)


## Download sample data