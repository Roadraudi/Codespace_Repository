import numpy as np

#mathematische Operationen
x = [0,1,2,3,4,5]
print(np.exp(x))

y = [0, (1/2)*np.pi, np.pi, (3/2)*np.pi, 2*np.pi]
print(np.sin(y))

#rechnen mit einem Polynom 4 Grades
coefficients = [-3, 2, -5, 4, 6]        #Koeffizienten des Polynoms -3*x^4+2*x^3-5*x^2+4*x+6
polynomial = np.poly1d(coefficients)
result = polynomial(2)
print("f(2) =", result)

# Polynom ableiten
derivative = np.polyder(polynomial)
print("Ableitung:", derivative)

# Polynom integrieren
integral = np.polyint(polynomial)
print("Integration:", integral)

# Beispiel für lineare Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # Matrixmultiplikation
print(np.linalg.det(A))  # Determinante berechnen
print(np.linalg.inv(A))  # Inverse Matrix berechnen