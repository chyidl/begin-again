Python import:
==============
```

dir(): -> list the contents of a namespace - local symbol table

When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, If a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.

```

* Reloading a Module
```
For reasons of efficiency, a module is only loaded once per interpreter session.

change to a module and need to reload it
importlib.reload(mod)

```

* Importing * From a Package
```
In summary, __all__ is used by both packages and modules to control what is imported when import * is specified.
  For a package, when __all__ is not defined, import * does not import anything
  For a module, when __all__ is not defined, import * imports everything (except--you guessed it--names starting with an underscore.)
```

