def sphere(individual):
    """
    Name: Sphere test objective function
    Type: minimization
    Dimension: none
    Range: none
    Global optima: 0
    Function: 'f(\mathbf{x}) = \sum_{i=1}^Nx_i^2'
    """

    return sum(gene * gene for gene in individual),

__all__ = ['sphere']