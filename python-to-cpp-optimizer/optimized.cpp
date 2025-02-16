#include <iostream>
#include <vector>
#include <limits>
#include <ctime>
#include <iomanip>

// LCG Constants
const unsigned int A = 1664525;
const unsigned int C = 1013904223;
const unsigned int M = 1U << 32;

unsigned int lcg(unsigned int& seed) {
    seed = (A * seed + C) % M;
    return seed;
}

long long max_subarray_sum(int n, unsigned int seed, int min_val, int max_val) {
    std::vector<int> random_numbers(n);
    for (int i = 0; i < n; ++i) {
        random_numbers[i] = (lcg(seed) % (max_val - min_val + 1)) + min_val;
    }

    long long max_sum = std::numeric_limits<long long>::min();
    for (int i = 0; i < n; ++i) {
        long long current_sum = 0;
        for (int j = i; j < n; ++j) {
            current_sum += random_numbers[j];
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
        }
    }
    return max_sum;
}

long long total_max_subarray_sum(int n, unsigned int initial_seed, int min_val, int max_val) {
    long long total_sum = 0;
    unsigned int seed = initial_seed;
    for (int i = 0; i < 20; ++i) {
        seed = lcg(seed);
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    return total_sum;
}

int main() {
    int n = 10000;
    unsigned int initial_seed = 42;
    int min_val = -10;
    int max_val = 10;

    std::clock_t start_time = std::clock();
    long long result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    std::clock_t end_time = std::clock();

    std::cout << "Total Maximum Subarray Sum (20 runs): " << result << "\n";
    std::cout << "Execution Time: " << std::fixed << std::setprecision(6)
              << (double)(end_time - start_time) / CLOCKS_PER_SEC << " seconds\n";

    return 0;
}

