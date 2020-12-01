#@Context context
#@SNTService snt
from sc.fiji.snt import Tree
from sc.fiji.snt.analysis import (TreeStatistics, GroupedTreeStatistics)
from sc.fiji.snt.analysis.graph import GraphColorMapper as GCM
from sc.fiji.snt.annotation import AllenUtils 



def showChart(chart, w, h):
    chart.setFontSize(16)
    chart.setSize(w, h)
    chart.show()


tree = snt.demoTrees()[0]
soma = tree.getRoot() ## retrieve soma
soma_loc = soma.getAnnotation().acronym() ## retrieve brain area abbrev. associated with soma


stats = TreeStatistics(tree)
hist = stats.getAnnotatedLengthHistogram()
hist.annotateCategory(soma_loc, "Soma")
showChart(hist, 400, 750)

soma_mesh = AllenUtils.getCompartment(soma_loc).getMesh()
viewer = snt.newRecViewer(True)  # GUI controls?
viewer.add(soma_mesh)
tree.setColor('red')
viewer.add(tree)
viewer.show()