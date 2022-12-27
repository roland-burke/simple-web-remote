# Python web remote
Usage: ./remote.py

A port can be specified with: ./remote.py \<port\>

The python script starts a http server, which serves as the remote.

## Implementation

The client sends a POST request to 'http://\<hostname\>:\<port\>' with the corresponding payload. For example:
```
{ "operation": "playpause" }
```
The server then emulates a press of the requested multimedia key.
## Screenshot

![Screenshot](https://user-images.githubusercontent.com/56251366/209732907-d68215a7-2977-49e4-ba97-f7d7c2e1220e.png)