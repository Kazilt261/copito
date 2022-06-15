

from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.easy_shaders as es
import grafica.scene_graph as sg
from grafica.assets_path import getAssetPath

def create_skybox(pipeline,box):
    shapeSky = bs.createTextureCube('cieloazul.jfif')
    gpuSky = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuSky)
    gpuSky.fillBuffers(shapeSky.vertices, shapeSky.indices, GL_STATIC_DRAW)
    gpuSky.texture = es.textureSimpleSetup(
        getAssetPath(box), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    
    skybox = sg.SceneGraphNode("skybox")
    skybox.transform = tr.matmul([tr.translate(0, 0, 0.99), tr.uniformScale(2)])
    skybox.childs += [gpuSky]

    return skybox
def create_sky(pipeline):
    shapeSky = bs.createTextureQuad(1, 1)
    gpuSky = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuSky)
    gpuSky.texture = es.textureSimpleSetup(
        getAssetPath("cieloazul.jfif"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    gpuSky.fillBuffers(shapeSky.vertices, shapeSky.indices, GL_STATIC_DRAW)

    sky = sg.SceneGraphNode("sky")
    sky.transform = tr.matmul([tr.translate(0, 0, 1.99),tr.scale(2, 2, 1)])
    sky.childs += [gpuSky]

    return sky

def create_floor(pipeline,suelo):
    shapeFloor = bs.createTextureQuad(0, 0)
    gpuFloor = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuFloor)
    gpuFloor.texture = es.textureSimpleSetup(
        getAssetPath(suelo), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    gpuFloor.fillBuffers(shapeFloor.vertices, shapeFloor.indices, GL_STATIC_DRAW)

    floor = sg.SceneGraphNode("floor")
    floor.transform = tr.matmul([tr.translate(0, 0, 0),tr.scale(2, 2, 1)])
    floor.childs += [gpuFloor]

    return floor
    