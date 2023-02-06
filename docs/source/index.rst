|PyPI|

ZTF - Digital Control using Z-transform 
============================================================

.. image:: https://raw.githubusercontent.com/rahulbhadani/ZTF/main/ztf.png
   :width: 600px
   :align: left

|
|
|
|
|
|
|
|
|
|

ZTF, stands for Z-domain transfer function, is a Python library to implement a transfer function based system for system modeling, and control.

Installation
^^^^^^^^^^^^^

.. code-block:: bash

   pip install ZTF

Quick Start
^^^^^^^^^^^^^^

We can implement a PID controller block that takes a timeseries input in the loop and outputs controlled value in open-loop setting

.. code-block:: python

    from ZTF import PID
    import math
    import time

    P = 12.2285752621432
    I = 7.40871870543199
    D = 4.88097496311707
    N = 37.0569659936971
    Ts = 0.05

    pid = PID(P, I, D, N, Ts)
    start_time = time.time()
    out = 0
    x = 0

    print("Input, Output")
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 10.0:
            break

        t = elapsed_time
        x = 3 * math.sin(t)
        out = pid.processing(x)
        print("{}, {}".format(x, out))
        time.sleep(Ts)


Contributing to the project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Feel free to submit an `issue <https://github.com/jmscslgroup/ZTF/issues/new/choose>`_
or send us an `email <mailto:rahulbhadani@email.arizona.edu>`_. 
If you like to contribute to this project, please fork this repository to your GitHub account,
create a new branch for yourself and send a pull request for the merge. After reviewing the changes,
we will decide if this is a good place to add your changes.
Your help to improve **ZTF** is highly appreciated.

Licensing
^^^^^^^^^^

| License: MIT License 
| Copyright Rahul Bhadani
| Initial Date: Feb 06, 2023
| Permission is hereby granted, free of charge, to any person obtaining 
| a copy of this software and associated documentation files 
| (the "Software"), to deal in the Software without restriction, including
| without limitation the rights to use, copy, modify, merge, publish,
| distribute, sublicense, and/or sell copies of the Software, and to 
| permit persons to whom the Software is furnished to do so, subject 
| to the following conditions:

| The above copyright notice and this permission notice shall be 
| included in all copies or substantial portions of the Software.

| THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF 
| ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
| TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
| PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT 
| SHALL THE AUTHORS
| BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
| AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
| OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
| OR OTHER DEALINGS IN THE SOFTWARE.

.. toctree::
   :caption: Main
   :maxdepth: 1
   :hidden:
   
.. toctree::
   :caption: API
   :maxdepth: 1
   :hidden:

   api_ZTF
   

.. |PyPI| image:: https://img.shields.io/pypi/v/ZTF.svg
   :target: https://pypi.org/project/ZTF

.. |PyPIDownloads| image:: https://pepy.tech/badge/ZTF
   :target: https://pepy.tech/project/ZTF
   

