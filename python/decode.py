#!/usr/bin/env python

# Copyright 2014 Jared Boone <jared@sharebrained.com>
#
# This file is part of gr-tpms.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import digital
from gnuradio import gr

class clock_recovery(gr.hier_block2):
	def __init__(self, input_rate, symbol_rate):
		super(clock_recovery, self).__init__(
			"clock_recovery",
			gr.io_signature(1, 1, gr.sizeof_float*1),
			gr.io_signature(1, 1, gr.sizeof_char*1),
		)

		samples_per_symbol = float(input_rate) / symbol_rate
		omega_relative_limit = 0.02
		gain_mu = 0.4 / samples_per_symbol

		self.clock_recovery = digital.clock_recovery_mm_ff(samples_per_symbol*(1+0.00), 0.25*gain_mu*gain_mu, 0.5, gain_mu, omega_relative_limit)
		self.slicer = digital.binary_slicer_fb()

		self.connect((self, 0), (self.clock_recovery, 0))
		self.connect((self.clock_recovery, 0), (self.slicer, 0))
		self.connect((self.slicer, 0), (self, 0))
