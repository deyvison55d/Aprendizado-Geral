class Livro():
    def __init__(self, autor, titulo, num_paginas, genero):
        self.autor = autor
        self.titulo = titulo
        self.num_paginas = num_paginas
        self.genero = genero
    
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo

meulivro = Livro(autor='Luiz', titulo='A bela e a fera', genero='Romance', num_paginas=100, )

print('título do livro: ',meulivro.titulo)

meulivro.set_titulo('abobora')

print(meulivro.get_titulo())