# Python profiling decorators

* simple_time
* yappi
* cprofile
* cprofile_dump
* line
* memory
* timeit
* calltree
* gprof2dot
* grind

Installing:
```shell
git clone https://github.com/vera-l/python-profilers.git
cd python-profilers
python setup.py install --user
```

Using:
```python
import profilers

@profilers.calltree
def some_f():
    pass
```
