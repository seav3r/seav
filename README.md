# Seav

seav is personal python library to document code projects

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install seav. Please navigate to the repo location in terminal. Then build a wheel distribution.

```bash
pip install wheel
python setup.py sdist bdist_wheel
```

Then navigate to the new \dist folder and pip install.

```bash
pip install seav-0.1.0-py3-none-any.whl
```

## Usage

```python
import seav

# returns 'PorkchopPlot'
orbits.porkchop.generate()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)