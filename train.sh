#!/usr/bin/env bash
echo "=== install packages ==="
pip install -r requirement.txt

echo "==== collect data ==="
cd data
scrapy runspider get_links.py -o links.json
scrapy runspider webCrawler.py
python create_dataset.py

echo "===training data ====="
cd ..
python train.py
