AsAbove is a [Sublime Text 2][sublime] package which will duplicate the characters above your cursor or selection.

## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] package installed, you can install JSDocs from inside Sublime Text itself. Open the Command Palette and select "Package Control: Install Package", then search for AsAbove and you're done!

### Without Package Control ###

Go to your Sublime Text 2 Packages directory and clone the repository using the command below:

    git clone https://github.com/spadgos/sublime-AsAbove.git AsAbove

Don't forget to keep updating it, though!

## Usage ##

The default hotkey to activate AsAbove is `Ctrl+Shift+'`, however this can be configured in your local `Default (...).sublime-keymap` file. The command is called `as_above`.

## Examples ##

Given the text below, and the cursor sitting at the position of the pipe (`|`):

    var Text = require('path/to/libraries/Text'),
        User|

By activating AsAbove (`Ctrl+Shift+'`) multiple times, you can duplicate the necessary parts of the line above easily.

    var Text = require('path/to/libraries/Text'),
        User = require('path/to/libraries/|

AsAbove works with selections, multiple cursors and multiple selections. With multiple selections/cursors, they are visited in a bottom-up order so that if there are selections on consecutive lines, the topmost line isn't copied down.

    // before
    foo
    bar
    qux
    dah

    // after making 3 selections on "bar", "qux" & "dah" and activating AsAbove
    foo
    foo
    bar
    qux

[sublime]: http://www.sublimetext.com/
[package_control]: http://wbond.net/sublime_packages/package_control
