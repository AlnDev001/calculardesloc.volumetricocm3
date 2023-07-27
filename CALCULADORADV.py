import math

def calcular_deslocamento_volumetrico(diametro_extrerno, diametro_interno, altura_engrenagem):
    volume = (math.pi / 4) * (diametro_extrerno**2 - diametro_interno**2) - altura_engrenagem
    return volume

# Pedir ao usuario as informaçoes necessarias

try: 
    diametro_extrerno = float(input("Digite  o diametro externo da engrenagem : "))
    diametro_interno = float (input("Digite o diamtro interno da engrenagem : "))
    altura_engrenagem = float (input("Digite a altura da engrenagem: "))

    deslocameto_volumetrico = calcular_deslocamento_volumetrico (diametro_extrerno, diametro_interno, altura_engrenagem)
    print(f"O deslocamento volumetrico da engrenagem é: {deslocameto_volumetrico} unidades cubicas")
except ValueError:
    print("Por favor, digite valores numericos validos para os diametros externo e interno, e a altura da engrenagem.")
