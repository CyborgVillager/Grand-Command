from gc_source_mod import *

def load_images(path_to_directory,height,width):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img,(int(640/width),int(640/height)))
                images[key] = img
    return images