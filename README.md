# Assistive Arm Project at Harvard

## Our setup
The general setup can be a bit cumbersome, but essentially what we need is the 
following: 

* 1 Raspberry Pi 4 Model B 2GB
* 1 Desktop for retrieving Motion Capture data
* 1 Macbook Pro
  
### Networking
Raspberry Pi and Desktop are connected to the same network via Ethernet, and 
communicate between them via a TCP port using ZMQ.

Coding is done from the Macbook Pro via SSH directly on the Raspberry Pi.

### IP addresses
On the Harvard secure network, both desktop and raspberry pi MUST be connected
to the network on the same way (WIFI or ETH), otherwise they won't be able to
communicate between them.

You might need to modify the IP address and make it static so that they are on 
the same network.


### Installing OpenSim Moco (Mac)

After having installed OpenSim (via the package manager), you should now have it
under `/Applications`. In order to install the Python API into the
poetry environment, you must do the following steps:

1. Navigate to the **sdk/Python** in the OpenSim 4.4 Installation (`/Applications/OpenSim/`)
```bash
cd /Applications/OpenSim\ 4.4/OpenSim\ 4.4.app/Contents/Resources/opensim/sdk/
```

2. Update DYLD_LIBRARY_PATH to include the OpenSim and Simbody libraries:
```bash
echo "export DYLD_LIBRARY_PATH='$DYLD_LIBRARY_PATH:$(pwd)/lib:$(pwd)/Simbody/lib'" >> ~/.zshrc
```

3. Depending on where your installation has been done, you might require
more permissions to be able to read the files within **OpenSim**. In general this
will be `/Applications`, so we must give the rights to read its content like so:

```bash
sudo chmod +r $(pwd)/*
```

4. Now, you can run pip to install the package. Note that although our environment
manager is **poetry**, right now OpenSim doesn't support PEP 517 builds, so we 
must install it with pip BUT with an active **poetry shell** in order to have it
in the environment:

```bash
sudo pip install "opensim @ file:///Applications/OpenSim%204.4/OpenSim%204.4.app/Contents/Resources/opensim/sdk/Python"
```

Great! You should now have OpenSim installed in your environment, check it via:

```bash
python -c "import opensim; print(opensim.GetVersionAndDate())"
```


