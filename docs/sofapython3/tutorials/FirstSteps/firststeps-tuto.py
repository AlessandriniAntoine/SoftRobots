from stlib3.scene import MainHeader, ContactHeader
from stlib3.physics.rigid import Floor
from stlib3.physics.rigid import Cube


def createScene(rootNode):
    """This is my first scene"""
    MainHeader(rootNode, gravity=[0.0, -981.0, 0.0])
    ContactHeader(rootNode, alarmDistance=15, contactDistance=10)

    Floor(rootNode,
          translation=[0.0, -160.0, 0.0],
          isAStaticObject=True)

    Cube(rootNode,
         translation=[0.0, 0.0, 0.0],
         uniformScale=20.0)

    return rootNode
