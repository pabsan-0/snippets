import os

import numpy as np
import ultralytics.data.build as build

# Easiest is to monkey patch the class
# build.YOLODataset = YOLOWeightedDataset


class YOLOWeightedDataset(build.YOLODataset):
    def __init__(self, *args, mode="train", **kwargs):
        """
        Weighted dataset that samples images randomly rather than fetching by index.
        """

        super(YOLOWeightedDataset, self).__init__(*args, **kwargs)

        self.train_mode = "train" in self.prefix

        self.weights = self.calculate_weights()
        self.probabilities = self.calculate_probabilities()

    def calculate_weights(self):
        """
        Calculate the weight for each file based on its source path.

        Returns:
            wts: A list of weights corresponding to each label.
        """
        wts = [1.0] * len(self.im_files)
        for idx, img_path in enumerate(self.im_files):

            # TODO
            # Custom logic to assign weights by filesystem paths
            if int(os.path.splitext(os.path.basename(img_path))[0]) < 5:
                wts[idx] *= 0.2
            else:
                wts[idx] *= 1.0

        return wts

    def calculate_probabilities(self):
        """
        Calculate and store the sampling probabilities based on the weights.

        Returns:
            list: A list of sampling probabilities corresponding to each label.
        """
        total_weight = sum(self.weights)
        probabilities = [w / total_weight for w in self.weights]
        return probabilities

    def __getitem__(self, index):
        """
        Return transformed label information based on the sampled index.
        """
        # Don't use for validation
        if not self.train_mode:
            return self.transforms(self.get_image_and_label(index))
        else:
            index = np.random.choice(len(self.labels), p=self.probabilities)
            return self.transforms(self.get_image_and_label(index))
