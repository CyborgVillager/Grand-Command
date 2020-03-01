from gc_source import *

# gc_loadimg uses gc_source_mod as an ref
try:
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
except:
    print('Unable to process gc_loadimg')