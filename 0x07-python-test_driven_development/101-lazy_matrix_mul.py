#!/usr/bin/python3
"""
File: 101-lazy_matrix_mul.py
Desc: This module contains a function: lazy_matrix_mul(m_a, m_b)
Author: Onyejekwe Philip (Donphili)
Date Created: 3 Jun 2023
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    computes matrix multiplication
    """
    return numpy.matmul(m_a, m_b)
