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