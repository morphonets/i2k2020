import sc.fiji.snt.*

/** Scriptable tracing cheatsheet: Who's who? **/

// SNTService (snt): Entry point to the program
#@SNTService snt
   
//SNT (plugin): The "core" (image data, threads, settings, etc.)
plugin = snt.getPlugin()
 
// PathAndFillManager (pafm): Keeps track of existing paths (and fills)
pafm = snt.getPathAndFillManager()
            
// SNTUI (ui): The dialogs, widgets, menus, etc.
ui = snt.getUI()

// Now that the introductions are done, let's start!


// Retrieve first path in 'Path Manager'
path = snt.getPaths()[0]

if (path == null) {

    snt.getUI().error("You forgot to create a path!")

} else {

    // enable A*star
    plugin = snt.getPlugin()
    plugin.enableAstar(true)

    //autoTrace accepts:
    // 1) list of points (at least 2) constraining search
    // 2) the point in _any_ existing path from which the new path should branch out
    // NB: path is automatically added to the manager
    newPath = plugin.autoTrace(path.getNodes(), null)
    println(newPath.getName() + "length: " + newPath.getLength())
}


// In detail: Templates>Neuroanatomy>Scripted Tracing Demos
// Wiki: https://imagej.net/SNT:_Scripting
// API: https://morphonets.github.io/SNT/
