import os


def get_images(actual_images = None):
    if actual_images is None:
        all_images = os.listdir("./data/images")
    else:
        all_images = actual_images

    for (i, image) in enumerate(all_images):
        if image.endswith(".jpg") == False or image.endswith(".png") == False or image.endswith(".jpeg") == False:
            del all_images[i]
            return get_images(all_images)

    all_images = get_images_path(all_images)

    return all_images


def get_images_path(images):
    for (i, image) in enumerate(images):
        images[i] = "./data/images/" + image

    return images
