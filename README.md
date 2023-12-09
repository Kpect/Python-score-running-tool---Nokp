# Nokp Performance Benchmark

Nokp Performance Benchmark is an open-source tool for benchmarking CPU performance. This tool provides both single-core and multi-core performance scores, along with detailed CPU information.
I spent 4 hours researching it, and it is a semi-finished product, as can be seen from the version name. I am a student with limited time, but I will use my free time to continuously improve and update its algorithms and UI. My energy and intelligence are limited, and I may not be able to come up with better algorithms. Please help me!

## Introduction

The Nokp Performance Benchmark is a Python-based application that utilizes the tkinter library for the graphical user interface and various system information libraries to gather CPU details and calculate performance scores.

## Features

- **Single-Core Performance**: Measures the performance of a single core by executing a complex calculation task and providing a score based on the elapsed time.
- **Multi-Core Performance**: Utilizes concurrent processing to measure the performance of multiple cores and aggregates the scores to provide a multi-core performance metric.
- **CPU Information**: Displays detailed CPU information including the CPU model and the number of CPU cores.

## How to Use

1. Launch the application.
2. Click the "Start Benchmark" button to initiate the benchmarking process.
3. The application will calculate and display the single-core and multi-core performance scores.
4. Detailed CPU information including the CPU model and core count will be presented in the UI.

## Requirements

To use the Nokp Performance Benchmark, ensure you have the following dependencies installed:

- Python 3.x
- tkinter library
- psutil library
- cpuinfo library
- wmi library
- ttkthemes library
- concurrent.futures library

## License

Copyright © 2023 Bingzi. All rights reserved.

## Version

Rough ver1.0

## Author

- **Bingzi**
