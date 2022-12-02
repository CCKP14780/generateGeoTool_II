import maya.cmds as cmds
import random

#-----------#
#    UI     #    
#-----------#

def generateGeomTool():
    if cmds.window('genGeomTool_window',q = True,ex=True):
        cmds.deleteUI('genGeomTool_window',window = True)
    cmds.window('genGeomTool_window',t='Generate Instance Object')

#-----------#
#    OBJ    #    
#-----------#

    cmds.columnLayout(adj=True)
    cmds.frameLayout(label='Object')
    
    cmds.radioCollection('obj_radioCol')
    cmds.radioButton('sphere_radioBtn',label='Sphere',select=True)
    cmds.radioButton('cube_radioBtn',label='Cube')
    cmds.radioButton('cone_radioBtn',label='Cone')
    cmds.radioButton('random_radioBtn',label='Random')
    
#-----------#
#  SETTING  #    
#-----------# 

    cmds.frameLayout(l='Setting')
    cmds.intSliderGrp('row_intSliderGrp',l='Row',field=True,value=1)

#-----------#
# TRANSFORM #    
#-----------#    
    
    cmds.frameLayout(label='Transform')
    cmds.text(label='Rotate')
    cmds.floatSliderGrp('rotMin_floatSliderGrp',l='min',field=True,minValue=0,maxValue=360,value=0)
    cmds.floatSliderGrp('rotMax_floatSliderGrp',l='max',field=True,minValue=0,maxValue=360,value=360)
       
    cmds.text(label='Scale')
    cmds.floatSliderGrp('sclMin_floatSliderGrp',l='min',field=True,minValue=0.1,maxValue=2,value=0.2)
    cmds.floatSliderGrp('sclMax_floatSliderGrp',l='max',field=True,minValue=0.1,maxValue=2,value=1.2)
   
#-----------#
#   BUTTON  #    
#-----------#

    cmds.button('create_btn',label='Create',h=30,c=createObject)
    
    cmds.showWindow('genGeomTool_window')
    cmds.window('genGeomTool_window',e = True,wh=[600,380])        

#-----------#
#  CONNECT  #    
#-----------#

def createObject(*args):
    primSel = cmds.radioCollection('obj_radioCol',q=True,select=True)
    
    if primSel == 'cube_radioBtn':
        prim = 'cube'
    if primSel == 'cone_radioBtn':
        prim = 'cone'
    if primSel == 'sphere_radioBtn':
        prim = 'sphere'
    elif primSel == 'random_radioBtn':
        prims = ['cube','sphere','cone']
        prim = random.choice(prims)
        
    roMin = cmds.floatSliderGrp('rotMin_floatSliderGrp',q=True,value=True)
    roMax = cmds.floatSliderGrp('rotMax_floatSliderGrp',q=True,value=True)
    sclMin = cmds.floatSliderGrp('sclMin_floatSliderGrp',q=True,value=True)
    sclMax = cmds.floatSliderGrp('sclMax_floatSliderGrp',q=True,value=True)
    
    num = cmds.intSliderGrp('row_intSliderGrp',q=True,value=True)
    
    generateGeo(num=num,prim=prim,rotate=[roMin,roMax],scale=[sclMin,sclMax])

#-----------#
#   FUNCT   #    
#-----------#

def generateGeo(num=5,amp=2,prim='cube',rotate=[0,360],scale=[1,1]):
    objs = []
    
    offset = (((num-1)*amp)/2)*(-1)#offset value
    for x in range(num):
        for z in range(num):
            for y in range(num):
                obj = ''
                if prim == 'cube':
                    obj = cmds.polyCube(ch=False)[0]#construction history
                elif prim == 'cone':
                    obj = cmds.polyCone(ch=False)[0]
                elif prim == 'sphere':
                    obj = cmds.polySphere(ch=False)[0]
                
                cmds.xform(obj,t=[(x*amp+offset),(y*amp),(z*amp+offset)],
                               ro=[random.uniform(rotate[0],rotate[1]),
                                   random.uniform(rotate[0],rotate[1]),
                                   random.uniform(rotate[0],rotate[1])
                               ],
                               s=[random.uniform(scale[0],scale[1]),
                                 random.uniform(scale[0],scale[1]),
                                 random.uniform(scale[0],scale[1])]
                )
                
                objs.append(obj)
    
    cmds.group(objs,n='prim_Grp')

generateGeomTool()