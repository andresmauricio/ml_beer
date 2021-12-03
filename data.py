from constans import Color, Sabor, Aroma

X = [
    [Color.YELLOW.value, Sabor.SUAVE.value, Aroma.GASEOSA.value],
    [Color.RED.value, Sabor.DULCE.value, Aroma.FRUTAS.value],
    [Color.RED.value, Sabor.DULCE.value, Aroma.NUECES.value],
    [Color.MARRON.value, Sabor.AMARGO.value, Aroma.CAFE.value],
    [Color.BLACK.value, Sabor.AMARGO.value, Aroma.MADERA.value],
    [Color.GLOD.value, Sabor.ACIDO.value, Aroma.FRUTAS.value],
]

Y = [
    'LAGER',
    'ALE',
    'ALE',
    'STOUT',
    'PORTER',
    'LAMBIC'
]

test_data = [
    [Color.MARRON.value, Sabor.AMARGO.value, Aroma.CAFE.value],
    [Color.RED.value, Sabor.DULCE.value, Aroma.FRUTAS.value],
    [Color.GLOD.value, Sabor.SUAVE.value, Aroma.FRUTAS.value],
]
