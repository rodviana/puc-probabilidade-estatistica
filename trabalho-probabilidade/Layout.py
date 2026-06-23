"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    Layout.py
    Classe para estilização dos layouts dos gráficos
"""


class Layout:

    def __init__(self):
        """
            Construtor: Classe Layout.
        """
        self.titulo = "titulo"
        self.axis_x_titulo = "x_titulo"
        self.axis_y_titulo = "y_titulo"
        self.titulo_size = 10
        self.axis_xy_titulo_size = 8
        self.label_size = 10
        self.barras_size = 1

    def layout_change(self, titulo_principal: str, titulo_x: str, titulo_y: str, titulo_xy_size: int,
                      label_size: int, titulo_size: int, barra_size: float):
        """
            Método para definir o layout de um gráfico

            Recebe como parâmetros:
                str titulo_principal:
                título do Gráfico

                str titulo_x:
                define o título do eixo horizontal

                str titulo_y:
                define o título do eixo vertical

                int titulo_xy_size:
                define o tamanho da fonte dos rótulos dos eixos vertical e horizontal

                int label_size:
                define o tamanho dos elementos do gráfico

                int titulo_size:
                define o tamanho da fonte do título

                float barra_size:
                define o tamanho da barras do gráfico
        """
        self.titulo = titulo_principal
        self.axis_x_titulo = titulo_x
        self.axis_y_titulo = titulo_y
        self.axis_xy_titulo_size = titulo_xy_size
        self.label_size = label_size
        self.titulo_size = titulo_size
        self.barras_size = barra_size
