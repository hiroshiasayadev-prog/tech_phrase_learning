# Source capture comparison

This report records the comparison made before the API-derived posts replaced the reviewed fixture source.
The pre-capture fixture is retained as `source-posts.pre-api-normalized.json`.
The API-derived result is now `source-posts.json`.

## Post comparison

| post | username | reply target | raw exact | whitespace-normalized |
|---|---|---|---|---|
| `#1` | yes | yes | no | yes |
| `#2` | yes | no | no | yes |
| `#4` | yes | yes | no | yes |
| `#7` | yes | yes | no | yes |

## Raw-text differences

### Post #1

- Reviewed characters: `8814`
- Captured characters: `8814`
- First mismatch offset: `106`
- Whitespace-normalized match: `True`

```diff
--- reviewed fixture
+++ captured API raw
@@ -1 +1,258 @@
-I'm new to the python packaging realm, but wanted to propose something that I've been wanting for a while.  I want to standardize hatchling targets.  From what I can tell hatchling and setuptools (which treats them as custom "commands") are the only popular backends that support custom targets.  Build frontends have no reason to support custom backend targets, so if you want to use custom targets you have to use hatch.  ## What do I mean by target?  I wasn't actually sure the correct terminology here, but I went with target since hatchling uses it.  A target can be any artifact that is created by applying some transformation to the source.  Obviously, wheels and sdists are targets.  I will refer to them as "standard targets" going forward.  ## Motivation  I personally believe that providing extensibility to the interface is a good thing.  The current system forces people who want to create a custom target to either use hatch specifically or create their own build frontend and backend.  ### Zipapps  The primary purpose custom targets will serve me is the ability to create targets like [shiv](https://shiv.readthedocs.io/en/latest/) which vendor their dependencies.  ### Other Examples  These examples are linked in the hatch documentation  - [hatch-zipped-directory](https://github.com/dairiki/hatch-zipped-directory)  - [hatch-aws](https://github.com/trash-panda-v91-beta/hatch-aws)  I also found this  - [hatch-babel](https://github.com/NiklasRosenstein/hatch-babel)  Other ideas  - If you had a python program that accepts python plugins, an alternative packaging scheme can be desirable for the plugins.  - Other forms of packaged python meant as a standalone application.  ### What This is Not  This is not intended to provide a means to provide different _flavors_ of targets.  What I mean by _flavors_ is performing some sort of transformation prior to creating a standard target.  I.e. if you wanted to perform some form of obfuscation or minification prior to building a wheel, this is not a separate target.  This is intended to be done through the `config_settings` passed to the backend.  ## Interface  Here's my idea for what an interface like this would look like.  This is a rough outline and I welcome any ideas on the best way to do this.  To keep in line with PEP 517 every target will have at least one required hook for building and one optional hook for getting build dependencies.  ### Build Hook  ```py build_XXX(output_directory, config_settings=None):   ... ```  Like the PEP 517 hooks, the first argument is the output directory of the build process. The same requirements hold for `build_wheel` and `build_sdist` as in PEP 517, but for targets outside of wheels and sdists, the hook must place the artifact(s) in the `output_directory`. If the hook creates a single file or directory, it must return the basename of that file or directory. Otherwise, it must return a list of the basenames of each file or directory it created.  Other than the special case of `build_wheel`, no additional arguments are allowed.  Every build configuration option should be set through `config_settings`.  ### Requirements Hook  ```py get_requires_for_build_XXX(config_settings=None):    ... ```  This follows the same specifications as in PEP 517. The returned dependencies will be installed when calling the associated `build_XXX` hook.  ### Target Naming  It might be convenient for the frontend or other tools to know what targets can be built.  Additionally, certain targets might not want to use the `build_XXX` or `get_requires_for_XXX` naming scheme.  My _initial_ solution to this is putting something in the pyproject.toml.  Targets are listed in the `build-system` table.  The `targets` key is a table containing the target name associated with another table containing an optional `build_function` and an optional `requires_function`.  By default, the build_function is `build_TARGETNAME` and the requires_function is `get_requires_for_BUILD_FUNCTION`.  Assume that the wheel target and sdist target are included by default, but they can be overritten by the targets key.  ```toml [build-system]  # Defined by PEP 518:  requires = ["my_custom_build_library"]  # Defined by PEP 517:  build-backend = "local_backend"  backend-path = ["backend"]  # Defined here  targets = {    shiv = {},    custom_target = {      build_function = "build_my_target",      requires_function = "get_my_requires"    },    other_target = {      build_function = "do_other"    }  }  ```  Alternatively, they can be defined like:  ```toml [build-system.targets.shiv]  #build_function = "build_shiv"  #requires_function = "get_requires_for_build_shiv"  [build-system.targets.custom_target]  build_function = "build_my_target"  requires_function = "get_my_requires"  [build-system.targets.other_target]  build_function = "do_other"  #requires_function = "get_requires_for_do_other"  ```  In this example, the backend may provide the `build_wheel`, `build_sdist`, `build_shiv`, `build_my_target`, and `do_other` functions.  If a build function is not provided by the backend it should raise an `AttributeError` when the frontend calls it.  The backend may optionally provide the `get_requires_for_build_wheel`, `get_requires_for_build_sdist`, `get_requires_for_build_shiv`, `get_my_requires`, and `get_requires_for_do_other` functions.  If a requires function is not provided by the backend, the frontend should assume an implementation equivalent to `return []` as described in PEP 517.  #### Notes  __I am looking for feedback here. I feel like this overcomplicates the pyproject.toml__  The primary intention with including the targets key is to provide static information to the build frontend and other tools that might use the `pyproject.toml`.  I don't know if this is a desirable feature.  I'm not sure whether or not the build frontend should support building targets that are not listed in the `targets` table.  I'm not sure if the `pyproject.toml` should include this information, or if this is something that should be handled solely by the build frontend.  For projects with many targets, it seems like using this might bloat the pyproject.toml.  I don't want build backends to have to support multiple targets outside of wheels and sdist.  Does including the `targets` as a key confuse users that lack a thorough understanding of their backend?  Should custom function names be allowed or should the format be restricted to `build_TARGETNAME`?  This would allow the `targets` key to just be a list of names instead of a table.  The requires_function is optional.  If the `pyproject.toml` specifies a specific `requires_function` and it doesn't exist, should this be silently ignored?  Should the frontend warn the user?  It might also make sense to support using different backends for different targets, but thought that would complicate this even further.  Something along the lines of this could make it easier to distribute custom backends meant for different targets.  ```toml [build-system]  requires = ["hatchling", "shiv_builder"]  build-backend = "hatchling.build"  targets = {   shiv = {      backend = "shiv_builder.build",     build_function = "build_shiv"    } }  ```  ### Minimal Alternative  To avoid the complications described above, it might be easier to just set up a basic interface that involves the build frontend dynamically looking up functions from the backend.  This might make implementation a lot simpler and get something like this pushed through the PEP pipeline much faster.  Simply, the build frontend exposes the ability to the user to set a target name, and then attempts to call `build_TARGETNAME`/`get_requires_for_build_TARGETNAME` from the backend.  This solution would be backwards compatible and would not require `pyproject.toml` updates.  A backend is free to use any implementation they like, but I imagine a module level `__getattr__` might make a lot of sense here:  ```py # backend/build.py  def build_sdist(...):    ...  def build_wheel(...):    ...  ...  def __getattr__(name):    return do_dynamic_lookup(name)  ```  #### Another Alternative  One other possible option to putting targets in the `pyproject.toml` would be to have a function like `get_targets` which the backend should define which lists the available targets (and possibly their custom function names). If undefined, the frontend should only assume the functions from PEP 517 are defined.  ## Conclusion  To recap, I just wanted to get the ball rolling on something that I've wanted out of python packaging. I'm not super familiar with how this process should go.  I'd be happy to flush this out further since clearly there's a lot of specifics that still have to be determined, but I wanted to get the general reception of this idea before spending more time working on this.
+I'm new to the python packaging realm, but wanted to propose something that I've been wanting for a while.
+
+I want to standardize hatchling targets.
+
+From what I can tell hatchling and setuptools (which treats them as custom "commands") are the only popular backends that support custom targets.
+
+Build frontends have no reason to support custom backend targets, so if you want to use custom targets you have to use hatch.
+
+## What do I mean by target?
+
+I wasn't actually sure the correct terminology here, but I went with target since hatchling uses it.
+
+A target can be any artifact that is created by applying some transformation to the source.
+
+Obviously, wheels and sdists are targets.
+
+I will refer to them as "standard targets" going forward.
+
+## Motivation
+
+I personally believe that providing extensibility to the interface is a good thing.
+
+The current system forces people who want to create a custom target to either use hatch specifically or create their own build frontend and backend.
+
+### Zipapps
+
+The primary purpose custom targets will serve me is the ability to create targets like [shiv](https://shiv.readthedocs.io/en/latest/) which vendor their dependencies.
+
+### Other Examples
+
+These examples are linked in the hatch documentation
+
+- [hatch-zipped-directory](https://github.com/dairiki/hatch-zipped-directory)
+
+- [hatch-aws](https://github.com/trash-panda-v91-beta/hatch-aws)
+
+I also found this
+
+- [hatch-babel](https://github.com/NiklasRosenstein/hatch-babel)
+
+Other ideas
+
+- If you had a python program that accepts python plugins, an alternative packaging scheme can be desirable for the plugins.
+
+- Other forms of packaged python meant as a standalone application.
+
+### What This is Not
+
+This is not intended to provide a means to provide different _flavors_ of targets.
+
+What I mean by _flavors_ is performing some sort of transformation prior to creating a standard target.
+
+I.e. if you wanted to perform some form of obfuscation or minification prior to building a wheel, this is not a separate target.
+
+This is intended to be done through the `config_settings` passed to the backend.
+
+## Interface
+
+Here's my idea for what an interface like this would look like.
+
+This is a rough outline and I welcome any ideas on the best way to do this.
+
+To keep in line with PEP 517 every target will have at least one required hook for building and one optional hook for getting build dependencies.
+
+### Build Hook
+
+```py
+build_XXX(output_directory, config_settings=None):
+  ...
+```
+
+Like the PEP 517 hooks, the first argument is the output directory of the build process. The same requirements hold for `build_wheel` and `build_sdist` as in PEP 517, but for targets outside of wheels and sdists, the hook must place the artifact(s) in the `output_directory`. If the hook creates a single file or directory, it must return the basename of that file or directory. Otherwise, it must return a list of the basenames of each file or directory it created.
+
+Other than the special case of `build_wheel`, no additional arguments are allowed.
+
+Every build configuration option should be set through `config_settings`.
+
+### Requirements Hook
+
+```py
+get_requires_for_build_XXX(config_settings=None):
+   ...
+```
+
+This follows the same specifications as in PEP 517. The returned dependencies will be installed when calling the associated `build_XXX` hook.
+
+### Target Naming
+
+It might be convenient for the frontend or other tools to know what targets can be built.
+
+Additionally, certain targets might not want to use the `build_XXX` or `get_requires_for_XXX` naming scheme.
+
+My _initial_ solution to this is putting something in the pyproject.toml.
+
+Targets are listed in the `build-system` table.
+
+The `targets` key is a table containing the target name associated with another table containing an optional `build_function` and an optional `requires_function`.
+
+By default, the build_function is `build_TARGETNAME` and the requires_function is `get_requires_for_BUILD_FUNCTION`.
+
+Assume that the wheel target and sdist target are included by default, but they can be overritten by the targets key.
+
+```toml
+[build-system]
+
+# Defined by PEP 518:
+
+requires = ["my_custom_build_library"]
+
+# Defined by PEP 517:
+
+build-backend = "local_backend"
+
+backend-path = ["backend"]
+
+# Defined here
... 142 additional diff lines omitted ...
```

### Post #2

- Reviewed characters: `756`
- Captured characters: `756`
- First mismatch offset: `201`
- Whitespace-normalized match: `True`

```diff
--- reviewed fixture
+++ captured API raw
@@ -1 +1,5 @@
-What *frontend* tools do you expect to support this new interface? I don't expect pip to - pip currently only uses `build_wheel` and the associated methods, we don't even have a need for `build_sdist`.  Without a frontend using these new APIs, I don't see a good reason for standardising anything.  There's also the fact that I've seen almost no demand for building "non-standard targets" of the form you're describing, but that may simply because I don't work on tools that would see such demand. I note that the examples you found are *plugins* for hatch, and therefore could easily have been created to satisfy one person's nice use case (I don't *know* if that's the case, though, so I'm not claiming there's no demand, just that I'm not aware of any).
+What *frontend* tools do you expect to support this new interface? I don't expect pip to - pip currently only uses `build_wheel` and the associated methods, we don't even have a need for `build_sdist`.
+
+Without a frontend using these new APIs, I don't see a good reason for standardising anything.
+
+There's also the fact that I've seen almost no demand for building "non-standard targets" of the form you're describing, but that may simply because I don't work on tools that would see such demand. I note that the examples you found are *plugins* for hatch, and therefore could easily have been created to satisfy one person's nice use case (I don't *know* if that's the case, though, so I'm not claiming there's no demand, just that I'm not aware of any).
```

### Post #4

- Reviewed characters: `3007`
- Captured characters: `3007`
- First mismatch offset: `227`
- Whitespace-normalized match: `True`

```diff
--- reviewed fixture
+++ captured API raw
@@ -1 +1,25 @@
-The goal with these non-standard targets isn't for them to be installed (by `pip` or related). They exist for any other context in which python code will need to be distributed. I.e. `shiv` or the other examples given earlier.   I understand that I'm approaching this from a more abstract standpoint as opposed to addressing a concrete problem.  I can't definitively say this one way of the other, but since this ecosystem is still relatively new, I feel as though the users who need to create custom targets have probably just stayed with their old build system.  Since I only provided examples for hatch targets in the original post, I went to go look for projects using distutils/[`setuptools.Command`](https://setuptools.pypa.io/en/latest/userguide/extension.html#setuptools.Command) to create these custom targets and found these.  - [py2app](https://github.com/ronaldoussoren/py2app/tree/main): creating macOS `.app` files of executeable python.  - [clamped](https://github.com/jimbaker/clamped): converting python code to java for use with Jython  - [pex](https://pex.readthedocs.io/en/v2.1.41/buildingpex.html#using-bdist-pex): pex uses `bdist_pex` to build `.pex` files with setuptools  - [conda-build](https://docs.conda.io/projects/conda-build/en/24.3.x/user-guide/recipes/build-without-recipe.html), [hatch-conda-build](https://pypi.org/project/hatch-conda-build/): builds conda packages  - [cx-freeze](https://cx-freeze.readthedocs.io/en/stable/builtdist.html): pretty much just `py2app` for multiple OSes  (side note: I found [Nuitka](https://nuitka.net/user-documentation/use-cases.html#setuptools-wheels) which compiles python into bytecode, but still seems to create a `.whl`, so that wouldn't really be considered a different target. It does create non wheel targets, so this proposal might be helpful for it, but it doesn't seem to use the traditional python packaging tools. I didn't dive deep enough to see how dependency management and environment creation is handled in the build process)  To answer the "what frontends do I expect to use this" more directly, I can see uv, hatch, pdm, and other frontends that strive to be extensible providing support for this (once again, hatch already supports this. Standardization of this interface would allow using the uv frontend with the hatchling backend). I am of the mentality that providing extensibility to python developers is good, but if it seems like this will go unused, then I can understand the desire to keep things simple.  Maybe I'm demanding too much within the constraints of the build ecosystem and instead this sort of process should operate on already built `.whl`s like how [PyApp](https://github.com/ofek/pyapp) works, but I find it convenient for developers to just have frontend tools like uv that are able to handle all parts of taking python code from its source to its final deliverable.  I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.
+The goal with these non-standard targets isn't for them to be installed (by `pip` or related). They exist for any other context in which python code will need to be distributed. I.e. `shiv` or the other examples given earlier. 
+
+I understand that I'm approaching this from a more abstract standpoint as opposed to addressing a concrete problem.
+
+I can't definitively say this one way of the other, but since this ecosystem is still relatively new, I feel as though the users who need to create custom targets have probably just stayed with their old build system.
+
+Since I only provided examples for hatch targets in the original post, I went to go look for projects using distutils/[`setuptools.Command`](https://setuptools.pypa.io/en/latest/userguide/extension.html#setuptools.Command) to create these custom targets and found these.
+
+- [py2app](https://github.com/ronaldoussoren/py2app/tree/main): creating macOS `.app` files of executeable python.
+
+- [clamped](https://github.com/jimbaker/clamped): converting python code to java for use with Jython
+
+- [pex](https://pex.readthedocs.io/en/v2.1.41/buildingpex.html#using-bdist-pex): pex uses `bdist_pex` to build `.pex` files with setuptools
+
+- [conda-build](https://docs.conda.io/projects/conda-build/en/24.3.x/user-guide/recipes/build-without-recipe.html), [hatch-conda-build](https://pypi.org/project/hatch-conda-build/): builds conda packages
+
+- [cx-freeze](https://cx-freeze.readthedocs.io/en/stable/builtdist.html): pretty much just `py2app` for multiple OSes
+
+(side note: I found [Nuitka](https://nuitka.net/user-documentation/use-cases.html#setuptools-wheels) which compiles python into bytecode, but still seems to create a `.whl`, so that wouldn't really be considered a different target. It does create non wheel targets, so this proposal might be helpful for it, but it doesn't seem to use the traditional python packaging tools. I didn't dive deep enough to see how dependency management and environment creation is handled in the build process)
+
+To answer the "what frontends do I expect to use this" more directly, I can see uv, hatch, pdm, and other frontends that strive to be extensible providing support for this (once again, hatch already supports this. Standardization of this interface would allow using the uv frontend with the hatchling backend). I am of the mentality that providing extensibility to python developers is good, but if it seems like this will go unused, then I can understand the desire to keep things simple.
+
+Maybe I'm demanding too much within the constraints of the build ecosystem and instead this sort of process should operate on already built `.whl`s like how [PyApp](https://github.com/ofek/pyapp) works, but I find it convenient for developers to just have frontend tools like uv that are able to handle all parts of taking python code from its source to its final deliverable.
+
+I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.
```

### Post #7

- Reviewed characters: `1006`
- Captured characters: `1006`
- First mismatch offset: `63`
- Whitespace-normalized match: `True`

```diff
--- reviewed fixture
+++ captured API raw
@@ -1 +1,5 @@
-[quote="Matthew Pleskow, post:4, topic:107565, username:MattP"] To answer the “what frontends do I expect to use this” more directly, I can see uv, hatch, pdm, and other frontends that strive to be extensible providing support for this (once again, hatch already supports this. Standardization of this interface would allow using the uv frontend with the hatchling backend). I am of the mentality that providing extensibility to python developers is good, but if it seems like this will go unused, then I can understand the desire to keep things simple. [/quote]  As a general rule for me, I want to see more than one tool implementing something with significant adoption before trying to standardize it. We provide this functionality in hatch via our plugin mechanism but many of the plugins that are not just flavors of wheels and sdists typically have relatively narrow use cases. The one exception might be the zipped directory plugin and hatch-aws which are really different flavors of the same thing.
+[quote="Matthew Pleskow, post:4, topic:107565, username:MattP"]
+To answer the “what frontends do I expect to use this” more directly, I can see uv, hatch, pdm, and other frontends that strive to be extensible providing support for this (once again, hatch already supports this. Standardization of this interface would allow using the uv frontend with the hatchling backend). I am of the mentality that providing extensibility to python developers is good, but if it seems like this will go unused, then I can understand the desire to keep things simple.
+[/quote]
+
+As a general rule for me, I want to see more than one tool implementing something with significant adoption before trying to standardize it. We provide this functionality in hatch via our plugin mechanism but many of the plugins that are not just flavors of wheels and sdists typically have relatively narrow use cases. The one exception might be the zipped directory plugin and hatch-aws which are really different flavors of the same thing.
```

## Source phrase checks

| interaction | exact phrase found | matching posts |
|---|---|---|
| `question-interaction.json` | yes | `#1` |
| `reply-interaction.json` | yes | `#2` |
