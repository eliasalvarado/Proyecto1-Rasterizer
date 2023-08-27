from gl import Renderer, Model
import shaders

#Dimensiones para fondo
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
sauronEye.loadTexture(texName="sauroneye.bmp")
sauronEye.setShaders(vertex= shaders.vertexShader,
                    fragment= shaders.multiTextureShader)
sauronEye.directionalLight = (-0.3, -0.4, -0.5)
rend.glAddModel(sauronEye)

#Segundo modelo
#Anillo del poder
scaleDimRing = 4
powerRing = Model(filename = "powerRing.obj",
                translate=(0.3, -13, -40),
                rotate=(0, 0, 0.5),
                scale=(scaleDimRing, scaleDimRing, scaleDimRing))
powerRing.loadTexture(texName="powerRing.bmp")
powerRing.setShaders(vertex= shaders.vertexShader,
                    fragment= shaders.metallicShader)
powerRing.directionalLight = (0, 0, -0.7)
rend.glAddModel(powerRing)

#Tercer modelo
#Espada Narsil rota
scaleDimSword = 10
narsilSword = Model(filename = "narsil.obj",
                translate=(0, -13, -40),
                rotate=(-90, 0, 0),
                scale=(scaleDimSword, scaleDimSword, scaleDimSword))
narsilSword.loadTexture(texName="narsil.bmp")
narsilSword.setShaders(vertex= shaders.vertexShader,
                    fragment= shaders.heightColorShader)
narsilSword.directionalLight = (0, -1, 0)
rend.glAddModel(narsilSword)

#Cuarto modelo
#Argonath
scaleDimStatue = 6
argonathStatue = Model(filename = "argonath.obj",
                translate=(0, -8, -50),
                rotate=(0.2, 0, 0),
                scale=(scaleDimStatue, scaleDimStatue, scaleDimStatue))
argonathStatue.loadTexture(texName="argonath.bmp")
argonathStatue.setShaders(vertex= shaders.vertexShader,
                        fragment= shaders.sepiaColorShader)
argonathStatue.directionalLight = (0, 0, -0.5)
rend.glAddModel(argonathStatue)

#Quinto modelo
#Espada de Frodo - Dardo
scaleDimDardo = 1.5
dardo = Model(filename = "dardo.obj",
            translate=(-17, -26, -100),
            rotate=(80, -10.1, 0),
            scale=(scaleDimDardo, scaleDimDardo, scaleDimDardo))
texturesDardo = ["dardotex.bmp", "dardotex1.bmp"]
for texture in texturesDardo:
    dardo.loadTexture(texName=texture)
dardo.setShaders(vertex= shaders.vertexShader,
                fragment= shaders.neonShader)
dardo.directionalLight = (1, 0, 0)
rend.glAddModel(dardo)

#Sexto modelo
#Hacha Gilmi
scaleDimAxe = 20
gimliLeft = Model(filename = "gilmi.obj",
                translate=(-2, -40, -50),
                rotate=(0, 0, 0.5),
                scale=(scaleDimAxe, scaleDimAxe, scaleDimAxe))
gimliLeft.loadTexture(texName="gilmi.bmp")
gimliLeft.setShaders(vertex= shaders.vertexShader,
                    fragment= shaders.normalMapShader)
gimliLeft.loadNormalMap(filename="gilminormal.bmp")
gimliLeft.directionalLight = (1, 0, -1)
rend.glAddModel(gimliLeft)

gimliRight = Model(filename = "gilmi.obj",
                translate=(2, -40, -50),
                rotate=(0, 0, -0.5),
                scale=(scaleDimAxe, scaleDimAxe, scaleDimAxe))
gimliRight.loadTexture(texName="gilmi.bmp")
gimliRight.setShaders(vertex= shaders.vertexShader,
                    fragment= shaders.normalMapShader)
gimliRight.loadNormalMap(filename="gilminormal.bmp")
gimliRight.directionalLight = (1, 0, -1)
rend.glAddModel(gimliRight)



rend.glLookAt(camPos=(0, 0, 0),
                eyePos=(0, 0, -500))

rend.glRender()
rend.glFinish("rasterizer.bmp")

