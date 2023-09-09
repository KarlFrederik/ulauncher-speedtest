# ulauncher-speedtest init script
# https://github.com/KarlFrederik/ulauncher-speedtest
# by KarlFrederik

#This Script will Install PIP, speedtest-cli

if which pip;
then
  echo "pip already installed continue..."
else
  echo "pip is not installed install..."
  sudo apt install python3-pip
fi

if pip show speedtest;
then
  echo "Library speedtest is installed but its presence breaks the extension it needs to be removed and install speedtest-cli insteadof"
  pip uninstall speedtest
fi

if pip show speedtest-cli;
then
  echo "speedtest-cli already installed no actions required"
else
  pip install speedtest-cli
fi

echo
echo
echo "End of the Installscript, follow the instruction on https://github.com/KarlFrederik/ulauncher-speedtest"
echo
echo
