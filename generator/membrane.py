# The MIT License (MIT)
#
# Copyright (c) 2011, 2013 OpenWorm.
# http://openworm.org
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the MIT License
# which accompanies this distribution, and is available at
# http://opensource.org/licenses/MIT
#
# Contributors:
#      OpenWorm - http://openworm.org/people.html
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import with_statement

'''
Created on Dec 25, 2013

@author: serg
'''
from helper.point import Vector3D
class membrane(object):
    '''
    classdocs
    '''


    def __init__(self, id,jd,kd):
        '''
        Constructor
        '''
        self.id =  id
        self.jd =  jd
        self.kd =  kd
    def __str__(self):
        return str(self.id) + " " + str(self.jd) + " " + str(self.kd)
    def get_normal(self,particles):
        try:
            a = particles[self.jd] - particles[self.id]
            b = particles[self.kd] - particles[self.id]
            self.normal = Vector3D.cross_prod(a, b)
            self.normal.normalize()
            return self.normal
        except ZeroDivisionError as e:
            print "Problem rise in plane [ %s ] normal has zero length"%(self.vertices)
    def inMembrane(self, p_index):
#         if p_index in self.points:
#             return True
        return False
    