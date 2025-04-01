# `envelope_proteomics`

This repository houses the code and data used in our project quantitatively 
exploring the envelope proteome of *Escherichia coli*.

## Installation

This project uses Python 3.12 with `uv` for dependency management.

### Prerequisites

- Python 3.12
- uv package manager (`pip install uv`)

### Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:cremerlab/envelope_proteomics
   cd envelope_proteomics
   ```

2. Create and activate virtual environment:
   ```bash
   python3.12 -m venv .venv
   
   # On macOS/Linux
   source .venv/bin/activate
   
   # On Windows
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   cd software/
   uv pip install -e .
   ```
## License

This project is licensed under a standard MIT License as follows:


```MIT License

Copyright (c) 2025 cremerlab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE.
```