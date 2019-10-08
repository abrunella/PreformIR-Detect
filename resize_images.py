import os
import glob
import cv2

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Resize raw images to uniformed target size."
    )
    parser.add_argument(
        "--raw-dir",
        help="Directory path to raw images.",
        default="./data/raw",
        type=str,
    )
    parser.add_argument(
        "--save-dir",
        help="Directory path to save resized images.",
        default="./data/images",
        type=str,
    )
    parser.add_argument(
        "--ext", help="Raw image files extension to resize.", default="jpg", type=str
    )
    parser.add_argument(
        "--target-scale",
        help="Target size to resize as a percentage.",
        default="25",
        type=str,
    )
    args = parser.parse_args()

    raw_dir = args.raw_dir
    save_dir = args.save_dir
    ext = args.ext
    target_size = args.target_scale
    #msg = "--target-size must be a tuple of 2 integers"
    #assert isinstance(target_size, tuple) and len(target_size) == 2, msg
    fnames = glob.glob(os.path.join(raw_dir, "*.{}".format(ext)))
    os.makedirs(save_dir, exist_ok=True)
    print(
        "{} files to resize from directory `{}` to target size:{}".format(
            len(fnames), raw_dir, target_size
        )
    )

    for i, fname in enumerate(fnames):
        print(".", end="", flush=True)
        img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
        width = int(img.shape[1] * int(target_size) / 100)
        height = int(img.shape[0] * int(target_size) / 100)
        dim = (width, height)
        img_small = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        new_fname = "{}.{}".format(str(i), ext)
        small_fname = os.path.join(save_dir, new_fname)
        cv2.imwrite(small_fname, img_small)
    
    print(
        "\nDone resizing {} files.\nSaved to directory: `{}`".format(
            len(fnames), save_dir
        )
    )


