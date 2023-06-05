import requests
import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import argparse
import cmd


def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    joke_setup = data["setup"]
    joke_punchline = data["punchline"]
    return joke_setup, joke_punchline


def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    quote = data["content"]
    return quote



def get_meme():
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    data = response.json()
    meme_data = random.choice(data["data"]["memes"])
    meme_url = meme_data["url"]
    return meme_url


def generate_item(item_type):
    if item_type == "joke":
        joke_setup, joke_punchline = get_joke()
        content = f"Joke:\n\n{joke_setup}\n\n{joke_punchline}"
        image = create_image_with_text(content)
        image.show()
    elif item_type == "quote":
        quote = get_quote()
        content = f"Quote:\n\n{quote}"
        image = create_image_with_text(content)
        image.show()
    elif item_type == "meme":
        meme_url = get_meme()
        response = requests.get(meme_url)
        meme_image = Image.open(BytesIO(response.content))
        meme_image.show()
    else:
        print("Invalid item type.")


def create_image_with_text(content):
    image_width = 800
    image_height = 400
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)
    font_size = 30
    margin = 50

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    lines = content.split("\n")
    y = margin
    for line in lines:
        line_width, line_height = draw.textsize(line, font=font)
        x = (image_width - line_width) // 2
        draw.text((x, y), line, fill=text_color, font=font)
        y += line_height + 10

    return image


class GeneratorShell(cmd.Cmd):
    intro = "Welcome to the Generator shell. Type 'help' to list commands."
    prompt = "(Generator) "

    def do_generate(self, args):
        item_type = self.select_item_type()
        generate_item(item_type)

    def select_item_type(self):
        while True:
            print("Select the item type:")
            print("1. Joke")
            print("2. Meme")
            print("3. Quote")
            choice = input("Enter the number corresponding to the item type: ")
            if choice == "1":
                return "joke"
            elif choice == "2":
                return "meme"
            elif choice == "3":
                return "quote"
            else:
                print("Invalid choice. Please try again.")

    def do_exit(self, args):
        print("Exiting...")
        return True


def main():
    shell = GeneratorShell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
