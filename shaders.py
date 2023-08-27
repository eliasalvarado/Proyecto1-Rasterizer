from npPirata import multMV, multMM, dot, vectorNegative, normVector, multVectorScalar, subtractVectors, reflectVector, invertMatrix, cross
from random import random

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]
    normal = kwargs["normal"]

    vt = [vertex[0], 
        vertex[1], 
        vertex[2], 
        1]

    matrix = multMM([vpMatrix, projectionMatrix, viewMatrix, modelMatrix])
    
    vt = multMV(matrix, vt)

    vt = [vt[0] / vt[3],
        vt[1] / vt[3],
        vt[2] / vt[3]]

    return vt

'''
    Shader encargado de unir varias texturas en un solo modelo.
    Su funcionamiento se basa en el promedio de la suma de los colores correspondientes a las distintas texturas.
'''
def multiTextureShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]
    dLight = kwargs["dLight"]
    normalMap = kwargs["normalMap"]
    tangent = kwargs["tangent"]

    r = g = b = 0

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight= vectorNegative(dLight)

    for texture in textures:
        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)    
            b += textureColor[2]
            g += textureColor[1]
            r += textureColor[0]

    r /= len(textures)
    g /= len(textures)
    b /= len(textures)

    intensity= dot(normal, dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]

'''
    Shader encargado hacer que el objeto, sin importar su textura, tenga un brillo más metálico
    Su funcionamiento se basa encontrar el vector reflejado entre la luz y la normal
'''
def metallicShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]
    dLight = kwargs["dLight"]
    viewDir = kwargs["camMatrix"]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2]]

    viewDir = [viewDir[0][2],
                viewDir[1][2],
                viewDir[2][2]]

    normal = normVector(normal)

    viewDir = vectorNegative(viewDir)
    reflection = reflectVector(dLight, normal)
    specIntensity = dot(viewDir, reflection)
    
    specIntensity = max(0, min(specIntensity, 1))

    r = g = b = 0

    for texture in textures:
        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)
            r += textureColor[0] * (1 - specIntensity) + specIntensity
            g += textureColor[1] * (1 - specIntensity) + specIntensity
            b += textureColor[2] * (1 - specIntensity) + specIntensity

    r /= len(textures)
    g /= len(textures)
    b /= len(textures)

    if (r > 1): r = 1
    if (g > 1): g = 1
    if (b > 1): b = 1

    return r, g, b

'''
    Shader encargado de hacer que el objeto tenga un tipo de difuminación desde la punta hasta la planta del mismo.
    Su funcionamiento se basa utilizar el punto actual en Y (vCoords[1]), y normalizarlo para conocer la proporción de
    difuminación se le debe aplicar
'''
def heightColorShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    u, v, w = kwargs["bCoords"]
    vCoords = kwargs["vCoords"]
    """ nA, nB, nC = kwargs["normals"]
    viewDir = kwargs["camMatrix"]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
            u * nA[1] + v * nB[1] + w * nC[1],
            u * nA[2] + v * nB[2] + w * nC[2]]

    viewDir = [viewDir[0][2],
                viewDir[1][2],
                viewDir[2][2]]

    glowAmount = 1 - dot(normal, viewDir) """

    r = b = g = 0
    for texture in textures:
        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)    
            r += textureColor[0]
            g += textureColor[1]
            b += textureColor[2]

    r /= len(textures)
    g /= len(textures)
    b /= len(textures)

    vCoords = normVector(vCoords)
    height_factor = vCoords[1]
    height_factor = 1 - height_factor

    r *= height_factor
    g *= height_factor
    b *= height_factor

    if (r > 1): r = 1
    if (g > 1): g = 1
    if (b > 1): b = 1

    return r, g, b

'''
    Shader encargado de hacer que el color del modelo sea más sepia.
    Su funcionamiento es muy simple, simplmente como se sabe que el sepia es la mezcla entre el amarillo y el marrón, se hacen
    las multiplicaciones respectivas a los colores para poder obtener este tono
'''
def sepiaColorShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]
    dLight = kwargs["dLight"]

    r = g = b = 1

    for texture in textures:
        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            textureColor = texture.getColor(tU, tV)    
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight= vectorNegative(dLight)
    intensity= dot(normal, dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    r *= 0.9
    g *= 0.8
    b *= 0.6

    if intensity > 0:
        return r, g, b

    else:
        return [0,0,0]

'''
    Shader encargado de hacer que el color de la textura sea un más brillante de lo normal.
    Su funcionamiento en intensificar el color actual, parecido al metálico, al utilizar el vector reflejado
'''
def neonShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]
    dLight = kwargs["dLight"]
    viewDir = kwargs["camMatrix"]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2]]

    viewDir = [viewDir[0][2],
                viewDir[1][2],
                viewDir[2][2]]

    normal = normVector(normal)

    intensity = dot(normal, dLight)
    intensity = max(0, min(intensity, 1))

    viewDir = vectorNegative(viewDir)
    reflection = reflectVector(dLight, normal)
    specIntensity = dot(viewDir, reflection)
    specIntensity = max(0, min(specIntensity, 1))

    r = b = g = specIntensity

    for texture in textures:
        if texture != None:
            tU = u * tA[0] + v * tB[0] + w * tC[0]
            tV = u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)    
            r += textureColor[0] * 2
            g += textureColor[1] * 2
            b += textureColor[2] * 2

    r /= len(textures)
    g /= len(textures)
    b /= len(textures)

    if r > 1: r = 1
    if g > 1: g = 1
    if b > 1: b = 1

    return r, g, b

'''
    Shader encargado del manejo de un Normal Map en un modelo
    Su funcionamiento se basa en el aprendido en clase
'''
def normalMapShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]
    dLight = kwargs["dLight"]
    normalMap = kwargs["normalMap"]
    tangent = kwargs["tangent"]

    r = g = b = 0

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight= vectorNegative(dLight)

    for texture in textures:
        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)    
            b += textureColor[2]
            g += textureColor[1]
            r += textureColor[0]

    r /= len(textures)
    g /= len(textures)
    b /= len(textures)

    if normalMap:
        texNormal = normalMap.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                    texNormal[1] * 2 - 1,
                    texNormal[2] * 2 - 1]

        texNormal = normVector(texNormal)

        biTangent = cross(normal, tangent)
        biTangent = normVector(biTangent)

        tangent = cross(normal, biTangent)
        tangent = normVector(tangent)

        tangentM = [[tangent[0], biTangent[0], normal[0]],
                    [tangent[1], biTangent[1], normal[1]],
                    [tangent[2], biTangent[2], normal[2]]]

        texNormal = multMV(tangentM, texNormal)
        texNormal = normVector(texNormal)

        texNormal = [texNormal[0],
                    texNormal[1],
                    texNormal[2]]

        intensity = dot(texNormal, dLight)
    else:
        intensity = dot(normal, dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if (r >= 1): r = 1
    if (g >= 1): g = 1
    if (b >= 1): b = 1

    if intensity > 0:
        return r, g, b

    else:
        return 0, 0, 0