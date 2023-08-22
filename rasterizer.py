from gl import Renderer, Model
import shaders

""" #Dims para fondo
width = 1200
height = 630 """

#Dims para fondo
width = 2560
height = 4170

#scaleDim = 50

rend = Renderer(width, height)
rend.directionalLight = (-1, 0, -1)

rend.glBackgroundTexture("fondo1.bmp")
rend.glClearBackground()

""" rend.directionalLight = (0, 0, -1)
m1 = Model(filename = "model.obj",
            translate=(0, 0, -500),
            rotate=(0, 0, 0),
            scale=(scaleDim, scaleDim, scaleDim))
for texture in ["model.bmp"]:
    m1.loadTexture(texName=texture)
m1.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.customShader)
m1.loadNormalMap("modelnormal.bmp")
rend.glAddModel(m1) """

""" m1 = Model(filename = "anillo.obj",
            translate=(0, 0, -500),
            rotate=(70, 0, 20),
            scale=(scaleDim, scaleDim, scaleDim))
for texture in ["anillotex.bmp"]:
    m1.loadTexture(texName=texture)
m1.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.multiTextureShader)
m1.loadNormalMap("swordnormal.bmp")
rend.glAddModel(m1) """


""" m1 = Model(filename = "sword.obj",
            translate=(0, 100, -500),
            rotate=(95, 50, 0),
            scale=(scaleDim, scaleDim, scaleDim))
for texture in ["swordtex.bmp", "swordtex1.bmp"]:
    m1.loadTexture(texName=texture)
m1.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.multiTextureShader)
m1.loadNormalMap("swordnormal.bmp")
rend.glAddModel(m1) """

""" #Ojo de Sauron
scaleDimSauron = 4
sauron = Model(filename = "eye1.obj",
            translate=(-355, 230, -500),
            rotate=(0.5, 99.5, 0),
            scale=(scaleDimSauron, scaleDimSauron, scaleDimSauron))
for texture in ["eyetex1.bmp"]:
    sauron.loadTexture(texName=texture)
sauron.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.pruebaShader)
rend.glAddModel(sauron) """

scaleDimSauron = 5
sauron = Model(filename = "eye1.obj",
            translate=(5, 160, -500),
            rotate=(0.3, 99.7, 0),
            scale=(scaleDimSauron, scaleDimSauron, scaleDimSauron))
for texture in ["eyetex1.bmp"]:
    sauron.loadTexture(texName=texture)
sauron.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.pruebaShader)
rend.glAddModel(sauron)

rend.glLookAt(camPos=(0, 0, 0),
                eyePos=(0, 0, -500))

rend.glRender()
rend.glFinish("output.bmp")

