#@Context context
#@LogService log
#@LUTService lut
#@SNTService snt
#@UIService ui


/**
 * file:	
 * version:	
 * info:	
 */

import sc.fiji.snt.*
import sc.fiji.snt.analysis.*
import sc.fiji.snt.analysis.graph.*
import sc.fiji.snt.analysis.sholl.*
import sc.fiji.snt.annotation.*
import sc.fiji.snt.io.*
import sc.fiji.snt.plugin.*
import sc.fiji.snt.util.*
import sc.fiji.snt.viewer.*

// Documentation Resources: https://imagej.net/SNT:_Scripting
// Latest SNT API: https://morphonets.github.io/SNT/
// Rec. Viewer's API: https://morphonets.github.io/SNT/index.html?sc/fiji/snt/viewer/Viewer3D.html
// Tip: Programmatic control of the Viewer's scene can be set using the Console info
// produced when calling viewer.logSceneControls() or pressing 'L' when viewer is frontmost

viewer = snt.getRecViewer()

listOfTrees = viewer.getTrees()
if (listOfTrees.isEmpty())
    ui.showDialog("No Trees loaded?", "Empty Scene")
viewer.setViewMode("side")
viewer.loadRefBrain("mouse")
viewer.setAnimationEnabled(true)