"""
MODULE:       r.agent.*
AUTHOR(S):    michael lustenberger inofix.ch
PURPOSE:      library file for the r.agent.* suite
COPYRIGHT:    (C) 2011 by Michael Lustenberger and the GRASS Development Team

              This program is free software under the GNU General Public
              License (>=v2). Read the file COPYING that comes with GRASS
              for details.
"""

class Agent(object):
    """Generic Agent class with limited capabilities, as a basis for
       child classes."""
    def __init__(self, timetolive, world, position=[]):
        self.ttl = timetolive
        self.world = world
        self.position = position
        self.knowscompass = False
        self.freedom = 0
    def setposition(self, position):
        if position and position != []:
            self.position[0] = position[0]
            self.position[1] = position[1]
    def getposition(self):
        return self.position
    def move(self, nrofsteps, direction):
        pass
    def age(self):
        if self.ttl > 0:
            self.ttl -= 1
            return True
        else:
            self.snuffit()
            return False
    def snuffit(self):
        """to die peacefully and without pain."""
        self.world.kill(self)

