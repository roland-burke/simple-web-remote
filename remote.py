#!/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer

import simplejson
from pynput.keyboard import Controller, Key


class MyRemoteServer(BaseHTTPRequestHandler):
	controller = Controller()

	def playpause(self):
		self.controller.press(Key.media_play_pause)
		self.controller.release(Key.media_play_pause)

	def next(self):
		self.controller.press(Key.media_next)
		self.controller.release(Key.media_next)

	def previous(self):
		self.controller.press(Key.media_previous)
		self.controller.release(Key.media_previous)

	def volumeup(self):
		self.controller.press(Key.media_volume_up)
		self.controller.release(Key.media_volume_up)

	def volumedown(self):
		self.controller.press(Key.media_volume_down)
		self.controller.release(Key.media_volume_down)

	def mute(self):
		self.controller.press(Key.media_volume_mute)
		self.controller.release(Key.media_volume_mute)

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		f = open("/home/roland/coding/web-remote/static/index.html", "r")
		self.wfile.write(f.read().encode())

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		self._set_headers()
		self.data_string = self.rfile.read(int(self.headers['Content-Length']))

		self.send_response(200)
		self.end_headers()

		data = simplejson.loads(self.data_string)
		print("{}".format(data["operation"]))
		if data["operation"] == "playpause":
			self.playpause()
		elif data["operation"] == "volumeup":
			self.volumeup()
		elif data["operation"] == "volumedown":
			self.volumedown()
		elif data["operation"] == "mute":
			self.mute()
		elif data["operation"] == "next":
			self.next()
		elif data["operation"] == "previous":
			self.previous()
		return


def run(server_class=HTTPServer, handler_class=MyRemoteServer, port=8080):
	server_address = ("0.0.0.0", port)
	httpd = server_class(server_address, handler_class)
	print('Starting server...')
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

if len(argv) == 2:
	run(port=int(argv[1]))
else:
	run()

