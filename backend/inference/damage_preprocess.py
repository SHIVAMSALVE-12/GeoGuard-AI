"""
GeoGuard AI

Damage Image Preprocessing

Author: Shivam Salve
"""

import numpy as np

import cv2

import torch

from backend.config.damage_config import (
    IMAGE_SIZE,
)


class DamagePreprocessor:

    """
    Preprocess image for Damage AI.
    """

    def __init__(self):

        self.image_size = IMAGE_SIZE

    def preprocess(self, image):

        """
        Parameters
        ----------
        image : np.ndarray
            RGB image

        Returns
        -------
        Tensor
        """

        if image is None:

            raise ValueError(
                "Input image is None."
            )

        if image.ndim != 3:

            raise ValueError(
                "Expected RGB image."
            )

        image = cv2.resize(

            image,

            (
                self.image_size,
                self.image_size,
            ),

            interpolation=cv2.INTER_LINEAR,
        )

        image = image.astype(
            np.float32
        )

        image = image / 255.0

        image = torch.from_numpy(
            image
        ).permute(
            2,
            0,
            1,
        )

        image = image.unsqueeze(0)

        return image

    def preprocess_file(
        self,
        image_path,
    ):

        image = cv2.imread(
            str(image_path)
        )

        if image is None:

            raise FileNotFoundError(
                image_path
            )

        image = cv2.cvtColor(

            image,

            cv2.COLOR_BGR2RGB,
        )

        tensor = self.preprocess(
            image
        )

        return image, tensor