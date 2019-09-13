#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019, Juan B Cabral
# License: BSD-3-Clause
#   Full Text: https://github.com/leliel12/pert/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""Pert testing"""


# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np

import pert


# =============================================================================
# CUSTOM STRATEGIE
# =============================================================================

class TestCasePert:

    def test_expect(self):
        o, p, m = 1, 2, 1
        result = pert.expect(o, p, m)
        np.testing.assert_almost_equal(result, 1.1666, decimal=4)

    def test_std(self):
        o, p = 1, 2
        result = pert.std(o, p)
        np.testing.assert_almost_equal(result, 0.1666, decimal=4)

    def test_var(self):
        o, p = 1, 2
        result = pert.var(o, p)
        np.testing.assert_almost_equal(result, 0.1666 ** 2, decimal=4)

    def test_estimate(self):
        o = [1, 2, 3, 4, 5]
        p = [3, 6, 9, 16, 25]
        m = [1, 3, 7, 12, 10]

        r68, r95, r99 = pert.estimate(o, p, m)

        np.testing.assert_almost_equal(r68, [27., 49.], decimal=4)
        np.testing.assert_almost_equal(r95, [19.6667, 49.], decimal=4)
        np.testing.assert_almost_equal(r99, [12.3333, 56.3333], decimal=4)
