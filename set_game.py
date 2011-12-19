dimensions = [
    ('one', 'two', 'three'),
    ('red', 'green', 'purple'),
    ('empty', 'striped', 'solid'),
    ('oval', 'diamond', 'squiggle'),
]

def construct_deck():
    """
    >>> deck = construct_deck()
    >>> len(deck)
    81
    >>> deck[0]
    ('one', 'red', 'empty', 'oval')
    """
    # Construct the deck of cards.
    cards = []
    indices = [0 for d in dimensions] # One index for each dimension.
    while True:
        # Create a card from the name of the current value for each index.
        cards.append(tuple(
            dimension[index]
            for dimension, index in zip(dimensions, indices)
        ))
        # Increment the indices.
        try:
            increment_indices(indices)
        except IndexError:
            break
    return cards

def increment_indices(indices):
    """
    Increments the indices in place, and returns them.

    >>> increment_indices([0, 0, 0, 0])
    [0, 0, 0, 1]
    >>> increment_indices([0, 0, 0, 2])
    [0, 0, 1, 0]
    >>> increment_indices([2, 2, 2, 2])
    Traceback (most recent call last):
        ...
    IndexError
    """
    for i in reversed(range(len(indices))):
        indices[i] += 1
        if indices[i] >= len(dimensions[i]):
            indices[i] = 0
        else:
            return indices
    else:
        raise IndexError()

deck = construct_deck()
print(deck)
