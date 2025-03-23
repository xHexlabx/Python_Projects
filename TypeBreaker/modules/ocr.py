from easyocr import Reader

def ocr (image_path : str) :

    reader = Reader(["en", "th"])  # English and Thai
    result = reader.readtext(image=image_path , detail=0)

    return result
