#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Reading from file
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening input file" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        // Process line
        std::cout << line << std::endl;
    }
    inputFile.close();

    // Writing to file
    std::ofstream outputFile("output.txt");
    if (!outputFile.is_open()) {
        std::cerr << "Error opening output file" << std::endl;
        return 1;
    }

    outputFile << "Hello, File!" << std::endl;
    outputFile.close();

    return 0;
}