# -*- coding: utf-8 -*-
#
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
#
##############################################################################
"""Convert :term:`BAM` format to :term:`WIGGLE` formats"""
from bioconvert import ConvBase
import colorlog

from bioconvert.core.decorators import requires

_log = colorlog.getLogger(__name__)

__all__ = ["BAM2WIGGLE"]


class BAM2WIGGLE(ConvBase):
    """Convert sorted :term:`BAM` file into :term:`WIGGLE` file 

    """
    _default_method = "wiggletools"
    _library_to_install = " wiggletools "

    def __init__(self, infile, outfile):
        """
        :param str infile: The path to the input BAM file. **It must be sorted**.
        :param str outfile: The path to the output file
        """
        super().__init__(infile, outfile)

    @requires("wiggletools")
    def _method_wiggletools(self, *args, **kwargs):
        """

        """
        cmd = "wiggletools {} > {}".format(self.infile, self.outfile)
        self.execute(cmd)

