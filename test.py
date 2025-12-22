#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Satoh-Narumi
# SPDX-License-Identifier: BSD-3-Clause

import os
import argparse
import sys
import subprocess
import requests
import math
from PIL import Image

Image_url='https://cdn.pixabay.com/photo/2025/11/29/16/26/nature-9985148_1280.jpg'
Input='nature-9985148_1280.jpg'

def imageimporter(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    
    except requests.exceptions.RequestException as e:
        return False
    
def image_dimention(path):#画像の縦横の長さ2つを返す
    with Image.open(path) as img:
        width,height = img.size
        return width, height
        
def weight_scale(path):
    size = os.path.getsize(path)
    return size

def cleaner(target):
    os.remove(Input)
    os.remove(target)

def main(image_url, input):
    
    if not os.path.exists(input):
        if(imageimporter(image_url, input) is not True):
            pass
    
    #851x1280
    
    width, height = image_dimention(input)
    size = round(weight_scale(input) / 1024 , 2)
    print(f"{width}x{height} {size}KB")
    
    result_reso = subprocess.run(['python3', 'gazo', 'reso', input, '50' ,'-util', 'debug'],capture_output=True, text=True)
    output_reso = float(result_reso.stdout.strip())
    if output_reso > size:
        sys.exit("reso失敗")
        cleaner("reresoluted_" + input)
    
    result_size = subprocess.run(['python3', 'gazo', 'size', input, '425', '640', '-util', 'debug'], capture_output=True, text=True)
    size_returns = result_size.stdout.split(',')
    output_width = int(size_returns[0])
    output_height = int(size_returns[1])
    print(f"{output_width}x{output_height}")
    if int(output_height) > height and int(output_width) > width:
        sys.exit("size失敗")
        cleaner("resized_" + input)
    
    result_get = subprocess.run(['python3', 'gazo', 'get', input, '-util', 'debug'], capture_output=True, text=True)
    get_returns = result_get.stdout.split(',')
    get_width = int(get_returns[0])
    get_height = int(get_returns[1])
    get_size = float(get_returns[2])
    print(f"{get_width}x{get_height},{get_size}")
    if get_width != width or get_height != height or get_size != size:
        sys.exit("get失敗")
        os.remove(Input)
        
    print(f"{Input},resized_{Input}")
    os.remove('reresoluted_' + input)
    os.remove('resized_' + input)
    os.remove(Input)
    print("done!")
    
    #以下異常入力
    
    #gazoのみ
    univ_1 = subprocess.run(['python3', 'gazo'],capture_output=True, text=True)
    #画像入力なし
    univ_2 = subprocess.run(['python3', 'gazo', 'get' ,'-util', 'debug'],capture_output=True, text=True)
    #-utilオプション入力なし
    univ_3 = subprocess.run(['python3', 'gazo', 'get', input ,'-util'],capture_output=True, text=True)
    #reso品質なし
    reso_1 = subprocess.run(['python3', 'gazo', 'reso', input, '-util', 'debug'],capture_output=True, text=True)
    #reso品質異常数値
    reso_2 = subprocess.run(['python3', 'gazo', 'reso', input, '0' ,'-util', 'debug'],capture_output=True, text=True)
    #size縦横比異常数値
    size_1 = subprocess.run(['python3', 'gazo', 'size', input, '0', '-100' ,'-util', 'debug'],capture_output=True, text=True)
    
    if (univ_1.returncode != 0 or
        univ_2.returncode != 0 or
        univ_3.returncode != 0 or
        reso_1.returncode != 0 or
        reso_2.returncode != 0 or
        size_1.returncode != 0):
        print("Abnormal test passed.")
    
if __name__ == '__main__':
    main(Image_url, Input)
