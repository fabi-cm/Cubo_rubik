class RubikCube:
    def __init__(self):
        # Inicializar el cubo con colores predeterminados
        self.cube = [
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
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

    def print_cube(self):
        for face in self.cube:
            for row in face:
                print(' '.join(row))
            print()

# Ejemplo de uso
cube = RubikCube()
if cube.load_cube_from_file('configuracion_cubo.txt'):
    cube.print_cube()