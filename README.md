# Personal Data Manager
A data manager is a software used to manage collected data from one's personal life.
I aim to keep this usable for companies and families.

This is a charity project.
People like me have concerns for privacy, thus not using commercial products to store data.

I myself use a modified version of this software.


## Installation (Linux)
You should already have Python 3 installed on your machine.

### Local use
1. Clone the repository
```git clone https://github.com/cschlay/Personal-Data-Manager.git```
2. Run the installation script
```source install.sh```, this will also start the server.
3. If you have it already installed, then run ```source pdatamana.sh```.

Note: Always close the server with CTRL + C, otherwise the port is not closed properly.
In case you encountered that problem, use ```fuser -k <port_number>/tcp```.
The port number should be 8000, at least on my machine.

## License
Everything under this repository is in MIT License.
