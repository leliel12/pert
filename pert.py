#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019, Juan B Cabral
# License: BSD-3-Clause
#   Full Text: https://github.com/leliel12/pert/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""The program (or project) evaluation and review technique (PERT).

Pert is a statistical tool used in project management, which was designed to
analyze and represent the tasks involved in completing a given project.

First developed by the United States Navy in the 1958, it is commonly used in
conjunction with the critical path method in the year 1957 (CPM).

Full information:
    https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique

"""


# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np


# =============================================================================
# FUNCTIONS_
# =============================================================================


def expect(o, p, m):
    """Caclulate the expected time.

    The best estimate of the time required to accomplish a
    task, accounting for the fact that things don't always proceed as normal
    (the implication being that the expected time is the average time the
    task would require if the task were repeated on a number of occasions over
    an extended period of time).

    ::

            TE = (O + 4M + P) ÷ 6

    Where:

    - optimistic time (O): the minimum possible time required to accomplish a
      task, assuming everything proceeds better than is normally expected
    - pessimistic time (P): the maximum possible time required to accomplish a
      task, assuming everything goes wrong (but excluding major catastrophes).
    - most likely time (M): the best estimate of the time required to
      accomplish a task, assuming everything proceeds as normal.

    """
    o, m, p = np.asarray(o), np.asarray(m), np.asarray(p)
    return (o + 4 * m + p) / 6.


def std(o, p):
    """Standar deviation.

    ::

        S = (P - O) / 6

    Where:

    - optimistic time (O): the minimum possible time required to accomplish a
      task, assuming everything proceeds better than is normally expected
    - pessimistic time (P): the maximum possible time required to accomplish a
      task, assuming everything goes wrong (but excluding major catastrophes).

    """
    o, p = np.asarray(o), np.asarray(p)
    return (p - o) / 6.


def var(o, p):
    """Variation.

    ::

        S = ((P - O) / 6) ^ 2

    Where:

    - optimistic time (O): the minimum possible time required to accomplish a
      task, assuming everything proceeds better than is normally expected
    - pessimistic time (P): the maximum possible time required to accomplish a
      task, assuming everything goes wrong (but excluding major catastrophes).

    """
    return std(o, p) ** 2


def estimate(o, p, m):
    """Create a estimation for a set of values.

    # 68.2%, 95.4%, 99.7%
    r68, r95, r99 = estimate([1, 2], [3, 4], [5, 6])


    """
    es, stds = np.sum(expect(o, p, m)), np.sum(std(o, p))
    return np.array([
        [es - stds if es - stds > 0 else 0, es + stds * 2],
        [es - stds * 2 if es - stds * 2 > 0 else 0, es + stds * 2],
        [es - stds * 3 if es - stds * 3 > 0 else 0, es + stds * 3],
    ])
