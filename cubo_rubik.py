class RubikCube:
    def __init__(self):
        # Inicializar el cubo con colores predeterminados
        self.cube = [
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Cara blanca
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # Cara naranja
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Cara roja
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Cara verde
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Cara azul
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]   # Cara amarilla
        ]

    def load_cube_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) != 18:
                    print("Error: El archivo debe contener 18 líneas")
                    return False

                for i, line in enumerate(lines):
                    line = line.strip().split()
                    if len(line) != 3:
                        print(f"Error en la línea {i+1}: Debe haber 3 colores separados por espacios")
                        return False

                    for j, color in enumerate(line):
                        if color not in ['W', 'O', 'R', 'G', 'B', 'Y']:
                            print(f"Error en la línea {i+1}, columna {j+1}: Color inválido '{color}'")
                            return False

                        self.cube[i // 3][i % 3][j] = color

                return True
        except FileNotFoundError:
            print(f"Error: El archivo '{filename}' no existe")
            return False

    def rotate_face_clockwise(self, face):
        # Rotar la cara dada en sentido horario
        rotated_face = [
            [self.cube[face][2][0], self.cube[face][1][0], self.cube[face][0][0]],
            [self.cube[face][2][1], self.cube[face][1][1], self.cube[face][0][1]],
            [self.cube[face][2][2], self.cube[face][1][2], self.cube[face][0][2]]
        ]
        self.cube[face] = rotated_face

    def rotate_face_counter_clockwise(self, face):
        # Rotar la cara dada en sentido anti-horario
        rotated_face = [
            [self.cube[face][0][2], self.cube[face][1][2], self.cube[face][2][2]],
            [self.cube[face][0][1], self.cube[face][1][1], self.cube[face][2][1]],
            [self.cube[face][0][0], self.cube[face][1][0], self.cube[face][2][0]]
        ]
        self.cube[face] = rotated_face

    def U(self):
        # Girar la cara superior (Up) en sentido horario
        self.rotate_face_clockwise(0)

    def U_prime(self):
        # Girar la cara superior (Up) en sentido anti-horario
        self.rotate_face_counter_clockwise(0)

    def F(self):
        # Girar la cara frontal (Front) en sentido horario
        self.rotate_face_clockwise(1)

    def F_prime(self):
        # Girar la cara frontal (Front) en sentido anti-horario
        self.rotate_face_counter_clockwise(1)

    def L(self):
        # Girar la cara izquierda (Left) en sentido horario
        self.rotate_face_clockwise(2)

    def L_prime(self):
        # Girar la cara izquierda (Left) en sentido anti-horario
        self.rotate_face_counter_clockwise(2)

    def R(self):
        # Girar la cara derecha (Right) en sentido horario
        self.rotate_face_clockwise(3)

    def R_prime(self):
        # Girar la cara derecha (Right) en sentido anti-horario
        self.rotate_face_counter_clockwise(3)

    def D(self):
        # Girar la cara inferior (Down) en sentido horario
        self.rotate_face_clockwise(4)

    def D_prime(self):
        # Girar la cara inferior (Down) en sentido anti-horario
        self.rotate_face_counter_clockwise(4)

    def B(self):
        # Girar la cara trasera (Back) en sentido horario
        self.rotate_face_clockwise(5)

    def B_prime(self):
        # Girar la cara trasera (Back) en sentido anti-horario
        self.rotate_face_counter_clockwise(5)

    def X(self):
        # Girar todo el cubo en sentido horario alrededor del eje X
        self.F()
        self.B_prime()
        self.L_prime()
        self.R()
        self.U()
        self.D_prime()

    def X_prime(self):
        # Girar todo el cubo en sentido anti-horario alrededor del eje X
        self.F_prime()
        self.B()
        self.L()
        self.R_prime()
        self.U_prime()
        self.D()

    def Y(self):
        # Girar todo el cubo en sentido horario alrededor del eje Y
        self.U()
        self.D_prime()
        self.F_prime()
        self.B()
        self.L_prime()
        self.R()

    def Y_prime(self):
        # Girar todo el cubo en sentido anti-horario alrededor del eje Y
        self.U_prime()
        self.D()
        self.F()
        self.B_prime()
        self.L()
        self.R_prime()

    def Z(self):
        # Girar todo el cubo en sentido horario alrededor del eje Z
        self.L()
        self.R_prime()
        self.F()
        self.B_prime()
        self.U()
        self.D_prime()

    def Z_prime(self):
        # Girar todo el cubo en sentido anti-horario alrededor del eje Z
        self.L_prime()
        self.R()
        self.F_prime()
        self.B()
        self.U()
        self.D_prime()

    def print_cube(self):
        for face in self.cube:
            for row in face:
                print(' '.join(row))
            print()

# Pruebas de uso:
cube = RubikCube()
if cube.load_cube_from_file('configuracion_cubo.txt'):
    cube.print_cube()
    print("Realizando movimientos...")
    cube.U()
    cube.print_cube()
    cube.F()
    cube.print_cube()
    cube.R_prime()
    cube.print_cube()
