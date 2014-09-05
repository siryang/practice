require 'rgl/adjacency'
# Use DOT to visualize this graph:
require 'rgl/dot'

dg=RGL::DirectedAdjacencyGraph[1,2 ,2,3 ,2,4, 4,5, 6,4, 1,6]

dg.write_to_graphic_file('a.jpg')
