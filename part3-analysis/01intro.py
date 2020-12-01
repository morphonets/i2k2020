#@Context context
#@SNTService snt
from sc.fiji.snt import Tree
from sc.fiji.snt.analysis import (TreeStatistics, GroupedTreeStatistics)
from sc.fiji.snt.analysis.graph import GraphColorMapper as GCM


tree = snt.demoTree('pyramidal')
stats = TreeStatistics(tree)
hist = stats.getHistogram("inter-node distance")
hist.show()

# what else can you do with the stats instance?
# https://morphonets.github.io/SNT/index.html?sc/fiji/snt/analysis/TreeStatistics.html