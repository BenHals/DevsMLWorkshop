# DevsMLWorkshop
Helper files for Devs ML Workshop


# How to run - Anaconda
1. Install Anaconda https://www.anaconda.com/products/individual#Downloads
2. (If needed) Add Anaconda to path.
    1. Test with ```conda --version```
3. Create new environment to install packages to.
    1. Run ```conda create -n {devsMLEnv} python=3.5```
    2. This creates a new environment with a clean python install.
4. Activate the environment so you can use it:
    1. ```conda activate devsMLEnv```
5. Install required packages
    1. ```conda install jupyter```
    2. Type ```y``` when prompted to accept install.
    3. (If needed) ```conda install pywin32```
    4. ```conda install scikit-learn```
6. Start ```jupyter``` in current directory to open notebook
    1. Navigate to git repository, use ```cd``` or open shell in correct directory.
    2. Run ```jupyter notebook```
    3. A browser window will open showing jupyter
7. Open notebook
    1. A directory tree should show of the current directory.
