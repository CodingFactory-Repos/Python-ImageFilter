import os


def get_images(actual_images=None):
    if actual_images is None:
        all_images = os.listdir("./data/images")
    else:
        all_images = actual_images

    for (i, image) in enumerate(all_images):
        image_extension = image.split('.')[1]
        valid_images = ["jpg", "png", "tga", "jpeg"]

        if image_extension not in valid_images:
            all_images.remove(image)
            print("Removed: " + image)
            print("actual_images: " + str(all_images))
            print("-- --- --")
            return get_images(all_images)

    all_images = get_images_path(all_images)

    return all_images


def get_images_path(images):
    for (i, image) in enumerate(images):
        images[i] = "./data/images/" + image

    return images
