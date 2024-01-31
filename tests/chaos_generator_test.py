import numpy as np
import random
import string
import time
import pytest

from tp_chaos_generator import ChaosGenerator, utils

def test_generate_key():
    cg = ChaosGenerator()
    keys1 = cg.generate_key()
    time.sleep(1)
    keys2 = cg.generate_key()
    assert len(keys1) > 0 and len(keys1) == len(keys2) \
        and not all(keys1[i] == keys2[i] for i in range(len(keys1)))

@pytest.fixture
def texts() -> list[str]:
    lengths = [10, 20, 50, 100, 500, 1000, 2000, 5000, 10000, 100000]
    return [''.join(random.choice(string.printable) for i in range(len)) for len in lengths]

@pytest.fixture
def images() -> list:
    sizes = [5, 10, 20, 50, 100]
    return [np.random.randint(0, 256, (3, len, len)) for len in sizes]

def test_texts(texts):
    cg = ChaosGenerator()
    key = cg.generate_key()
    decrypted_texts = []
    for text in texts:
        text_b = utils.convert_to_bytes(text)
        en_s = cg.encrypt(text_b, key)
        de_b = cg.decrypt(en_s, key)
        de_text = utils.convert_to_string(de_b)
        decrypted_texts.append(de_text)
    assert len(texts) == len(decrypted_texts)
    assert all(texts[i] == decrypted_texts[i] for i in range(len(texts)))

def test_images(images):
    cg = ChaosGenerator()
    key = cg.generate_key()
    decrypted_images = []
    for image in images:
        _, h, w = image.shape
        en_image = cg.encrypt(list(image.reshape(-1)), key)
        de_image = cg.decrypt(en_image, key)
        decrypted_images.append(np.array(de_image).reshape((3, h, w)))
    assert len(images) == len(decrypted_images)
    assert all(np.all(images[i] == decrypted_images[i]) for i in range(len(images)))