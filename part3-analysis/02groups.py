#@Context context
#@SNTService snt
from sc.fiji.snt import Tree
from sc.fiji.snt.analysis import (TreeStatistics, GroupedTreeStatistics)
from sc.fiji.snt.analysis.graph import GraphColorMapper as GCM



group1 = snt.demoTrees()[0:2]
group2 = snt.demoTrees()[2:4]
stats = GroupedTreeStatistics()
stats.addGroup(group1, "Group 1")
stats.addGroup(group2, "Group 2")
hist = stats.getHistogram("inter-node distance")
hist.show()
plot = stats.getBoxPlot("total length")
plot.show()

g1_stats = stats.getGroupStats("Group 1")
g1_summary = g1_stats.getSummaryStats("total length")
print(g1_summary)

viewer = snt.newRecViewer(True)  # GUI controls?
for tree in group1:
    tree.setColor("green")
for tree in group2:
    tree.setColor("magenta")
viewer.add(group1)
viewer.add(group2)
viewer.show()
