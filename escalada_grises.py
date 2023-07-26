import cv2
imagen = cv2.imread('C:\\Users\\ANGEL\\Desktop\\Angel\\OutUni\\phyton\\Udemy\\Udemy_Python\\contorno.jpg')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)


cv2.imshow('Imagen a Gris:', gris)
cv2.imshow('Imagen a Original:', imagen)
cv2.waitKey(0) #1-> video | 0->img
cv2.destroyAllWindows()
