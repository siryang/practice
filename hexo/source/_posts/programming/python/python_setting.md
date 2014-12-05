







* Python HOOK

python的两个HOOK sitecustomize  和 usercustomize用于对python定制

```python
import site
site.getusersitepackages()
```

`python -s xxx.py`可以避开HOOK