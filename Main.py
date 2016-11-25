from FB_ejercicios import Usuario

user = Usuario()

print(type(user))

print("Nombre de usuario antes de la petición")
print(user.nombre)

respuesta = user.obtenInformacion()

print("Respuestaaaaa")
print(type(respuesta))
print ("hola")