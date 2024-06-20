# Reproducing the tensorflow issue

Run the following command to reproduce the issue:

```bash
bazel run //:dataset
```

You should see the following error:

```
  File "/private/var/tmp/_bazel_sundaramananthanarayanan/083e5cf8bb86e91a4da0a228060acc1c/execroot/_main/bazel-out/darwin_arm64-fastbuild/bin/dataset.runfiles/_main/dataset.py", line 2, in <module>
    import tensorflow as tf
ModuleNotFoundError: No module named 'tensorflow'
```

If you removed the `experimental_index_url` option from MODULE.bazel, then the issue will not occur.
The above command should run successfully and print the following output:

```
INFO: 5 processes: 5 internal.
INFO: Build completed successfully, 5 total actions
INFO: Running command line: bazel-bin/dataset
(10000, 28, 28)
<class 'tuple'>
```
