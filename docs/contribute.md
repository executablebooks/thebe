# Contributing Guide

Thanks for your interest in contributing to `thebe`, your contributions are welcome and appreciated 🎉. This page contains some information to help you get started.

```{note}
`thebe` was recently called `thebelab`, so you may see mentions of `thebelab` scattered throughout the repository. Feel free to flag these and suggest we rename them to `thebe`.
```

## Contributing guide

See the [ExecutableBooks developer guidelines](https://executablebooks.org/en/latest/contributing.html) for conventions and practices around developing `thebe`. However, note that some practices, such as creating releases, may be different because `thebe` is primarily an Javascript (`npm`) package rather than a Python package.

## Repository structure

`thebe` is primarily written in Javascript, and structured as an NPM package.

- `src/` contains the code and assets that make up `thebe`. This is what you'll edit to make changes to the project.
- `examples/` provides a few HTML examples of how `thebe` can be used. It is mostly for documentation

(dev-install)=

## Set up a development environment

In order to get Thebe running locally, you'll need to have Node installed on your system.

Minimum requirements are:

- nodejs v15.0 or greater
- npm v6.0 or greater
- yarn v1.22 or greater

You can install it in several ways, the most common being:

- Install Node by [following the nodejs instructions](https://nodejs.org/en/download/)
- Using the [node version manager](https://github.com/nvm-sh/nvm#installing-and-updating)
- Install Node through `conda`

```bash
conda install -c conda-forge nodejs
```

Once installed, also install `yarn` which is what you will run in order to run Thebe locally.

```bash
npm install -g yarn
```

Next, clone the repository and install the required dependencies:

```bash
git clone https://github.com/executablebooks/thebe
cd thebe
yarn install
```

This will install all dependencies needed to run `thebe` (specified in `package.json`). By default, `yarn install` will also have created a production build in `lib`

If you are using `npm` v7 you may encounter **Peer Dependency Errors** see comments below to resolve these.

```{note}
Using `yarn install` will ensure that you install the latest tested dependencies, and will not make any unintentional local upgrades. `yarn` uses `npm` under the hood, please do not use `npm install` directly to install dependencies.
```

#### Peer Dependency Errors

Due to recent changes in `npm` as of v7 peer dependency issues are flagged as critical errors. However, many projects have not yet resolved these issues in their code base, this means that a project's co-dependencies can prevent installation of a package. This is a know issue, to resolve this there are two options:

1. Downgrade `npm` to v6

```bash
  npm install -g npm@6
```

2. Set the `legacy-peer-deps` option in your local environment

```bash
  npm config set legacy-peer-deps true
```

## Build and demo `thebe` locally

To use your local copy of `thebe` (e.g., if you make any changes to the `src/` folder), you can run a local build and serve a sample web page. To do so, run:

```bash
yarn run build:watch
```

This will build `thebe/` locally (including any changes you've made to the source code).

You can now demo the latest `thebe/` changes by opening the file at `development.html`. Open this file to see Thebe running.

The content of `development.html` is a simple HTML page that demonstrates Thebe functionality. You can edit it to test out new features or configurations.

Running the `yarn run develop` command will start building the source code with webpack and serve it along with `development.html`.
As you change the code in `src/`,
the javascript will automatically be re-built,
but you'll be required to refresh the page.

## Committing changes

Thebe uses code autoformatting so you don't need to worry about style lint,
so whenever you are ready to commit changes
run `yarn run fmt` to autoformat the javascript.
You can put this script in `.git/hooks/pre-commit`:

```bash
#!/bin/sh
if [[ -f package.json ]]; then
    yarn run fmt
fi
```

to run auto-formatting prior to each commit.

## Testing Thebe

You can test manually, interactively by running `yarn run develop` to open and serve `development.html` with the current build of thebe.

### Running automated tests

There are two types of automated test environment in place in thebe both using the Jest testing library. These are:

1.  a standard javascript testing setup for unit / component level testing of the thebe library. These can be run using `yarn run test` or `yarn run test:watch` and test code is located in the `test` folder.
2.  e2e style tests using jest + puppeteer that can be run `yarn run test:e2e` or `yarn run test:e2e:watch` and test code is located in the `e2e` folder.

Alternately, you can push your changes to GitHub and let the tests run automatically via GitHub Actions.

TODO: get testing infrastructure to a point where we can reasonably request tests for new features.

#### Adding unit tests

Unit style tests work by loading the thebe library or part of it in javascript; mocking inputs and/or dependencies, executing a function and asserting on outputs of mocks. A good first example to look at is `tests/bootstrap.spec.js`. This test:

- loads thebe js code `import * as thebelab from "../src/thebelab";`
- manipulates the dom to prep the test (via built in JSDOM)
- calls the `thebe.bootstrap()` function
- checks for expected behaviour

If you are new to Jest check their [getting started](https://jestjs.io/docs/en/getting-started), [mocking](https://jestjs.io/docs/en/mock-functions) and [expect assertion api](https://jestjs.io/docs/en/expect) docs.

#### Adding e2e Tests

e2e style tests are achieved using [Puppeteer](https://github.com/puppeteer/puppeteer) a headless chrome api that can be used to load a page complete with thebe scripts, allowing full execution as though it was in an end user browser and then assertion of end state.

Adding new e2e tests involves:
(see `e2e/readonly.test.js` for an example)

- creating a test html page that load and uses thebe, placing this in the `e2e/fixtures/HTML` folder
- load the fixture page at the start of your test

```javascript
beforeAll(async () => {
  await page.goto(
    `file:${path.join(__dirname, "/fixtures/HTML/readonly1.html")}`,
    { waitUntil: ["load", "domcontentloaded", "networkidle0"] }
  );
});
```

- Assert on initial page state
- Invoke UI actions to trigger behavior
- assert on final state

## Building docs locally

Thebe uses [Sphinx](https://www.sphinx-doc.org/) and [JupyterBook](https://jupyterbook.org/) for building documentation. Thebe documentation is located in the `/docs` directory.
You will need the development environment setup, see the above {ref}`dev-install` to learn more.
You will also need Python installed, and can install the requirements for the documentation using:

```bash
cd docs/
pip install -r doc-requirements.txt
```

Once you are in the documentation folder:

```bash
make html
```

Finally, run the following to view the built documentation locally:

```bash
make show
```

## Releasing Thebe

To release thebe, follow the [EBP guidelines](https://executablebooks.org/en/latest/contributing.html#releases-and-change-logs) to make sure the repo is ready for release.

Once prepared, bump the version with:

1. Use yarn to update the thebe version in the `package.json` file and to create
   a git tag for the version using `yarn version NEW_VERSION`, e.g. `yarn version 0.5.1`
2. Push the tag to github: `git push --follow-tags`
3. Create a release for the new tag on github at
   https://github.com/executablebooks/thebe/releases/new; this will trigger a
   github action that uploads the latest version to unpkg.com/browse/thebe/.

## Thebe architecture

Thebe consumes three principal APIs:

1. [jQuery][] for manipulating elements on the page
2. [JupyterLab][] for talking to a running Jupyter server to execute code and display outputs
3. [BinderHub][] for requesting kernels from a BinderHub instance, such as mybinder.org.

### Manipulating the page

The first thing Thebe does is find elements on the page
that should be made executable.
It does this with [jQuery][],
finding (by default) elements that look like `<div data-executable="true">...`,
with a query such as the `$("[data-executable])` (this is the default, but can be customized).
Once it has found these elements,
Cell objects are created (more on Cells in the JupyterLab API), which then _replace_ the elements that were found.

### JupyterLab APIs

The main thing Thebe does is execute code and display output.
This is done with JupyterLab APIs.
A Cell is an element wrapping a code input area and associated OutputArea for displaying the outputs that result from execution.

Main APIs used:

- OutputArea for rendering outputs on the page
- Session for starting kernels
- Kernel for sending/receiving messages to/from a connected kernel
- WidgetManager for working with interactive widgets

### Configuration

Configuration is handled by adding a `script` tag with type="text/x-thebe-config". This should specify a javascript object.

More information in the README (TODO: move it here?)

```html
<script type="text/x-thebe-config">
  {
    binderOptions: {
      repo: "minrk/ligo-binder",
      ref: "master",
    }
  }
</script>
```

[jquery]: https://jquery.com
[jupyterlab]: https://jupyterlab.readthedocs.io
[binderhub]: https://binderhub.readthedocs.org
