#!/bin/bash
# install.sh — Raspberry Pi 4B (aarch64 / ARM64) setup script
# Run with: bash install.sh

set -e

echo "=== Checking architecture ==="
ARCH=$(uname -m)
if [[ "$ARCH" != "aarch64" && "$ARCH" != "armv7l" ]]; then
    echo "Warning: This script is intended for Raspberry Pi (ARM). Detected: $ARCH"
fi

echo "=== Installing system dependencies ==="
sudo apt update
sudo apt install -y \
    python3-pip \
    python3-dev \
    libopenblas-dev \
    libatlas-base-dev \
    libjpeg-dev \
    libopenjp2-7 \
    libgl1 \
    libglib2.0-0

echo "=== Upgrading pip ==="
pip3 install --upgrade pip

echo "=== Installing PyTorch for ARM (CPU only) ==="
# Official PyTorch ARM wheel for Pi 4B
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# If the above fails, uncomment and try the community ARM builds:
# pip3 install torch --extra-index-url https://torch.kmtea.eu/whl/stable

echo "=== Installing remaining requirements ==="
pip3 install -r requirements.txt

echo "=== Verifying PyTorch ==="
python3 -c "import torch; print('PyTorch version:', torch.__version__); print('CPU only, CUDA available:', torch.cuda.is_available())"

echo "=== Done! ==="
