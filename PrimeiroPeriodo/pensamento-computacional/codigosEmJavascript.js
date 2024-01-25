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

// Módulo 3: As expressões em código de computador
// (Reconhecer expressões)

// Uso da expressão aritmética "multiplicar" para diminuir a intensidade da cor verde na imagem, e deixá-la mais laranja.
const img2 = new SimpleImage("flores.jpg");

for (let pixel of img2) {
    pixel.setGreen(pixel.getGreen() * 0.7);
}

console.log(img2);

// Uso de expressões aritméticas "somar" e "dividir" para deixar a imagem em escala de cinza
const img3 = new SimpleImage("flores.jpg");

for (let pixel of img3) {
    const soma = (pixel.getRed() + pixel.getGreen() + pixel.getBlue());
    const media = soma / 3;
    pixel.setRed(media);
    pixel.setGreen(media);
    pixel.setBlue(media);
}

console.log(img3);

// Módulo 4: A estrutura condicional if
// (Distinguir a estrutura condicional if)

// Uso da condição if para distinguir os pixels em vermelho 255, verde/azul 0 e transformá-los em cinza
const img4 = new SimpleImage("RGB.png");
for (let pixel of img4) {

    if (pixel.getRed() == 255 && pixel.getGreen() == 0 && pixel.getBlue() == 0) {
        pixel.setRed(120);
        pixel.setGreen(120);
        pixel.setBlue(120);
    }

}
console.log(img4);