# Project Template

This is a ready-to-use project template built off of the [GSLab Template](https://github.com/gslab-econ/template) and augmented to reflect my own organizational idiosyncrasies. A few project files have been pre-populated to exhibit the basic functionality of the [SCons](http://scons.org/)-based system used here. The organizational philosophy motivating this template and its appropriate use has been heavily influenced by the [GSLab RA Manual](https://github.com/gslab-econ/ra-manual/wiki/Getting-Started).

This README includes two sections. First, "Setting up a new project" outlines the process for setting up a new project using this template. This section should be deleted once a new project has been initialized (the README title and this opening section should also be replaced). Second, "Running the project" outlines the process for setting up and operating an existing project, and includes FAQs regarding the operation of this project. This section should be preserved in new projects to assist onboarding collaborators and interested replicators.

Please note that while the source template was designed with both Windows and Mac/Linux in mind, this augmented version is fully focused on Mac/Linux development. Thus, any instructions regarding Windows below may be out of date. Please alert [Ben](mailto:leyden@cornell.edu) about any issues regarding Windows so that the README or template can be corrected.

## Getting Started

### Prerequisites

You'll need the following to run the template. [Homebrew](https://brew.sh/) for Mac and [Linuxbrew](http://linuxbrew.sh/) for Linux make this easier.
* Windows `cmd.exe`, Mac OS X `bash`, or Linux `bash`.
* [Python >= 3.8](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) for [Windows](https://docs.python.org/3/using/windows.html), [Mac](https://docs.python.org/3/using/mac.html) or [Linux](https://docs.python.org/3/using/unix.html).
* [git](https://git-scm.com/downloads) for version control.
    * [git-lfs](https://git-lfs.github.com/) for versioning large files.
    * You'll need both git and git-lfs to clone the repository.
* [latexmk](https://ctan.org/pkg/latexmk) for automated LaTeX document generation
    * Add latexmk to your PATH for [Windows](http://www.computerhope.com/issues/ch000549.htm), [Mac](http://hathaway.cc/post/69201163472/how-to-edit-your-path-environment-variables-on-mac), and [Linux](http://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux).
    * The beamer theme [`metropolis`](https://github.com/matze/mtheme). This is part of MikTeX since Dec 2014.

### Setting Up a New Project (Delete after setup)

1. Open a shell, clone the repository, and navigate to its root.
    ```bash
    git lfs clone https://github.com/gslab-econ/template.git YourProjectName
    cd YourProjectName
    ```
2. Remove the template git history (optional, but recommended) and initialize a new git repo. Be careful to not remove `.gitignore` and `.gitattributes`.
    ```
    rm -rf .git
    git init
    git add .
    git commit -m "Initalize project organization."
    ```
    Then you can link and push the new repo to a GitHub remote as appropriate.
3. Follow the remaining steps in "Quick Start" below, beginning with step 2.

### Quick Start
1. Open a shell, clone the repository, and navigate to its root.
    ```bash
    git lfs clone https://github.com/btleyden/YourProjectName.git YourProjectName
    cd YourProjectName
    ```
2. Create a Python >= 3.8 virtual environment
    ```bash
    python3 -m venv YourVENVName
    source YourVENVName/bin/activate
    ```
    You may need to replace `python3` with an alternative command depending on your local instalation of Python. Ensure the VENV has been activated any time you are working on the project.
3. Install Python dependencies ([btleyden fork of GSLab Python](https://github.com/btleyden/gslab_python/), [PyYAML](http://pyyaml.org/), [numpy](http://www.numpy.org/), and [matplotlib]('matplotlib')). Python requirements should always be stored in `config/requirements.txt`.
    ```bash
    pip install -r config/requirements.txt
    ```
4. Unzip the scons package.
    ```bash
    unzip config/scons.zip -d config/scons # Do manually on Windows
    ```
5. Navigate to the `analysis` or `paper_slides` subdirectory.
    ```bash
    cd analysis
    ```
6. You're ready to go. We'll prompt you to enter any necessary information and store it in `config_user.yaml` as your scripts run.
    * To build everything in the subdirectory that has been modified or with dependencies in the subdirectory that have been modified.
        ```bash
        python run.py
        ```
    Optionally, you can run this in parallel (`0` will use all available cores).
        ```bash
        python run.py -j <number of workers>
    * To build everything in a single directory of targets that has been modified and all of their dependencies that have been modified.
        ```bash
        python run.py build/path/to/directory
        ```
    * To build a single target that has been modified and all of its dependencies that have been modified.
        ```bash
        python run.py build/path/to/file.txt
        ```
    * To install the analysis relaeses to `paper_slides/input`, specify the `paper_slides` directory.
        ```bash
        python run.py ../paper_slides/
        ```

### FAQ

#### What is `config_user.yaml`?

Each user is allowed to have different local specifications: We don't put any restrictions on where you keep large files, what you call your executables, or how you manage shared directories. We do need to find these things, and that's what `config_user.yaml` is for. Each user maintains an **unversioned** [YAML file](http://yaml.org/) with these sorts of specifications. Each script uses its associated YAML-parsing module to read these specifications each time the script is run.

If you try to build a directory without `config_user.yaml`, we'll copy a template to your current working directory. You can always switch back to this template by deleting your current `config_user.yaml` and rerunning.

#### What do I put in `config_user.yaml`?

There's no "default" for `config_user.yaml` because it depends on system specifications and user preferences. Three things we do recommend keeping in `config_user.yaml` are the names of your executables, the location of a [SCons cache directory](http://scons.org/doc/2.0.1/HTML/scons-user/c4213.html), and the location of a release directory. These fields don't have to be specified if you're not using them, and we'll prompt you for their values at runtime if you've forgotten to specify them and they're necessary.

#### What is `config_global.yaml`?

The `config_global.yaml` tracks paths, specifications, variables, and software checks that are constant across users. We treat this file in the same manner as `config_user.yaml`, except that we do version `config_global.yaml`.

One important function of `config_global.yaml` is that it tracks the version of [gslab-python](https://github.com/gslab-econ/gslab_python) you expect your users to have installed.

#### How do I handle data external to my repository?

We are agnostic about how you incorporate external data into the template. There's no custom builder for these assets, by design. Our suggestions:

* When a large dataset is stored locally, `config_user.yaml` can include an entry specifying the user-specific path to that dataset. The key of the entry should be constant across users and documented in the top-level readme of the repository.

* When a large dataset is stored externally, there are a few options.
    * The top-level readme can specify manual download and storage instructions. This is simple, easy to customize, and unlikely to cause errors during a SCons build. It does, however, require each user to successfully download the same dataset, perhaps in an unstructured manner.
    * The download can be incorporated into the SCons build. We either execute a program to transfer data (e.g., `rsync` or `rclone`) using our "Anything builder" or from within a script executed by one of our other custom builders. These methods have the benefits of automation and dependency tracking, but they can introduce idiosyncratic errors if the download steps are prone to failure.
    * Regardless of the download method, the path to the dataset should be added to `config_global.yaml` and `.gitignore` if it is stored within the repository and to `config_user.yaml` if it is stored elsewhere.

* Any pointers to directories you store under the `input` key in either configuration yaml file will have their contents checked and recorded at runtime. We complete the check using our `record_dir` function and store its contents in `release/state_of_input.log`.

#### How do I use the outputs of `analysis` as inputs for `paper_slides`?

We recommend that you manually copy the desired files or directories from the `release` directory in `analysis` to a directory called `input` in `paper_slides`. We uncouple these top-level subdirectories to compartmentalize the research process. A busy coauthor can build `paper_slides` in a reproducible manner without wrangling data or repeating a lengthy analysis.

There are lighter-weight methods to connect these subdirectories, but they may make your project more prone to errors.
* Create a symlink between `analysis/release` and `paper_slides/input` (not platform-independent).
* Point to `analysis/release` from the `config_global.yaml` in `paper_slides` (hard to parse YAML in LyX and LaTeX).

You can recouple the SCons subdirectories by [installing](http://scons.org/doc/1.2.0/HTML/scons-user/c2848.html) the output from `analysis` into `paper_slides` Add the following line to the SConstruct in `analysis`

```
env.Install('../paper_slides/input', '#release/')
```

You'll also need to give SCons permission to build targets outside the `analysis` directory; so run

```bash
python run.py ../paper_slides
```

#### What software can I use for data analysis?

We have custom builders for Python, R, Stata, and MATLAB. They all use the same syntax. You'll need to add the builder to the SCons environment by uncommenting its definition in the SConstruct. Also check that its executable has been added to your PATH and recorded in `config_user.yaml`.

See `analysis/source/prepare_data/` for sample scripts in each language. To run one of the sample scripts, uncomment its block in `analysis/source/prepare_data/SConscript` and its builder in `analysis/SConstruct`. Note that all sample scripts produce the same output, so only one block is allowed to run for each SCons build. If you uncomment the block for one software, you need to comment out the blocks for all others.

* If you're using R, make sure you've installed its dependencies.
```bash
Rscript config/config_r.r
```
* If you're using Stata, make sure the executable is stored in `config_user.yaml` with the key `stata_executable` and that you've installed its dependencies.
```
statamp -e config/config_stata.do // Stata executable may be different
```
* If you're using Matlab, make sure it's been added to your PATH and that you have installed the Matlab YAML parser following the instructions [here](https://github.com/gslab-econ/gslab_matlab/blob/f11eff492e0c982cf344c60b7e7ce0e7b7a66872/README.md#installation-instructions-for-matlab-r2016b).

#### Is there support for other software?

We support additional software through our "Anything builder." It let's you execute shell commands as a build step using the syntax, logging, and error management of our other custom builders. We turn your commands into a SCons node at runtime, and SCons will track your dependencies and build the node if necessary. SCons will always execute your commands using your system's shell, and you can use this functionality to incorporate arbitrary steps into your build.

An example using standard Bash commands is in `analysis/source/prepare_data/SConscript` and `analysis/source/prepare_data/build_data.sh`. This code won't run on Windows.

#### Can I pass "command line style" arguments to a script?

You bet. All of our custom builders accept "command line style" arguments with the same method. Enumerate the arguments in a list and pass them to the builder through the `CL_ARG` keyword argument, exactly the same way you specify sources and targets. We'll format this list, and `scons` will pass its contents to the script at runtime. You can reference these arguments when writing a script using the standard practice for its language.

#### How is the build process logged?

Each of our custom builders produces a log of its process in the same directory as the first of its targets. Each log is named `sconscript.log` by default, and you can insert custom text between `sconscript` and `.log` by passing it as a string through the builder's `log_ext` keyword argument. It's similar to the way that you specify sources and targets, except that the `log_ext` argument must be a string. You should specify the `log_ext` argument for builders that produce logs in the same directory, otherwise the default `sconscript.log` will be overwritten by each builder.

After all the steps in the build are completed, we'll comb through the directory and look for for any files named `sconscript*.log`. These logs will be concatenated—with the earliest completed ones first and all logs with errors on top. We'll store this concatenated log in `release/sconstruct.log`.

#### Can I release my repository?

Yes, a [custom tool](https://github.com/btleyden/gslab_python/tree/master/gslab_scons) allows you to release to GitHub and a local destination specified in `config_user.yaml`. A new release can be transfered to a remote manually (e.g., using `rsync` or `rclone`) or automatically by specifying a local destination that's synced to a remote (e.g., a Dropbox directory).

Every file intended for release should be added to the `release` directory. Files not intended for release to GitHub should be added to `.gitignore`. Our tool will transfer everything in `release` to the local destination and create a [GitHub release](https://help.github.com/articles/creating-releases/) with all the versioned files—those not added to `.gitignore`—in `release`.

Our custom tool creates a local release of the SCons subdirectory in which its run but a GitHub release of the entire repository. We therefore suggest you prepend the name of the SCons subdirectory to the title of the release.

#### What if there are large files I need to put in `release` that cannot be versioned?

Our protocol is to keep these files in a designated subdirectory named `release/lg`. By default, `release/lg` is in `.gitignore`. When you use our custom release tool, `release/lg` will be included in the local destination release but not pushed to GitHub.

#### Where should I track the prerequisites for my repository?

Required packages for Python, R, and Stata should be added to their configuration scripts under `config`. If you require the installation of many packages for another language, we suggest you set up a new configuration script in the same location. Other requirements can be added a la carte to the Prerequisites section of this readme.

## License

The MIT License (MIT)

Copyright (c) 2017 Matthew Gentzkow, Jesse Shapiro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
