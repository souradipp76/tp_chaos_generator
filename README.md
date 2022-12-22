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
