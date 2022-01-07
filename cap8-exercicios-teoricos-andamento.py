'''
Exercícios Teoricos | Capítulo 8

1) O que entende por imagem bitmap?

São compostos por pontos individuais e minúsculos que se misturam para criar uma imagem clara;
Contrariamente ao que acontece com as imagens vetoriais, o formato bitmap não permite que as imagens
possam ser esticadas ou ampliadas sem comprometer a qualidade;

Exemplo:

Imagine que divide uma imagem em milhares de quadrados! Esses quadrados são designados de bitmaps.

Assim, cada um dos quadrados vai conter dados relacionados com as cores que o mesmo representa. No final,
independentemente dos formatos de imagem, irá obter uma fotografia perfeita (isso se os dpi forem suficientes).

É importante frisar que os gráficos raster ou bitmaps estão intimamente relacionados, embora não sejam
exatamente a mesma coisa:

Um bitmap refere-se a um tipo específico de armazenamento de dados – um mapa de bits.
Um pixmap, por exemplo, é um mapa de pixels.
Um gráfico raster pode ser qualquer uma das opções anteriores, dependendo essencialmente
da complexidade dos dados armazenados.

As imagens bitmaps têm vários formatos por onde pode optar, sendo que cada um tem vantagens e desvantagens!
Os mais comuns são: BMP, GIF, JPEG, EXIF, PNG e TIFF.
Windows usa exclusivamente BMP
GIF, PNG e JPEG são utilizados maioritariamente para transferências web uma vez que são simples de compactar
EXIF estão por norma associados a câmaras fotográficas
BMP são arquivos grandes e completos que não podem ser compactados

Obs: o tamanho do arquivo está diretamente relacionado com a sua qualidade. Quanto maior a qualidade,
maior o tamanho do ficheiro. Um gráfico bitmap pode ficar pixelizado. se esticar a imagem, o mais provável
é que os pixels fiquem visíveis, tornando a imagem num borrão.


2) O que entende por pixel?

É uma combinação dos termos “picture” e “element”. Ou seja, “elemento de imagem”.

Um pixel é a menor unidade que compõe uma imagem, seja ela uma foto ou um frame (quadro) de um vídeo.
Eles estão presentes não só em filmes, animações e capturas fotográficas, como também são parte importante das
telas de TVs, monitores e smartphones e de sensores de câmeras.

Cada pixel é baseado nas três cores básicas: vermelho, verde e azul. Cada cor possui 256 tonalidades,
o que proporciona até 16 milhões de combinações de cores diferentes.


3) O que entende por resolução de uma imagem?

É o nível de detalhe que uma imagem comporta. O termo se aplica igualmente a imagens digitais, imagens em
filme e outros tipos de imagem. Resoluções mais altas significam mais detalhes na imagem.

a resolução quantifica quão próximas as linhas podem ficar umas das outras e ainda assim serem visivelmente
determinadas. As unidades de resolução podem ser ligadas a tamanhos físicos (por exemplo, linhas por mm,
linhas por polegada etc.) ou ao tamanho total de uma figura (linhas por altura da imagem, também conhecidas
simplesmente por linhas ou linhas de televisão).


4) O que entende por modo RGB?

A abreviatura RGB (Red, Green, Blue) representa o método de cores utilizadas em monitores e eletrônicos emissores,
fazendo referência aos tons vermelho, verde e azul para compor imagens coloridas nas telas.

Já o padrão CMYK (Cyan, Magenta, Yellow, Black) emprega as cores Ciano, Magenta, Amarelo e Preto e é
utilizado para produção de materiais impressos. Sua proposta é reproduzir, da maneira mais fiel possível,
a maioria das cores do espectro visível e é por isso que é o esquema oficial do universo gráfico.


5) A ordem e o modo de percorrer uma imagem são irrelevantes. Concorda com esta afirmação?

Não. (pesquisar melhor o porquê)


6) Quais as vantagens e os inconvenientes de usar o mecanismo de abstração procedimental?


7) O que entende por filtro ou máscara?

Uma maneira de melhorar a qualidade da imagem baseia-se numa técnica que permite suavizar as transições
entre intensidades de píxeis vizinhos. Máscaras são conhecidas por operadores de Sobel.


8) O que entende por convolução?

A convolução é calculada pelo seguinte método: a imagem representa a matriz da imagem original
e o filtro é a matriz do kernel.
(FILTRO GAUSSIANO)

9) O que entende por operadores de Sobel?

Uma imagem digital é representada por uma matriz que armazena o valor RGB / BGR / HSV (qualquer espaço de cor ao qual
a imagem pertence) de cada pixel em linhas e colunas.
A derivada de uma matriz é calculada por um operador chamado Laplaciano . Para calcular um Laplaciano, você precisará
calcular primeiro duas derivadas, chamadas derivadas de Sobel , cada uma das quais leva em consideração as variações
do gradiente em uma determinada direção: uma horizontal, a outra vertical.

Derivada horizontal de Sobel (Sobel x) : É obtida através da convolução da imagem com uma matriz denominada
kernel que sempre tem tamanho ímpar. O kernel com tamanho 3 é o caso mais simples.

Derivada vertical de Sobel (Sobel y) : É obtida através da convolução da imagem com uma matriz denominada
kernel que sempre tem tamanho ímpar. O kernel com tamanho 3 é o caso mais simples.

A convolução é calculada pelo seguinte método: a imagem representa a matriz da imagem original
e o filtro é a matriz do kernel.


10) Quanto maior for o filtro usado, melhor se consegue o efeito pretendido. Concorda com esta afirmação?


11) Quando se usa um filtro, por que razão se cria uma nova imagem?


'''