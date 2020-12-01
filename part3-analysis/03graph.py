#@Context context
#@SNTService snt
from sc.fiji.snt import Tree
from sc.fiji.snt.analysis import (TreeColorMapper, TreeStatistics, GroupedTreeStatistics)
from sc.fiji.snt.analysis.graph import GraphColorMapper as GCM


tree = snt.demoTree("pyramidal")
graph = tree.getGraph()
GCM(context).map(graph, "Edge weight", "Ice")
graph.show()

TreeColorMapper(context).map(tree, "branch length", "Ice")
tree.show2D()
tree.show3D()
