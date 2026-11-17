import os
import argparse
from PIL import Image

def cut_spritesheet(input_path, tile_w, tile_h, out_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return

    os.makedirs(out_dir, exist_ok=True)
    width, height = img.size
    cols = width // tile_w
    rows = height // tile_h

    count = 0
    for row in range(rows):
        for col in range(cols):
            left = col * tile_w
            upper = row * tile_h
            right = left + tile_w
            lower = upper + tile_h
            
            tile = img.crop((left, upper, right, lower))
            # Ignora blocos totalmente transparentes
            if tile.getextrema() == ((0, 0), (0, 0), (0, 0), (0, 0)):
                continue

            out_file = os.path.join(out_dir, f"sprite_{row}_{col}.png")
            tile.save(out_file)
            count += 1
            print(f"Salvo: {out_file}")

    print(f"Finalizado. {count} sprites extraídos com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sprite Cutter do Game Dev Toolkit")
    parser.add_argument("--input", required=True, help="Caminho para a spritesheet")
    parser.add_argument("--tw", type=int, required=True, help="Largura do tile")
    parser.add_argument("--th", type=int, required=True, help="Altura do tile")
    parser.add_argument("--out", required=True, help="Diretório de saída")
    
    args = parser.parse_args()
    cut_spritesheet(args.input, args.tw, args.th, args.out)
