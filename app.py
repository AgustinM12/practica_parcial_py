def girl_or_boy(nombre_usuario):  
    letras = {}
    
    for letra in nombre_usuario:
        if letra.isupper():
            return "No se admiten nombres con mayúsculas"
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
            
    if len(letras) % 2 == 0:
        return "¡ITS A GIRL!"
    else: 
        return "¡ITS A BOY!"

assert girl_or_boy("Juan") == "No se admiten nombres con mayúsculas", "Error en la función" 

print(girl_or_boy("joan"))