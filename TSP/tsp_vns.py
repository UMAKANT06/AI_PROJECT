from nodes_generator import NodeGenerator
from vns import VariableNeighborhoodSearch

def main():
    '''set the simulated annealing algorithm params'''
    stopping_iter = 10000
    '''set the dimensions of the grid'''
    size_width = 200
    size_height = 200

    '''set the number of nodes'''
    population_size = 20

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''run simulated annealing algorithm with 2-opt'''
    vn = VariableNeighborhoodSearch(nodes, stopping_iter)
    vn.vns()
    vn.animateSolutions()
    vn.plotLearning()


if __name__ == "__main__":
    main()
