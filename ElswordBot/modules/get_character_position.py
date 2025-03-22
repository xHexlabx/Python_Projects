def get_character_position(model, image):
    """Predict character position using the YOLO model."""
    res = model.predict(image, verbose=False)  # Suppress output

    if res and res[0].boxes.xywh.numel() > 0:
        return res[0].boxes.xywh  # Return position if found

    return None  # Return False if no object is detected
