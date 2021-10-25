==============
User Interface
==============

Thebe includes support for some built-in user interface elements.

The aim is to provide simple elements that can be added to a page and styled accordingly by the consumer without needing to [re]write code.
Using these UI elements in the way shown here, assumes that you already have Thebe statically loaded on page.

Built in UI elements are:

- Activate Button
- Kernel Status Widget
- Cell Buttons (for every cell): Run, Restart and Restart All

Activate Button
===============

When this button is pressed, it will run the `thebelab.bootstrap` function on the page.
Configure this UI element as follows.

Add a ``div`` element to the page in the desired location.

.. code-block:: html

  <div class="thebe-activate" />

Then set the following option to :code:`mountActivateWidget:true` in the Thebe config object

Status Widget
=============

This element will display the status of the kernel, it will update when the kernel sends new messages or when code is executed.
Configure this UI element as follows.

Add a :code:`div` element to the page in the desired location.

.. code-block:: html

  <div class="thebe-status" />

Then set the following option to :code:`mountStatusWidget:true` in the Thebe config object

Cell Buttons
=============

The buttons are optional. By default, all buttons are mounted. To remove a button set its respective option to :code:`false`.
The options are :code:`mountRunButton`, :code:`mountRestartButton`, :code:`mountRestartallButton`.

Example
=======

Adding the following to a page will render both Activate and Status widgets.

.. code-block:: html

  <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
  <script type="text/x-thebe-config">
    {
      requestKernel: true,
      binderOptions: {
        repo: "binder-examples/requirements",
      },
      mountActivateWidget: true,
      mountStatusWidget: true
    }
  </script>
  <div class="thebe-activate" />
  <div class="thebe-status" />

Pressing activate will convert the following code into an activate cell, and the kernel status widget
will show status of the kernel launch.

.. raw:: html

  <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
  <script type="text/x-thebe-config">
    {
      requestKernel: true,
      binderOptions: {
        repo: "binder-examples/requirements",
      },
      mountActivateWidget: true,
      mountStatusWidget: true
    }
  </script>
  <div class="thebe-activate"></div>
  <div class="thebe-status"></div>


.. raw:: html

   <pre data-executable="true" data-language="python">
   %matplotlib inline
   import numpy as np
   import matplotlib.pyplot as plt
   x = np.linspace(0,10)
   plt.plot(x, np.sin(x))
   plt.plot(x, np.cos(x))
   </pre>


Note: If you are looking to load Thebe dynamically, check the custom launch button `in the example here. <https://github.com/executablebooks/thebe/blob/feat/kernel-status/examples/demo-launch-button.html>`_
