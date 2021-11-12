def set_res(cap, res='480p'):
    # Establñecemos las dimensiones validas
    std_dim = {
        '480p': (640, 480),
        '720p': (1280, 720),
        '1080p': (1920, 1080)
    }

    # verificamos la validez del valor facilitado
    if res not in list(std_dim.keys()):
        w, h = std_dim['480p']
    else:
        w, h = std_dim[res]

    # establecemos la resolucion
    cap.set(3, w)
    cap.set(4, h)
