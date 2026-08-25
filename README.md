# Shopping List

A command-line shopping list built in Python. Add items, remove them, view the list, and quit — all through a simple menu.

This was my first program written from scratch while learning Python.

## Running it

Requires Python 3.

```bash
python3 shopping.py
```

It asks for your name, then shows a menu:


## How it works

- `get_name()` — asks for a name and keeps asking until it gets valid input, rejecting empty entries and numbers
- `add_item(item)` — adds an item to the list
- `remove_item(item)` — removes an item, or says so if it isn't there
- `show_list()` — prints every item, or says the list is empty

The menu runs inside a `while` loop so the program keeps going until you choose to quit.

## What I learned

- Defining and calling functions, and passing values into them
- Using `while True` with `continue` and `break` to control loops
- Validating user input before acting on it
- Why `input()` returns text, not numbers — comparing to `1` instead of `"1"` fails silently

## Limitations

- The list isn't saved, so it's empty again each time you run it
- Item names are case-sensitive, so "Milk" and "milk" are treated as different

## Next steps

- [ ] Save the list to a file so it survives restarting
- [ ] Make searching and removing case-insensitive
- [ ] Add an option to clear the whole list
