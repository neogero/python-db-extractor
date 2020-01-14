# BUGS

## 001 - Error when table recordset is empty

Error:

```text
    keys = collection[0].keys()
    IndexError: list index out of range
```

Solucion:

- Evaluamos si el tamaño de la colección es mayor que 0
