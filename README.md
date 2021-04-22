# PyARENA

Procedural maps for first-person shooters, written in Python. 

## Installation

`git clone` or download this repository and run `poetry shell`, then `python src/main.py`). Poetry is available from pip, as well as most other package managers.

## Usage

`main.py [-h] width height`

Arguments: the width and height of the map. Using `-h` shows the help message.

It's not really useful to anyone other than me at this time. I might expand it later.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. The "tests" are currently just a file in `src/`.

## Acknowledgements & Related Works

This program is based on the paper [ARENA - Dynamic Run-Time Map Generation for Multiplayer Shooters](https://hal.inria.fr/hal-01408516/document) (Wong, et. al, 2014)
> Anand Bhojan, Hong Wong. ARENA - Dynamic Run-Time Map Generation for Multiplayer Shooters. 13th International Conference Entertainment Computing (ICEC), Oct 2014, Sydney, Australia.
pp.149-158, ff10.1007/978-3-662-45212-7_19ff. ffhal-01408516f

The program takes inspiration from [Herringbone-Wang Tiles](https://www.nothings.org/gamedev/herringbone/)

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

Copyright &copy; Gideon Grinberg 2021.
