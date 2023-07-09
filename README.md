![CI Build](https://github.com/souradipp76/tp_chaos_generator/actions/workflows/main.yml/badge.svg)

# Triple Pendulum based Chaos Generator

``tp_chaos_generator`` is a package which provides a library for encrypting and decrypting data using a 
triple-pendulum based chaos generator.
## Requirements

- Python (>= 3.8)

## Installation

You can install ``tp_chaos_generator`` with:

```
    $ pip install -e .
```

## Usage

```python
    >>> from tp_chaos_generator import chaos_generator, utils
    >>> cg = chaos_generator.ChaosGenerator()
    >>> key = cg.generate_key()
    >>> text = utils.convert_to_bytes("A really secret message. Not for prying eyes.")
    >>> tokens = cg.encrypt(text, key)
    >>> tokens
    '...'
    >>> data = cg.decrypt(tokens, key)
    >>> utils.convert_to_string(data)
    'A really secret message. Not for prying eyes.'
```

## Citation
If you find the code useful in your research, please consider citing:
```
@ARTICLE{9969592,
  author = {Paul, Bikram and Pal, Souradip and Agrawal, Abhishek and Trivedi, Gaurav},
  journal = {IEEE Access}, 
  title = {Triple Pendulum Based Nonlinear Chaos Generator and its Applications in Cryptography}, 
  year = {2022},
  volume = {10},
  pages = {127073-127093},
  doi = {10.1109/ACCESS.2022.3226515}
}
```

## FAQ
Please create a [new issue](https://github.com/souradipp76/tp_chaos_generator/issues/new/choose).

