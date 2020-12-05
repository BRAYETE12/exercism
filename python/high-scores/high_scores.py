def latest(scores):
    return scores[ len(scores) - 1 ]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores = sorted(scores)
    n = len(scores)
    i = 0  if (n-3) < 0  else (n-3)
    return sorted( scores[ i : n ], reverse=True )
