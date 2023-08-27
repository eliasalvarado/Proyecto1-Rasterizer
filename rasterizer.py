from gl import Renderer, Model
import shaders

""" #Dims para fondo
width = 500
height = 500 """

#Dims para fondo
width = 1240
height = 2048

rend = Renderer(width, height)

rend.glBackgroundTexture("fondo.bmp")
rend.glClearBackground()

#Primer modelo
#Ojo de Sauron
scaleDimSauron = 4
sauronEye = Model(filename = "sauroneye.obj",
            translate=(0.2, 31.2, -100),
            rotate=(0.3, 99.7, 0),
            scale=(scaleDimSauron, scaleDimSauron, scaleDimSauron))
for texture in ["sauroneye.bmp"]:
    sauronEye.loadTexture(texName=texture)
sauronEye.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.gouradShader)
sauronEye.directionalLight = (-0.3, -0.4, -0.5)
rend.glAddModel(sauronEye)

""" #Segundo modelo
#Anillo del poder
scaleDimRing = 4
powerRing = Model(filename = "anillo1.obj",
            translate=(0.3, -13, -40),
            rotate=(0, 0, 0.5),
            scale=(scaleDimRing, scaleDimRing, scaleDimRing))
for texture in ["anillo1tex.bmp"]:
    powerRing.loadTexture(texName=texture)
powerRing.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.multiTextureShader)
powerRing.directionalLight = (0, 0, -0.7)
rend.glAddModel(powerRing) """

""" #Tercer modelo
#Espada Narsil rota
scaleDimSword = 10
narsilSword = Model(filename = "sword4.obj",
            translate=(0, -13, -40),
            rotate=(-90, 0, 0),
            scale=(scaleDimSword, scaleDimSword, scaleDimSword))
for texture in ["sword1tex.bmp"]:
    narsilSword.loadTexture(texName=texture)
narsilSword.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.pruebaShader)
narsilSword.directionalLight = (0, 1, 0)
rend.glAddModel(narsilSword) """

""" #Cuarto modelo
#Argonath
scaleDimStatue = 6
argonathStatue = Model(filename = "estatua.obj",
            translate=(0, -8, -50),
            rotate=(0.2, 0, 0),
            scale=(scaleDimStatue, scaleDimStatue, scaleDimStatue))
for texture in ["estatuatex.bmp"]:
    argonathStatue.loadTexture(texName=texture)
argonathStatue.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.pruebaShader)
argonathStatue.directionalLight = (0, 0, -0.5)
rend.glAddModel(argonathStatue) """

""" #Quinto modelo
#Espada de Frodo - Dardo
scaleDimDardo = 1.5
dardo = Model(filename = "swordprueba.obj",
            translate=(-17, -26, -100),
            rotate=(80, -10.1, 0),
            scale=(scaleDimDardo, scaleDimDardo, scaleDimDardo))
for texture in ["swordtex.bmp", "swordtex1.bmp"]:
    dardo.loadTexture(texName=texture)
dardo.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.neonShader)
dardo.directionalLight = (1, 0, 0)
rend.glAddModel(dardo) """

""" #Sexto modelo
#Hacha Gilmi
scaleDimAxe = 20
gimliLeft = Model(filename = "hacha.obj",
            translate=(-2, -40, -50),
            rotate=(0, 0, 0.5),
            scale=(scaleDimAxe, scaleDimAxe, scaleDimAxe))
for texture in ["hachatex2.bmp"]:
    gimliLeft.loadTexture(texName=texture)
gimliLeft.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.multiTextureShader)
gimliLeft.loadNormalMap(filename="hachanormal.bmp")
gimliLeft.directionalLight = (1, 0, -1)
rend.glAddModel(gimliLeft)

gimliRight = Model(filename = "hacha.obj",
            translate=(2, -40, -50),
            rotate=(0, 0, -0.5),
            scale=(scaleDimAxe, scaleDimAxe, scaleDimAxe))
for texture in ["hachatex2.bmp"]:
    gimliRight.loadTexture(texName=texture)
gimliRight.setShaders(vertex= shaders.vertexShader,
            fragment= shaders.multiTextureShader)
gimliRight.loadNormalMap(filename="hachanormal.bmp")
gimliRight.directionalLight = (1, 0, -1)
rend.glAddModel(gimliRight) """



rend.glLookAt(camPos=(0, 0, 0),
                eyePos=(0, 0, -500))

rend.glRender()
rend.glFinish("output.bmp")

