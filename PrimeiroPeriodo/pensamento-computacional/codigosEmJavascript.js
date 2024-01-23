// TEMA 5: Noções de Programação: Exemplos Com Manipulação de Imagens Digitais

// Módulo 1: Manipulação de dados 
// (Definir instruções para manipulação simples de dados)

// Manipular um pixel por vez
const img = new SimpleImage("circulo.bmp");  // Armazena imagem na variável "img"
img.setZoom(20);                             // Zoom de 20x do tamanho original
const pixel = img.getPixel(4, 4);            // Referência do pixel e atribui à variável "pixel"
pixel.setRed(255);                           // Ajustar para 255 o nível de vermelho do pixel em questão
pixel.setGreen(0);                           // Ajustar para 0 o nível de verde do pixel em questão
pixel.setBlue(0);                            // Ajustar para 0 o nível de azul do pixel em questão
console.log(img);                            // Apresenta imagem na tela

// Módulo 2: Repetição for
// (Distinguir a estrutura de repetição for)

// Manipular todos os pixels de uma vez através da Repetição for (Loop)
const img1 = new SimpleImage("passaro.jpg");

for (let pixel of img1) {
    pixel.setRed(0);
    pixel.setGreen(0);
    pixel.setBlue(0);
}

console.log(img1);