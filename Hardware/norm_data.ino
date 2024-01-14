#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <limits>

//normalizando os dados https://learn.microsoft.com/pt-br/azure/machine-learning/component-reference/media/module/aml-normalization-minmax.png?view=azureml-api-2
float normalize(float x, float min_val, float max_val) {
    return (x - min_val) / (max_val - min_val);
}

int main() {

    // Vector para armazenar os dados lidos do Arduino
    std::vector<float> arduinoValues;

    // Lê os valores da string e os armazena no vetor
    while (std::getline(ss, token, ',')) {
        arduinoValues.push_back(std::stof(token));
    }

    // Encontrar os valores mínimo e máximo no vetor
    float min_val = std::numeric_limits<float>::max();
    float max_val = std::numeric_limits<float>::min();

    for (float value : arduinoValues) {
        if (value < min_val) {
            min_val = value;
        }
        if (value > max_val) {
            max_val = value;
        }
    }

    // Aplicar normalização e imprimir os resultados
    std::cout << "Dados normalizados:\n";
    for (float value : arduinoValues) {
        float normalized_value = normalize(value, min_val, max_val);
        std::cout << normalized_value << " ";
    }

    return 0;
}
