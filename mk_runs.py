#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2018-S1-MU-65"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['041149_294226'] = [ 91657, 92266,  92425]

on['IRAS04166+2706'] = [ 85886, 85890, 85917, 85921, 85925, 85935, 85998,
                         86002, 86006, 88198, 88927, 88931, 88935, 89024,
                         89028, 89032, 89036, 90102, 90106, 90239, 90422,
                         90426, 90428, 90432, 90724, 90726, 90730, 90987,
                         90991, 91102, 91106, 91519, 92161,
                        ]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['041149_294226']   = ""
pars1['IRAS04166+2706']  = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['041149_294226']   = "srdp=1 admit=0"
pars2['IRAS04166+2706']  = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
