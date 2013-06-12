# Copyright (C) 2012  Alex Nitz
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


#
# =============================================================================
#
#                                   Preamble
#
# =============================================================================
#
import numpy
import events

def threshold(series, value):
    arr = series.numpy()
    mask = abs(arr) > value
    vals = arr[mask]
    locs = mask.nonzero()[0]
    peaks = numpy.zeros(len(vals), dtype=events.subset_dtype(series.dtype))
    peaks['loc'] = locs
    peaks['val'] = vals
    return peaks


