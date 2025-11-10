#include <iostream>

const long long MOD = 1e9 + 7;

// Modular addition
long long addMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) + (b % mod)) % mod;
}

// Modular subtraction
long long subMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) - (b % mod) + mod) % mod;
}

// Modular multiplication
long long mulMod(long long a, long long b, long long mod = MOD) {
    return ((a % mod) * (b % mod)) % mod;
}

// Modular exponentiation (fast power)
long long powerMod(long long base, long long exp, long long mod = MOD) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Modular inverse using Fermat's little theorem (when mod is prime)
long long modInverse(long long a, long long mod = MOD) {
    return powerMod(a, mod - 2, mod);
}

// Modular division
long long divMod(long long a, long long b, long long mod = MOD) {
    return mulMod(a, modInverse(b, mod), mod);
}

int main() {
    long long a = 1000000000;
    long long b = 999999999;

    std::cout << "Add: " << addMod(a, b) << std::endl;
    std::cout << "Mul: " << mulMod(a, b) << std::endl;
    std::cout << "Power: " << powerMod(2, 10) << std::endl;
    std::cout << "Inverse: " << modInverse(3) << std::endl;

    return 0;
}