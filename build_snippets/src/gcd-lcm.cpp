#include <iostream>
#include <numeric> // For std::gcd and std::lcm (C++17)
#include <algorithm>

// Manual GCD implementation (Euclidean algorithm)
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Manual LCM implementation
long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

// Extended Euclidean Algorithm
// Finds gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)
long long extendedGCD(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long gcd = extendedGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return gcd;
}

int main() {
    long long a = 48, b = 18;

    // Using manual implementation
    std::cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << std::endl;
    std::cout << "LCM(" << a << ", " << b << ") = " << lcm(a, b) << std::endl;

    // Using C++17 STL
    std::cout << "STL GCD: " << std::gcd(a, b) << std::endl;
    std::cout << "STL LCM: " << std::lcm(a, b) << std::endl;

    // Extended GCD
    long long x, y;
    long long g = extendedGCD(a, b, x, y);
    std::cout << "Extended GCD: " << g << std::endl;
    std::cout << a << "*" << x << " + " << b << "*" << y << " = " << g << std::endl;

    return 0;
}