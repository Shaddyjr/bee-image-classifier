import numpy as np
from skimage.transform import rescale, resize, rotate
from skimage.color import rgb2gray

class ImageHandler():
    def __init__(self, images):
        self.images = np.asanyarray([np.asarray(image) for image in images])
        self.index = np.array(range(len(self.images)))
        self._is_clone = False

    @property
    def images_for_display(self):
        '''getter for image data intended for visualization (no negatives, and scaled appropriately)'''

        if len(self.images.shape) == 4 and self.images.shape[3] == 1: # grayscale can simply return as is without 3rd dim.
            return np.squeeze(self.images)

        if len(self.images.shape) == 1: # unaltered .images
            return self.images

        return self._handle_normalized_state(
            lambda : self.images / 255,
            lambda : self.images + .5,
            lambda err : "Could not convert images to standard format"
        )

    def _handle_normalized_state(self, if_255_func, if_norm_func, err_func = None):
        try:
            return if_255_func() if self.images.max() > 1 else if_norm_func()
        except Exception as e:
            if err_func:
                raise Exception(err_func(e))
            raise e

    def get_by_index(self, indeces):
        # should return a new handler for chaining
        return ImageHandler(self.images[indeces])

    def resize(self, resizing):
        '''
        resizing = (W,H)
        '''
        context = self._get_context()
        context.images = np.asanyarray([resize(image, resizing, anti_aliasing=True, mode = "constant", preserve_range = True) for image in context.images])
        return context

    def grayscale(self):
        context = self._get_context()
        context.images = np.expand_dims(rgb2gray(context.images), axis = 3)
        return context

    def rotate(self):
        context = self._get_context()
        out = []
        # original
        out.extend(context.images)
        
        #rotated
        rotated = [rotate(image, angle) for angle in range(90,360,90) for image in context.images]
        out.extend(rotated)
        
        #mirroring
        # mirrored = [np.flipud(image) for image in out]
        # out.extend(mirrored)

        context.images = np.asanyarray(out)

        ## alter context index
        original      = context.index
        angles        = np.repeat(context.index, 3)
        all_angles    = np.append(original, angles)
        # context.index = np.append(all_angles, all_angles)
        context.index = all_angles
        return context

    def invert(self):
        context = self._get_context()

        context.images =  context._handle_normalized_state(
            lambda : 255 - context.images,
            lambda : .5 - context.images
        )
        return context

    def normalize(self):
        if self.images.dtype != "float64":
            raise Exception("Images are differently shaped. Try to .resize() first.")
        context = self._get_context()
        context.images =  context._handle_normalized_state(
            lambda : (context.images / 255) - 0.5,
            lambda : context.images - 0.5
        )
        return context

    def transform(self, resize = False, normalize = False, grayscale = False, invert = False, rotate = False):
        context = self._get_context()
        if resize:
            context.resize(resize)
        if normalize:
            context.normalize()
        if grayscale:
            context.grayscale()
        if rotate:
            context.rotate()
        if invert:
            context.invert()
        return context

    def _clone(self):
        clone = ImageHandler(self.images.copy())
        clone._is_clone = True
        return clone
    
    def _get_context(self):
        '''returns context. if current object not clone, will return a cloned verson of self'''
        return self._clone() if not self._is_clone else self
