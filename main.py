from flet import *
from PIL import Image
import pyscreenshot as ImageGrab
import time
# TIME FOR YOU FILE JPG FILE




def main(page:Page):

	# and NOW I CREATE BLUE CONTAINER FOR SCREENSHOT 
	# AND SAVE TO JPG FILE MY CONTAINER

	ct = Container(
		bgcolor="blue",
		padding=10,
		width=200,
		alignment=alignment.center,
		height=150,
		content=Column([
			Text("Test Flet Shoot",size=30,color="white")
			])
		)
	def myscreenshot(e):
		# AND NOW GET AXIS y AND X 
		# y is top OF YOU Container
		# x is left of yu cointaer
		y = page.window_top + 10
		# 10 IS MY OPINION SIZE YOU CAN CHANGE IF IMAGE IS CUT
		x = page.window_left

		# AND W and H IS WIDTH AND HEIGHT OF YOU COINTAINER
		# NOW I GET width from my cointainer width page.controls

		w = page.controls[0].controls[0].width + 20
		# 20 IS MY OPNION YOU CAN CHANGE SIZE IF IMAGE RESULT IS CUT
		h = page.controls[0].controls[0].height + 20


		# AND NOW SCREENSHOT 
		# AND SAVE TO ASSETS FOLDER
		screen = ImageGrab.grab(
			# and DEFINE AREA FOR SCREENSHOT
			bbox = (x,y,w+x,h+y)
			)
		# AND NOW SAVE TO FILE NAME WITH TIME RENAME
		t = str(time.time())
		# AND SAVE TO LOCATION ASSETS
		myimagelocation = f"assets/{t.split('.')[0]}.png"
		# AND SAVE IT
		screen.save(myimagelocation)


	page.add(
		Column([
			ct,
			# AND CREATE BUTTON FOR SAVE YOU CONTAINER
			ElevatedButton("Save TO JPG",
				on_click=myscreenshot
				)
			])
		)

flet.app(target=main,assets_dir="assets")