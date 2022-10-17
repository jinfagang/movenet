import os
import cv2
import torch
from movenet.opts import opts
from movenet.detectors.detector_factory import detector_factory

image_ext = ["jpg", "jpeg", "png", "webp"]
video_ext = ["mp4", "mov", "avi", "mkv"]
time_stats = ["tot", "load", "pre", "net", "dec", "post", "merge"]


def demo(opt):
    os.environ["CUDA_VISIBLE_DEVICES"] = opt.gpus_str
    opt.debug = max(opt.debug, 1)
    Detector = detector_factory[opt.task]
    detector = Detector(opt)

    model = detector.model
    a = torch.randn([1, 3, 256, 256])
    traced_m = torch.jit.trace(model, [a])
    traced_m.save('movenet.pt')



if __name__ == "__main__":
    opt = opts().init()
    demo(opt)