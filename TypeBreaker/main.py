from modules import ocr , type , data_screen_capture

SCREEN_POSITION = {
    "x1" : 200 ,
    "y1" : 800 ,
    "x2" : 2600 ,
    "y2" : 900 ,
    "interval_seconds" : 0.5 ,
    "output_folder" : "./images"
}

def main () :

    data_screen_capture (**SCREEN_POSITION)

if __name__ == "__main__" :

    main()