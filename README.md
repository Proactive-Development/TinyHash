#TinyHash
A tiny hash generator. Turn massive files to a few characters.

## Installation

Coming Soon

## Usage
### Small hash
This will create a small hash of the input string which is 4 digits or more. This algorithm is not cryptographically secure.

```
python -m tinyhash -s Hello_World
```

You can also use a file 

```
python -m tinyhash -s --file hello_world.txt
```

The output of `Hello_World` is `33464`

### Large hash
This will create a larger hash of the input string which is 6 digits or more. This algorithm is not cryptographically secure.

```
python -m tinyhash -l Hello_World
```

You can also use a file 

```
python -m tinyhash -l --file hello_world.txt
```

The output of `Hello_World` is `3346f74`

